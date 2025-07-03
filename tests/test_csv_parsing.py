import pytest
from source.main import filter_data, aggregate_data, sort_data, is_number

TEST_DATA = [
    ["name", "brand", "price", "rating"],
    ["iphone 15 pro", "apple", "999", "4.9"],
    ["galaxy s23 ultra", "samsung", "1199", "4.8"],
    ["redmi note 12", "xiaomi", "199", "4.6"],
    ["poco x5 pro", "xiaomi", "299", "4.4"],
]


def test_filter_data_gt():
    result = filter_data(TEST_DATA, "price>500")
    assert len(result) == 3
    assert result[1][0] == "iphone 15 pro"


def test_filter_data_lt():
    result = filter_data(TEST_DATA, "price<500")
    assert len(result) == 3
    assert result[1][0] == "redmi note 12"


def test_filter_data_eq():
    result = filter_data(TEST_DATA, "brand=apple")
    assert len(result) == 2
    assert result[1][0] == "iphone 15 pro"


def test_aggregate_avg():
    result = aggregate_data(TEST_DATA, "price=avg")
    assert result[1][0] == round((999 + 1199 + 199 + 299) / 4, 2)


def test_aggregate_max():
    result = aggregate_data(TEST_DATA, "rating=max")
    assert result[1][0] == 4.9


def test_aggregate_min():
    result = aggregate_data(TEST_DATA, "rating=min")
    assert result[1][0] == 4.4


def test_sort_string_asc():
    result = sort_data(TEST_DATA, "price=asc")
    assert result[1][0] == "redmi note 12"


def test_sort_string_desc():
    result = sort_data(TEST_DATA, "price=desc")
    assert result[1][0] == "galaxy s23 ultra"


def test_sort_number_asc():
    result = sort_data(TEST_DATA, "rating=asc")
    assert result[1][0] == "poco x5 pro"


def test_sort_number_desc():
    result = sort_data(TEST_DATA, "rating=desc")
    assert result[1][0] == "iphone 15 pro"


def test_is_number():
    s1 = "123"
    s2 = "random string"
    assert is_number(s1)
    assert not is_number(s2)