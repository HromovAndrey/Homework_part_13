# Завдання 1
# Маємо певний словник з назвами країн і столиць. Назва
# країни використовується як ключ, назва столиці — як значення. Реалізуйте: додавання, видалення, пошук, редагування,
# збереження та завантаження даних (використовуючи стиснення та розпакування).

import pickle
import gzip
countries_capitals = {
    "Україна": "Київ",
    "США": "Вашингтон",
    "Франція": "Париж",
    "Німеччина": "Берлін",
    "Італія": "Рим"
}

def add_country(country, capital):
    countries_capitals[country] = capital
    print("Країну '{}' зі столицею '{}' успішно додано.".format(country, capital))
def remove_country(country):
    if country in countries_capitals:
        del countries_capitals[country]
        print("Країну '{}' успішно видалено.".format(country))
    else:
        print("Країна '{}' не знайдена.".format(country))
def find_capital(country):
    if country in countries_capitals:
        print("Столиця країни '{}': '{}'".format(country, countries_capitals[country]))
    else:
        print("Країна '{}' не знайдена.".format(country))
def edit_capital(country, new_capital):
    if country in countries_capitals:
        countries_capitals[country] = new_capital
        print("Столицю країни '{}' успішно змінено на '{}'.".format(country, new_capital))
    else:
        print("Країна '{}' не знайдена.".format(country))
def save_data(filename):
    with gzip.open(filename, 'wb') as f:
        pickle.dump(countries_capitals, f)
    print("Дані успішно збережено у файлі {}.".format(filename))
def load_data(filename):
    try:
        with gzip.open(filename, 'rb') as f:
            loaded_data = pickle.load(f)
            print("Дані успішно завантажено з файлу {}.".format(filename))
            return loaded_data
    except FileNotFoundError:
        print("Файл {} не знайдено.".format(filename))
        return None
add_country("Іспанія", "Мадрид")
remove_country("Франція")
find_capital("Україна")
edit_capital("Україна", "Львів")
save_data("countries_data.pklz")
loaded_data = load_data("countries_data.pklz")
if loaded_data:
    print("Завантажені дані:", loaded_data)
