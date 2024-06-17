from typing import Any


def filter_by_state(distionary_list: Any, state: str = "EXECUTED") -> Any:

    """ Функция, принимает на вход список словарей и значение для ключа state """

    new_list = []

    for i in distionary_list:
        if i.get("state") == state:
            new_list.append(i)
    return new_list


print(filter_by_state([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
