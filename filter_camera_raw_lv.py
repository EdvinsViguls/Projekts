import time
import keyboard
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
import pyautogui


app = Application(backend="uia").start(r"C:\Program Files\Adobe\Adobe Photoshop 2024\Photoshop.exe").connect(title="Adobe Photoshop 2024", timeout=100)

time.sleep(2)


prg = app.window(title="Adobe Photoshop 2024")


prg.set_focus()

# Atver visas fotografijas no noteiktas mapes
send_keys("^o") # atver failu pārluku
time.sleep(4)
send_keys("^l") # Izceļ tekstu
send_keys(r"C:\Users\edvin\Desktop\automat\foto") # Ieraksta mapi, no kuras jāņem fotografijas
send_keys("{ENTER}")
prg.Image.click_input() # Klikšķis uz fotografiju
send_keys("^a") # Izcel visas fotgrafijas
send_keys("{ENTER}") # Atver visas fotografijas Adobe Photoshop 2024
time.sleep(4)

exit_loop = False

while not app['Adobe Photoshop 2024'].exists() and not exit_loop:
    
    # Filtrs Camera raw(Фильтр Camera raw)
    send_keys("+^a") #  Atver Filtrs Camera raw(Фильтр Camera raw)
    time.sleep(4)
    target_x = 1800 # peles x pozīcija
    target_y = 390 # peles y pozīcija
    pyautogui.doubleClick(target_x, target_y) 
    # Gaisma (Свет)
    send_keys("2") # Ekspozīcija (Экспозиция)
    send_keys("{TAB}")
    send_keys("22") # Kontrasts (Контрастность)
    send_keys("{TAB}")
    send_keys("22") # Gaismas zonas (Светлые области)
    send_keys("{TAB}")
    send_keys("22") # Ēna (Тени)
    send_keys("{TAB}")
    send_keys("22") # Baltie(Белые)
    send_keys("{TAB}")
    send_keys("22") # Melnie (Черные)

    # Krāsa (Цвет)
    target_x = 1800 # peles x pozīcija
    target_y = 740 # peles y pozīcija
    pyautogui.doubleClick(target_x, target_y) 
    send_keys("33") # Temperatūra (Температура)
    send_keys("{TAB}")
    send_keys("65") # Tonis (Оттенок)
    send_keys("{TAB}")
    send_keys("54") # Krāsainība (Красочность)
    send_keys("{TAB}")
    send_keys("77") # Piesātinājums (Насыщеность)
    send_keys("{TAB}")
    # Efekts(Эффекты)
    send_keys("25") # Tekstūra (Текстура)
    send_keys("{TAB}")
    send_keys("46") # Skaidrība (Четкость)
    send_keys("{TAB}")
    send_keys("22") # Miglas noņemšana(Удаление дымки)
    send_keys("{TAB}")
    send_keys("22") # Vinjete(Виньетка)
    send_keys("{TAB}")
    send_keys("22") # Graudains (Зерно)
    send_keys("{TAB}")
    # Līkne (Кривая)
    send_keys("22") # Gaismas zonas(Светлые области)
    send_keys("{TAB}")
    send_keys("22") # Gaišie toņi(Светлые тона)
    send_keys("{TAB}")
    send_keys("22") # Tumši toņi (Темные тона)
    send_keys("{TAB}")
    send_keys("22") # Ēna(Тени)
    send_keys("{TAB}")
    target_x = 1860 # peles x pozīcija
    target_y = 580 # peles y pozīcija
    pyautogui.doubleClick(target_x, target_y)

    target_x = 1790 # peles x pozīcija
    target_y = 320 # peles y pozīcija
    pyautogui.doubleClick(target_x, target_y)
    # Krāsu sajaukšana (Смешение цветов)
    send_keys("22") # Sarkans (Красные)
    send_keys("{TAB}")
    send_keys("22") # Oranža (Оранжевые)
    send_keys("{TAB}")
    send_keys("22") # Dzeltens (Желтые)
    send_keys("{TAB}")
    send_keys("22") # Zaļš(Зеленые)
    send_keys("{TAB}")
    send_keys("22") # Akvamarīns (Аквамариновые)
    send_keys("{TAB}")
    send_keys("22") # Zils (Синие)
    send_keys("{TAB}")
    send_keys("22") # Lillā (Лиловые)
    send_keys("{TAB}")
    send_keys("22") # Purpura (Пурпурные)
    send_keys("{TAB}")
    # Krāsu korekcija (Цветокоpрекция)
    send_keys("22") # Sajaukšana (Смешение)
    send_keys("{TAB}")
    send_keys("22") # Līdzsvars (Баланс)
    send_keys("{TAB}")
    # Detalizácija (Детализация)
    send_keys("2") # Asuma regulēšana (Регулировка резкости)
    send_keys("{TAB}")
    send_keys("2") # Trokšņa samazināšana (Уменьшение шума)
    send_keys("{TAB}")
    send_keys("2") # Krāsu trokšņu samazināšana (Уменьшение цветового шума)
    send_keys("{TAB}")
    # Optika (Оптика)
    send_keys("2") # izkropļojums (Искажение)
    send_keys("{TAB}")
    send_keys("2") # Vinjete (Виньетка)
    target_x = 1860 # peles x pozīcija
    target_y = 950 # peles y pozīcija
    pyautogui.doubleClick(target_x, target_y) 
    pyautogui.doubleClick(target_x, target_y)  
    target_x = 1790 # peles x pozīcija
    target_y = 680 # peles y pozīcija
    pyautogui.doubleClick(target_x, target_y)
    # Kalibrēšana (Калибровка)
    ## Pamata sarkans (Основной красный)
    send_keys("22") # Krāsu tonis (Цветовой тон)
    send_keys("{TAB}")
    send_keys("22") # Piesātinājums (Насыщенность)
    send_keys("{TAB}")
    # Pamata zaļš(Основной зелёный)
    send_keys("22") # Krāsu tonis (Цветовой тон)
    send_keys("{TAB}")
    send_keys("22") # Piesātinājums (Насыщенность)
    send_keys("{TAB}")
    # Pamata zils (Основной синий)
    send_keys("22") # Krāsu tonis (Цветовой тон)
    send_keys("{TAB}")
    send_keys("22") # Piesātinājums (Насыщенность)
    send_keys("{ENTER}")
    send_keys("{ENTER}")
    time.sleep(8)

        # Apstrādātā fotoattēla saglabāšana un aizvēršana
    send_keys("+^s") # atver failu pārluku
    time.sleep(6)
    send_keys("^l") # Izcel tekstu
    send_keys(r"C:\Users\edvin\Desktop\automat\apstradats") # Norāda mapi, kurā saglabāt fotoattēlu
    send_keys("{ENTER}")
    time.sleep(1)
    send_keys("{ENTER}")
    time.sleep(1)  
    send_keys("{TAB}")
    send_keys("{TAB}")
    send_keys("{ENTER}")
    time.sleep(2)
    send_keys("11") # Kvalitāte (Качество)
    send_keys("{ENTER}")
    time.sleep(4)
    send_keys("^w") # Pēc saglabāšanas aizver fotoattēlu
    time.sleep(3)
    if app['Adobe Photoshop 2024'].exists():
        exit_loop = True
    time.sleep(1)


app.kill() # Aizver Adobe Photoshop 2024