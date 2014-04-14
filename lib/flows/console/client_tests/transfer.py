#!/usr/bin/env python
"""End to end tests for lib.flows.general.transfer."""

import hashlib
import re
import socket
import threading


import logging
from grr.lib import aff4
from grr.lib import flow
from grr.lib import rdfvalue
from grr.lib.flows.console.client_tests import base
from grr.lib.rdfvalues import crypto
from grr.proto import tests_pb2


class MultiGetFileTestFlowArgs(rdfvalue.RDFProtoStruct):
  protobuf = tests_pb2.MultiGetFileTestFlowArgs


class MultiGetFileTestFlow(flow.GRRFlow):
  """This flow checks MultiGetFile correctly transfers files."""
  args_type = MultiGetFileTestFlowArgs

  @flow.StateHandler(next_state=["HashFile"])
  def Start(self):
    """Create some files to transfer.

    Using /dev/urandom ensures the file actually gets transferred and we don't
    just test the cache. The files created on the client will be automatically
    deleted.  If you need the client files for debugging, remove the lifetime
    parameter from CopyPathToFile.
    """
    self.state.Register("client_hashes", {})
    urandom = rdfvalue.PathSpec(path="/dev/urandom",
                                pathtype=rdfvalue.PathSpec.PathType.OS)

    for _ in range(self.args.file_limit):
      self.CallClient("CopyPathToFile",
                      offset=0,
                      length=2 * 1024 * 1024,  # 4 default sized blobs
                      src_path=urandom,
                      dest_dir="",
                      gzip_output=False,
                      lifetime=60,
                      next_state="HashFile")

  @flow.StateHandler(next_state=["MultiGetFile"])
  def HashFile(self, responses):
    if not responses.success:
      raise flow.FlowError(responses.status)

    for response in responses:
      self.CallFlow("FingerprintFile", next_state="MultiGetFile",
                    pathspec=response.dest_path)

  @flow.StateHandler(next_state="VerifyHashes")
  def MultiGetFile(self, responses):
    if not responses.success:
      raise flow.FlowError(responses.status)
    for response in responses:
      fd = aff4.FACTORY.Open(response, "VFSFile", mode="r", token=self.token)
      binary_hash = fd.Get(fd.Schema.FINGERPRINT)
      hash_digest = binary_hash.results[0].GetItem("sha256").encode("hex")
      self.state.client_hashes[str(response)] = hash_digest

      self.CallFlow("MultiGetFile", pathspecs=[binary_hash.pathspec],
                    next_state="VerifyHashes")

  @flow.StateHandler()
  def VerifyHashes(self, responses):
    if not responses.success:
      raise flow.FlowError(responses.status)
    for response in responses:
      fd = aff4.FACTORY.Open(response.aff4path, "VFSBlobImage",
                             mode="r", token=self.token)
      server_hash = hashlib.sha256(fd.Read(response.st_size)).hexdigest()
      client_hash = self.state.client_hashes[response.aff4path]

      if server_hash != client_hash:
        format_string = ("Hash mismatch server hash: %s doesn't match"
                         "client hash: %s for file: %s")
        raise flow.FlowError(format_string % (server_hash, client_hash,
                                              response.aff4path))


class TestMultiGetFile(base.LocalClientTest):
  platforms = ["linux", "darwin"]
  flow = "MultiGetFileTestFlow"
  args = {}

  def CheckFlow(self):
    # Reopen the object to update the state.
    flow_obj = aff4.FACTORY.Open(self.session_id, token=self.token)

    # Check flow completed normally, checking is done inside the flow
    self.assertEqual(
        flow_obj.state.context.state, rdfvalue.Flow.State.TERMINATED)
    self.assertFalse(flow_obj.state.context.get("backtrace", ""))


#########
# Linux #
#########


class TestGetFileTSKLinux(base.ClientTestBase):
  """Tests if GetFile works on Linux using Sleuthkit."""
  platforms = ["linux"]

  flow = "GetFile"
  args = {"pathspec": rdfvalue.PathSpec(
      path="/bin/ls",
      pathtype=rdfvalue.PathSpec.PathType.TSK)}

  # Interpolate for /dev/mapper-...
  output_path = "/fs/tsk/.*/bin/ls"

  def CheckFlow(self):
    pos = self.output_path.find("*")
    if pos > 0:
      prefix = self.client_id.Add(self.output_path[:pos])
      for urn in base.RecursiveListChildren(prefix=prefix):
        if re.search(self.output_path + "$", str(urn)):
          self.to_delete = urn
          return self.CheckFile(aff4.FACTORY.Open(urn))
    else:
      urn = self.client_id.Add(self.output_path)
      fd = aff4.FACTORY.Open(urn)
      if isinstance(fd, aff4.BlobImage):
        return self.CheckFile(fd)

    self.fail("Output file not found.")

  def CheckFile(self, fd):
    data = fd.Read(10)
    self.assertEqual(data[1:4], "ELF")

  def tearDown(self):
    super(TestGetFileTSKLinux, self).tearDown()
    if hasattr(self, "to_delete"):
      urn = self.to_delete
    else:
      urn = self.client_id.Add(self.output_path)
    self.DeleteUrn(urn)
    # Make sure the deletion acutally worked.
    self.assertRaises(AssertionError, self.CheckFlow)


class TestMultiGetFileTSKLinux(TestGetFileTSKLinux):
  """Tests if MultiGetFile works on Linux using Sleuthkit."""
  flow = "MultiGetFile"
  args = {"pathspecs": [rdfvalue.PathSpec(
      path="/bin/ls",
      pathtype=rdfvalue.PathSpec.PathType.TSK)]}


class TestGetFileOSLinux(TestGetFileTSKLinux):
  """Tests if GetFile works on Linux."""
  args = {"pathspec": rdfvalue.PathSpec(
      path="/bin/ls",
      pathtype=rdfvalue.PathSpec.PathType.OS)}
  output_path = "/fs/os/bin/ls"


class TestMultiGetFileOSLinux(TestGetFileOSLinux):
  """Tests if MultiGetFile works on Linux."""
  flow = "MultiGetFile"
  args = {"pathspecs": [rdfvalue.PathSpec(
      path="/bin/ls",
      pathtype=rdfvalue.PathSpec.PathType.OS)]}


class TestSendFile(base.ClientTestBase):
  """Test SendFile."""
  platforms = ["linux"]
  flow = "SendFile"
  key = rdfvalue.AES128Key("1a5eafcc77d428863d4c2441ea26e5a5")
  iv = rdfvalue.AES128Key("2241b14c64874b1898dad4de7173d8c0")

  args = dict(host="127.0.0.1",
              port=12345,
              pathspec=rdfvalue.PathSpec(pathtype=0, path="/bin/ls"),
              key=key,
              iv=iv)

  def setUp(self):

    if self.local_client:
      logging.info("Setting up local listener.  This only works if the client"
                   " is running on localhost!! Pass local_client=False if it "
                   "isn't.")
    else:
      logging.info("Skipping TestSendFile because client isn't running "
                   "locally.")
      return

    class Listener(threading.Thread):
      result = []
      daemon = True

      def run(self):
        for res in socket.getaddrinfo(
            None, 12345, socket.AF_INET,
            socket.SOCK_STREAM, 0, socket.AI_ADDRCONFIG):
          af, socktype, proto, _, sa = res
          try:
            s = socket.socket(af, socktype, proto)
          except socket.error:
            s = None
            continue
          try:
            s.bind(sa)
            s.listen(1)
          except socket.error:
            s.close()
            s = None
            continue
          break
        conn, _ = s.accept()
        while 1:
          data = conn.recv(1024)
          if not data: break
          self.result.append(data)
        conn.close()

    self.listener = Listener()
    self.listener.start()

  def CheckFlow(self):
    if self.local_client:
      original_data = open("/bin/ls", "rb").read()
      received_cipher = "".join(self.listener.result)
      cipher = crypto.AES128CBCCipher(key=self.key, iv=self.iv,
                                      mode=crypto.AES128CBCCipher.OP_DECRYPT)
      received_data = cipher.Update(received_cipher) + cipher.Final()

      self.assertEqual(received_data, original_data)


##########
# Darwin #
##########


class TestGetFileTSKMac(TestGetFileTSKLinux):
  """Tests if GetFile works on Mac using Sleuthkit."""
  platforms = ["darwin"]

  def CheckFile(self, fd):
    data = fd.Read(10)
    self.assertEqual(data[:4], "\xca\xfe\xba\xbe")


class TestMultiGetFileTSKMac(TestGetFileTSKMac):
  """Tests if MultiGetFile works on Mac using Sleuthkit."""
  flow = "MultiGetFile"
  args = {"pathspecs": [rdfvalue.PathSpec(
      path="/bin/ls",
      pathtype=rdfvalue.PathSpec.PathType.TSK)]}


class TestGetFileOSMac(TestGetFileTSKMac):
  """Tests if GetFile works on Mac."""
  args = {"pathspec": rdfvalue.PathSpec(
      path="/bin/ls",
      pathtype=rdfvalue.PathSpec.PathType.OS)}


class TestMultiGetFileOSMac(TestGetFileOSMac):
  """Tests if MultiGetFile works on Mac."""
  flow = "MultiGetFile"
  args = {"pathspecs": [rdfvalue.PathSpec(
      path="/bin/ls",
      pathtype=rdfvalue.PathSpec.PathType.OS)]}


###########
# Windows #
###########


class TestGetFileOSWindows(TestGetFileOSLinux):
  """Tests if GetFile works on Windows."""
  platforms = ["windows"]
  args = {"pathspec": rdfvalue.PathSpec(
      path="C:\\Windows\\regedit.exe",
      pathtype=rdfvalue.PathSpec.PathType.OS)}
  output_path = "/fs/os/C:/Windows/regedit.exe"

  def CheckFile(self, fd):
    data = fd.Read(10)
    self.assertEqual(data[:2], "MZ")


class TestMultiGetFileOSWindows(TestGetFileOSWindows):
  """Tests if MultiGetFile works on Windows."""
  flow = "MultiGetFile"
  args = {"pathspecs": [rdfvalue.PathSpec(
      path="C:\\Windows\\regedit.exe",
      pathtype=rdfvalue.PathSpec.PathType.OS)]}


class TestGetFileTSKWindows(TestGetFileOSWindows):
  """Tests if GetFile works on Windows using TSK."""
  args = {"pathspec": rdfvalue.PathSpec(
      path="C:\\Windows\\regedit.exe",
      pathtype=rdfvalue.PathSpec.PathType.TSK)}

  def CheckFlow(self):
    urn = self.client_id.Add("/fs/tsk")
    fd = aff4.FACTORY.Open(urn, mode="r", token=self.token)
    volumes = list(fd.OpenChildren())
    found = False
    for volume in volumes:
      file_urn = volume.urn.Add("Windows/regedit.exe")
      fd = aff4.FACTORY.Open(file_urn, mode="r",
                             token=self.token)
      try:
        data = fd.Read(10)
        if data[:2] == "MZ":
          found = True
          self.to_delete = file_urn
          break
      except AttributeError:
        # If the file does not exist on this volume, Open returns a aff4volume
        # which does not have a Read method.
        pass
    self.assertTrue(found)


class TestMultiGetFileTSKWindows(TestGetFileTSKWindows):
  """Tests if MultiGetFile works on Windows using TSK."""
  flow = "MultiGetFile"
  args = {"pathspecs": [rdfvalue.PathSpec(
      path="C:\\Windows\\regedit.exe",
      pathtype=rdfvalue.PathSpec.PathType.TSK)]}
