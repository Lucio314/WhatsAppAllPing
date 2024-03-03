import pyautogui
import time

nbrPers = int(input("Entrez le nombre de personnes du groupe : "))

time.sleep(1)
print("Initialisation du script......")
time.sleep(2)
input(
    "Appuyez sur la touche Entrer pour activer le script et \n déplacez vous rapidement dans  la discussion du groupe"
)

time.sleep(2)

i = 1
while i <= nbrPers:
    pyautogui.typewrite("@")
    j = i
    while j <= i:
        time.sleep(1)
        pyautogui.press("down")
        j += 1
    pyautogui.press("enter")
    pyautogui.hotkey("shift", "enter")
    i += 1
