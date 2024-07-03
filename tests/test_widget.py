from src.widget import mask_account_card, get_data


def test_mask_account_card(card_numbers, account_numbers):
    assert mask_account_card("Maestro 7000792289606361") == card_numbers

    assert mask_account_card("Счет 73654108430135874305") == account_numbers


def test_get_data(number_data):
    assert get_data("2024-03-11T02:26:18.671407") == number_data
