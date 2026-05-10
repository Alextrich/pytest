# Как вывести ответ в JSON а не в строку
import json                                                         # импортируем библиотеку json как в примере

human = {
    "name": "Alex",
    "age": 40,
    "education": False,
    "list_of_items": ["математика", "физика", "программирование"],
    "country": {
        "Bulgary":"born",
        "Russia": "live"
    }
}
print(json.dumps(human, ensure_ascii=False, indent=4))             # выводим все как указано и 2 это команда для кириллицы и последняя - табуляция = 4 пробела