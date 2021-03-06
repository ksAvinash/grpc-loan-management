# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: loan.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='loan.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nloan.proto\"g\n\x11\x63reateLoanRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x15\n\rinterest_rate\x18\x02 \x01(\x02\x12\x17\n\x0frepayment_terms\x18\x03 \x01(\x05\x12\x13\n\x0bloan_amount\x18\x04 \x01(\x05\"%\n\x12\x63reateLoanResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"%\n\x14showRepaymentRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"\x8f\x01\n\rrepaymentItem\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x11\n\tprincipal\x18\x02 \x01(\x05\x12\x10\n\x08interest\x18\x03 \x01(\x02\x12\r\n\x05total\x18\x04 \x01(\x05\x12\x0c\n\x04\x64\x61te\x18\x05 \x01(\t\x12\x0e\n\x06status\x18\x06 \x01(\t\x12\r\n\x05\x65mail\x18\x07 \x01(\t\x12\x0f\n\x07loan_no\x18\x08 \x01(\t\"6\n\x15showRepaymentResponse\x12\x1d\n\x05items\x18\x01 \x03(\x0b\x32\x0e.repaymentItem\"C\n\x14makeRepaymentRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x0c\n\x04term\x18\x02 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x05\"(\n\x15makeRepaymentResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\xcb\x01\n\nQuikLoaner\x12\x36\n\tsave_loan\x12\x12.createLoanRequest\x1a\x13.createLoanResponse\"\x00\x12\x42\n\x0fshow_repayments\x12\x15.showRepaymentRequest\x1a\x16.showRepaymentResponse\"\x00\x12\x41\n\x0emake_repayment\x12\x15.makeRepaymentRequest\x1a\x16.makeRepaymentResponse\"\x00\x62\x06proto3'
)




_CREATELOANREQUEST = _descriptor.Descriptor(
  name='createLoanRequest',
  full_name='createLoanRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='createLoanRequest.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='interest_rate', full_name='createLoanRequest.interest_rate', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='repayment_terms', full_name='createLoanRequest.repayment_terms', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='loan_amount', full_name='createLoanRequest.loan_amount', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=14,
  serialized_end=117,
)


_CREATELOANRESPONSE = _descriptor.Descriptor(
  name='createLoanResponse',
  full_name='createLoanResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='createLoanResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=119,
  serialized_end=156,
)


_SHOWREPAYMENTREQUEST = _descriptor.Descriptor(
  name='showRepaymentRequest',
  full_name='showRepaymentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='showRepaymentRequest.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=158,
  serialized_end=195,
)


_REPAYMENTITEM = _descriptor.Descriptor(
  name='repaymentItem',
  full_name='repaymentItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='term', full_name='repaymentItem.term', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='principal', full_name='repaymentItem.principal', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='interest', full_name='repaymentItem.interest', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total', full_name='repaymentItem.total', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date', full_name='repaymentItem.date', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='repaymentItem.status', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='repaymentItem.email', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='loan_no', full_name='repaymentItem.loan_no', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=198,
  serialized_end=341,
)


_SHOWREPAYMENTRESPONSE = _descriptor.Descriptor(
  name='showRepaymentResponse',
  full_name='showRepaymentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='showRepaymentResponse.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=343,
  serialized_end=397,
)


_MAKEREPAYMENTREQUEST = _descriptor.Descriptor(
  name='makeRepaymentRequest',
  full_name='makeRepaymentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='makeRepaymentRequest.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='term', full_name='makeRepaymentRequest.term', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='makeRepaymentRequest.amount', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=399,
  serialized_end=466,
)


_MAKEREPAYMENTRESPONSE = _descriptor.Descriptor(
  name='makeRepaymentResponse',
  full_name='makeRepaymentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='makeRepaymentResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=468,
  serialized_end=508,
)

_SHOWREPAYMENTRESPONSE.fields_by_name['items'].message_type = _REPAYMENTITEM
DESCRIPTOR.message_types_by_name['createLoanRequest'] = _CREATELOANREQUEST
DESCRIPTOR.message_types_by_name['createLoanResponse'] = _CREATELOANRESPONSE
DESCRIPTOR.message_types_by_name['showRepaymentRequest'] = _SHOWREPAYMENTREQUEST
DESCRIPTOR.message_types_by_name['repaymentItem'] = _REPAYMENTITEM
DESCRIPTOR.message_types_by_name['showRepaymentResponse'] = _SHOWREPAYMENTRESPONSE
DESCRIPTOR.message_types_by_name['makeRepaymentRequest'] = _MAKEREPAYMENTREQUEST
DESCRIPTOR.message_types_by_name['makeRepaymentResponse'] = _MAKEREPAYMENTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

createLoanRequest = _reflection.GeneratedProtocolMessageType('createLoanRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATELOANREQUEST,
  '__module__' : 'loan_pb2'
  # @@protoc_insertion_point(class_scope:createLoanRequest)
  })
_sym_db.RegisterMessage(createLoanRequest)

createLoanResponse = _reflection.GeneratedProtocolMessageType('createLoanResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATELOANRESPONSE,
  '__module__' : 'loan_pb2'
  # @@protoc_insertion_point(class_scope:createLoanResponse)
  })
_sym_db.RegisterMessage(createLoanResponse)

showRepaymentRequest = _reflection.GeneratedProtocolMessageType('showRepaymentRequest', (_message.Message,), {
  'DESCRIPTOR' : _SHOWREPAYMENTREQUEST,
  '__module__' : 'loan_pb2'
  # @@protoc_insertion_point(class_scope:showRepaymentRequest)
  })
_sym_db.RegisterMessage(showRepaymentRequest)

repaymentItem = _reflection.GeneratedProtocolMessageType('repaymentItem', (_message.Message,), {
  'DESCRIPTOR' : _REPAYMENTITEM,
  '__module__' : 'loan_pb2'
  # @@protoc_insertion_point(class_scope:repaymentItem)
  })
_sym_db.RegisterMessage(repaymentItem)

showRepaymentResponse = _reflection.GeneratedProtocolMessageType('showRepaymentResponse', (_message.Message,), {
  'DESCRIPTOR' : _SHOWREPAYMENTRESPONSE,
  '__module__' : 'loan_pb2'
  # @@protoc_insertion_point(class_scope:showRepaymentResponse)
  })
_sym_db.RegisterMessage(showRepaymentResponse)

makeRepaymentRequest = _reflection.GeneratedProtocolMessageType('makeRepaymentRequest', (_message.Message,), {
  'DESCRIPTOR' : _MAKEREPAYMENTREQUEST,
  '__module__' : 'loan_pb2'
  # @@protoc_insertion_point(class_scope:makeRepaymentRequest)
  })
_sym_db.RegisterMessage(makeRepaymentRequest)

makeRepaymentResponse = _reflection.GeneratedProtocolMessageType('makeRepaymentResponse', (_message.Message,), {
  'DESCRIPTOR' : _MAKEREPAYMENTRESPONSE,
  '__module__' : 'loan_pb2'
  # @@protoc_insertion_point(class_scope:makeRepaymentResponse)
  })
_sym_db.RegisterMessage(makeRepaymentResponse)



_QUIKLOANER = _descriptor.ServiceDescriptor(
  name='QuikLoaner',
  full_name='QuikLoaner',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=511,
  serialized_end=714,
  methods=[
  _descriptor.MethodDescriptor(
    name='save_loan',
    full_name='QuikLoaner.save_loan',
    index=0,
    containing_service=None,
    input_type=_CREATELOANREQUEST,
    output_type=_CREATELOANRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='show_repayments',
    full_name='QuikLoaner.show_repayments',
    index=1,
    containing_service=None,
    input_type=_SHOWREPAYMENTREQUEST,
    output_type=_SHOWREPAYMENTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='make_repayment',
    full_name='QuikLoaner.make_repayment',
    index=2,
    containing_service=None,
    input_type=_MAKEREPAYMENTREQUEST,
    output_type=_MAKEREPAYMENTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUIKLOANER)

DESCRIPTOR.services_by_name['QuikLoaner'] = _QUIKLOANER

# @@protoc_insertion_point(module_scope)
