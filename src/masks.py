from typing import Any


def get_mask_card_number(card: str) -> Any:
    """Функция, маскирнющая карты"""
    card_number = card.split()[-1]

    private_number = card_number[:6] + (len(card_number[6:-4]) * "*") + card_number[-4:]

    chunks, chunk_size = len(private_number), len(private_number) // 4
    return " ".join(
        [private_number[i: i + chunk_size] for i in range(0, chunks, chunk_size)]
    )


print(get_mask_card_number("7000792289606361"))


def get_mask_account(account: str) -> Any:
    """Функция, маскирнющая счет """
    account_number = account.split()[-1]

    private_number = (len(account_number[:-4]) * "*") + account_number[-4:]
    chunks, chunk_size = len(private_number), len(private_number) // 4

    return " ".join(
        [private_number[i: i + chunk_size] for i in range(0, chunks, chunk_size)]
    )


print(get_mask_account("73654108430135874305"))
