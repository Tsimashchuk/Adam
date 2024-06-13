import masks
def mask_account_card(nums: str) -> str:
    """ Функция маскирует маскирует карты и счета """


    if "Счет" in nums:
        return masks.get_mask_account(nums)

    else:
        cards = masks.get_mask_account(nums[:-16])
        new_card = nums.replace(nums[:-16], cards)
        return new_card


print(mask_account_card("Счет 35383033474447895560"))




