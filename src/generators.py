from typing import Generator


def filter_by_currency(transactions: list, currency: str) -> Generator:
    ''' Генератор который принимает на вход список словарей, представляющих транзакции '''
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list) -> Generator:
    ''' Генератор который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди '''
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator:
    ''' Генератор , который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX '''
    for number in range(start, end + 1):
        card_number_str = f"{number:016d}"
        formated_card_number = ' '.join(card_number_str[i:i + 4] for i in range(0, 16, 4))
        yield formated_card_number
