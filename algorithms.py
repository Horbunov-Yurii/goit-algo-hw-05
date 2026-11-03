def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)

    if m == 0:
        return 0

    if m > n:
        return -1

    # Створюємо таблицю останніх входжень символів
    last = {}

    for i in range(m):
        last[pattern[i]] = i

    # Початкова позиція підрядка в тексті
    shift = 0

    while shift <= n - m:
        j = m - 1

        # Порівнюємо символи справа наліво
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1

        # Якщо всі символи збіглися
        if j < 0:
            return shift

        # Обчислюємо зсув за правилом поганого символу
        bad_char = text[shift + j]
        move = j - last.get(bad_char, -1)

        shift += max(1, move)

    return -1


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    if m == 0:
        return 0

    if m > n:
        return -1

    # Створюємо таблицю префіксів
    lps = [0] * m

    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    # Пошук підрядка в тексті
    i = 0
    j = 0

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                return i - j

        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1


def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)

    if m == 0:
        return 0

    if m > n:
        return -1

    prime = 101
    base = 256

    pattern_hash = 0
    text_hash = 0
    h = 1

    # Обчислюємо значення h
    for i in range(m - 1):
        h = (h * base) % prime

    # Обчислюємо початкові хеші
    for i in range(m):
        pattern_hash = (
            base * pattern_hash + ord(pattern[i])
        ) % prime

        text_hash = (
            base * text_hash + ord(text[i])
        ) % prime

    # Перевіряємо всі можливі позиції
    for i in range(n - m + 1):

        # Якщо хеші збігаються, перевіряємо самі рядки
        if pattern_hash == text_hash:
            if text[i:i + m] == pattern:
                return i

        # Обчислюємо хеш наступного фрагмента
        if i < n - m:
            text_hash = (
                base * (text_hash - ord(text[i]) * h)
                + ord(text[i + m])
            ) % prime

            if text_hash < 0:
                text_hash += prime

    return -1