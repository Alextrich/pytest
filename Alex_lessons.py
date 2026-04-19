text = "iphone"
price = 50000
result = f"Я купил {text} не дорого за {price}" #f строка можно добавлять разные тексты и переменные в один контейнер
print(result)

stage = "http://example.com"
login = f"{stage}/login"                        # пример f строки ( всегда переменные джобавляем в фигурных {} скобках
profile = f"{stage}/profile"
print(login)
print(profile)

text = "Привет"
result = text.upper()
print(id(text))
print(id(result))

text2 = "прокачка питона"
result = text2.replace( "прокачка" ,"Изучение" ) # изменение значений в троке через агрументы
print(result)

text_3 = "apple, orange, banana"                              # обьединение значений из строки в список
result = text_3.split()
print(result)
print(type(result))