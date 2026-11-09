from random import random
from time import sleep
RAZMER=10
RADIUS=1
VYZHIVAET=[2, 3]
ROZHDAETSYA=[3]
SDVIGI=[(ds, db) for ds in range(-RADIUS, RADIUS+1)
                 for db in range(-RADIUS, RADIUS+1) if (ds, db)!=(0, 0)]
if 2*RADIUS+1>RAZMER:
    print("RADIUS слишком большой для такого поля")
    exit()
ZHIVAYA="■"
PUSTAYA="·"
OCHISTIT_EKRAN="\033[2J\033[H"
SPRAVKA="""q-выйти
?-справка
c строка столбец-изменить клетку (числа от 1 до 10)
r доля-заполнить поле случайно (число от 0 до 1)
n-один шаг игры
a [пауза]-анимация (пауза в секундах, по умолчанию 0.3; Ctrl+C-остановить)"""
def pokazat_pole(pole):
    print(*("".join(s) for s in pole), sep="\n")
def sluchaynoe_zapolnenie(pole, dolya):
    for stroka in range(RAZMER):
        for stolbec in range(RAZMER):
            pole[stroka][stolbec]=ZHIVAYA if random()<dolya else PUSTAYA
def chislo_sosedey(pole, stroka, stolbec):
    return sum(pole[(stroka+ds)%RAZMER][(stolbec+db)%RAZMER]==ZHIVAYA
               for ds, db in SDVIGI)
def shag_igry(pole):
    novoe_pole=[s[:] for s in pole]
    for stroka in range(RAZMER):
        for stolbec in range(RAZMER):
            sosedi=chislo_sosedey(pole, stroka, stolbec)
            if pole[stroka][stolbec]==ZHIVAYA and sosedi not in VYZHIVAET:
                novoe_pole[stroka][stolbec]=PUSTAYA
            elif pole[stroka][stolbec]==PUSTAYA and sosedi in ROZHDAETSYA:
                novoe_pole[stroka][stolbec]=ZHIVAYA
    return novoe_pole
def animaciya(pole, pauza):
    try:
        while True:
            print(OCHISTIT_EKRAN, end="")
            pokazat_pole(pole)
            novoe_pole=shag_igry(pole)
            if novoe_pole==pole:
                print("Игра окончена")
                break
            pole=novoe_pole
            sleep(pauza)
    except KeyboardInterrupt:
        print("\nАнимация остановлена")
    return pole
def main():
    pole=[[PUSTAYA]*RAZMER for _ in range(RAZMER)]
    while True:
        pokazat_pole(pole)
        komanda=input(">> ").split()
        if not komanda:
            continue
        try:
            match komanda[0]:
                case "q":
                    break
                case "?":
                    print(SPRAVKA)
                case "c":
                    stroka, stolbec=int(komanda[1])-1, int(komanda[2])-1
                    if 0<=stroka<RAZMER and 0<=stolbec<RAZMER:
                        pole[stroka][stolbec]=PUSTAYA if pole[stroka][stolbec]==ZHIVAYA else ZHIVAYA
                    else:
                        print("Нужно от 1 до 10")
                case "r":
                    dolya=float(komanda[1])
                    if 0<=dolya<=1:
                        sluchaynoe_zapolnenie(pole, dolya)
                    else:
                        print("Нужно от 0 до 1")
                case "n":
                    novoe_pole=shag_igry(pole)
                    if novoe_pole==pole:
                        print("Игра окончена")
                    else:
                        pole=novoe_pole
                case "a":
                    pauza=float(komanda[1]) if len(komanda)>1 else 0.3
                    if pauza>=0:
                        pole=animaciya(pole, pauza)
                    else:
                        print("Пауза не может быть меньше 0")
        except (ValueError, IndexError):
            print("Ошибка ввода")
main()
