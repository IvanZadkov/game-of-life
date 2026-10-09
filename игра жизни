from random import random
RAZMER=10
SPRAVKA="Команды: q-выйти, ?-справка, c (строка столбец)-изменить клетку, r доля-случайно заполнить поле, n-один шаг игры"
def pokazat_pole(pole):
    print("\n".join("".join("■" if k else "·" for k in s) for s in pole))
def sluchaynoe_zapolnenie(pole, dolya):
    for stroka in range(RAZMER):
        for stolbec in range(RAZMER):
            pole[stroka][stolbec]=1 if random()<dolya else 0
def chislo_sosedey(pole, stroka, stolbec):
    summa=0
    for ds in (-1, 0, 1):
        for db in (-1, 0, 1):
            if ds!=0 or db!=0:
                summa+=pole[(stroka+ds)%RAZMER][(stolbec+db)%RAZMER]
    return summa
def shag_igry(pole):
    novoe_pole=[[0]*RAZMER for _ in range(RAZMER)]
    for stroka in range(RAZMER):
        for stolbec in range(RAZMER):
            sosedi=chislo_sosedey(pole, stroka, stolbec)
            if sosedi==3:
                novoe_pole[stroka][stolbec]=1
            elif sosedi==2:
                novoe_pole[stroka][stolbec]=pole[stroka][stolbec]
    return novoe_pole
def main():
    pole=[[0]*RAZMER for _ in range(RAZMER)]
    while True:
        pokazat_pole(pole)
        komanda=input(">> ").split()
        match komanda[0]:
            case "q":
                break
            case "?":
                print(SPRAVKA)
            case "c":
                stroka, stolbec=int(komanda[1])%RAZMER, int(komanda[2])%RAZMER
                pole[stroka][stolbec]=1-pole[stroka][stolbec]
            case "r":
                sluchaynoe_zapolnenie(pole, float(komanda[1]))
            case "n":
                novoe_pole=shag_igry(pole)
                if novoe_pole==pole:
                    print("Игра окончена")
                pole=novoe_pole
main()
