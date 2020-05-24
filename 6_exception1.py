"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""

def ask_user():
    """
    Замените pass на ваш код
    """
    answer = ''
    try:
        while answer != 'Хорошо':
            answer = input('Как дела? ')
    except KeyboardInterrupt:
        print('Пока!')

if __name__ == "__main__":
    ask_user()
