# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: syft_proto/generic/pointers/v1/object_pointer.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft_proto.types.syft.v1 import id_pb2 as syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='syft_proto/generic/pointers/v1/object_pointer.proto',
  package='syft_proto.generic.pointers.v1',
  syntax='proto3',
  serialized_options=b'\n+org.openmined.syftproto.generic.pointers.v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n3syft_proto/generic/pointers/v1/object_pointer.proto\x12\x1esyft_proto.generic.pointers.v1\x1a!syft_proto/types/syft/v1/id.proto\"\xfe\x01\n\rObjectPointer\x12\x39\n\tobject_id\x18\x01 \x01(\x0b\x32\x1c.syft_proto.types.syft.v1.IdR\x08objectId\x12=\n\x0blocation_id\x18\x02 \x01(\x0b\x32\x1c.syft_proto.types.syft.v1.IdR\nlocationId\x12O\n\x15object_id_at_location\x18\x03 \x01(\x0b\x32\x1c.syft_proto.types.syft.v1.IdR\x12objectIdAtLocation\x12\"\n\rpoint_to_attr\x18\x04 \x01(\tR\x0bpointToAttrB-\n+org.openmined.syftproto.generic.pointers.v1b\x06proto3'
  ,
  dependencies=[syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2.DESCRIPTOR,])




_OBJECTPOINTER = _descriptor.Descriptor(
  name='ObjectPointer',
  full_name='syft_proto.generic.pointers.v1.ObjectPointer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_id', full_name='syft_proto.generic.pointers.v1.ObjectPointer.object_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='objectId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location_id', full_name='syft_proto.generic.pointers.v1.ObjectPointer.location_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='locationId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='object_id_at_location', full_name='syft_proto.generic.pointers.v1.ObjectPointer.object_id_at_location', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='objectIdAtLocation', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='point_to_attr', full_name='syft_proto.generic.pointers.v1.ObjectPointer.point_to_attr', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pointToAttr', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=123,
  serialized_end=377,
)

_OBJECTPOINTER.fields_by_name['object_id'].message_type = syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2._ID
_OBJECTPOINTER.fields_by_name['location_id'].message_type = syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2._ID
_OBJECTPOINTER.fields_by_name['object_id_at_location'].message_type = syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2._ID
DESCRIPTOR.message_types_by_name['ObjectPointer'] = _OBJECTPOINTER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObjectPointer = _reflection.GeneratedProtocolMessageType('ObjectPointer', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTPOINTER,
  '__module__' : 'syft_proto.generic.pointers.v1.object_pointer_pb2'
  # @@protoc_insertion_point(class_scope:syft_proto.generic.pointers.v1.ObjectPointer)
  })
_sym_db.RegisterMessage(ObjectPointer)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
