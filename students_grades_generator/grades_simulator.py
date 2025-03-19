import pandas as pd
import random


def edu_stats():
    # Список учеников
    names = ["Алексей", "Мария", "Иван", "София", "Дмитрий", "Анна", "Егор", "Полина", "Кирилл", "Екатерина"]
    subjects = ["Математика", "Русский язык", "Физика", "История", "Литература"]

    # Создаём список данных
    data = []

    for name in names:
        for subject in subjects:
            for _ in range(17):  # 17 оценок на ученика по каждому предмету
                data.append([name, subject, random.randint(2, 5)])  # Генерируем оценку от 2 до 5

    # Создаём DataFrame
    df = pd.DataFrame(data, columns=["Имя", "Предмет", "Оценка"])

    # Сохраняем в CSV
    csv_filename = "students_grades.csv"
    df.to_csv(csv_filename, index=False, encoding="utf-8-sig")

    return csv_filename  # Возвращаем имя файла