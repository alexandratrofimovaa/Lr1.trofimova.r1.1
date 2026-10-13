RED = '\u001b[41m'
BLUE = '\u001b[46m'
WHITE = '\u001b[47m'
RESET = '\u001b[0m'

def flag():   #функция изображения флага
    heigh = 10 #длина изображения
    for i in range(heigh):
        if i < heigh//2: #изображение верхней половины флага
            print(f"{WHITE}{'    ' * heigh} {RESET}")
        else:  #изображение нижней половины флага
            print(f"{RED}{'    ' * heigh} {RESET}")


import time
def draw(): #функция создания повторяющегося узора
    heigh = 5 #высота узора
    width = 11 #длина узора
    colors = [63,46,162,25] #индексы цветов
    while True: #цикл для создания повторения
        for color in colors: #цикл для перебора цветов
            for i in range (heigh+1): #цикл для построения узора
                if i%2!=0: #заполнение нечётных строк
                    print(f"\u001b[48;5;{color}m{'  ' * width}{RESET}")
                if i==2: #заполнение второй строки
                    print(f"{RESET}{'  ' * int(width/2)}\u001b[48;5;{color}m{'  ' * int(width*0.1)}{RESET}")
                if i==4: #заполнение четвёртой строки
                    print(f"{RESET}{'  ' * int(width/4)}\u001b[48;5;{color}m{'  ' * int(width * 0.1)}{RESET}{'  ' * int(width/2)}\u001b[48;5;{color}m{'  ' * int(width * 0.1)}{RESET}")

            print(f"\u001b[{heigh + 2}A") #возвращаем курсор на исходную позицию
            print(f"\u001b[{width + 1}D")
            time.sleep(0.8) #создание временной задержки в смене цветов


import os
def animate(): #функция анимации
    lenght = 5 #длина последовательности
    for i in range (lenght + 1):
        kadri = ['*' * i + ' ' * (lenght - i)] #список всех кадров
        for kadr in kadri: #перебор кадров
            os.system('cls' if os.name == 'nt' else 'clear') #очистка консоли
            print(f'\x1B[1;10H[{kadr}]') #перемещение курсора в 10 строку
            time.sleep(0.15)


def sequence(): #функция диаграммы процентного соотношения
    file = open('sequence.txt', 'r')
    partp = []
    partv = []
    c = 0
    for line in file: #цикл для распределения чисел в файле по двум спискам
        c+=1 #номер числа в последовательности
        if c<=125:
            partp.append(abs(float(line))) #первые 125 чисел по модулю в последовательности
        else:
            partv.append(abs(float(line))) #вторые 125 чисел по модулю в последовательности
    sredp = int(sum(partp)/125) #среднее из первого списка
    sredv = int(sum(partv)/125) #среднее из второго списка

    file.close()

    print(f'{BLUE}{' ' * sredp}{RESET} {sredp/(sredp + sredv) * 100}%') #отношение среднего числа по модулю из первого списка ко второму в процентах
    print(f'{RED}{' ' * sredv}{RESET} {sredv/(sredp + sredv) * 100}%')  #отношение среднего числа по модулю из второго списка к первому в процентах


print(flag())
print(draw())
print(animate())
print(sequence())

