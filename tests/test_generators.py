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
