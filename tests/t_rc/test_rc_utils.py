import pytest

from hipiregio.rc.rc_utils import get_text_id_from_full_id, create_full_id, is_full_id_from_given_culture


@pytest.mark.parametrize(
    "full_id, expected_text_id",
    [
        ("test_pl-PL", "test"),
        ("test_pl-WLKP", "test"),
    ])
def test_get_text_id_from_full_id(full_id, expected_text_id):
    actual = get_text_id_from_full_id(full_id)
    assert actual == expected_text_id, f"get_text_id_from_full_id({full_id})"


@pytest.mark.parametrize(
    "text_id, culture, expected_full_id",
    [
        ("test-001", "pl-PL", "test-001_pl-PL"),
        ("test-001", "pl-WLKP", "test-001_pl-WLKP"),
    ])
def test_create_full_id(text_id, culture, expected_full_id):
    actual = create_full_id(text_id, culture)
    assert actual == expected_full_id, f"create_full_id({text_id}, {culture})"


@pytest.mark.parametrize(
    "full_id, culture, expected",
    [
        ("test-001_pl-PL", "pl-PL", True),
        ("test-001_pl-PL", "pl-WLKP", False),
        ("test-001_pl-WLKP", "pl-PL", False),
        ("test-001_pl-WLKP", "pl-WLKP", True),
    ])
def test_is_full_id_from_given_culture(full_id, culture, expected):
    actual = is_full_id_from_given_culture(full_id, culture)
    assert actual == expected, f"is_full_id_from_given_culture({full_id}, {culture})"
