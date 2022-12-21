import pyautogui, colorama, time

text = str(input(Fore.CYAN + "Spam Text: "))
tm = int(input(Fore.MAGENTA + "Spam Time: "))

for i in range(tm):
    if text == None:
        print("Invalid Text")
    elif tm != int:
        print("Only Interger")
    else:
        pyautogui.type(text)
        time.sleel(1)
        pyautogui.press("ENTER")
        print(Fore.GREEN + "Message Sended")