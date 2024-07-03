from src import masks


def mask_account_card(nums: str) -> str:
    """ Функция, маскирует маскирует карты и счета """

    if "Счет" in nums:
        return nums[:-20] + masks.get_mask_account(nums)
    else:
        new_card = nums[:-20] + " " + nums[-19:-12] + "** **** " + nums[-4:]
        return new_card


def get_data(date: str) -> str:
    """ Функция, выводящая дату """

    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
