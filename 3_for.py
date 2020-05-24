"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""


def main():
    classes = [
        {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
        {'school_class': '5a', 'scores': [3, 1, 2, 5, 2]},
        {'school_class': '6a', 'scores': [1, 4, 2, 5, 5]},
    ]
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    all_scores = [score for class_ in classes for score in class_['scores']]

    average = sum(all_scores) / len(all_scores)

    for class_ in classes:
        scores = class_['scores']
        average_by_class = sum(scores) / len(scores)
        print(f'Average in {class_["school_class"]}: {average_by_class} ')

    print(f"Average in school: {average}")


if __name__ == "__main__":
    main()
