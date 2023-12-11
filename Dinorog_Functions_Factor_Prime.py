# Function for getting an integer
def get_user_integer(prompt):
    while True:
        try:
            user_integer = int(input(prompt))
            if user_integer >= 2:
                return user_integer
            else:
                print("[Invalid input. Enter a number greater than or equal to 2]")
        except ValueError:
            print("[Error 404. Please input an integer]")


def get_user_options(prompt):
    while True:
        user_options = input(prompt)
        if user_options in ['0', '1', '2', '3']:
            return user_options

        else:
            print("Invalid input. Please enter options ['0', '1', '2', '3']")


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def display_primes(num):
    print(f"Prime numbers between 1 and {num}:")
    for i in range(2, num + 1):
        if is_prime(i):
            print(i, end=" ")
    print()


# Loop
while True:
    print("CS112: Computer Programming 1")
    print("ACTIVITY: \"FACTORS & PRIMES\" ")
    print("Created by: Artjohn Clark E. Dinorog | CS 1E")

    while True:
        user_input = get_user_integer("\n> Enter your number: ")
        print("\n> Select Options "
              "\n[0] Terminate"
              "\n[1] Smallest Factor"
              "\n[2] Prime Number"
              "\n[3] Both Prime Number and Smallest Factor")
        user_choice = get_user_options("> Option: ")

        if user_choice == '0':
            print("[Program Terminated]")
            break

        if user_choice == '1':
            for i in range(2, int(user_input ** 0.5) + 1):
                if user_input % i == 0:
                    print(f"The smallest factor other than 1 for {user_input} is {i}")

        elif user_choice == '2':
            display_primes(user_input)

        elif user_choice == '3':
            smallest_factor = None
            for i in range(2, int(user_input ** 0.5) + 1):
                if user_input % i == 0:
                    smallest_factor = i
                    break  # Exit the loop after finding the smallest factor

            if smallest_factor is not None:
                print("Smallest Factor:", smallest_factor)
                display_primes(user_input)
            else:
                print(f"{user_input} is a prime number.")

    break
