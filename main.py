def show_menu():
    print("1. Распечатать справочник",
          "2. Найти телефон по фамили",
          "3. Изменить номер телефона",
          "4. Удалить запись",
          "5. Найти абонента в справочник",
          "6. Добавить абонента в справочник ",
          "7. Закончить работу", sep="\n")

def read_text(filename):

    phone_book = []
    fields = ["Фамилия","Имя","Телефон","Описание",]

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            record = dict(zip(fields, map(str.strip, line.split(","))))
            if record.get("Фамилия"):
                phone_book.append(record)
        
        phone_book = [user for user in phone_book if user.get('Фамилия')]
    return phone_book

def write_txt(filename, phone_book):

    with open(filename, "w", encoding="utf-8") as ff:
        for i in range(len(phone_book)):
            s = " "
            for v in phone_book[i].values():
                s += v + ","
            ff.write(f"{s[:-1]}\n")
        return ff    

def work_with_phonebook():


    show_menu()
    choice = int(input("Что вас интересует ? "))

    while choice != 7:
        if choice == 1:
            print(read_text("phonebook.csv"))
        elif choice == 2:
            last_name = input("Введите фамилию: ")
            print("Текущий номер телефона абонента: ", find_by_lastname(last_name))
            break
            
        elif choice == 3:
            last_name = input("Введите фамилию, которой хотите присвоить новый нмоер телефона: ")
            new_number = input("Введите новый номер телефона: ")
            change_number(last_name, new_number)
            print("Номер телефона был изменен! ")

        elif choice == 4:
            last_name = input("Введите фамилию: ")
            delet_by_lastname(last_name)
            print("Запись была удалина из файла!")

        elif choice == 5:
            number = input("Введите номер телефона абонента: ")
            print("Все данные пользователя из файла: ", find_by_number(number))
        elif choice == 6:
            user_data = {"Фамилия": None, "Имя": None, "Телефон": None, "Описание": None}
            for i in user_data:
                data = input("Введите данные абонента по очереди: фамилия, имя, телефон, описание")
                user_data[i] = data
            add_user(user_data)
            
        show_menu()
        choice = int(input("Что вас интересует ? "))




def find_by_lastname(last_name):
    try:
        phone_book = read_text("phonebook.csv")
        for i in phone_book:
            if i["Фамилия"] == last_name:
                number = i["Телефон"]
                break
        return number    
    except UnboundLocalError:            
        print("Фамилии не сущевствует!")

def change_number(last_name, new_number):
        phone_book = read_text("phonebook.csv")

        for i in phone_book:
            if i["Фамилия"] == last_name:
                i["Телефон"] = new_number
        write_txt("phonebook.csv", phone_book)
        
def delet_by_lastname(last_name):

    phone_book = read_text("phonebook.csv")

    for i in phone_book:
        if i.get("Фамилия") == last_name:
            phone_book.remove(i)
    
    file = write_txt("phonebook.csv", phone_book)
    return file

def find_by_number(number):

    phone_book = read_text("phonebook.csv")

    for i in phone_book:
        if i["Телефон"] == number:
            return i

def add_user(user_data):

    phone_book = (read_text("phonebook.csv"))
    print(phone_book)
    phone_book.append(user_data)
    
    write_txt("phonebook.csv", phone_book)
   

work_with_phonebook()


    
