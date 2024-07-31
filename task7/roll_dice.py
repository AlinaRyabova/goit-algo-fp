import random
import matplotlib.pyplot as plt
import pandas as pd

def roll_dice():
    """Функція для симуляції кидка двох кубиків"""
    return random.randint(1, 6) + random.randint(1, 6)

def monte_carlo_simulation(num_trials):
    """Функція для виконання симуляції методу Монте-Карло"""
    sum_counts = {i: 0 for i in range(2, 13)}

    for _ in range(num_trials):
        dice_sum = roll_dice()
        sum_counts[dice_sum] += 1

    probabilities = {s: (count / num_trials) * 100 for s, count in sum_counts.items()}
    return probabilities

def plot_probabilities(simulated_probabilities, theoretical_probabilities):
    """Функція для побудови графіку ймовірностей"""
    sums = list(simulated_probabilities.keys())
    simulated_probs = list(simulated_probabilities.values())
    theoretical_probs = list(theoretical_probabilities.values())

    plt.bar(sums, simulated_probs, color='skyblue', alpha=0.7, label='Симульовані ймовірності')
    plt.plot(sums, theoretical_probs, color='red', marker='o', label='Теоретичні ймовірності')
    plt.xlabel('Сума на кубиках')
    plt.ylabel('Ймовірність (%)')
    plt.title('Ймовірності сум чисел, що випали на кубиках')
    plt.xticks(sums)
    plt.legend()
    plt.show()

def create_comparison_table(simulated_probabilities, theoretical_probabilities):
    """Функція для створення порівняльної таблиці"""
    data = {
        'Сума': list(simulated_probabilities.keys()),
        'Симульована ймовірність (%)': list(simulated_probabilities.values()),
        'Теоретична ймовірність (%)': list(theoretical_probabilities.values())
    }
    df = pd.DataFrame(data)
    print("\nПорівняльна таблиця ймовірностей:\n")
    print(df)

def main():
    num_trials = 1000000  # Кількість симуляцій
    simulated_probabilities = monte_carlo_simulation(num_trials)

    # Теоретичні ймовірності для кожної суми (у відсотках)
    theoretical_probabilities = {
        2: (1 / 36) * 100,
        3: (2 / 36) * 100,
        4: (3 / 36) * 100,
        5: (4 / 36) * 100,
        6: (5 / 36) * 100,
        7: (6 / 36) * 100,
        8: (5 / 36) * 100,
        9: (4 / 36) * 100,
        10: (3 / 36) * 100,
        11: (2 / 36) * 100,
        12: (1 / 36) * 100
    }

    # Вивід ймовірностей на екран
    print("Симульовані ймовірності сум чисел, що випали на кубиках (Метод Монте-Карло):")
    for dice_sum, prob in simulated_probabilities.items():
        print(f"Сума {dice_sum}: ймовірність {prob:.2f}%")

    print("\nТеоретичні ймовірності сум чисел, що випали на кубиках:")
    for dice_sum, prob in theoretical_probabilities.items():
        print(f"Сума {dice_sum}: ймовірність {prob:.2f}%")

    # Побудова графіку
    plot_probabilities(simulated_probabilities, theoretical_probabilities)

    # Створення порівняльної таблиці
    create_comparison_table(simulated_probabilities, theoretical_probabilities)

if __name__ == "__main__":
    main()
