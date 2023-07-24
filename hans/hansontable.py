# import random

# def calculate_probability(start_range, end_range, total_numbers):
#     if start_range > end_range:
#         start_range, end_range = end_range, start_range
    
#     numbers_in_range = len([num for num in range(start_range, end_range + 1)])
#     probability = (numbers_in_range / total_numbers) * 100
#     return probability

# total_numbers_on_table = 37
# start_range = 13
# end_range = 36

# random_number = random.randint(1, total_numbers_on_table)
# probability = calculate_probability(start_range, end_range, total_numbers_on_table)

# print(f"Random number: {random_number}")
# print(f"The probability of numbers in the range {start_range}-{end_range} is: {probability:.2f}%")

# if start_range <= random_number <= end_range:
#     print("Congratulations, you won!")
# else:
#     print("Sorry, you lost.")

import random


def play_game(num_attempts):
    balance = 0

    for _ in range(num_attempts):
        random_number = random.randint(1, 37)

        if 1 <= random_number <= 12:
            balance -= 20
            # print(f"Number {random_number}: You lost $20. Balance: {balance}")
        elif 13 <= random_number <= 36:
            balance += 10
            # print(f"Number {random_number}: You won $10. Balance: {balance}")
        else:
            balance -= 20
            # print(f"Number {random_number}: It's not in the range. Balance: {balance}")

    # print(f"Final balance: {balance}")

    # Записываем итоговый баланс в текстовый документ
    with open("results.txt", "a") as file:
        file.write(f"After {num_attempts} attempts - balance: {balance}\n")

for i in range(1000000):
    if __name__ == "__main__":
        play_game(150)
