from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
import threading

ascii_letters = {
    "R": [
        "█████ ",
        "█    █",
        "█████ ",
        "█  █  ",
        "█   █ "
    ],
    "A": [
        "  ███  ",
        " █   █ ",
        "██████ ",
        "█     █",
        "█     █"
    ],
    "T": [
        "███████",
        "   █   ",
        "   █   ",
        "   █   ",
        "   █   "
    ],
    "M": [
        "█     █",
        "██   ██",
        "█ █ █ █",
        "█  █  █",
        "█     █"
    ],
    "E": [
        "███████",
        "█      ",
        "█████  ",
        "█      ",
        "███████"
    ],
    "İ": [
        "  █  ",
        "     ",
        "  █  ",
        "  █  ",
        "  █  "
    ],
    "N": [
        "█     █",
        "██    █",
        "█ █   █",
        "█  █  █",
        "█   █ █"
    ]
}

dark_colors = [
    Fore.LIGHTBLACK_EX,
    Fore.BLUE,
    Fore.GREEN,
    Fore.MAGENTA,
    Fore.CYAN,
    Fore.LIGHTBLACK_EX,
    Fore.BLUE,
    Fore.GREEN
]

letters = ["R","A","T","M","E","R","İ","N"]

def print_ratmerin():
    for idx, letter in enumerate(letters):
        color = dark_colors[idx]
        indent = " " * (idx * 5)
        for line in ascii_letters[letter]:
            print(indent + color + line + Style.RESET_ALL)
        print()
        sleep(0.3)

system("cls||clear")
print_ratmerin()

servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if not attribute.startswith('__'):
            servisler_sms.append(attribute)

while True:
    system("cls||clear")
    print_ratmerin()
    print(f"{Fore.LIGHTCYAN_EX}Sms servis sayısı: {len(servisler_sms)}   {Style.RESET_ALL}by {Fore.LIGHTRED_EX}@Codza\n")
    try:
        menu = input(Fore.LIGHTMAGENTA_EX + " 1- SMS Gönder (Normal)\n\n 2- SMS Gönder (Turbo)\n\n 3- Çıkış\n\n" + Fore.LIGHTYELLOW_EX + " Seçim: ")
        if menu == "":
            continue
        menu = int(menu)
    except ValueError:
        print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
        sleep(3)
        continue

    if menu == 1:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız (Birden çoksa 'enter' tuşuna basınız): "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        tel_liste = []
        if tel_no == "":
            system("cls||clear")
            print(Fore.LIGHTYELLOW_EX + "Telefon numaralarının kayıtlı olduğu dosyanın dizinini yazınız: "+ Fore.LIGHTGREEN_EX, end="")
            dizin = input()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            tel_liste.append(i)
                sonsuz = ""
            except FileNotFoundError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı dosya dizini. Tekrar deneyiniz.")
                sleep(3)
                continue
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
                sonsuz = "(Sonsuz ise 'enter' tuşuna basınız)"
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.")
                sleep(3)
                continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.")
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + f"Kaç adet SMS göndermek istiyorsun {sonsuz}: "+ Fore.LIGHTGREEN_EX, end="")
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Kaç saniye aralıkla göndermek istiyorsun: "+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
            sleep(3)
            continue
        system("cls||clear")

        if kere is None:
            while True:
                for tel in tel_liste:
                    sms = SendSms(tel, mail)
                    for fonk in servisler_sms:
                        getattr(sms, fonk)()
                        sleep(aralik)
        else:
            for tel in tel_liste:
                sms = SendSms(tel, mail)
                while sms.adet < kere:
                    for fonk in servisler_sms:
                        if sms.adet >= kere:
                            break
                        getattr(sms, fonk)()
                        sleep(aralik)
        print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
        input()

    elif menu == 2:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız: "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.")
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.")
            sleep(3)
            continue
        system("cls||clear")
        send_sms = SendSms(tel_no, mail)
        dur = threading.Event()
        def Turbo():
            while not dur.is_set():
                thread = []
                for fonk in servisler_sms:
                    t = threading.Thread(target=getattr(send_sms, fonk), daemon=True)
                    thread.append(t)
                    t.start()
                for t in thread:
                    t.join()
        try:
            Turbo()
        except KeyboardInterrupt:
            dur.set()
            system("cls||clear")
            print("\nCtrl+C tuş kombinasyonu algılandı. Menüye dönülüyor..")
            sleep(2)

    elif menu == 3:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        break
