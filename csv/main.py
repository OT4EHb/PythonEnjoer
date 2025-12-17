import csv
from datetime import *


def to_en(date_str):
    month = {
        'январь': 'January',
        'февраль': 'February',
        'март': 'March',
        'апрель': 'April',
        'май': 'May',
        'июнь': 'June',
        'июль': 'July',
        'август': 'August',
        'сентябрь': 'September',
        'октябрь': 'October',
        'ноябрь': 'November',
        'декабрь': 'December'
    }
    str = date_str.lower()
    for ru, en in month.items():
        if ru in str:
            return str.replace(ru, en)
    raise ValueError(f"{date_str} Не дата")


date = input("Введите дату (dd mm yyyy)\n") + " 00:00"
date = datetime.strptime(date, "%d %m %Y  %H:%M")
fname = input("Введите название файла:\n")
with open(fname) as f:
# with open("8 - 1.csv") as f:
    csv_read = csv.reader(f)
    data = [i for i in csv_read]
    headers = data[0]
    need = float(headers[9].split('/')[1].replace(',', '.')) * 0.6
    data = data[1:-2]
    nouspex = set()
    uspex=set()
    count = 0
    for i in data:
        if i[7] == "-":
            continue
        if float(i[9].replace(',','.')) >= need:
            uspex.add(i[0]+" "+i[1])
            continue
        nouspex.add(i[0]+" "+i[1])
        if (datetime.strptime(
                to_en(i[7]),
                "%d %B %Y  %H:%M"
        ) > date):
            count+=1
    print("Тест на сдали:")
    for i in nouspex.difference(uspex):
        print(i)
    print("Всего неудачных попыток позже заданной даты:",count)
