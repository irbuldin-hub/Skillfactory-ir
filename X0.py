# Создаем игровое поле - список из 9 элементов (3 строки по 3 клетки)
board = [" "] * 9

# Функция для отображения игрового поля
def show_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

# Функция для проверки победы
def check_win():
    # Проверяем горизонтальные линии
    for i in [0, 3, 6]:
        if board[i] == board[i+1] == board[i+2] != " ":
            return True
    
    # Проверяем вертикальные линии
    for i in [0, 1, 2]:
        if board[i] == board[i+3] == board[i+6] != " ":
            return True
    
    # Проверяем диагонали
    if board[0] == board[4] == board[8] != " ":
        return True
    if board[2] == board[4] == board[6] != " ":
        return True
    
    return False

# Основная функция игры
def play_game():
    current_player = "X"  # Первым ходит X
    
    print("Добро пожаловать в крестики-нолики!")
    print("Чтобы сделать ход, введи номер клетки (1-9):")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print()
    
    for _ in range(9):  # Максимум 9 ходов в игре
        show_board()
        
        # Получаем ход от игрока
        while True:
            try:
                move = int(input(f"Игрок {current_player}, твой ход (1-9): ")) - 1
                if 0 <= move <= 8 and board[move] == " ":
                    break
                else:
                    print("Некорректный ход. Попробуй еще раз.")
            except ValueError:
                print("Пожалуйста, введи число от 1 до 9.")
        
        # Делаем ход
        board[move] = current_player
        
        # Проверяем победу
        if check_win():
            show_board()
            print(f"Игрок {current_player} победил! Поздравляю!")
            return
        
        # Меняем игрока
        current_player = "O" if current_player == "X" else "X"
    
    # Если все клетки заполнены и нет победителя
    show_board()
    print("Ничья!")

# Запускаем игру
play_game()