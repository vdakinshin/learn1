name = input('Как тебя зовут?: ')
age = input('В каком году Вы родились?: ')
message = "Привет, {}! Ты родился в {}-м году на краю города!" .format(name,age) 
print(message)