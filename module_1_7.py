grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = sorted(students)
# print(students_list) -> проверка порядка отсортированных студентов
first_average_score = sum(grades[0]) / len(grades[0])
second_average_score = sum(grades[1]) / len(grades[1])
third_average_score = sum(grades[2]) / len(grades[2])
fourth_average_score = sum(grades[3]) / len(grades[3])
fifth_average_score = sum(grades[4]) / len(grades[4])
average_score = {students_list[0]: first_average_score,
                 students_list[1]: second_average_score,
                 students_list[2]: third_average_score,
                 students_list[3]: fourth_average_score,
                 students_list[4]: fifth_average_score}
print(average_score)