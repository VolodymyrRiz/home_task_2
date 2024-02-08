# Модуль Книга записів

from collections import UserDict
from datetime import date, datetime, timedelta
import os
import re
import sys
import json
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
console = Console()

class Field:
    
    def __init__(self, value):
        self.__value = None
        self.value = value
        
    @property    
    def __str__(self):
        return str(self.__value)
    
    @__str__.setter
    def __str__(self):
        return str(self.__value)
       
class Name(Field):
    # реалізація клас
    pass

class Phone(Field):
    # реалізація класу
    
    def __init__(self, value):
        
        self.phone = value
        self.validate(value)
        super().__init__(value)
            
         
    def validate(self, phone):
          
        while True:
            
            self.phone = phone            
            long_ = len(self.phone)
            symb = str(self.phone).isnumeric()
            
            if long_ == 10 and symb == True:
                
                return self.phone
            else:
                print("Введіть номер телефона без пробілів, символів, має бути 10 цифр, натисність Enter: ")
                phone = input()
                                            
                
class Birthday(Field):
#     # реалізація класу
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)   
    def __str__(self):
        self.birth = self.value
        return self.birth        
     
        
    def validate(self, txt_valid):   
        self.txt_valid = txt_valid         
        self.txt_valid = "Введіть день народження у такому форматі: спочатку РІК, потім місяць ММ, потім день ДД,\nнаприклад: 2000 12 31"
        return self.txt_valid
    
    
class Email(Field):
     # реалізація класу
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)   
    def __str__(self):
        self.email = self.value
        return self.email        
     
        
    def validate(self, email):    
        while True:
            
            self.email = email
            name_split = self.email.split('@')
            for n_sp in name_split:
                pass
            len_mail = len(self.email)            
            rah_1 = self.email.count('@')
            rah_2 = self.email.count(' ')
            rah_3 = n_sp.count('.')
            rah_4 = self.email.count(',')
            
            if len_mail > 4 and rah_2 == 0 and rah_1 == 1 and rah_3 > 0 and rah_4 == 0:
                return self.email
            else:
                print("Введіть електронну адресу латинськими літерами у такому форматі: name@name.name, натисність Enter: ")
                email = input()


class Adress(Field):
     # реалізація класу
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)   
    def __str__(self):
        self.adress = self.value
        return self.adress        
     
      
class Record:  
       
    def __init__(self, name):
        self.name = Name(name)        
        self.phones = []
        self.emails = []
        self.adress = ' '
                
    # реалізація класу
        
    def add_phone(self, phone):                
        
        self.phone = phone                 
        Phone.validate(self, self.phone)
        
        self.phones.append(self.phone)  
            
        phones_ = self.phones        
        return phones_
    
    def days_to_birthday(self, birth_yer, birth_mont, birth_day):
        txt_valid = ' '
        day_now = date.today() 
        rik = day_now.year
        self.birth_yer = birth_yer        
        self.birth_mont = birth_mont        
        self.birth_day = birth_day
        print('')
        console.print('У В А Г А !!!', style='bold red')
        print('')
        
        try:
            birth = date(rik, self.birth_mont, self.birth_day)        
            dniv = int((birth - day_now).days)
            if dniv == 0:
                console.print(f'Сьогодні день народження у [yellow]{Name_}[/yellow]', style='bold blue')
            if dniv < 0:    
                console.print(f'У цьому році день народження у {Name_} вже минув', style='reverse red')     
            if dniv > 0:
                console.print(f'До дня народження [red]{Name_}[/red] залишилося днів - {dniv}', style='bold green')   
            birth = date(self.birth_yer, self.birth_mont, self.birth_day)
        except ValueError:
            Birthday.validate(self, txt_valid)
            print(self.txt_valid)
            birth = []          
        return birth                 
    
    
    def add_email(self, email):                
        
        self.email = email                 
        Email.validate(self, self.email)
       
        self.emails.append(self.email)      
       
        emails_ = self.emails        
        return emails_
    
    def add_adress(self, adress):                
        
        self.adress = adress                 
        
        adress_ = self.adress        
        return adress_ 
        
    def remove_phone(self, phone):
        try:
            self.phone = phone        
            self.phones.remove(self.phone)        
            phones_ = self.phones  
            return phones_
        except ValueError:
            dd = f"Телефон {self.phone} відсутній"     
            print(dd)
                    
    
    def edit_phone(self, a, b):
        index_ = self.phones.index(a)
        self.phones[index_] = b        
        pass    
          
    def __str__(self):       
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    
    def __init__(self, data, phones):
        self.data = data        
        self.phones = phones
        file_name = 'data.json'
        with open(file_name, "r") as fh:        
            unpacked = json.load(fh)    
            self.data = unpacked               
             
    def add_record(self, *argv, **kwarg):           
                    
        self.data.update({Name_: phones_, Name_+'_день народження': str(birth_), Name_+'_Email': emails_, Name_+'_Адреса': adress_}) 
        
        file_name = 'data.json'        
        with open(file_name, "w") as fh:
            json.dump(self.data, fh)  
        
        if flag_new == 1:
            return
                
            
    def find(self, name):
        if name in self.data:
            return name       
        
    def find_phone(self, ph_):
        
        for dict_ in self.data.items():            
            count_ = str(dict_).count(str(ph_))            
            if count_ > 0:                
                return ph_
            if count_ == 0:
                print('Телефон не знайдено')
                return
            else:
                continue
                 
    
    def delete(self, rec):        
        try:
            self.data.pop(rec)
            self.data.pop(rec+'_день народження')
            self.data.pop(rec+'_Email')
            self.data.pop(rec+'_Адреса')
        except KeyError:
            print("Немає такого імені")
            return
        
        a_ = f'[red]DELETED RECORD[/red] {rec}'
        console.print(a_)
        
        file_name = 'data.json'        
        with open(file_name, "w") as fh:
            json.dump(self.data, fh)          
                
    def iterator(self, item_number):
        self.item_number = item_number               
        counter_ = 0
        counterr_ = 0
        resultt = ''
        len_data = len(self.data)
        
        for item_, recordd in self.data.items():            
            resultt += f'{item_}: {recordd} \n'   
            counter_ += 1
            counterr_ += 1
            if  counterr_ == len_data:
                console.print(resultt)
                return
            if counter_ == self.item_number:                
                console.print(resultt)         
                counter_ = 0
                resultt = ''
                print('Продовжити перегляд? Натисніть ENTER')
                inp = input()
        
# О С Н О В Н И Й  Б Л О К  К О Д У    
       
data = {}
phones = []
phones_ = []
phone = ''
birth = []
email = ''
emails = []
emails_ = []
adress_ = ' '
adress = ' '
name_new = ''
flag_new = 0


# Запуск коду. Привітання, знаходиться у файлі README.md, який має бути у папці коду
lich = 0
while lich < 20:
    lich += 1
    print('')
with open("README.md", encoding="utf-8") as readme:
    markdown = Markdown(readme.read())
console.print(markdown, style='bold red')
lich = 0
while lich < 10:
    lich += 1
    print('')

book = AddressBook(data, phones)
kilkist = len(book.data)

   # Виведення всіх записів з книги за пошуковим словом або всіх записів через Enter
print('Перегляд усіх записів за пошуковим словом')
  
#nme = ''
o = 1
lich__ = 0
# while True:
#     nme = input()
#     if nme == '':        
#         if o == 2:
#             break
#         print('Введіть пошукове слово та натисніть Enter або просто натисніть ENTER для виходу')
#         o = o + 1
#         continue
#     for name, record in book.data.items():
            
#         if nme in name or nme in record:
#             lich__ += 1
#             console.print('ЗНАЙДЕНО ЗАПИС: ', style='bold yellow')
#             print(name, record)
#         if lich__ == 0:
#             console.print('ЗАПИС НЕ ЗНАЙДЕНО! ', style='bold red')   
#     break
            
            
try:
    nme = input()
    for name, record in book.data.items():
            
        if nme in name or nme in record:
            lich__ += 1
            console.print('ЗНАЙДЕНО ЗАПИС: ', style='bold yellow')
            print(name, record)
        if lich__ == 0:
            console.print('ЗАПИС НЕ ЗНАЙДЕНО! ', style='bold red')   
except EOFError as e: 
    pass
        #if nme == '':
        #   print("ПОШУКОВЕ СЛОВО НЕ ЗАДАНО!")

# ПЕРЕГЛЯД УСІХ ДНІВ НАРОДЖЕННЯ з вказівкою на кількість днів до святкування

print('')
console.print('У В А Г А !!!', style='bold red')

day_now = date.today()
rik = day_now.year
db = "_день народження"

file_name = 'data.json'
with open(file_name, "r") as fh:        
    unpacked = json.load(fh)    

for key_birth, val_birth in unpacked.items():
   
    if db in key_birth:
        ind = key_birth.index(db)
        name_birth = key_birth[0:ind]
        misiac = int(val_birth[5:7])
        den = int(val_birth[8:10])
        
        data_birth_1 = date(rik, misiac, den)        
        dniv = int((data_birth_1 - day_now).days)
        if dniv == 0:
            console.print(f'Сьогодні день народження у [yellow]{name_birth}[/yellow]', style='bold blue')
        if dniv < 0:    
            console.print(f'У цьому році день народження у {name_birth} вже минув', style='reverse red')     
        if dniv > 0:
            console.print(f'До дня народження [red]{name_birth}[/red] залишилося днів - {dniv}', style='bold green')
     
# РОБОТА з КНИГОЮ КОНТАКТІВ
inp = ''
nme = ''
while True:
    
    flag_new = 1
    print(' ')
    print('Заповнити книгу контактів? - Enter\nВивести повний запис за іменем? - f + Enter\nПереглянути книгу? - r + Enter\nВидалити запис? - d + Enter\nВийти? - q + Enter')
          #\nРедагувати запис? - ed + Enter')
    try:
        inp = input()
        if inp == 'q':        
            os.abort()
    except EOFError as e:
        pass
 
 # ВІДКРИТТЯ ПОВНОГО ЗАПИСУ ЗА ІМЕНЕМ       
    if inp == 'f':
        telef = ''
        maill = ''
        dat_birth = ''
        adr = ''
        print("Введіть ім'я для виведення повного запису: ")
        nme = input()
        lich = 0   
        lich_ = 0
        
        if nme == '':
            console.print('Такого імені нема!', style='bold red')
            continue
        for name, record  in book.data.items():  
            count_nme = name.count(nme) 
            lich_ += 1
                         
            if count_nme != 1 and lich_ != kilkist:
                continue
            if count_nme != 1 and lich_ == kilkist:
                console.print('Такого імені нема!', style='bold red')                
                break
                                            
            if lich == 0:        
                for teleff in record:
                    telef += f"{teleff}\n"                        
                    lich += 1           
                continue
            if lich == 1:
                dat_birth = record
                lich += 1  
                continue 
            if 'Email' in name:
                for mailll in record:
                    maill += f"{mailll}\n"                 
                continue
            if 'Адреса' in name:
                adr = record
                break
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Ім'я", style="dim", width=12)
        table.add_column("Телефон", width=23)
        table.add_column("День народження", justify="right")
        table.add_column("Email", justify="left", width=23)
        table.add_column("Адреса", justify="left", width=23)
        table.add_row(nme, telef, dat_birth, maill, adr)
                
        console.print('ЗНАЙДЕНО ЗАПИС: ', style='bold yellow')
        console.print(table)               
        continue        
        
    if inp == 'r':
            
    # ПОСТОРІНКОВИЙ ПЕРЕГЛЯД КНИГИ КОНТАКТІВ
        book.iterator(10)  
        continue   
    
    # ВИДАЛЕННЯ ЗАПИСУ
    if inp == 'd':
        print("Введіть ім'я для видалення запису")
        imia = input()
        book.delete(imia)
        continue
    
    # РЕДАГУВАННЯ ЗАПИСУ
    
    # if inp == 'ed':
    #     console.print('ЯК БУДЕМО РЕДАГУВАТИ? ', style='bold yellow')   
    #     console.print("[blue]1.[/blue] Видалити телефон? - натисни номер та Enter\n[green]2.[/green] Додати телефон? - натисни номер та Enter\n[yellow]3.[/yellow] Видалити email? - натисни номер та Enter\n[red]4.[/red] Додати email? - натисни номер та Enter\n[blue]5.[/blue] Редагувати адресу? - натисни номер та Enter\n[green]6.[/green] Змінити день народження? - натисни номер та Enter\n[reverse]7.[/reverse] Вийти з режиму редагування? - натисни номер та Enter")
    #     inp = input()     
        
    #     if inp == '1':
            
    #         print("Введіть телефон, який треба видалити: ")
    #         phone = input()            
    #         phonee = Phone(phone)
            
    #         #print(phone)
    #         #Phone.validate(phone)
                       
    #         console.print('Телефон [blue]видалено[/blue]')
    #         file_name = 'data.json'   
            
    #         with open(file_name, "w") as fh:
    #             json.dump(data, fh) 
    #         continue
        
    #     if inp == '2':
    #         continue
    #     if inp == '3':
    #         continue
    #     if inp == '4':
    #         continue
    #     if inp == '5':
    #         continue
    #     if inp == '6':
    #         continue
    #     if inp == '7':
    #         continue
        
# Основний блок заповнення Книги контактів
    new_name = ''
    new_phone = ''
    birth_yer = 0
    birth_mont = 0
    birth_day = 0
    new_email = ''
    new_adress = ' '
    
    
        
    print("Введіть ім'я та натисність Enter: ")
    try:
        new_name = input()
        if new_name == '':
            print("Ви забули ввести ім'я?")
            new_name = input()
        if new_name == '':
            print("Не хочете вводити - натисніть Enter")
            new_name = input()
            if new_name == '':
                os.abort()
    except EOFError as e:
        pass
    
    new_record = Record(new_name)
    Name_ = new_record.name.value
        
    print("Введіть номер телефона без пробілів, символів, має бути 10 цифр, натисність Enter: ")
    try:
        new_phone = input()
        phones_ = new_record.add_phone(new_phone)
    except EOFError as e:
        pass
    print("Введіть дату народження.")
    int_ = 0
    while int_ != 1000:        
        int_ += 1
        print("Рік? (чотири цифри + Enter): ")
        try:
            try:
                birth_yer = int(input())
            except EOFError as e:
                pass
        except ValueError:
            continue
        break
   
    int_ = 0
    while int_ != 1000:        
        int_ += 1
        print("Місяць? (дві цифри + Enter): ")
        try:
            try:
                birth_mont = int(input())
            except EOFError as e:
                pass
        except ValueError:
            continue
        break
    
    int_ = 0
    while int_ != 1000:        
        int_ += 1
        print("День? (дві цифри + Enter): ")
        try:            
            try:
                birth_day = int(input())
            except EOFError as e:
                pass
        except ValueError:
            continue
        break 
    
    birth_ = new_record.days_to_birthday(birth_yer, birth_mont, birth_day)
    
    print("Введіть електронну адресу латинськими літерами у такому форматі: name@name.name, натисність Enter: ")
    try:
        new_email = input()      
        emails_ = new_record.add_email(new_email)    
    except EOFError as e:
        pass
    print("Введіть адресу в довільному форматі та натисність Enter: ")
    try:
        new_adress = input()
        adress_ = new_record.add_adress(new_adress) 
    except EOFError as e: 
        adress_ = new_record.add_adress(new_adress) 
    
    book.add_record(new_record)