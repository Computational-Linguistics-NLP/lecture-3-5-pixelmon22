text = input("Введите текст: ")
length = len(text)
if length < 2:
    result = "чудовищно мало"
elif length < 5:
    result = "очень мало"
elif length < 10:
    result = "мало"
elif length < 30:
    result = "ок"
elif length < 100:
    result = "много"
else:
    result = "чудовищно много"
print(result)