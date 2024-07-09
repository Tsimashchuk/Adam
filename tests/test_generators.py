import pytest


from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency_with_mathing_currency(sample_transactions):
    filtered_transactions = list(filter_by_currency(sample_transactions, "USD"))
    assert all(transaction["operationAmount"]["currency"]["code"] == "USD" for transaction in filtered_transactions)
    assert len(filtered_transactions) == 3


def test_filter_by_currency_with_no_mathing_currency(sample_transactions):
    filtered_transactions = list(filter_by_currency(sample_transactions, "EUR"))
    assert len(filtered_transactions) == 0


def test_filter_by_currency_with_no_empty_currency(sample_transactions):
    filtered_transactions = list(filter_by_currency([], "USD"))
    assert len(filtered_transactions) == 0


def test_transaction_descriptions_correct(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))
    assert len(descriptions) == 5


def test_transaction_descriptions_with_no_empty_list(sample_transactions):
    descriptions = list(transaction_descriptions([]))
    assert len(descriptions) == 0


@pytest.mark.parametrize('card_number', [
    ('XXXXXXXXXXXXXXXX', '0000000000000001'),
    ('XXXXXXXXXXXXXXXX', '0000000000000002'),
    ('XXXXXXXXXXXXXXXX', '0000000000000003'),
    ('XXXXXXXXXXXXXXXX', '0000000000000004'),
    ('XXXXXXXXXXXXXXXX', '0000000000000005'),
    ('XXXXXXXXXXXXXXXX', '0000000000000006'),
    ('XXXXXXXXXXXXXXXX', '0000000000000007'),
    ('XXXXXXXXXXXXXXXX', '9999999999999991'),
    ('XXXXXXXXXXXXXXXX', '9999999999999992'),
    ('XXXXXXXXXXXXXXXX', '9999999999999993'),
    ('XXXXXXXXXXXXXXXX', '9999999999999994'),
    ('XXXXXXXXXXXXXXXX', '9999999999999995'),
    ('XXXXXXXXXXXXXXXX', '9999999999999996'),
    ('XXXXXXXXXXXXXXXX', '9999999999999997'),
    ('XXXXXXXXXXXXXXXX', '9999999999999998'),
    ('XXXXXXXXXXXXXXXX', '9999999999999999'),
])
def test_card_number_generator(card_number):
    for card_number in card_number_generator(1, 5):
        assert list(card_number)
