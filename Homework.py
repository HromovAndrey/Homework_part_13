# Завдання 2
# Маємо певний словник з назвами музичних груп (виконавців) та альбомів. Назва групи використовується як ключ,
# назва альбомів — як значення. Реалізуйте: додавання, видалення, пошук, редагування, збереження та завантаження
# даних (використовуючи стиснення та розпакування).
import pickle
import gzip

bands_albums = {
    "The Beatles": "Abbey Road",
    "Pink Floyd": "The Dark Side of the Moon",
    "Led Zeppelin": "Led Zeppelin IV",
    "Queen": "A Night at the Opera",
    "The Rolling Stones": "Exile on Main St."
}

def add_band(band, album):
    bands_albums[band] = album
    print("Музичну групу '{}' з альбомом '{}' успішно додано.".format(band, album))

def remove_band(band):
    if band in bands_albums:
        del bands_albums[band]
        print("Музичну групу '{}' успішно видалено.".format(band))
    else:
        print("Музична група '{}' не знайдена.".format(band))

def find_album(band):
    if band in bands_albums:
        print("Альбом музичної групи '{}': '{}'".format(band, bands_albums[band]))
    else:
        print("Музична група '{}' не знайдена.".format(band))

def edit_album(band, new_album):
    if band in bands_albums:
        bands_albums[band] = new_album
        print("Альбом музичної групи '{}' успішно змінено на '{}'.".format(band, new_album))
    else:
        print("Музична група '{}' не знайдена.".format(band))

def save_data(filename):
    with gzip.open(filename, 'wb') as f:
        pickle.dump(bands_albums, f)
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

add_band("Metallica", "Master of Puppets")
remove_band("Pink Floyd")
find_album("The Beatles")
edit_album("The Rolling Stones", "Sticky Fingers")

save_data("bands_data.pklz")
loaded_data = load_data("bands_data.pklz")
if loaded_data:
    print("Завантажені дані:", loaded_data)
