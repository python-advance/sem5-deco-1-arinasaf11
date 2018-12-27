import urllib.request #открытие и чтение URL
from xml.etree import ElementTree as ET # ET чтобы оборачивать структуру элементов из XML и в XML

def logger(function):
    import functools
    import datetime
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
      result = float (in_currency) * rub2
    elif convert_to == "dollar":
      result = (float (in_currency) * rub2) / rub1
    elif convert_to == "euro":
      result = float (in_currency)
    elif convert_to == "iena":
      result = (float (in_currency) * rub2) / rub3

  elif convert_from == "iena":  
    if convert_to == "rubl":
      result = float (in_currency) * rub3
    elif convert_to == "dollar":
      result = (float (in_currency) * rub3) / rub1
    elif convert_to == "euro":
      result = (float (in_currency) * rub3) / rub2
    elif convert_to == "iena":
      result = float (in_currency)     
  return result

result = convert(summa)

print (summa, convert_from, " = ", result, convert_to)
