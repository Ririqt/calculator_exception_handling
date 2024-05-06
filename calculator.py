def calculator():
    def add_number(number_1, number_2):
        return number_1 + number_2

    def subtract_number(number_1, number_2):
        return number_1 - number_2

    def multiply_number(number_1, number_2):
        return number_1 * number_2

    def divide_number(number_1, number_2):
        if number_2 == 0:
            raise ZeroDivisionError()
        return number_1 / number_2

    while True:
        try:
            print("-------Choose Your Operation-------\n")
            print("1. Addition (+) ")
            print("2. Subtraction (-) ")
            print("3. Multiplication (*) ")
            print("4. Division (/)")
            choice = int(input("Enter the Operation from 1-4 (1,2,3,4): "))

            if choice not in [1, 2, 3, 4]:
                raise ValueError()

            num_1 = float(input("Please Enter The First Number: "))
            num_2 = float(input("Please Enter the Second Number: "))
            