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
time.sleep(2)
send_keys("^l") # Izceļ tekstu
send_keys(r"C:\Users\edvin\Desktop\automat\foto") # Ieraksta mapi, no kuras jāņem fotografijas
send_keys("{ENTER}")
prg.Image.click_input() # Klikšķis uz fotografiju
send_keys("^a") # Izcel visas fotgrafijas
send_keys("{ENTER}") # Atver visas fotografijas Adobe Photoshop 2024
time.sleep(4)

exit_loop = False

while not app['Adobe Photoshop 2024'].exists() and not exit_loop:
    
    #Spilgtums/Kontrasts (Яркость/Контрастность)
    send_keys("^.") # Atver Spilgtums/Kontrasts (Яркость/Контрастность )
    send_keys("150")# Spilgtums (Яркость)
    send_keys("{TAB}")
    send_keys("-50")# Kontrasts (Контрастность)
    send_keys("{ENTER}")

    # Līmeņi (Уровни)
    send_keys("^l") # Atver līmeņi (уровни)
    time.sleep(1)
    send_keys("{TAB}")
    send_keys("{TAB}")
    send_keys("{TAB}")
        #Ievades vērtības (Входные значения):
    send_keys("30") 
    send_keys("{TAB}")  
    send_keys("1,60") 
    send_keys("{TAB}")
    send_keys("235") 
    send_keys("{TAB}")
        # Izvades vērtības (Выходные значения):
    send_keys("3") 
    send_keys("{TAB}")
    send_keys("240") 
    send_keys("{TAB}")
    send_keys("{ENTER}")

    # Līknes (Кривые)
    send_keys("^m") # Atver līknes ( Кривые)
    time.sleep(1)
    target_x = 360 # peles x pozīcija
    target_y = 500 # peles y pozīcija
    pyautogui.click(target_x, target_y) # peles klikšķis uz koordinātām
    pyautogui.click() # peles klikšķis
    send_keys("{TAB}")
    send_keys("{TAB}")
    send_keys("{TAB}")
    send_keys("100") # Izeja (Выход)
    send_keys("{TAB}")
    send_keys("200") # Ieeja (Вход)
    send_keys("{ENTER}")

    # Ekspozīcija (Экспозиция)
    send_keys("+^m") # Atver ekspozīcija (Экспозиция)
    time.sleep(1)
    send_keys("2") # Ekspozīcija (Экспозиция)
    send_keys("{TAB}")
    send_keys("0,25") # Nobīde (Сдвиг)
    send_keys("{TAB}")
    send_keys("6") # Gamma-korekcija (Гамма-коррекция)
    send_keys("{ENTER}") 

    # Krāsainība (Красочность)
    send_keys("+^q") # Atver krāsainība (Красочность)
    time.sleep(1)
    send_keys("37") # Krāsainība (Красочность)
    send_keys("{TAB}")
    send_keys("50") # Piesātinājums (Насыщенность)
    send_keys("{ENTER}") 

    # Gudrs asums (Умная резкость)
    send_keys("+^p") # Atver gudrs asums (Умная резкость)
    time.sleep(1)
    send_keys("{TAB}")
    send_keys("{TAB}")
    send_keys("{TAB}")
    send_keys("300") # Efekts (Эффект)
    send_keys("{TAB}")
    send_keys("13") # Rādiuss (Радиус)
    send_keys("{TAB}")
    send_keys("72") # Samazinat troksni (Уменьшить шум)
    send_keys("{ENTER}") 
    time.sleep(20)

    # Kontūras asums (Контурная резкость)
    send_keys("%^x") # Atver kontūras asums (Контурная резкость)
    time.sleep(1)
    send_keys("300") # Efekts (Эффект)
    send_keys("{TAB}")
    send_keys("13") # Rādiuss (Радиус)
    send_keys("{TAB}")
    send_keys("72") # Slieksnis (Порог)
    send_keys("{ENTER}") 
    time.sleep(1)

    send_keys("%^d") # Asums + (Резкость +)
    time.sleep(1)

    send_keys("%^h") # Asums malās (Резкость на краях)
    time.sleep(1)
    send_keys("%^q") # Asuma pastiprināšana (Усиление резкости)
    time.sleep(1)

    # Attēla izmērs
    send_keys("%^i") # Atver attēla izmērs
    time.sleep(1)
    send_keys("300") # Platums (Ширина)
    send_keys("{TAB}")
    send_keys("{TAB}")
    send_keys("{TAB}")
    send_keys("{TAB}")
    send_keys("72") # izšķirtspēja (Разрешение)
    send_keys("{ENTER}") 

        # Apstrādātā fotoattēla saglabāšana un aizvēršana
    send_keys("+^s") # atver failu pārluku
    time.sleep(2)
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
    time.sleep(2)
    send_keys("^w") # Pēc saglabāšanas aizver fotoattēlu
    time.sleep(1)
    if app['Adobe Photoshop 2024'].exists():
        exit_loop = True
    time.sleep(1)


app.kill() # Aizver Adobe Photoshop 2024
