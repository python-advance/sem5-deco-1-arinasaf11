# Инвариантная самостоятельная работа

2.1 Разработать прототип программы «Калькулятор», позволяющую выполнять базовые арифметические действия и функцию обертку, сохраняющую название выполняемой операции, аргументы и результат в файл.

Программа «Калькулятор» - это программа, позволяющая осуществлять конвертацию курса валюты, на основе информации ЦБР. Основа программы - функция (класс), принимающая число (в том числе число с плавающей точкой) и условное обозначение валюты, из которой идет преобразование и валюты, в которую преобразовывается.

2.2 Дополнение программы «Калькулятор» декоратором, сохраняющий действия, которые выполняются в файл-журнал.

2.3 Рефакторинг (модификация) программы с декоратором модулем functools.

```python
import urllib.request #открытие и чтение URL
from xml.etree import ElementTree as ET # ET чтобы оборачивать структуру элементов из XML и в XML

def logger(function):
    import functools
    @functools.wraps(function) #functools.wraps - функция, реализующая логику копирования внутренних атрибутов оборачиваемой функции.
    def wrapper(summa):
        result = function(summa)
        with open('Record.txt', 'a') as f:
            f.write("Переводим " + str(summa) + " " + str(convert_from) + " в " + str(convert_to) + "\n")
            f.write("Результат: " + str(result) + " " + str(convert_to) +"\n")
        return result
    return wrapper

summa = float(input("Введите сумму: "))
convert_from = input("Введите валюту, из которой переводим (rubl, dollar, euro, iena): ")
convert_to = input("Введите валюту, в которую переводим (rubl, dollar, euro, iena): ")

id_dollar = "R01235" #USD
id_euro = "R01239" #EUR
id_iena = "R01820" #GBP

valuta = ET.parse(urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp")) #открываем url

@logger
def convert(summa):
  for line in valuta.findall('Valute'): #findall - возвращает список всех найденных совпадений
    id_v = line.get('ID')
    if id_v == id_dollar:
        rub1 = line.find('Value').text
    elif id_v == id_euro:
        rub2 = line.find('Value').text
    elif id_v == id_iena:
        rub3 = line.find('Value').text
       
  rub1 = float(rub1.replace(',', '.')) #меняем запятые на точки
  rub2 = float(rub2.replace(',', '.'))
  rub3 = float(rub3.replace(',', '.'))


  if convert_from == "rubl":
    if convert_to == "rubl":
      result = float(summa)
    elif convert_to == "dollar":
      result = float(summa) / rub1
    elif convert_to == "euro":
      result = float(summa) / rub2
    elif convert_to == "iena":
      result = float(summa) / rub3
   
  elif convert_from == "dollar":  
    if convert_to == "rubl":
      result = float(summa) * rub1
    elif convert_to == "dollar":
      result = float(summa)
    elif convert_to == "euro":
      result = (float(summa) * rub1) / rub2
    elif convert_to == "iena":
      result = (float(summa) * rub1) / rub3

  elif convert_from == "euro":  
    if convert_to == "rubl":
      result = float (summa) * rub2
    elif convert_to == "dollar":
      result = (float (summa) * rub2) / rub1
    elif convert_to == "euro":
      result = float (summa)
    elif convert_to == "iena":
      result = (float (summa) * rub2) / rub3

  elif convert_from == "iena":  
    if convert_to == "rubl":
      result = float (summa) * rub3
    elif convert_to == "dollar":
      result = (float (summa) * rub3) / rub1
    elif convert_to == "euro":
      result = (float (summa) * rub3) / rub2
    elif convert_to == "iena":
      result = float (summa)     
  return result

result = convert(summa)

print (summa, convert_from, " = ", result, convert_to)
```
Результат:

![рез](https://github.com/python-advance/sem5-deco-1-arinasaf11/blob/master/ISR/cur_calc.jpg?raw=true)

Запись в файл:

![](https://github.com/python-advance/sem5-deco-1-arinasaf11/blob/master/ISR/record.jpg?raw=true)

# Вариативная самостоятельная работа

2.3 Разработка функции-декоратора, вычисляющей время выполнения декорируемой функции.

```python
def time_decorator(func):
    """
    Декоратор, выводящий время, которое заняло
    выполнение декорируемой функции.
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.time() #время перед выполнением декорируемой ф-и
        res = func(*args, **kwargs)
        print("Время выполнения: ", time.time() - t)       
        return res
    return wrapper

@time_decorator
def plus(x, y):
    print("%d + %d = %d" % (x, y, x + y))
    return x + y

plus(2, 3)
```

Результат:

![результат](https://github.com/python-advance/sem5-deco-1-arinasaf11/blob/master/VSR/time_deco.jpg?raw=true)
