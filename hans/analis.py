import tkinter as tk

def analyze_results(file_path):
    total_attempts = 0
    total_balance = 0
    wins = 0
    total_spent = 0
    all_total_attempts = 0

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("After"):
                total_attempts += 1
                words = line.split()
                attempts = int(words[1])
                all_total_attempts += attempts
                balance = int(words[-1])
                total_balance += balance
                if balance > 0:
                    wins += 1
                total_spent += abs(balance)

    win_percentage = (wins / total_attempts) * 100
    if win_percentage > 50:
        result_text = "Ваша стратегия бы выиграла"
        result_color = "green"
    elif win_percentage < 50:
        result_text = "Ваша стратегия бы проиграла"
        result_color = "red"
    else:
        result_text = "Ваша стратегия бы ничего не проиграла и не выиграла"
        result_color = "black"

    result_text += f"\nПо такой стратегии вы бы набрали {wins} баллов из {total_attempts} количества попыток."
    result_text += f"\nВаш процент побед равен = {win_percentage:.2f}%"
    result_text += f"\nВсего было ставок {all_total_attempts}, на сумму {all_total_attempts * 10} рублей."
    result_text += f"\nОбщая прибыль составила {total_balance} рублей."

    root = tk.Tk()
    root.title("Результаты анализа")
    root.geometry("600x100")

    # Загрузка иконки окна
    root.iconbitmap("icon.ico")

    # Создание кастомного шрифта
    custom_font = ("Arial", 12, "bold")

    result_label = tk.Label(root, text=result_text, font=custom_font, padx=20, pady=10, fg=result_color)
    result_label.pack()

    root.mainloop()

if __name__ == "__main__":
    analyze_results("results.txt")
