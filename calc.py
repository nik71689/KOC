print ("загрузка приложения...")
print ("*" * 20, "калькулятор версия 1. введите число и оператора.", "*" * 20)     # заголовок программы
while True:   # цикл
    num1 = input ("введите первое число>>>") 
    operator = input ("введите оператора>>>")
    num2 = input ("введите второе число>>>")
    if operator == "+":
       num1 = int (num2) 
       num2 = int (num2) 
       summa =  num1 + num2
       print (summa)
    elif operator == "-":
      num1 = int (num1)
      num2 = int (num2)
      raznost = num1 - num2 
      print (raznost)
    elif operator == "выход":
       break;  # прерывание цикла пользовальтелем
    elif operator == "*":
       num1 = int (num1)
       num2 = int (num2)
       proizvidenie = num1 * num2 
       print (proizvidenie)
    elif operator == "/":
       num1 = int (num1)
       num2 = int (num2)
       chastnoe = num1 / num2 or num1 // num2 
       print (chastnoe)
    elif operator == "=?":
       num1 = int (num1)
       num2 = int (num2)
       redy = round (num1) and round (num2)
       print (redy)
    elif operator == "**":
       num1 = int (num1)
       num2 = int (num2)
       stepen = num1 ** num2 
       print (stepen)
    else:
       print ("оператор не найден. ") # действие если выбран отсутствующий оператор
