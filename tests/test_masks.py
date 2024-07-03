import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize('value, expected', [
    ('7000792289606361', '7000 79** **** 6361'),
    ('7158300734726758', '7158 30** **** 6758'),
    ('6831982476737658', '6831 98** **** 7658'),
])
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize('value, expected', [
    ('64686473678894779589', '**9589'),
    ('35383033474447895560', '**5560'),
    ('73654108430135874305', '**4305'),
])
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected


# def test_get_mask_card_number(card_number):
#     assert get_mask_card_number("7000792289606361") == card_number
#
#
# def test_get_mask_account(account_number):
#     assert get_mask_account("73654108430135874305") == account_number
