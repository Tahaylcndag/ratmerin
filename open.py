import os
import time
from colorama import Fore, Style, init

init(autoreset=True)

# Ekranı temizle
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Renkler
dot_color = Fore.LIGHTYELLOW_EX
text_color = Fore.LIGHTCYAN_EX + Style.BRIGHT

# RATMERİN ASCII yazısı
ratmerin_ascii = f"""{text_color}
██████╗  █████╗ ████████╗███╗   ███╗███████╗██████╗ ██╗███╗   ██╗
██╔══██╗██╔══██╗╚══██╔══╝████╗ ████║██╔════╝██╔══██╗██║████╗  ██║
██████╔╝███████║   ██║   ██╔████╔██║█████╗  ██████╔╝██║██╔██╗ ██║
██╔═══╝ ██╔══██║   ██║   ██║╚██╔╝██║██╔══╝  ██╔══██╗██║██║╚██╗██║
██║     ██║  ██║   ██║   ██║ ╚═╝ ██║███████╗██║  ██║██║██║ ╚████║
╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
"""

# Nokta animasyonu
def animate_dots():
    height = 20
    left_margin = 2
    right_margin = 60

    for i in range(height):
        clear()
        print(ratmerin_ascii)
        for j in range(i):
            print()
        print(" " * left_margin + dot_color + "●" + " " * (right_margin - left_margin) + dot_color + "●")
        time.sleep(0.1)

    # Ortada buluşma efekti
    for _ in range(3):
        clear()
        print(ratmerin_ascii)
        for _ in range(height):
            print()
        print(" " * (right_margin // 2) + Fore.LIGHTGREEN_EX + "◆")
        time.sleep(0.3)

# Başlat
if __name__ == "__main__":
    animate_dots()
