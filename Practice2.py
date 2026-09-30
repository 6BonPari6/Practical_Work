https://www.figma.com/board/xj0DvhuiIH8vC6vej0ui6r/2?node-id=0-1&p=f&t=OxuaEWDyeRjbHswK-0

https://www.figma.com/board/7Vr9W2qLnCWJnQmmTBVyLP/1?t=OxuaEWDyeRjbHswK-0

https://www.figma.com/board/8XPIPxJEidkyojFsLuTgjo/3?t=OxuaEWDyeRjbHswK-0


name = input("Введите имя: ")
age_str = input("Введите возраст: ")
subjects_str = input("Любимые предметы (через запятую): ")
age = int(age_str)
subjects_list = [s.strip() for s in subjects_str.split(',')]
student = {
    "name": name,
    "age": age,
    "subjects": subjects_list
}
print("==============================")
print("АНКЕТА СТУДЕНТА")
print("==============================")
print(f"Имя: {student['name']}")
print(f"Возраст: {student['age']}")
print(f"Любимые предметы: {student['subjects']}")
print("===============================")
