def calculate_per_amount(amount: int, percent: float) -> float:
    """
    This function will calculate percent amount of any given principle
    percentage formula  output = principle_amount * per/100
    :param amount:
    :param percent:
    :return:
    """
    per_amount = amount * (percent/100)
    return per_amount

# result = calculate_per_amount(1000, 5.25)
# print(result)