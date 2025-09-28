def calculate_average():
    """
    Calculate the average of a series of numbers entered by the user.
    Input terminates when user enters -1.
    Returns the average of all numbers entered (excluding -1).
    """
    total_sum = 0
    count = 0

    while True:
        try:
            # Get first input from user
            user_input = input("enter a number (-1 to finish): ")

            # Check if user wants to exit
            if user_input == "-1":
                break

            # Convert input to number and validate
            number = float(user_input)  # Using float instead of int to accept decimal numbers

            # Add to running sum and increment count
            total_sum += number
            count += 1

        except ValueError:
            print("Error: Please entre a valid number.")
        except Exception as e:
            print(f"An unexpected error occured: {e}")

        # Calculate and return average if possible
        if count > 0:
            average = total_sum / count
            print (f"The average of the {count} number is: {average}")
            return average
        else:
            print("No valid numbers were entered.")
            return None

# Execute the function if script is run directly
if __name__ == "__main__":
    calculate_average()

