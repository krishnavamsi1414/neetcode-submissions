def is_balance_low(balance: int) -> str:
    if balance <=100:
        return "Warning: Low balance."


# do not modify below this line
print(is_balance_low(99))
print(is_balance_low(100))
is_balance_low(101)
