import timeit

from algorithms import boyer_moore, kmp_search, rabin_karp


# 1. Зчитуємо тексти з файлів

with open("article1.txt", "r", encoding="utf-8") as file:
    text1 = file.read()

with open("article2.txt", "r", encoding="utf-8") as file:
    text2 = file.read()


# 2. Перевіряємо завантажені тексти

print("КІЛЬКІСТЬ СИМВОЛІВ")
print("-" * 50)

print("Перша стаття:", len(text1))
print("Друга стаття:", len(text2))

if text1 == text2:
    print("УВАГА: обидва файли містять однаковий текст!")


# 3. Визначаємо підрядки для пошуку

# Підрядок, який точно є в першій статті
pattern1_exists = text1[100:130]

# Підрядок, якого немає в першій статті
pattern1_missing = "XYZ_ABCD_123456"

# Підрядок, який є в другій статті
pattern2_exists = "рекомендаційної системи"

# Підрядок, якого немає в другій статті
pattern2_missing = "NONEXISTENT_PATTERN_987"


# 4. Створюємо список алгоритмів

algorithms = {
    "Boyer-Moore": boyer_moore,
    "KMP": kmp_search,
    "Rabin-Karp": rabin_karp
}


# 5. Створюємо список тестів

tests = [
    ("Стаття 1 — підрядок є", text1, pattern1_exists),
    ("Стаття 1 — підрядка немає", text1, pattern1_missing),
    ("Стаття 2 — підрядок є", text2, pattern2_exists),
    ("Стаття 2 — підрядка немає", text2, pattern2_missing)
]


# 6. Вимірюємо час виконання алгоритмів

number = 1000

# Зберігаємо загальний час кожного алгоритму
total_times = {
    "Boyer-Moore": 0,
    "KMP": 0,
    "Rabin-Karp": 0
}

print("\nРЕЗУЛЬТАТИ ПОШУКУ")
print("-" * 65)

for test_name, text, pattern in tests:

    print("\n", test_name)
    print("-" * 65)

    results = {}

    for algorithm_name, algorithm in algorithms.items():

        # Перевіряємо правильність результату
        result = algorithm(text, pattern)

        if result != text.find(pattern):
            raise ValueError(
                f"Помилка в алгоритмі {algorithm_name}"
            )

        # Вимірюємо час виконання
        elapsed_time = timeit.timeit(
            lambda: algorithm(text, pattern),
            number=number
        )

        # Середній час одного пошуку
        average_time = elapsed_time / number

        results[algorithm_name] = average_time

        # Додаємо час до загального результату
        total_times[algorithm_name] += average_time

        print(
            f"{algorithm_name:<15} "
            f"{average_time:.9f} секунд"
        )

    # Визначаємо найшвидший алгоритм для поточного тесту
    fastest = min(results, key=results.get)

    print(f"\nНайшвидший алгоритм: {fastest}")


# 7. Визначаємо загальний результат

print("\n\nЗАГАЛЬНЕ ПОРІВНЯННЯ")
print("-" * 65)

for algorithm_name, total_time in total_times.items():
    print(
        f"{algorithm_name:<15} "
        f"{total_time:.9f} секунд"
    )

fastest_overall = min(total_times, key=total_times.get)

print("\nНайшвидший алгоритм загалом:", fastest_overall)