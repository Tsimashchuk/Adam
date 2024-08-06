import logging


logger = logging.getLogger('masks')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/masks.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card: str) -> str:
    """Функция, маскирнющая карты"""

    private_card = card[-16:-12] + " " + card[-12:-10] + "**" + " " + "****" + " " + card[-4:]
    logger.info(f'Выполняем маскировку карты')
    return private_card


def get_mask_account(account: str) -> str:
    """Функция, маскирнющая счет """

    account = "**" + account[-4:]
    logger.info(f'Выполняем маскировку счета')
    return account
