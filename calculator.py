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

            if choice == 1:
                print("Result: ", add_number(num_1, num_2))
            elif choice == 2:
                print("Result: ", subtract_number(num_1, num_2))
            elif choice == 3:
                print("Result: ", multiply_number(num_1, num_2))
            elif choice == 4:
                print("Result: ", divide_number(num_1, num_2))

        except ValueError:
            error_message = "You Have Entered an Invalid Character, Number, or Choice"
            print("ValueError: " + error_message)

        except ZeroDivisionError:
            zero_division_error_message = "The Number Cannot Be Divided By Zero"
            print("ZeroDivisionError:" + zero_division_error_message)

        except Exception as exception:
            print("An error occurred: Please Try Again!", exception)

        while True:
            try:
                repeat = input("Do you want to use the Program again? ('y' for Yes / 'n' for No): ").strip().lower()
                if repeat not in ['y', 'n']:
                    repeat_error_message = "Invalid input! Please enter 'y' for Yes or 'n' for No."
