# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grr/proto/artifact.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import grr.proto.jobs_pb2
import grr.proto.semantic_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='grr/proto/artifact.proto',
  package='',
  serialized_pb='\n\x18grr/proto/artifact.proto\x1a\x14grr/proto/jobs.proto\x1a\x18grr/proto/semantic.proto\"\x87\x06\n\tCollector\x12P\n\x0e\x63ollector_type\x18\x01 \x01(\x0e\x32\x18.Collector.CollectorTypeB\x1e\xe2\xfc\xe3\xc4\x01\x18\x12\x16The type of collector.\x12K\n\x04\x61rgs\x18\x02 \x01(\x0b\x32\x05.DictB6\xe2\xfc\xe3\xc4\x01\x30\x12.The name of the action the collector performs.\x12n\n\nconditions\x18\x03 \x03(\tBZ\xe2\xfc\xe3\xc4\x01T\x12RObject filter conditions that decide if this collector will run on a given system.\x12\x90\x01\n\x0ereturned_types\x18\x04 \x03(\tBx\xe2\xfc\xe3\xc4\x01r\x12pA list types that may be returned by this artifact. Anything returned that is not in this list will be filtered.\x12~\n\x0csupported_os\x18\x05 \x03(\tBh\xe2\xfc\xe3\xc4\x01\x62\x12`A list of operating systems the collector will use to decide if it should run on a given system.\"\xd7\x01\n\rCollectorType\x12\x1a\n\x16\x43OLLECTOR_TYPE_UNKNOWN\x10\x00\x12\x08\n\x04\x46ILE\x10\x01\x12\x10\n\x0cREGISTRY_KEY\x10\x02\x12\x12\n\x0eREGISTRY_VALUE\x10\x03\x12\x07\n\x03WMI\x10\x04\x12\x0c\n\x08\x41RTIFACT\x10\x05\x12\x15\n\x11GRR_CLIENT_ACTION\x10(\x12\x0e\n\nLIST_FILES\x10)\x12\x12\n\x0e\x41RTIFACT_FILES\x10*\x12\x08\n\x04GREP\x10+\x12\x0b\n\x07\x43OMMAND\x10-\x12\x11\n\rREKALL_PLUGIN\x10.\"\xca\x04\n\x08\x41rtifact\x12;\n\x04name\x18\x01 \x01(\tB-\xe2\xfc\xe3\xc4\x01\'\x12%Globally unique name of the artifact.\x12X\n\nconditions\x18\x02 \x03(\tBD\xe2\xfc\xe3\xc4\x01>\x12<A list of conditions that decide if the artifact should run.\x12\x31\n\x03\x64oc\x18\x03 \x01(\tB$\xe2\xfc\xe3\xc4\x01\x1e\x12\x1c\x44oc string for the artifact.\x12\x41\n\x06labels\x18\x04 \x03(\tB1\xe2\xfc\xe3\xc4\x01+\x12)A list of labels the artifact belongs to.\x12P\n\x0csupported_os\x18\x05 \x03(\tB:\xe2\xfc\xe3\xc4\x01\x34\x12\x32\x41 list of operating systems the artifact supports.\x12\x45\n\x04urls\x18\x06 \x03(\tB7\xe2\xfc\xe3\xc4\x01\x31\x12/A list of urls that help document the artifact.\x12\x46\n\ncollectors\x18\x07 \x03(\x0b\x32\n.CollectorB&\xe2\xfc\xe3\xc4\x01 \x12\x1e\x41 list of artifact collectors.\x12P\n\x08provides\x18\x08 \x03(\tB>\xe2\xfc\xe3\xc4\x01\x38\x12\x36\x41 list of knowledgebase values this artifact provides.')



_COLLECTOR_COLLECTORTYPE = _descriptor.EnumDescriptor(
  name='CollectorType',
  full_name='Collector.CollectorType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COLLECTOR_TYPE_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTRY_KEY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTRY_VALUE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WMI', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARTIFACT', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRR_CLIENT_ACTION', index=6, number=40,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIST_FILES', index=7, number=41,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARTIFACT_FILES', index=8, number=42,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GREP', index=9, number=43,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMAND', index=10, number=45,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REKALL_PLUGIN', index=11, number=46,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=637,
  serialized_end=852,
)


_COLLECTOR = _descriptor.Descriptor(
  name='Collector',
  full_name='Collector',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='collector_type', full_name='Collector.collector_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\342\374\343\304\001\030\022\026The type of collector.')),
    _descriptor.FieldDescriptor(
      name='args', full_name='Collector.args', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\342\374\343\304\0010\022.The name of the action the collector performs.')),
    _descriptor.FieldDescriptor(
      name='conditions', full_name='Collector.conditions', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\342\374\343\304\001T\022RObject filter conditions that decide if this collector will run on a given system.')),
    _descriptor.FieldDescriptor(
      name='returned_types', full_name='Collector.returned_types', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\342\374\343\304\001r\022pA list types that may be returned by this artifact. Anything returned that is not in this list will be filtered.')),
    _descriptor.FieldDescriptor(
      name='supported_os', full_name='Collector.supported_os', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\342\374\343\304\001b\022`A list of operating systems the collector will use to decide if it should run on a given system.')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COLLECTOR_COLLECTORTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=77,
  serialized_end=852,
)


_ARTIFACT = _descriptor.Descriptor(
  name='Artifact',
  full_name='Artifact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Artifact.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\342\374\343\304\001\'\022%Globally unique name of the artifact.')),
    _descriptor.FieldDescriptor(
      name='conditions', full_name='Artifact.conditions', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\342\374\343\304\001>\022<A list of conditions that decide if the artifact should run.')),
    _descriptor.FieldDescriptor(
      name='doc', full_name='Artifact.doc', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\342\374\343\304\001\036\022\034Doc string for the artifact.')),
    _descriptor.FieldDescriptor(
      name='labels', full_name='Artifact.labels', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\342\374\343\304\001+\022)A list of labels the artifact belongs to.')),
    _descriptor.FieldDescriptor(
      name='supported_os', full_name='Artifact.supported_os', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\342\374\343\304\0014\0222A list of operating systems the artifact supports.')),
    _descriptor.FieldDescriptor(
      name='urls', full_name='Artifact.urls', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\342\374\343\304\0011\022/A list of urls that help document the artifact.')),
    _descriptor.FieldDescriptor(
      name='collectors', full_name='Artifact.collectors', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\342\374\343\304\001 \022\036A list of artifact collectors.')),
    _descriptor.FieldDescriptor(
      name='provides', full_name='Artifact.provides', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\342\374\343\304\0018\0226A list of knowledgebase values this artifact provides.')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=855,
  serialized_end=1441,
)

_COLLECTOR.fields_by_name['collector_type'].enum_type = _COLLECTOR_COLLECTORTYPE
_COLLECTOR.fields_by_name['args'].message_type = grr.proto.jobs_pb2._DICT
_COLLECTOR_COLLECTORTYPE.containing_type = _COLLECTOR;
_ARTIFACT.fields_by_name['collectors'].message_type = _COLLECTOR
DESCRIPTOR.message_types_by_name['Collector'] = _COLLECTOR
DESCRIPTOR.message_types_by_name['Artifact'] = _ARTIFACT

class Collector(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COLLECTOR

  # @@protoc_insertion_point(class_scope:Collector)

class Artifact(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ARTIFACT

  # @@protoc_insertion_point(class_scope:Artifact)


_COLLECTOR.fields_by_name['collector_type'].has_options = True
_COLLECTOR.fields_by_name['collector_type']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\342\374\343\304\001\030\022\026The type of collector.')
_COLLECTOR.fields_by_name['args'].has_options = True
_COLLECTOR.fields_by_name['args']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\342\374\343\304\0010\022.The name of the action the collector performs.')
_COLLECTOR.fields_by_name['conditions'].has_options = True
_COLLECTOR.fields_by_name['conditions']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\342\374\343\304\001T\022RObject filter conditions that decide if this collector will run on a given system.')
_COLLECTOR.fields_by_name['returned_types'].has_options = True
_COLLECTOR.fields_by_name['returned_types']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\342\374\343\304\001r\022pA list types that may be returned by this artifact. Anything returned that is not in this list will be filtered.')
_COLLECTOR.fields_by_name['supported_os'].has_options = True
_COLLECTOR.fields_by_name['supported_os']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\342\374\343\304\001b\022`A list of operating systems the collector will use to decide if it should run on a given system.')
_ARTIFACT.fields_by_name['name'].has_options = True
_ARTIFACT.fields_by_name['name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\342\374\343\304\001\'\022%Globally unique name of the artifact.')
_ARTIFACT.fields_by_name['conditions'].has_options = True
_ARTIFACT.fields_by_name['conditions']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\342\374\343\304\001>\022<A list of conditions that decide if the artifact should run.')
_ARTIFACT.fields_by_name['doc'].has_options = True
_ARTIFACT.fields_by_name['doc']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\342\374\343\304\001\036\022\034Doc string for the artifact.')
_ARTIFACT.fields_by_name['labels'].has_options = True
_ARTIFACT.fields_by_name['labels']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\342\374\343\304\001+\022)A list of labels the artifact belongs to.')
_ARTIFACT.fields_by_name['supported_os'].has_options = True
_ARTIFACT.fields_by_name['supported_os']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\342\374\343\304\0014\0222A list of operating systems the artifact supports.')
_ARTIFACT.fields_by_name['urls'].has_options = True
_ARTIFACT.fields_by_name['urls']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\342\374\343\304\0011\022/A list of urls that help document the artifact.')
_ARTIFACT.fields_by_name['collectors'].has_options = True
_ARTIFACT.fields_by_name['collectors']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\342\374\343\304\001 \022\036A list of artifact collectors.')
_ARTIFACT.fields_by_name['provides'].has_options = True
_ARTIFACT.fields_by_name['provides']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\342\374\343\304\0018\0226A list of knowledgebase values this artifact provides.')
# @@protoc_insertion_point(module_scope)
