import pytest

from pbsreport import utils


def test_convert_bytes():
    assert utils.convert_bytes(0, from_unit="b", to_unit="b") == 0
    assert utils.convert_bytes(1024, from_unit="b", to_unit="b") == 1024
    assert utils.convert_bytes(1024, from_unit="b", to_unit="kb") == 1
    assert utils.convert_bytes(1024, from_unit="b", to_unit="gb") == 0
    assert utils.convert_bytes(1, from_unit="kb", to_unit="b") == 1024
    assert utils.convert_bytes(2, from_unit="kb", to_unit="b") == 2048
    assert utils.convert_bytes(1, from_unit="mb", to_unit="kb") == 1024
    assert utils.convert_bytes(1, from_unit="gb", to_unit="mb") == 1024
    assert utils.convert_bytes(1, from_unit="gb", to_unit="kb") == 1024**2
    assert utils.convert_bytes(1, from_unit="gb", to_unit="b") == 1024**3
    assert utils.convert_bytes(1, from_unit="yb", to_unit="b") == 1024**8
    with pytest.raises(ValueError):
        utils.convert_bytes(-1, from_unit="kb", to_unit="b")
        utils.convert_bytes(1, from_unit="x", to_unit="b")
        utils.convert_bytes(1, from_unit="b", to_unit="x")


def test_convert_raw_bytes():
    assert utils.convert_raw_bytes("1000b", to_unit="b") == 1000
    assert utils.convert_raw_bytes("1024b", to_unit="b") == 1024
    assert utils.convert_raw_bytes("1kb", to_unit="b") == 1024
    assert utils.convert_raw_bytes("2kb", to_unit="b") == 2048
    assert utils.convert_raw_bytes("1mb", to_unit="kb") == 1024
    assert utils.convert_raw_bytes("1gb", to_unit="mb") == 1024
    assert utils.convert_raw_bytes("1gb", to_unit="kb") == 1024**2
    assert utils.convert_raw_bytes("1yb", to_unit="bb") == 1024**8
    with pytest.raises(ValueError):
        utils.convert_raw_bytes("-1b", to_unit="b")
        utils.convert_raw_bytes("1x", to_unit="b")
        utils.convert_raw_bytes("1b", to_unit="x")


def test_bytes_split():
    assert utils.bytes_split("1000b") == (1000, "b")
    assert utils.bytes_split("1000kb") == (1000, "kb")


def test_human_size():
    assert utils.human_size(0) == "0b"
    assert utils.human_size(1) == "1b"
    assert utils.human_size(1024) == "1Kb"
    assert utils.human_size(1024**2) == "1Mb"
    assert utils.human_size(1024**3) == "1Gb"
    assert utils.human_size(1024**8) == "1Yb"
