# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/bigquery/storage_v1beta2/proto/avro.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/bigquery/storage_v1beta2/proto/avro.proto",
    package="google.cloud.bigquery.storage.v1beta2",
    syntax="proto3",
    serialized_options=_b(
        "\n)com.google.cloud.bigquery.storage.v1beta2B\tAvroProtoP\001ZLgoogle.golang.org/genproto/googleapis/cloud/bigquery/storage/v1beta2;storage"
    ),
    serialized_pb=_b(
        '\n6google/cloud/bigquery/storage_v1beta2/proto/avro.proto\x12%google.cloud.bigquery.storage.v1beta2"\x1c\n\nAvroSchema\x12\x0e\n\x06schema\x18\x01 \x01(\t"*\n\x08\x41vroRows\x12\x1e\n\x16serialized_binary_rows\x18\x01 \x01(\x0c\x42\x86\x01\n)com.google.cloud.bigquery.storage.v1beta2B\tAvroProtoP\x01ZLgoogle.golang.org/genproto/googleapis/cloud/bigquery/storage/v1beta2;storageb\x06proto3'
    ),
)


_AVROSCHEMA = _descriptor.Descriptor(
    name="AvroSchema",
    full_name="google.cloud.bigquery.storage.v1beta2.AvroSchema",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="schema",
            full_name="google.cloud.bigquery.storage.v1beta2.AvroSchema.schema",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=97,
    serialized_end=125,
)


_AVROROWS = _descriptor.Descriptor(
    name="AvroRows",
    full_name="google.cloud.bigquery.storage.v1beta2.AvroRows",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="serialized_binary_rows",
            full_name="google.cloud.bigquery.storage.v1beta2.AvroRows.serialized_binary_rows",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=127,
    serialized_end=169,
)

DESCRIPTOR.message_types_by_name["AvroSchema"] = _AVROSCHEMA
DESCRIPTOR.message_types_by_name["AvroRows"] = _AVROROWS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AvroSchema = _reflection.GeneratedProtocolMessageType(
    "AvroSchema",
    (_message.Message,),
    dict(
        DESCRIPTOR=_AVROSCHEMA,
        __module__="google.cloud.bigquery.storage_v1beta2.proto.avro_pb2",
        __doc__="""Avro schema.
  Attributes:
      schema:
          Json serialized schema, as described at
          https://avro.apache.org/docs/1.8.1/spec.html.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.bigquery.storage.v1beta2.AvroSchema)
    ),
)
_sym_db.RegisterMessage(AvroSchema)

AvroRows = _reflection.GeneratedProtocolMessageType(
    "AvroRows",
    (_message.Message,),
    dict(
        DESCRIPTOR=_AVROROWS,
        __module__="google.cloud.bigquery.storage_v1beta2.proto.avro_pb2",
        __doc__="""Avro rows.
  Attributes:
      serialized_binary_rows:
          Binary serialized rows in a block.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.bigquery.storage.v1beta2.AvroRows)
    ),
)
_sym_db.RegisterMessage(AvroRows)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
