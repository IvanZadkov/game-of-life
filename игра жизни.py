from random import random
RAZMER=10
ZHIVAYA="■"
PUSTAYA="·"
SPRAVKA="""q-выйти
?-справка
c строка столбец-изменить клетку (числа от 1 до 10)
r доля-заполнить поле случайно (число от 0 до 1)
n-один шаг игры"""
def pokazat_pole(pole):
    print(*("".join(s) for s in pole), sep="\n")
def sluchaynoe_zapolnenie(pole, dolya):
    for stroka in range(RAZMER):
        for stolbec in range(RAZMER):
            pole[stroka][stolbec]=ZHIVAYA if random()<dolya else PUSTAYA
def chislo_sosedey(pole, stroka, stolbec):
    return sum(pole[(stroka+ds)%RAZMER][(stolbec+db)%RAZMER]==ZHIVAYA
               for ds in (-1, 0, 1) for db in (-1, 0, 1) if (ds, db)!=(0, 0))
def shag_igry(pole):
    novoe_pole=[s[:] for s in pole]
    for stroka in range(RAZMER):
        for stolbec in range(RAZMER):
            sosedi=chislo_sosedey(pole, stroka, stolbec)
            if pole[stroka][stolbec]==ZHIVAYA and (sosedi<2 or sosedi>3):
                novoe_pole[stroka][stolbec]=PUSTAYA
            elif pole[stroka][stolbec]==PUSTAYA and sosedi==3:
                novoe_pole[stroka][stolbec]=ZHIVAYA
    return novoe_pole
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
        except (ValueError, IndexError):
            print("Ошибка ввода")
main()
