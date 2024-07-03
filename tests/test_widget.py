from src.widget import mask_account_card, get_data


def test_mask_account_card():
    assert mask_account_card("Maestro 7000 7922 8960 6361") == "Maestro 7000 79** **** 6361"

    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"


def test_get_data():
    assert get_data("2024-03-11T02:26:18.671407") == "11.03.2024"
