import os
from typing import Any

import masks


def mask_account_card(nums: Any) -> Any:
    """ Функция, маскирует маскирует карты и счета """

    if "Счет" in nums:
        return nums[:-20] + masks.get_mask_account(nums)
    else:
        cards = masks.get_mask_card_number(nums)
        new_card = nums[:-16] + cards
        return new_card


print(mask_account_card("Maestro 1596837868705199"))


def get_data(date: Any) -> Any:
    """ Функция, выводящая дату """

    return f"{date[9:11]}.{date[6:8]}.{date[1:5]}"


print(get_data("v2018-07-11T02:26:18.671407"))
