text = input("Введите текст: ")
length = len(text)
if length < 2:
    result = "чудовищно мало"
elif 2 <= length < 5:
    result = "очень мало"
elif 5 <= length < 10:
    result = "мало"
elif 10 <= length < 30:
    result = "ок"
elif 30 <= length < 100:
    result = "много"
elif length >= 100:
    result = "чудовищно много"
print(result)