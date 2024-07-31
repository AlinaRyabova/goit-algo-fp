items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорій до вартості у спадному порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []
    
    # Вибираємо страви з найвищим співвідношенням калорій до вартості, поки не вичерпається бюджет
    for item, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            selected_items.append(item)
            total_cost += info['cost']
            total_calories += info['calories']
    
    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    # Ініціалізуємо таблицю DP
    dp = [0] * (budget + 1)
    selected_items = [[] for _ in range(budget + 1)]
    
    # Проходимо через всі страви і оновлюємо таблицю DP
    for item, info in items.items():
        for b in range(budget, info['cost'] - 1, -1):
            if dp[b - info['cost']] + info['calories'] > dp[b]:
                dp[b] = dp[b - info['cost']] + info['calories']
                selected_items[b] = selected_items[b - info['cost']] + [item]
    
    max_calories = dp[budget]
    optimal_items = selected_items[budget]
    total_cost = sum(items[item]['cost'] for item in optimal_items)
    
    return optimal_items, total_cost, max_calories

# Приклад використання
budget = 100

# Жадібний алгоритм
greedy_selected_items, greedy_total_cost, greedy_total_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print(f"Обрані страви: {greedy_selected_items}")
print(f"Загальна вартість: {greedy_total_cost}")
print(f"Загальна калорійність: {greedy_total_calories}")

# Алгоритм динамічного програмування
dp_selected_items, dp_total_cost, dp_total_calories = dynamic_programming(items, budget)
print("\nАлгоритм динамічного програмування:")
print(f"Обрані страви: {dp_selected_items}")
print(f"Загальна вартість: {dp_total_cost}")
print(f"Загальна калорійність: {dp_total_calories}")
