import json
from pathlib import Path
from typing import  Any

from src.config import ROOT_PATH


def read_json_file(file_path: Any) -> list[dict]:
    """ Функция для проверки JSON-файла """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError:
                print("Ошибка декорирования файла")
                return []
    except FileNotFoundError:
        print("Файл не найден")
        return []


file_path = Path(ROOT_PATH, "../data/operations.json")
transactions = read_json_file(file_path)
# print(transactions)
