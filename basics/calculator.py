class Calculator:

    def add_values(self, a, b):
        return a + b

    def sub_values(self, a, b):
        return a - b

    def div_values(self, a, b):
        try:
            return a / b
        except ZeroDivisionError as e:
            return False

    def mul_values(self, a, b):
        return a * b


if __name__ == "__main__":

    calculator = Calculator()

    assert calculator.div_values(1, 0) == False