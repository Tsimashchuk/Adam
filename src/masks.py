def get_mask_card_number(card: str) -> str:
    """Функция, маскирнющая карты"""
    private_card = card[-16:-12] + " " + card[-12:-10] + "**" + " " + "****" + " " + card[-4:]

    return private_card


def get_mask_account(account: str) -> str:
    """Функция, маскирнющая счет """

    account = "**" + account[-4:]

    return account
