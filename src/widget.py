from src import masks


def mask_account_card(nums: str) -> str:
    """ Функция, маскирует маскирует карты и счета """

    if "Счет" in nums:
        return nums[:-20] + masks.get_mask_account(nums)
    else:
        cards = masks.get_mask_card_number(nums)
        new_card = nums[:-16] + cards
        return new_card


def get_data(date: str) -> str:
    """ Функция, выводящая дату """

    return f"{date[9:11]}.{date[6:8]}.{date[1:5]}"
