def calculate_average():
    """
    Calculate the average of a series of numbers entered by the user.
    Input terminates when user enters -1.
    Returns the average of all numbers entered (excluding -1).
    """
    total_sum = 0
    count = 0

    # Get first input from user
    user_input = input("enter a number (-1 to finish): ")

    # Continue until user enters -1
    while user_input != "-1":
        #Add the number to our running sum and increment count
        total_sum += int(user_input)
        count += 1

        # Get next number
        user_input = input("enter a number (-1 to finish): ")

    # Calculate and return average if possible
    if count > 0:
        average = total_sum / count
        print (f"The average is: {average}")
        return average
    else:
        print("No numbers were entered.")

# Execute the function if script is run directly
if __name__ == "__main__":
    calculate_average()

