def get_mask_card_number(card: str) -> str:
    """Функция, маскирнющая карты"""
    card = str(card)
    new_card = card[:4] + " " + card[4:6] +  "**" + " " + "****" + " " + card[:4]

    return new_card


print(get_mask_card_number("7000792289606361"))


def get_mask_account(account: str) -> str:
    """Функция, маскирнющая счет """

    account_user = str(account)
    account = "**" + account_user[:4]

    return account

print(get_mask_account("73654108430135874305"))
