from DD_to_DDM import convert
import pytest

TEST_DATA_LONGITUDE = [
    pytest.param(-180, "180^0W", id="'-180' -> '180^0W'"),
    pytest.param(-180.0, "180^0W", id="'-180.0' -> '180^0W'"),
    pytest.param(-13.912, "13^54.72W", id="'-13.912' -> '13^54.72W'"),
    pytest.param(0, "0^0E", id="'0' -> '0^0E'"),
    pytest.param(180.0, "180^0E", id="'180.0' -> '180^0E'"),
    pytest.param(180, "180^0E", id="'180' -> '180^0E'"),
    pytest.param(170.0323, "170^1.938E", id="'170.0323' -> '170^1.938E'")]


@pytest.mark.parametrize("given_dd, expected_ddm", TEST_DATA_LONGITUDE)
def test_cordinates(given_dd, expected_ddm):
    """Parameterized test takes as input a value in DD format and an expected value in DDM format.
    :param DD - Decimal Degrees.
    :param DDM - Degrees Decimal Minutes.
    :param TEST_DATA_LONGITUDE - Verification data"""
    assert convert(given_dd) == expected_ddm
