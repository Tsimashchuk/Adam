def filter_by_state(distionary_list: list[dict[str, list]], state: str = "EXECUTED") -> list[dict[str, list]]:

    """ Функция, возвращает новый список, содержащий только те словари,
    у которых по ключу содержит переданное в функцию значение """

    new_list = []

    for i in distionary_list:
        if i.get("state") == state:
            new_list.append(i)
    return new_list


def sort_by_date(sorted_list: list[dict[str, list]], descendig: bool = True) -> list[dict[str, list]]:

    """ Функция в которой, исходные словари отсортированы по убыванию даты"""

    decreasing_date = sorted(sorted_list, key=lambda t: t.get("date"), reverse=descendig)
    return decreasing_date
