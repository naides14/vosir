from datetime import *

# расчет очков
def calculate_score(word, attempts_used, max_attempts, difficulty):
    basescore = len(word) * 10
    attemptbonus = (max_attempts - attempts_used) * 5
    mul = {'легкий': 1, 'средний': 2, 'сложный': 3}[difficulty]
    return (basescore + attemptbonus) * mul

# сохранение счета
def save_score(player, score, word, difficulty):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open('scores.txt', 'a', encoding='utf-8') as f:
            f.write(f"{timestamp} | {player} | {difficulty} | {word} | {score}\n")
    except Exception as e:
        print(f"Не удалось сохранить счет: {e}")