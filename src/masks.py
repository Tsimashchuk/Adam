from typing import Any


def get_mask_card_number(card: Any) -> Any:
    """Функция, маскирнющая карты"""
    private_card = card[-16:-12] + " " + card[-12:-10] + "**" + " " + "****" + " " + card[-4:]

    return private_card


print(get_mask_card_number("Maestro 1596837868705199"))


def get_mask_account(account: Any) -> Any:
    """Функция, маскирнющая счет """

    account = "**" + account[-4:]

    return account


print(get_mask_account("Счет 73654108430135874305"))
