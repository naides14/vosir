# Словари для разных уровней сложности
WORD_LISTS = {
    'легкий': ['кот', 'дом', 'сад', 'нос', 'рот', 'сон', 'мир', 'час', 'брат', 'цвет'],
    'средний': ['программа', 'компьютер', 'библиотека', 'телефон', 'солнце', 'погода'],
    'сложный': ['электричество', 'достопримечательность', 'самостоятельность', 'благополучие']
}

# Максимальное количество ошибок для каждого уровня
MAX_ATTEMPTS = {'легкий': 8, 'средний': 6, 'сложный': 4}


def get_difficulty():
    """Выбор сложности"""
    print("\nВыберите сложность:")
    print("1 - Легкий (8 попыток)")
    print("2 - Средний (6 попыток)")
    print("3 - Сложный (4 попытки)")

    while True:
        choice = input("Ваш выбор (1-3): ")
        difficulties = {'1': 'легкий', '2': 'средний', '3': 'сложный'}
        if choice in difficulties:
            return difficulties[choice]
        print("Неверный выбор! Введите 1, 2 или 3.")


def display_word(word, guessed_letters):
    """Отображение слова с угаданными буквами"""
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def play_game():
    """Основная функция игры"""
    difficulty = get_difficulty()
    player_name = input("\nВведите ваше имя: ") or "Игрок"

    word = random.choice(WORD_LISTS[difficulty]).upper()
    max_attempts = MAX_ATTEMPTS[difficulty]
    attempts = 0
    guessed_letters = set()

    print(f"\nИгра началась! Слово из {len(word)} букв. Попыток: {max_attempts}")

    while attempts < max_attempts:
        print(f"\nСлово: {display_word(word, guessed_letters)}")
        print(f"Осталось попыток: {max_attempts - attempts}")
        show_hangman(max_attempts - attempts, max_attempts)

        guess = input("Введите букву: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Введите одну букву!")
            continue

        if guess in guessed_letters:
            print("Вы уже вводили эту букву!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Верно!")

            # Проверка победы
            if all(letter in guessed_letters for letter in word):
                score = calculate_score(word, attempts, max_attempts, difficulty)
                print(f"\nПоздравляем! Вы угадали слово: {word}")
                print(f"Ваш счет: {score} очков")
                save_score(player_name, score, word, difficulty)
                return
        else:
            attempts += 1
            print("Не угадали!")
        # Проигрыш
    print(f"\nИгра окончена! Загаданное слово: {word}")
    show_hangman(0, max_attempts)
    save_score(player_name, 0, word, difficulty)

def play_with_friend():
    """Режим игры с другом"""
    print("\n=== РЕЖИМ С ДРУГОМ ===")
    
    # Игрок, который загадывает слово
    print("\nИгрок 1 (загадывающий):")
    player1 = input("Введите ваше имя: ") or "Игрок 1"
    
    # Игрок, который отгадывает
    print("\nИгрок 2 (отгадывающий):")
    player2 = input("Введите ваше имя: ") or "Игрок 2"
    
    # Загадывание слова
    print(f"\n{player1}, загадайте слово:")
    word = input("Введите слово: ").upper().strip()
    print("\n" * 20)
    
    # Проверка введенного слова
    while not word.isalpha() or len(word) < 2:
        print("Слово должно содержать только буквы и быть не короче 2 символов!")
        word = input("Введите слово: ").upper().strip()
    
    # Выбор сложности (количества попыток)
    print(f"\n{player1}, выберите количество попыток для {player2}:")
    print("1 - Легкий (8 попыток)")
    print("2 - Средний (6 попыток)")
    print("3 - Сложный (4 попытки)")
    
    while True:
        choice = input("Ваш выбор (1-3): ")
        if choice == '1':
            max_attempts = 8
            difficulty = 'легкий'
            break
        elif choice == '2':
            max_attempts = 6
            difficulty = 'средний'
            break
        elif choice == '3':
            max_attempts = 4
            difficulty = 'сложный'
            break
        else:
            print("Неверный выбор! Введите 1, 2 или 3.")
    
    # Очистка экрана (условная)
    print("\n" * 50)
    print(f"{player2}, теперь ваша очередь отгадывать!")
    
    # Процесс отгадывания
    attempts = 0
    guessed_letters = set()
    
    print(f"\nСлово из {len(word)} букв. Попыток: {max_attempts}")

    while attempts < max_attempts:
        print(f"\nСлово: {display_word(word, guessed_letters)}")
        print(f"Осталось попыток: {max_attempts - attempts}")
        show_hangman(max_attempts - attempts, max_attempts)

        guess = input("Введите букву: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Введите одну букву!")
            continue

        if guess in guessed_letters:
            print("Вы уже вводили эту букву!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Верно!")

            # Проверка победы
            if all(letter in guessed_letters for letter in word):
                score = calculate_score(word, attempts, max_attempts, difficulty)
                print(f"\nПоздравляем, {player2}! Вы угадали слово: {word}")
                print(f"Счет {player2}: {score} очков")
                save_score(player2, score, word, difficulty)
                return
        else:
            attempts += 1
            print("Не угадали!")

    # Проигрыш
    print(f"\nИгра окончена! Загаданное слово: {word}")
    show_hangman(0, max_attempts)
    print(f"{player1} загадал(а) слово: {word}")
    save_score(player2, 0, word, difficulty)
    