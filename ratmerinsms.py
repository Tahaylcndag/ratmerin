# ratmerin.py
# by RATMERİN — Codza & Reborn altyapısı üzerine kurulmuştur

from colorama import Fore, Style, init
from time import sleep
from os import system
from sms import SendSms
import threading

init(autoreset=True)

# RATMERİN ASCII Başlık
print(Fore.LIGHTCYAN_EX + """
██████╗  █████╗ ████████╗███╗   ███╗███████╗██████╗ ██╗███╗   ██╗
██╔══██╗██╔══██╗╚══██╔══╝████╗ ████║██╔════╝██╔══██╗██║████╗  ██║
██████╔╝███████║   ██║   ██╔████╔██║█████╗  ██████╔╝██║██╔██╗ ██║
██╔══██╗██╔══██║   ██║   ██║╚██╔╝██║██╔══╝  ██╔══██╗██║██║╚██╗██║
██║  ██║██║  ██║   ██║   ██║ ╚═╝ ██║███████╗██║  ██║██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
""" + Style.RESET_ALL)
sleep(3)
# Servisleri yükle
servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value) and not attribute.startswith('__'):
        servisler_sms.append(attribute)

# Ana Menü Döngüsü
while True:
    system("cls||clear")
    print(f"{Fore.LIGHTMAGENTA_EX}\nSMS Servisi: {len(servisler_sms)} aktif servis\n")
    print(Fore.LIGHTYELLOW_EX + " 1- SMS Gönder (Normal)")
    print(" 2- SMS Gönder (Turbo)")
    print(" 3- Çıkış\n")
    secim = input(Fore.CYAN + " Seçim: ").strip()

    if secim == "1":
        system("cls||clear")
        tel_no = input(Fore.LIGHTGREEN_EX + "Telefon numarası (başında +90 olmadan): ").strip()

        if len(tel_no) != 10 or not tel_no.isdigit():
            print(Fore.LIGHTRED_EX + "Hatalı numara girdiniz.")
            sleep(2)
            continue

        mail = input(Fore.LIGHTGREEN_EX + "Mail adresi (zorunlu değil): ").strip()

        try:
            kere = input(Fore.LIGHTGREEN_EX + "Kaç adet SMS? (sonsuz için boş bırak): ")
            kere = int(kere) if kere else None
        except ValueError:
            print(Fore.LIGHTRED_EX + "Hatalı sayı girdiniz.")
            sleep(2)
            continue

        try:
            aralik = int(input(Fore.LIGHTGREEN_EX + "Kaç saniye aralıkla?: "))
        except ValueError:
            print(Fore.LIGHTRED_EX + "Hatalı sayı girdiniz.")
            sleep(2)
            continue

        system("cls||clear")
        sms = SendSms(tel_no, mail)

        if kere is None:
            while True:
                for servis in servisler_sms:
                    getattr(sms, servis)()
                    sleep(aralik)
        else:
            while sms.adet < kere:
                for servis in servisler_sms:
                    if sms.adet >= kere:
                        break
                    getattr(sms, servis)()
                    sleep(aralik)
        input(Fore.LIGHTMAGENTA_EX + "\nBitti. Menüye dönmek için ENTER.")

    elif secim == "2":
        system("cls||clear")
        tel_no = input(Fore.LIGHTGREEN_EX + "Telefon numarası (başında +90 olmadan): ").strip()

        if len(tel_no) != 10 or not tel_no.isdigit():
            print(Fore.LIGHTRED_EX + "Hatalı numara girdiniz.")
            sleep(2)
            continue

        mail = input(Fore.LIGHTGREEN_EX + "Mail adresi (zorunlu değil): ").strip()

        send_sms = SendSms(tel_no, mail)
        durdur = threading.Event()

        def turbo_mode():
            while not durdur.is_set():
                threadler = []
                for servis in servisler_sms:
                    t = threading.Thread(target=getattr(send_sms, servis), daemon=True)
                    t.start()
                    threadler.append(t)
                for t in threadler:
                    t.join()

        try:
            turbo_mode()
        except KeyboardInterrupt:
            durdur.set()
            print(Fore.LIGHTRED_EX + "\nDurduruldu. Menüye dönülüyor...")
            sleep(2)

    elif secim == "3":
        print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        break

    else:
        print(Fore.LIGHTRED_EX + "Geçersiz seçim.")
        sleep(1.5)
