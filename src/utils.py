import json
from pathlib import Path
from typing import Any
import logging

from src.config import ROOT_PATH


logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/utils.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_json_file(file_path: Any) -> list[dict[Any, Any]]:
    """
    Функция для проверки JSON-файла
    """
    try:
        logger.info(f'Открываем JSON-файл')
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                logger.info(f'Проверяем JSON-файл')
                data = json.load(file)
                return data
            except json.JSONDecodeError as er:
                logger.error(f'Произошла ошибка: {er}')
                print("Ошибка декорирования файла")
                return []
    except FileNotFoundError as er:
        logger.error(f'Произошла ошибка: {er}')
        print("Файл не найден")
        return []


file_path = Path(ROOT_PATH, "../data/operations.json")
transactions = read_json_file(file_path)
print(transactions)
