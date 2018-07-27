# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: automanlib_classes.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='automanlib_classes.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x18\x61utomanlib_classes.proto\"\x17\n\tDimension\x12\n\n\x02id\x18\x01 \x01(\t\"\xd7\x03\n\x04Task\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x11\n\timage_url\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x13\n\x0bimg_alt_txt\x18\x04 \x01(\t\x12\x0f\n\x07pattern\x18\x05 \x01(\t\x12\x0e\n\x06\x62udget\x18\x06 \x01(\x01\x12\x12\n\nconfidence\x18\x07 \x01(\x01\x12\x13\n\x0bsample_size\x18\x08 \x01(\x05\x12\x0f\n\x07options\x18\t \x03(\t\x12\x1e\n\ndimensions\x18\n \x03(\x0b\x32\n.Dimension\x12\x13\n\x0b\x64ont_reject\x18\x0b \x01(\x08\x12\x1a\n\x12pay_all_on_failure\x18\x0c \x01(\x08\x12\x0f\n\x07\x64ry_run\x18\r \x01(\x08\x12\x1b\n\x13\x61llow_empty_pattern\x18\x0e \x01(\x08\x12\x1a\n\x12pattern_error_text\x18\x10 \x01(\t\x12#\n\x1bquestion_timeout_multiplier\x18\x11 \x01(\x05\x12#\n\x1binitial_worker_timeout_in_s\x18\x12 \x01(\x05\x12\x0c\n\x04wage\x18\x13 \x01(\x01\x12\x11\n\tmax_value\x18\x14 \x01(\x01\x12\x11\n\tmin_value\x18\x15 \x01(\x01\x12\x16\n\x0e\x63onfidence_int\x18\x16 \x01(\x01\"\x15\n\x13UnconstrainedConInt\"\x1e\n\x0fSymmetricConInt\x12\x0b\n\x03\x65rr\x18\x01 \x01(\x01\"5\n\x10\x41symmetricConInt\x12\x0f\n\x07low_err\x18\x01 \x01(\x01\x12\x10\n\x08high_err\x18\x02 \x01(\x01\"R\n\x0cValueOutcome\x12\x0b\n\x03\x65st\x18\x01 \x01(\x01\x12\x0b\n\x03low\x18\x02 \x01(\x01\x12\x0c\n\x04high\x18\x03 \x01(\x01\x12\x0c\n\x04\x63ost\x18\x04 \x01(\x01\x12\x0c\n\x04\x63onf\x18\x05 \x01(\x01\"\x1f\n\rStringOutcome\x12\x0e\n\x06option\x18\x01 \x01(\t\"\x98\x02\n\x12\x41\x64\x61pterCredentials\x12\x33\n\nadptr_type\x18\x01 \x01(\x0e\x32\x1f.AdapterCredentials.AdapterType\x12\x11\n\taccess_id\x18\x02 \x01(\t\x12\x12\n\naccess_key\x18\x03 \x01(\t\x12@\n\x0f\x61\x64\x61pter_options\x18\x04 \x03(\x0b\x32\'.AdapterCredentials.AdapterOptionsEntry\x1a\x35\n\x13\x41\x64\x61pterOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"-\n\x0b\x41\x64\x61pterType\x12\x13\n\x0fUNKNOWN_ADAPTER\x10\x00\x12\t\n\x05MTURK\x10\x01*U\n\x0bOutcomeType\x12\x13\n\x0fUNKNOWN_OUTCOME\x10\x00\x12\r\n\tCONFIDENT\x10\x01\x12\x12\n\x0eLOW_CONFIDENCE\x10\x02\x12\x0e\n\nOVERBUDGET\x10\x03\x62\x06proto3')
)

_OUTCOMETYPE = _descriptor.EnumDescriptor(
  name='OutcomeType',
  full_name='OutcomeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_OUTCOME', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIDENT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOW_CONFIDENCE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OVERBUDGET', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1037,
  serialized_end=1122,
)
_sym_db.RegisterEnumDescriptor(_OUTCOMETYPE)

OutcomeType = enum_type_wrapper.EnumTypeWrapper(_OUTCOMETYPE)
UNKNOWN_OUTCOME = 0
CONFIDENT = 1
LOW_CONFIDENCE = 2
OVERBUDGET = 3


_ADAPTERCREDENTIALS_ADAPTERTYPE = _descriptor.EnumDescriptor(
  name='AdapterType',
  full_name='AdapterCredentials.AdapterType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_ADAPTER', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MTURK', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=990,
  serialized_end=1035,
)
_sym_db.RegisterEnumDescriptor(_ADAPTERCREDENTIALS_ADAPTERTYPE)


_DIMENSION = _descriptor.Descriptor(
  name='Dimension',
  full_name='Dimension',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Dimension.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=51,
)


_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='Task.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_url', full_name='Task.image_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='Task.title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='img_alt_txt', full_name='Task.img_alt_txt', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pattern', full_name='Task.pattern', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='budget', full_name='Task.budget', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='Task.confidence', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sample_size', full_name='Task.sample_size', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='Task.options', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dimensions', full_name='Task.dimensions', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dont_reject', full_name='Task.dont_reject', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pay_all_on_failure', full_name='Task.pay_all_on_failure', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dry_run', full_name='Task.dry_run', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allow_empty_pattern', full_name='Task.allow_empty_pattern', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pattern_error_text', full_name='Task.pattern_error_text', index=14,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='question_timeout_multiplier', full_name='Task.question_timeout_multiplier', index=15,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initial_worker_timeout_in_s', full_name='Task.initial_worker_timeout_in_s', index=16,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wage', full_name='Task.wage', index=17,
      number=19, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_value', full_name='Task.max_value', index=18,
      number=20, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_value', full_name='Task.min_value', index=19,
      number=21, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confidence_int', full_name='Task.confidence_int', index=20,
      number=22, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=525,
)


_UNCONSTRAINEDCONINT = _descriptor.Descriptor(
  name='UnconstrainedConInt',
  full_name='UnconstrainedConInt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=527,
  serialized_end=548,
)


_SYMMETRICCONINT = _descriptor.Descriptor(
  name='SymmetricConInt',
  full_name='SymmetricConInt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='SymmetricConInt.err', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=550,
  serialized_end=580,
)


_ASYMMETRICCONINT = _descriptor.Descriptor(
  name='AsymmetricConInt',
  full_name='AsymmetricConInt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='low_err', full_name='AsymmetricConInt.low_err', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='high_err', full_name='AsymmetricConInt.high_err', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=582,
  serialized_end=635,
)


_VALUEOUTCOME = _descriptor.Descriptor(
  name='ValueOutcome',
  full_name='ValueOutcome',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='est', full_name='ValueOutcome.est', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='low', full_name='ValueOutcome.low', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='high', full_name='ValueOutcome.high', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cost', full_name='ValueOutcome.cost', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conf', full_name='ValueOutcome.conf', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=637,
  serialized_end=719,
)


_STRINGOUTCOME = _descriptor.Descriptor(
  name='StringOutcome',
  full_name='StringOutcome',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='option', full_name='StringOutcome.option', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=721,
  serialized_end=752,
)


_ADAPTERCREDENTIALS_ADAPTEROPTIONSENTRY = _descriptor.Descriptor(
  name='AdapterOptionsEntry',
  full_name='AdapterCredentials.AdapterOptionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='AdapterCredentials.AdapterOptionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='AdapterCredentials.AdapterOptionsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=935,
  serialized_end=988,
)

_ADAPTERCREDENTIALS = _descriptor.Descriptor(
  name='AdapterCredentials',
  full_name='AdapterCredentials',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='adptr_type', full_name='AdapterCredentials.adptr_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_id', full_name='AdapterCredentials.access_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_key', full_name='AdapterCredentials.access_key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adapter_options', full_name='AdapterCredentials.adapter_options', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ADAPTERCREDENTIALS_ADAPTEROPTIONSENTRY, ],
  enum_types=[
    _ADAPTERCREDENTIALS_ADAPTERTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=755,
  serialized_end=1035,
)

_TASK.fields_by_name['dimensions'].message_type = _DIMENSION
_ADAPTERCREDENTIALS_ADAPTEROPTIONSENTRY.containing_type = _ADAPTERCREDENTIALS
_ADAPTERCREDENTIALS.fields_by_name['adptr_type'].enum_type = _ADAPTERCREDENTIALS_ADAPTERTYPE
_ADAPTERCREDENTIALS.fields_by_name['adapter_options'].message_type = _ADAPTERCREDENTIALS_ADAPTEROPTIONSENTRY
_ADAPTERCREDENTIALS_ADAPTERTYPE.containing_type = _ADAPTERCREDENTIALS
DESCRIPTOR.message_types_by_name['Dimension'] = _DIMENSION
DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.message_types_by_name['UnconstrainedConInt'] = _UNCONSTRAINEDCONINT
DESCRIPTOR.message_types_by_name['SymmetricConInt'] = _SYMMETRICCONINT
DESCRIPTOR.message_types_by_name['AsymmetricConInt'] = _ASYMMETRICCONINT
DESCRIPTOR.message_types_by_name['ValueOutcome'] = _VALUEOUTCOME
DESCRIPTOR.message_types_by_name['StringOutcome'] = _STRINGOUTCOME
DESCRIPTOR.message_types_by_name['AdapterCredentials'] = _ADAPTERCREDENTIALS
DESCRIPTOR.enum_types_by_name['OutcomeType'] = _OUTCOMETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Dimension = _reflection.GeneratedProtocolMessageType('Dimension', (_message.Message,), dict(
  DESCRIPTOR = _DIMENSION,
  __module__ = 'automanlib_classes_pb2'
  # @@protoc_insertion_point(class_scope:Dimension)
  ))
_sym_db.RegisterMessage(Dimension)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), dict(
  DESCRIPTOR = _TASK,
  __module__ = 'automanlib_classes_pb2'
  # @@protoc_insertion_point(class_scope:Task)
  ))
_sym_db.RegisterMessage(Task)

UnconstrainedConInt = _reflection.GeneratedProtocolMessageType('UnconstrainedConInt', (_message.Message,), dict(
  DESCRIPTOR = _UNCONSTRAINEDCONINT,
  __module__ = 'automanlib_classes_pb2'
  # @@protoc_insertion_point(class_scope:UnconstrainedConInt)
  ))
_sym_db.RegisterMessage(UnconstrainedConInt)

SymmetricConInt = _reflection.GeneratedProtocolMessageType('SymmetricConInt', (_message.Message,), dict(
  DESCRIPTOR = _SYMMETRICCONINT,
  __module__ = 'automanlib_classes_pb2'
  # @@protoc_insertion_point(class_scope:SymmetricConInt)
  ))
_sym_db.RegisterMessage(SymmetricConInt)

AsymmetricConInt = _reflection.GeneratedProtocolMessageType('AsymmetricConInt', (_message.Message,), dict(
  DESCRIPTOR = _ASYMMETRICCONINT,
  __module__ = 'automanlib_classes_pb2'
  # @@protoc_insertion_point(class_scope:AsymmetricConInt)
  ))
_sym_db.RegisterMessage(AsymmetricConInt)

ValueOutcome = _reflection.GeneratedProtocolMessageType('ValueOutcome', (_message.Message,), dict(
  DESCRIPTOR = _VALUEOUTCOME,
  __module__ = 'automanlib_classes_pb2'
  # @@protoc_insertion_point(class_scope:ValueOutcome)
  ))
_sym_db.RegisterMessage(ValueOutcome)

StringOutcome = _reflection.GeneratedProtocolMessageType('StringOutcome', (_message.Message,), dict(
  DESCRIPTOR = _STRINGOUTCOME,
  __module__ = 'automanlib_classes_pb2'
  # @@protoc_insertion_point(class_scope:StringOutcome)
  ))
_sym_db.RegisterMessage(StringOutcome)

AdapterCredentials = _reflection.GeneratedProtocolMessageType('AdapterCredentials', (_message.Message,), dict(

  AdapterOptionsEntry = _reflection.GeneratedProtocolMessageType('AdapterOptionsEntry', (_message.Message,), dict(
    DESCRIPTOR = _ADAPTERCREDENTIALS_ADAPTEROPTIONSENTRY,
    __module__ = 'automanlib_classes_pb2'
    # @@protoc_insertion_point(class_scope:AdapterCredentials.AdapterOptionsEntry)
    ))
  ,
  DESCRIPTOR = _ADAPTERCREDENTIALS,
  __module__ = 'automanlib_classes_pb2'
  # @@protoc_insertion_point(class_scope:AdapterCredentials)
  ))
_sym_db.RegisterMessage(AdapterCredentials)
_sym_db.RegisterMessage(AdapterCredentials.AdapterOptionsEntry)


_ADAPTERCREDENTIALS_ADAPTEROPTIONSENTRY.has_options = True
_ADAPTERCREDENTIALS_ADAPTEROPTIONSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
