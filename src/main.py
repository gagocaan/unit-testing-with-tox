from decimal import Decimal


def divide(a: Decimal, b: Decimal) -> Decimal:
    return a / b


if __name__ == "__main__":
    print(divide(Decimal(2.34), Decimal(1.85)))
