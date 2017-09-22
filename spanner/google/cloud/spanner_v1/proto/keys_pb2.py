# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/spanner_v1/proto/keys.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/spanner_v1/proto/keys.proto',
  package='google.spanner.v1',
  syntax='proto3',
  serialized_pb=_b('\n(google/cloud/spanner_v1/proto/keys.proto\x12\x11google.spanner.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xf4\x01\n\x08KeyRange\x12\x32\n\x0cstart_closed\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.ListValueH\x00\x12\x30\n\nstart_open\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.ListValueH\x00\x12\x30\n\nend_closed\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.ListValueH\x01\x12.\n\x08\x65nd_open\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.ListValueH\x01\x42\x10\n\x0estart_key_typeB\x0e\n\x0c\x65nd_key_type\"l\n\x06KeySet\x12(\n\x04keys\x18\x01 \x03(\x0b\x32\x1a.google.protobuf.ListValue\x12+\n\x06ranges\x18\x02 \x03(\x0b\x32\x1b.google.spanner.v1.KeyRange\x12\x0b\n\x03\x61ll\x18\x03 \x01(\x08\x42x\n\x15\x63om.google.spanner.v1B\tKeysProtoP\x01Z8google.golang.org/genproto/googleapis/spanner/v1;spanner\xaa\x02\x17Google.Cloud.Spanner.V1b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_KEYRANGE = _descriptor.Descriptor(
  name='KeyRange',
  full_name='google.spanner.v1.KeyRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_closed', full_name='google.spanner.v1.KeyRange.start_closed', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_open', full_name='google.spanner.v1.KeyRange.start_open', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_closed', full_name='google.spanner.v1.KeyRange.end_closed', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_open', full_name='google.spanner.v1.KeyRange.end_open', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='start_key_type', full_name='google.spanner.v1.KeyRange.start_key_type',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='end_key_type', full_name='google.spanner.v1.KeyRange.end_key_type',
      index=1, containing_type=None, fields=[]),
  ],
  serialized_start=124,
  serialized_end=368,
)


_KEYSET = _descriptor.Descriptor(
  name='KeySet',
  full_name='google.spanner.v1.KeySet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keys', full_name='google.spanner.v1.KeySet.keys', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ranges', full_name='google.spanner.v1.KeySet.ranges', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='all', full_name='google.spanner.v1.KeySet.all', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=370,
  serialized_end=478,
)

_KEYRANGE.fields_by_name['start_closed'].message_type = google_dot_protobuf_dot_struct__pb2._LISTVALUE
_KEYRANGE.fields_by_name['start_open'].message_type = google_dot_protobuf_dot_struct__pb2._LISTVALUE
_KEYRANGE.fields_by_name['end_closed'].message_type = google_dot_protobuf_dot_struct__pb2._LISTVALUE
_KEYRANGE.fields_by_name['end_open'].message_type = google_dot_protobuf_dot_struct__pb2._LISTVALUE
_KEYRANGE.oneofs_by_name['start_key_type'].fields.append(
  _KEYRANGE.fields_by_name['start_closed'])
_KEYRANGE.fields_by_name['start_closed'].containing_oneof = _KEYRANGE.oneofs_by_name['start_key_type']
_KEYRANGE.oneofs_by_name['start_key_type'].fields.append(
  _KEYRANGE.fields_by_name['start_open'])
_KEYRANGE.fields_by_name['start_open'].containing_oneof = _KEYRANGE.oneofs_by_name['start_key_type']
_KEYRANGE.oneofs_by_name['end_key_type'].fields.append(
  _KEYRANGE.fields_by_name['end_closed'])
_KEYRANGE.fields_by_name['end_closed'].containing_oneof = _KEYRANGE.oneofs_by_name['end_key_type']
_KEYRANGE.oneofs_by_name['end_key_type'].fields.append(
  _KEYRANGE.fields_by_name['end_open'])
_KEYRANGE.fields_by_name['end_open'].containing_oneof = _KEYRANGE.oneofs_by_name['end_key_type']
_KEYSET.fields_by_name['keys'].message_type = google_dot_protobuf_dot_struct__pb2._LISTVALUE
_KEYSET.fields_by_name['ranges'].message_type = _KEYRANGE
DESCRIPTOR.message_types_by_name['KeyRange'] = _KEYRANGE
DESCRIPTOR.message_types_by_name['KeySet'] = _KEYSET

KeyRange = _reflection.GeneratedProtocolMessageType('KeyRange', (_message.Message,), dict(
  DESCRIPTOR = _KEYRANGE,
  __module__ = 'google.cloud.spanner_v1.proto.keys_pb2'
  ,
  __doc__ = """KeyRange represents a range of rows in a table or index.
  
  A range has a start key and an end key. These keys can be open or
  closed, indicating if the range includes rows with that key.
  
  Keys are represented by lists, where the ith value in the list
  corresponds to the ith component of the table or index primary key.
  Individual values are encoded as described
  [here][google.spanner.v1.TypeCode].
  
  For example, consider the following table definition:
  
  ::
  
      CREATE TABLE UserEvents (
        UserName STRING(MAX),
        EventDate STRING(10)
      ) PRIMARY KEY(UserName, EventDate);
  
  The following keys name rows in this table:
  
  ::
  
      ["Bob", "2014-09-23"]
      ["Alfred", "2015-06-12"]
  
  Since the ``UserEvents`` table's ``PRIMARY KEY`` clause names two
  columns, each ``UserEvents`` key has two elements; the first is the
  ``UserName``, and the second is the ``EventDate``.
  
  Key ranges with multiple components are interpreted lexicographically by
  component using the table or index key's declared sort order. For
  example, the following range returns all events for user ``"Bob"`` that
  occurred in the year 2015:
  
  ::
  
      "start_closed": ["Bob", "2015-01-01"]
      "end_closed": ["Bob", "2015-12-31"]
  
  Start and end keys can omit trailing key components. This affects the
  inclusion and exclusion of rows that exactly match the provided key
  components: if the key is closed, then rows that exactly match the
  provided components are included; if the key is open, then rows that
  exactly match are not included.
  
  For example, the following range includes all events for ``"Bob"`` that
  occurred during and after the year 2000:
  
  ::
  
      "start_closed": ["Bob", "2000-01-01"]
      "end_closed": ["Bob"]
  
  The next example retrieves all events for ``"Bob"``:
  
  ::
  
      "start_closed": ["Bob"]
      "end_closed": ["Bob"]
  
  To retrieve events before the year 2000:
  
  ::
  
      "start_closed": ["Bob"]
      "end_open": ["Bob", "2000-01-01"]
  
  The following range includes all rows in the table:
  
  ::
  
      "start_closed": []
      "end_closed": []
  
  This range returns all users whose ``UserName`` begins with any
  character from A to C:
  
  ::
  
      "start_closed": ["A"]
      "end_open": ["D"]
  
  This range returns all users whose ``UserName`` begins with B:
  
  ::
  
      "start_closed": ["B"]
      "end_open": ["C"]
  
  Key ranges honor column sort order. For example, suppose a table is
  defined as follows:
  
  ::
  
      CREATE TABLE DescendingSortedTable {
        Key INT64,
        ...
      ) PRIMARY KEY(Key DESC);
  
  The following range retrieves all rows with key values between 1 and 100
  inclusive:
  
  ::
  
      "start_closed": ["100"]
      "end_closed": ["1"]
  
  Note that 100 is passed as the start, and 1 is passed as the end,
  because ``Key`` is a descending column in the schema.
  
  
  Attributes:
      start_key_type:
          The start key must be provided. It can be either closed or
          open.
      start_closed:
          If the start is closed, then the range includes all rows whose
          first ``len(start_closed)`` key columns exactly match
          ``start_closed``.
      start_open:
          If the start is open, then the range excludes rows whose first
          ``len(start_open)`` key columns exactly match ``start_open``.
      end_key_type:
          The end key must be provided. It can be either closed or open.
      end_closed:
          If the end is closed, then the range includes all rows whose
          first ``len(end_closed)`` key columns exactly match
          ``end_closed``.
      end_open:
          If the end is open, then the range excludes rows whose first
          ``len(end_open)`` key columns exactly match ``end_open``.
  """,
  # @@protoc_insertion_point(class_scope:google.spanner.v1.KeyRange)
  ))
_sym_db.RegisterMessage(KeyRange)

KeySet = _reflection.GeneratedProtocolMessageType('KeySet', (_message.Message,), dict(
  DESCRIPTOR = _KEYSET,
  __module__ = 'google.cloud.spanner_v1.proto.keys_pb2'
  ,
  __doc__ = """``KeySet`` defines a collection of Cloud Spanner keys and/or key ranges.
  All the keys are expected to be in the same table or index. The keys
  need not be sorted in any particular way.
  
  If the same key is specified multiple times in the set (for example if
  two ranges, two keys, or a key and a range overlap), Cloud Spanner
  behaves as if the key were only specified once.
  
  
  Attributes:
      keys:
          A list of specific keys. Entries in ``keys`` should have
          exactly as many elements as there are columns in the primary
          or index key with which this ``KeySet`` is used. Individual
          key values are encoded as described
          [here][google.spanner.v1.TypeCode].
      ranges:
          A list of key ranges. See
          [KeyRange][google.spanner.v1.KeyRange] for more information
          about key range specifications.
      all:
          For convenience ``all`` can be set to ``true`` to indicate
          that this ``KeySet`` matches all keys in the table or index.
          Note that any keys specified in ``keys`` or ``ranges`` are
          only yielded once.
  """,
  # @@protoc_insertion_point(class_scope:google.spanner.v1.KeySet)
  ))
_sym_db.RegisterMessage(KeySet)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\025com.google.spanner.v1B\tKeysProtoP\001Z8google.golang.org/genproto/googleapis/spanner/v1;spanner\252\002\027Google.Cloud.Spanner.V1'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
