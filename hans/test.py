
import random

def play_game(attempts):
    balance = 0
    total_bet = 0
    results = []

    for i in range(attempts):
        bet = 20
        total_bet += bet

        # Симулируем результаты случайных чисел от 1 до 37
        result = random.randint(1, 37)

        if 13 <= result <= 36:
            balance += 10
        else:
            balance -= 20

        results.append(balance)

        print(f"After {i+1} attempts - balance: {balance}")

    with open("results2.txt", "w") as file:
        for balance in results:
            file.write(f"After {i+1} attempts - balance: {balance}\n")

    return total_bet, balance

def analyze_results(file_path):
    total_attempts = 0
    total_balance = 0
    wins = 0
    total_spent = 0

    with open(file_path, "r") as file:
        for line in file:
            total_attempts += 1
            words = line.split()
            balance = int(words[-1])
            total_balance = balance  # Обновляем общий баланс на текущий баланс
            if balance > 0:
                wins += 1
            # Рассчитываем сумму потраченных баллов как общий баланс минус текущий баланс
            total_spent += total_balance - balance

    win_percentage = (wins / total_attempts) * 100
    total_points = total_attempts * 20  # Общая сумма ставок

    print(f"По такой стратегии вы бы набрали {wins} баллов из {total_attempts} количества попыток.")
    print(f"Ваш процент побед равен = {win_percentage:.2f}%")
    print(f"Общая прибыль составила {total_balance} рублей.")
    print(f"Всего было поставлено {total_points} баллов.")
    print(f"Всего было затрачено {total_spent + total_balance} баллов.")

if __name__ == "__main__":
    attempts = 150
    total_bet, final_balance = play_game(attempts)
    print("\nResults analysis:")
    analyze_results("results2.txt")
    print(f"\nTotal bets: {total_bet}")
    print(f"Final balance: {final_balance}")
    print(f"Total profit: {final_balance - total_bet}")
