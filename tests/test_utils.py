import pytest

import pbsreport.utils as utils


def test_convert_bytes():
    assert utils.convert_bytes(0, from_unit="b", to_unit="b") == 0
    assert utils.convert_bytes(1024, from_unit="b", to_unit="b") == 1024
    assert utils.convert_bytes(1024, from_unit="b", to_unit="kb") == 1
    assert utils.convert_bytes(1024, from_unit="b", to_unit="gb") == 0
    assert utils.convert_bytes(1, from_unit="kb", to_unit="b") == 1024
    assert utils.convert_bytes(2, from_unit="kb", to_unit="b") == 2048
    assert utils.convert_bytes(1, from_unit="mb", to_unit="kb") == 1024
    assert utils.convert_bytes(1, from_unit="gb", to_unit="mb") == 1024
    assert utils.convert_bytes(1, from_unit="gb", to_unit="kb") == 1024 ** 2
    assert utils.convert_bytes(1, from_unit="gb", to_unit="b") == 1024 ** 3
    assert utils.convert_bytes(1, from_unit="y", to_unit="b") == 1024 ** 8
    with pytest.raises(ValueError):
        utils.convert_bytes(-1, from_unit="kb", to_unit="b")
