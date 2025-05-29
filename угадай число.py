print ("запуск игры...")
import random 
print (  "********** игра угадай число**********")
print ("компьютер выберет случайное число в диапозоне от 1 до 10.Попробуй угадать это число. Для выхода нажмите 0")
answer = 1
score = 0
i = 0
while answer:
        rand = random.randint(1, 10)
        answer = int(input("введите число:"))
        if answer == 0:
            break 
        if answer == rand:
            score = score + 1
            print ("правильно!")
        else:
            print ("попробуйте ещё раз!")
        i = i + 1
        
        print("ваш счёт", score, "из", i)
if (answer == 0):
    import subprocess
    subprocess.run(["/home/nik/Рабочий стол/Школьник для Linux/КОС/sys 8/system/KOC.out"])
