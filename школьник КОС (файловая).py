import os
input ("для загрузки нажмите Enter")
print ( "*" * 30, "Вы находитесь в загрузочном меню. Выберите действие" , "*" * 30)
boot = input ("Доступные действия загрузка/выход.>>>")
if (boot == "загрузка"):
    print("введите логин")
    login = input()
    print("введите пароль") # ввод пароля
    password = input ()
    if (login == "никита" and password =="123"):
        print ("загрузка системы, пожалуйста подождите...")
        print ("copyright © 2025 компания школьник все права защищены")
        try:
         while True:
          carp = "/home/nik/Рабочий стол/Школьник для Linux/файловая система/"
          addres =  carp + input (">>>")
          contents = os.listdir(addres)
          print (contents)
          if addres == "0":
             break;
          if addres == "h":
             file = open("/home/nik/Рабочий стол/Школьник для Linux/КОС/helps/help KOS", 'r') 
             content = file.read() 
             print(content) 
             file.close()
        except FileNotFoundError: 
           print ("нет такого файла или каталога.")