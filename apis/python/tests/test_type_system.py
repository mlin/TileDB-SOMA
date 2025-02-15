import pyarrow as pa
import pytest

import tiledbsoma as soma

"""
Arrow types we expect to work. A handful of types will promote, eg, string->large_string.
Most must be literally as requested, or error out.

Tuple is (requested_type, expected_type).
"""
SUPPORTED_ARROW_TYPES = [
    (pa.bool_(),) * 2,
    (pa.int8(),) * 2,
    (pa.int16(),) * 2,
    (pa.int32(),) * 2,
    (pa.int16(),) * 2,
    (pa.uint8(),) * 2,
    (pa.uint16(),) * 2,
    (pa.uint32(),) * 2,
    (pa.uint64(),) * 2,
    (pa.float32(),) * 2,
    (pa.float64(),) * 2,
    (pa.timestamp("s"),) * 2,
    (pa.timestamp("ms"),) * 2,
    (pa.timestamp("us"),) * 2,
    (pa.timestamp("ns"),) * 2,
    (pa.string(), pa.large_string()),
    (pa.binary(), pa.large_binary()),
    (pa.large_string(),) * 2,
    (pa.large_binary(),) * 2,
]


"""Arrow types we expect to fail"""
UNSUPPORTED_ARROW_TYPES = [
    pa.null(),
    pa.date64(),
    pa.time64("us"),
    pa.time64("ns"),
    pa.float16(),
    pa.date32(),
    pa.time32("s"),
    pa.time32("ms"),
    pa.duration("s"),
    pa.duration("ms"),
    pa.duration("us"),
    pa.duration("ns"),
    pa.month_day_nano_interval(),
    pa.binary(10),
    pa.decimal128(1),
    pa.decimal128(38),
    pa.list_(pa.int8()),
    pa.large_list(pa.bool_()),
    pa.map_(pa.string(), pa.int32()),
    pa.struct([("f1", pa.int32()), ("f2", pa.string())]),
    pa.dictionary(pa.int32(), pa.string()),
]


@pytest.mark.parametrize("arrow_type_info", SUPPORTED_ARROW_TYPES)
def test_arrow_types_supported(tmp_path, arrow_type_info):
    """Verify round-trip conversion of types which should work "as is" """
    arrow_type, expected_arrow_type = arrow_type_info

    sdf = soma.DataFrame(tmp_path.as_posix())
    assert sdf == sdf.create(pa.schema([(str(arrow_type), arrow_type)]))
    schema = sdf.schema
    assert schema is not None
    assert sorted(schema.names) == sorted(
        ["soma_joinid", "soma_rowid", str(arrow_type)]
    )
    assert schema.field(str(arrow_type)).type == expected_arrow_type


@pytest.mark.parametrize("arrow_type", UNSUPPORTED_ARROW_TYPES)
def test_arrow_types_unsupported(tmp_path, arrow_type):
    """Verify explicit error for unsupported types"""

    sdf = soma.DataFrame(tmp_path.as_posix())

    with pytest.raises(TypeError, match=r"unsupported type|Unsupported Arrow type"):
        assert sdf == sdf.create(pa.schema([(str(arrow_type), arrow_type)]))
