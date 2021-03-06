# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: syft_proto/types/torch/v1/tensor.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft_proto.types.syft.v1 import id_pb2 as syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2
from syft_proto.types.torch.v1 import tensor_data_pb2 as syft__proto_dot_types_dot_torch_dot_v1_dot_tensor__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='syft_proto/types/torch/v1/tensor.proto',
  package='syft_proto.types.torch.v1',
  syntax='proto3',
  serialized_options=b'\n&org.openmined.syftproto.types.torch.v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&syft_proto/types/torch/v1/tensor.proto\x12\x19syft_proto.types.torch.v1\x1a!syft_proto/types/syft/v1/id.proto\x1a+syft_proto/types/torch/v1/tensor_data.proto\"\xc5\x04\n\x0bTorchTensor\x12,\n\x02id\x18\x01 \x01(\x0b\x32\x1c.syft_proto.types.syft.v1.IdR\x02id\x12L\n\rcontents_data\x18\x02 \x01(\x0b\x32%.syft_proto.types.torch.v1.TensorDataH\x00R\x0c\x63ontentsData\x12#\n\x0c\x63ontents_bin\x18\x03 \x01(\x0cH\x00R\x0b\x63ontentsBin\x12<\n\x05\x63hain\x18\x04 \x01(\x0b\x32&.syft_proto.types.torch.v1.TorchTensorR\x05\x63hain\x12\x45\n\ngrad_chain\x18\x05 \x01(\x0b\x32&.syft_proto.types.torch.v1.TorchTensorR\tgradChain\x12\x12\n\x04tags\x18\x06 \x03(\tR\x04tags\x12 \n\x0b\x64\x65scription\x18\x07 \x01(\tR\x0b\x64\x65scription\x12Q\n\nserializer\x18\x08 \x01(\x0e\x32\x31.syft_proto.types.torch.v1.TorchTensor.SerializerR\nserializer\"{\n\nSerializer\x12\x1a\n\x16SERIALIZER_UNSPECIFIED\x10\x00\x12\x14\n\x10SERIALIZER_TORCH\x10\x01\x12\x14\n\x10SERIALIZER_NUMPY\x10\x02\x12\x11\n\rSERIALIZER_TF\x10\x03\x12\x12\n\x0eSERIALIZER_ALL\x10\x04\x42\n\n\x08\x63ontentsB(\n&org.openmined.syftproto.types.torch.v1b\x06proto3'
  ,
  dependencies=[syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2.DESCRIPTOR,syft__proto_dot_types_dot_torch_dot_v1_dot_tensor__data__pb2.DESCRIPTOR,])



_TORCHTENSOR_SERIALIZER = _descriptor.EnumDescriptor(
  name='Serializer',
  full_name='syft_proto.types.torch.v1.TorchTensor.Serializer',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SERIALIZER_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SERIALIZER_TORCH', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SERIALIZER_NUMPY', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SERIALIZER_TF', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SERIALIZER_ALL', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=596,
  serialized_end=719,
)
_sym_db.RegisterEnumDescriptor(_TORCHTENSOR_SERIALIZER)


_TORCHTENSOR = _descriptor.Descriptor(
  name='TorchTensor',
  full_name='syft_proto.types.torch.v1.TorchTensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='syft_proto.types.torch.v1.TorchTensor.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents_data', full_name='syft_proto.types.torch.v1.TorchTensor.contents_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsData', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents_bin', full_name='syft_proto.types.torch.v1.TorchTensor.contents_bin', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsBin', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chain', full_name='syft_proto.types.torch.v1.TorchTensor.chain', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='chain', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='grad_chain', full_name='syft_proto.types.torch.v1.TorchTensor.grad_chain', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='gradChain', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='syft_proto.types.torch.v1.TorchTensor.tags', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='tags', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='syft_proto.types.torch.v1.TorchTensor.description', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='description', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serializer', full_name='syft_proto.types.torch.v1.TorchTensor.serializer', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='serializer', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TORCHTENSOR_SERIALIZER,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='contents', full_name='syft_proto.types.torch.v1.TorchTensor.contents',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=150,
  serialized_end=731,
)

_TORCHTENSOR.fields_by_name['id'].message_type = syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2._ID
_TORCHTENSOR.fields_by_name['contents_data'].message_type = syft__proto_dot_types_dot_torch_dot_v1_dot_tensor__data__pb2._TENSORDATA
_TORCHTENSOR.fields_by_name['chain'].message_type = _TORCHTENSOR
_TORCHTENSOR.fields_by_name['grad_chain'].message_type = _TORCHTENSOR
_TORCHTENSOR.fields_by_name['serializer'].enum_type = _TORCHTENSOR_SERIALIZER
_TORCHTENSOR_SERIALIZER.containing_type = _TORCHTENSOR
_TORCHTENSOR.oneofs_by_name['contents'].fields.append(
  _TORCHTENSOR.fields_by_name['contents_data'])
_TORCHTENSOR.fields_by_name['contents_data'].containing_oneof = _TORCHTENSOR.oneofs_by_name['contents']
_TORCHTENSOR.oneofs_by_name['contents'].fields.append(
  _TORCHTENSOR.fields_by_name['contents_bin'])
_TORCHTENSOR.fields_by_name['contents_bin'].containing_oneof = _TORCHTENSOR.oneofs_by_name['contents']
DESCRIPTOR.message_types_by_name['TorchTensor'] = _TORCHTENSOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TorchTensor = _reflection.GeneratedProtocolMessageType('TorchTensor', (_message.Message,), {
  'DESCRIPTOR' : _TORCHTENSOR,
  '__module__' : 'syft_proto.types.torch.v1.tensor_pb2'
  # @@protoc_insertion_point(class_scope:syft_proto.types.torch.v1.TorchTensor)
  })
_sym_db.RegisterMessage(TorchTensor)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
