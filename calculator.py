# Creating a Function for the Calculator
def calculator():
    # Creating the Operation of Addition, Subtraction, Multiplication, and Division
    def add_number(number_1, number_2):
        result = number_1 + number_2
        return int(result) if result.is_integer() else result

    def subtract_number(number_1, number_2):
        result = number_1 - number_2
        return int(result) if result.is_integer() else result

    def multiply_number(number_1, number_2):
        result = number_1 * number_2
        return int(result) if result.is_integer() else result

    def divide_number(number_1, number_2):
        if number_2 == 0:
            raise ZeroDivisionError()
        result = round(number_1 / number_2, 2)
        return int(result) if result.is_integer() else result

    # Creating the Program's Interface
    while True:
        try:
            print("-------Choose Your Operation-------\n")
            print("\033[94m1. Addition (+) \033[0m")
            print("\033[92m2. Subtraction (-) \033[0m")
            print("\033[93m3. Multiplication (*) \033[0m")
            print("\033[31m4. Division (/) \033[0m")
            choice = int(input("Enter the Operation from 1-4 (1,2,3,4): "))

            if choice not in [1, 2, 3, 4]:
                raise ValueError()

            # User's Input for the Numbers
            num_1_str = input("Please Enter The First Number: ")
            if num_1_str.startswith('0') and not num_1_str.startswith('0.'):
                raise ValueError()

            num_2_str = input("Please Enter the Second Number: ")
            if num_2_str.startswith('0') and not num_2_str.startswith('0.'):
                raise ValueError()

            num_1 = float(num_1_str)
            num_2 = float(num_2_str)

            # Call the Desired Functions upon user's choice
            if choice == 1:
                print("Result: ", add_number(num_1, num_2))
            elif choice == 2:
                print("Result: ", subtract_number(num_1, num_2))
            elif choice == 3:
                print("Result: ", multiply_number(num_1, num_2))
            elif choice == 4:
                print("Result: ", divide_number(num_1, num_2))

        # Getting the Errors
        except ValueError:
            error_message = "You Have Entered an Invalid Character, Number, or Choice"
            print("\033[91m" + "ValueError: " + error_message)
            print("\033[0m")

        except ZeroDivisionError:
            zero_division_error_message = "The Number Cannot Be Divided By Zero"
            print("\033[91m" + "ZeroDivisionError:" + zero_division_error_message)
            print("\033[0m")

        except Exception as exception:
            print("\033[91m" + "An error occurred: Please Try Again!", exception)
            print("\033[0m")

        # Creating a Loop if the User wants to try again
        while True:
            try:
                repeat = input("Do you want to use the Program again? ('y' for Yes / 'n' for No): ").strip().lower()
                if repeat not in ['y', 'n']:
                    repeat_error_message = "Invalid input! Please enter 'y' for Yes or 'n' for No."
                    raise ValueError("\033[91m" + repeat_error_message + "\033[0m")
                break

            except ValueError as exception:
                print(exception)
                
        # Display the "Thank You!" message
        if repeat != 'y':
            print("\033[95m" + "Thank You for using this Calculator!")
            break


# Call The Main Function
calculator()
