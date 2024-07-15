import pytest


from src.widget import mask_account_card, get_data


@pytest.mark.parametrize('value, expected', [
    ('Maestro 7000792289606361', 'Maestro 7000 79** **** 6361'),
    ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
    ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
    ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
    ('Счет 64686473678894779589', 'Счет **9589'),
    ('Счет 35383033474447895560', 'Счет **5560'),
    ('Счет 73654108430135874305', 'Счет **4305'),
])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


def test_get_data(number_data):
    assert get_data("2024-03-11T02:26:18.671407") == number_data


# def test_mask_account_card(card_numbers, account_numbers):
#     assert mask_account_card("Maestro 7000792289606361") == card_numbers
#
#     assert mask_account_card("Счет 73654108430135874305") == account_numbers
