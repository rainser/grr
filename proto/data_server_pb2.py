# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grr/proto/data_server.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import grr.proto.data_store_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='grr/proto/data_server.proto',
  package='',
  serialized_pb='\n\x1bgrr/proto/data_server.proto\x1a\x1agrr/proto/data_store.proto\"\xab\x02\n\x10\x44\x61taStoreCommand\x12*\n\x07\x63ommand\x18\x01 \x01(\x0e\x32\x19.DataStoreCommand.Command\x12\"\n\x07request\x18\x02 \x01(\x0b\x32\x11.DataStoreRequest\"\xc6\x01\n\x07\x43ommand\x12\r\n\tMULTI_SET\x10\x00\x12\x17\n\x13MULTI_RESOLVE_REGEX\x10\x01\x12\x11\n\rRESOLVE_MULTI\x10\x02\x12\x12\n\x0e\x44\x45LETE_SUBJECT\x10\x03\x12\x15\n\x11\x44\x45LETE_ATTRIBUTES\x10\x04\x12\x1b\n\x17\x44\x45LETE_ATTRIBUTES_REGEX\x10\x05\x12\x10\n\x0cLOCK_SUBJECT\x10\x06\x12\x12\n\x0eUNLOCK_SUBJECT\x10\x07\x12\x12\n\x0e\x45XTEND_SUBJECT\x10\x08\"0\n\x12\x44\x61taServerInterval\x12\r\n\x05start\x18\x01 \x01(\x04\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x04\"\xab\x01\n\x0f\x44\x61taServerState\x12\'\n\x06status\x18\x01 \x01(\x0e\x32\x17.DataServerState.Status\x12\x0c\n\x04load\x18\x02 \x01(\x04\x12\x0c\n\x04size\x18\x03 \x01(\x04\x12\x16\n\x0enum_components\x18\x04 \x01(\x04\x12\x15\n\ravg_component\x18\x05 \x01(\x04\"$\n\x06Status\x12\r\n\tAVAILABLE\x10\x00\x12\x0b\n\x07OFFLINE\x10\x01\"\x8d\x01\n\x15\x44\x61taServerInformation\x12\r\n\x05index\x18\x01 \x01(\x04\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x04\x12\x1f\n\x05state\x18\x04 \x01(\x0b\x32\x10.DataServerState\x12%\n\x08interval\x18\x05 \x01(\x0b\x32\x13.DataServerInterval\"s\n\x11\x44\x61taServerMapping\x12\x0f\n\x07version\x18\x01 \x01(\x04\x12\x13\n\x0bnum_servers\x18\x02 \x01(\x04\x12\'\n\x07servers\x18\x03 \x03(\x0b\x32\x16.DataServerInformation\x12\x0f\n\x07routing\x18\x04 \x03(\t\"V\n\x1b\x44\x61taServerClientInformation\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x13\n\x0bpermissions\x18\x03 \x01(\t\"J\n\x1b\x44\x61taServerClientCredentials\x12+\n\x05users\x18\x01 \x03(\x0b\x32\x1c.DataServerClientInformation\"V\n\x13\x44\x61taServerRebalance\x12\n\n\x02id\x18\x01 \x01(\t\x12#\n\x07mapping\x18\x02 \x01(\x0b\x32\x12.DataServerMapping\x12\x0e\n\x06moving\x18\x03 \x03(\x04\"]\n\x12\x44\x61taServerFileCopy\x12\x14\n\x0crebalance_id\x18\x01 \x01(\t\x12\x11\n\tdirectory\x18\x02 \x01(\t\x12\x10\n\x08\x66ilename\x18\x03 \x01(\t\x12\x0c\n\x04size\x18\x04 \x01(\x04')



_DATASTORECOMMAND_COMMAND = _descriptor.EnumDescriptor(
  name='Command',
  full_name='DataStoreCommand.Command',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MULTI_SET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MULTI_RESOLVE_REGEX', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESOLVE_MULTI', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE_SUBJECT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE_ATTRIBUTES', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE_ATTRIBUTES_REGEX', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCK_SUBJECT', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNLOCK_SUBJECT', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXTEND_SUBJECT', index=8, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=161,
  serialized_end=359,
)

_DATASERVERSTATE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='DataServerState.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AVAILABLE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OFFLINE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=547,
  serialized_end=583,
)


_DATASTORECOMMAND = _descriptor.Descriptor(
  name='DataStoreCommand',
  full_name='DataStoreCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='DataStoreCommand.command', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request', full_name='DataStoreCommand.request', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DATASTORECOMMAND_COMMAND,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=60,
  serialized_end=359,
)


_DATASERVERINTERVAL = _descriptor.Descriptor(
  name='DataServerInterval',
  full_name='DataServerInterval',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='DataServerInterval.start', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='DataServerInterval.end', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=361,
  serialized_end=409,
)


_DATASERVERSTATE = _descriptor.Descriptor(
  name='DataServerState',
  full_name='DataServerState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='DataServerState.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='load', full_name='DataServerState.load', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='DataServerState.size', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_components', full_name='DataServerState.num_components', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avg_component', full_name='DataServerState.avg_component', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DATASERVERSTATE_STATUS,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=412,
  serialized_end=583,
)


_DATASERVERINFORMATION = _descriptor.Descriptor(
  name='DataServerInformation',
  full_name='DataServerInformation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='DataServerInformation.index', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address', full_name='DataServerInformation.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='DataServerInformation.port', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='DataServerInformation.state', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='interval', full_name='DataServerInformation.interval', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=586,
  serialized_end=727,
)


_DATASERVERMAPPING = _descriptor.Descriptor(
  name='DataServerMapping',
  full_name='DataServerMapping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='DataServerMapping.version', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_servers', full_name='DataServerMapping.num_servers', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='servers', full_name='DataServerMapping.servers', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='routing', full_name='DataServerMapping.routing', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=729,
  serialized_end=844,
)


_DATASERVERCLIENTINFORMATION = _descriptor.Descriptor(
  name='DataServerClientInformation',
  full_name='DataServerClientInformation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='DataServerClientInformation.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='DataServerClientInformation.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='DataServerClientInformation.permissions', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=846,
  serialized_end=932,
)


_DATASERVERCLIENTCREDENTIALS = _descriptor.Descriptor(
  name='DataServerClientCredentials',
  full_name='DataServerClientCredentials',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='users', full_name='DataServerClientCredentials.users', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=934,
  serialized_end=1008,
)


_DATASERVERREBALANCE = _descriptor.Descriptor(
  name='DataServerRebalance',
  full_name='DataServerRebalance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='DataServerRebalance.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mapping', full_name='DataServerRebalance.mapping', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='moving', full_name='DataServerRebalance.moving', index=2,
      number=3, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1010,
  serialized_end=1096,
)


_DATASERVERFILECOPY = _descriptor.Descriptor(
  name='DataServerFileCopy',
  full_name='DataServerFileCopy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rebalance_id', full_name='DataServerFileCopy.rebalance_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='directory', full_name='DataServerFileCopy.directory', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filename', full_name='DataServerFileCopy.filename', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='DataServerFileCopy.size', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1098,
  serialized_end=1191,
)

_DATASTORECOMMAND.fields_by_name['command'].enum_type = _DATASTORECOMMAND_COMMAND
_DATASTORECOMMAND.fields_by_name['request'].message_type = grr.proto.data_store_pb2._DATASTOREREQUEST
_DATASTORECOMMAND_COMMAND.containing_type = _DATASTORECOMMAND;
_DATASERVERSTATE.fields_by_name['status'].enum_type = _DATASERVERSTATE_STATUS
_DATASERVERSTATE_STATUS.containing_type = _DATASERVERSTATE;
_DATASERVERINFORMATION.fields_by_name['state'].message_type = _DATASERVERSTATE
_DATASERVERINFORMATION.fields_by_name['interval'].message_type = _DATASERVERINTERVAL
_DATASERVERMAPPING.fields_by_name['servers'].message_type = _DATASERVERINFORMATION
_DATASERVERCLIENTCREDENTIALS.fields_by_name['users'].message_type = _DATASERVERCLIENTINFORMATION
_DATASERVERREBALANCE.fields_by_name['mapping'].message_type = _DATASERVERMAPPING
DESCRIPTOR.message_types_by_name['DataStoreCommand'] = _DATASTORECOMMAND
DESCRIPTOR.message_types_by_name['DataServerInterval'] = _DATASERVERINTERVAL
DESCRIPTOR.message_types_by_name['DataServerState'] = _DATASERVERSTATE
DESCRIPTOR.message_types_by_name['DataServerInformation'] = _DATASERVERINFORMATION
DESCRIPTOR.message_types_by_name['DataServerMapping'] = _DATASERVERMAPPING
DESCRIPTOR.message_types_by_name['DataServerClientInformation'] = _DATASERVERCLIENTINFORMATION
DESCRIPTOR.message_types_by_name['DataServerClientCredentials'] = _DATASERVERCLIENTCREDENTIALS
DESCRIPTOR.message_types_by_name['DataServerRebalance'] = _DATASERVERREBALANCE
DESCRIPTOR.message_types_by_name['DataServerFileCopy'] = _DATASERVERFILECOPY

class DataStoreCommand(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DATASTORECOMMAND

  # @@protoc_insertion_point(class_scope:DataStoreCommand)

class DataServerInterval(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DATASERVERINTERVAL

  # @@protoc_insertion_point(class_scope:DataServerInterval)

class DataServerState(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DATASERVERSTATE

  # @@protoc_insertion_point(class_scope:DataServerState)

class DataServerInformation(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DATASERVERINFORMATION

  # @@protoc_insertion_point(class_scope:DataServerInformation)

class DataServerMapping(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DATASERVERMAPPING

  # @@protoc_insertion_point(class_scope:DataServerMapping)

class DataServerClientInformation(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DATASERVERCLIENTINFORMATION

  # @@protoc_insertion_point(class_scope:DataServerClientInformation)

class DataServerClientCredentials(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DATASERVERCLIENTCREDENTIALS

  # @@protoc_insertion_point(class_scope:DataServerClientCredentials)

class DataServerRebalance(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DATASERVERREBALANCE

  # @@protoc_insertion_point(class_scope:DataServerRebalance)

class DataServerFileCopy(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DATASERVERFILECOPY

  # @@protoc_insertion_point(class_scope:DataServerFileCopy)


# @@protoc_insertion_point(module_scope)
