def main():
    """Главное меню"""
    show_welcome()

    while True:
        print("\n=== ВИСЕЛИЦА ===")
        print("1 - Новая игра (против компьютера)")
        print("2 - Игра с другом")
        print("3 - Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            play_game()
        elif choice == '2':
            play_with_friend()
        elif choice == '3':
            print("До свидания!")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()