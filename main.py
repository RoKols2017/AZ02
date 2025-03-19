import pandas as pd
import matplotlib.pyplot as plt
from students_grades_generator.grades_simulator import edu_stats


# Укажите путь к вашему CSV-файлу
csv_filename = edu_stats()

# Открываем CSV-файл и создаем DataFrame
df = pd.read_csv(csv_filename, encoding="utf-8-sig")

# Вычисляем среднюю оценку по каждому предмету
average_grades = df.groupby("Предмет")["Оценка"].mean()

# Вычисляем медианную оценку по каждому предмету
median_grades = df.groupby("Предмет")["Оценка"].median()

# Фильтруем только оценки по математике
math_scores = df[df["Предмет"] == "Математика"]["Оценка"]

# Вычисляем квартиль 1 (Q1), квартиль 3 (Q3) и межквартильный размах (IQR)
Q1_math = math_scores.quantile(0.25)
Q3_math = math_scores.quantile(0.75)
IQR_math = Q3_math - Q1_math

# Вычисляем стандартное отклонение
std_math = math_scores.std()

# Вывод результатов
print("Выводим 2 строки")
print(df.head(2))
print(f"\nСредние оценки по предметам:\n{average_grades.round(2)}")
print(f"\nМедианные оценки по предметам:\n{median_grades.round(2)}")
print(f"Q1 (25-й процентиль) по математике: {Q1_math:.2f}")
print(f"Q3 (75-й процентиль) по математике: {Q3_math:.2f}")
print(f"IQR (межквартильный размах) по математике: {IQR_math:.2f}")
print(f"Стандартное отклонение по математике: {std_math:.2f}")

# Создаем boxplot (ящик с усами) для визуализации оценок по каждому предмету
plt.figure(figsize=(10, 6))
df.boxplot(column="Оценка", by="Предмет", grid=False)

# Настройки графика
plt.title("Boxplot (ящик с усами) оценок по предметам")
plt.suptitle("")  # Убираем автоматический заголовок, добавляем свой
plt.xlabel("Предмет")
plt.ylabel("Оценка")
plt.xticks(rotation=20)  # Наклон подписей предметов для удобства чтения

# Показываем график
plt.show()
