import sqlite3
from tkinter import *
from tkinter.scrolledtext import ScrolledText
user_id = 0
def reg_w(): #окно при запуске
    zap_label.place_forget()
    reg_button.place_forget()
    enter_button.place_forget()
    reg_label.place(relx=0.3, rely=0.1)
    name_vvod_label.place(relx=0.1, rely=0.3)
    password_vvod_label.place(relx=0.1, rely=0.6)
    name_vvod.place(relx=0.5, rely=0.33)
    password_vvod.place(relx=0.5, rely=0.63)
    vvod_button.place(relx=0.3 , rely=0.8)
def ent_w(): #окно входа
    zap_label.place_forget()
    reg_button.place_forget()
    enter_button.place_forget()
    ent_label.place(relx=0.3, rely=0.1)
    name_vvod_label.place(relx=0.1, rely=0.3)
    password_vvod_label.place(relx=0.1, rely=0.6)
    name_vvod.place(relx=0.5, rely=0.33)
    password_vvod.place(relx=0.5, rely=0.63)
    ent_button.place(relx=0.3 , rely=0.8)
def reg() : #регистрация
    craft_user = f" INSERT INTO users (name , password) VALUES('{name_vvod.get()}','{password_vvod.get()}')"
    cursor.execute(craft_user)
    db.commit()
    print('Пользователь добавлен')
    reg_label.place_forget()
    name_vvod_label.place_forget()
    password_vvod_label.place_forget()
    name_vvod.place_forget()
    password_vvod.place_forget()
    vvod_button.place_forget()
    zap_label.place(relx=0.2, rely=0.1)
    reg_button.place(relx=0.2, rely=0.3)
    enter_button.place(relx=0.2, rely=0.6)
    name_vvod.delete(0, END)
    password_vvod.delete(0, END)
def ent() : #Вход
    enter_user = f"SELECT * FROM users WHERE name ='{name_vvod.get()}'AND password ='{password_vvod.get()}'"
    cursor.execute(enter_user)
    dates = cursor.fetchall()
    global user_id
    user_id = dates[0][0]
    print("Зашел пользователь с id : " + str(user_id))
    ent_label.place_forget()
    ent_button.place_forget()
    name_vvod_label.place_forget()
    name_vvod.place_forget()
    password_vvod_label.place_forget()
    password_vvod.place_forget()
    show_records_def()
    record_list_label.place(relx=0.3, rely=0.2)
    create_record.place(relx=0.05, rely=0.1)
    show_records.place(relx=0.05, rely=0.3)
    delete_rec_button.place(relx=0.5, rely=0.1)

def create_rec(): #окно создания записи
    record_list_label.place_forget()
    create_record.place_forget()
    show_records.place_forget()
    create_record_label.place(relx=0.1, rely=0.1)
    record_vvod.place(relx=0.1, rely=0.25, relheight=0.4, relwidth=0.8)
    create_record_vvod.place(relx=0.3, rely=0.7)

def create_rec_vvod(): #создание записи
    zapis = f" INSERT INTO records (user_id , letter) VALUES('{user_id}','{record_vvod.get()}')"
    cursor.execute(zapis)
    db.commit()
    record_vvod.delete(0, END)
    print('Запись добавлена')
    show_records_def()
    create_record_label.place_forget()
    record_vvod.place_forget()
    create_record_vvod.place_forget()
    create_record.place(relx=0.05, rely=0.1)
    show_records.place(relx=0.05, rely=0.3)
    record_list_label.place(relx=0.3, rely=0.2)

def show_records_def(): #вывод записей
    show_records.delete("1.0" , END)
    zap_user = "SELECT * FROM records WHERE user_id =" + str(user_id)
    cursor.execute(zap_user)
    dates = cursor.fetchall()
    for record in dates:
        show_records.insert("1.0" , f'Запись номер {record[0]}:\n{record[2]}\n')
def delete_rec_vvod():
    delete_rec_button.place_forget()
    delete_label.place(relx=0.5, rely=0.05)
    delete_entry.place(relx=0.5, rely=0.15)
    delete_button.place(relx=0.8, rely=0.15)
def delete_rec():
    zap_delete = "DELETE FROM records WHERE record_id =" + str(delete_entry.get())
    cursor.execute(zap_delete)
    db.commit()
    print('Запись удалена')
    delete_entry.delete(0,END)
    delete_label.place_forget()
    delete_entry.place_forget()
    delete_button.place_forget()
    delete_rec_button.place(relx=0.5, rely=0.1)
    show_records_def()






create_ut = "CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT , password TEXT)"
create_rt = "CREATE TABLE IF NOT EXISTS records(record_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id TEXT , letter TEXT )"
with sqlite3.connect('datebase.db') as db:
    cursor = db.cursor()
    cursor.execute(create_ut)
    cursor.execute(create_rt)

root = Tk()
root.title('Записная книжка')
root.geometry('600x500')
root.iconbitmap('C:\\Users\kamal\OneDrive\Рабочий стол\Kotocode\documentediting_editdocuments_text_documentedi_2820.ico')
zap_label = Label(root, text='Записная книжка', font= ("Comic Sans MS", 20), fg= 'blue')
reg_button = Button(root, text='Зарегестрироваться', command=reg_w, font= ("Comic Sans MS", 20), fg= 'red', bg= 'black', activebackground='white', activeforeground='blue')
enter_button = Button(root, text='Войти', command=ent_w, font= ("Comic Sans MS", 20), fg= 'red', bg= 'black', activebackground='white', activeforeground='blue')
zap_label.place(relx=0.2, rely=0.1)
reg_button.place(relx=0.2, rely=0.3)
enter_button.place(relx=0.2, rely=0.6)

reg_label = Label(root, text='Регистрация', font= ("Comic Sans MS", 20), fg= 'blue')
name_vvod_label = Label(root, text='Введите имя', font= ("Comic Sans MS", 20), fg= 'blue')
password_vvod_label = Label(root, text='Введите пароль', font= ("Comic Sans MS", 20), fg= 'blue')
name_vvod = Entry(root)
password_vvod = Entry(root, show='*')
vvod_button = Button(root, text='Внести данные', command=reg, font= ("Comic Sans MS", 20), fg= 'red', bg= 'black', activebackground='white', activeforeground='blue')

ent_label = Label(root, text='Вход', font= ("Comic Sans MS", 20), fg= 'blue')
ent_button = Button(root, text='Войти', command=ent, font= ("Comic Sans MS", 20), fg= 'red', bg= 'black', activebackground='white', activeforeground='blue')

create_record = Button(root, text='Создать запись', command=create_rec, font= ("Comic Sans MS", 15), fg= 'red', bg= 'black', activebackground='white', activeforeground='blue')
record_list_label = Label(root, text='Ваши записи:', font= ("Comic Sans MS", 15), fg= 'blue')
show_records = ScrolledText(root, width=45, height=12, font= ("Comic Sans MS", 15), fg= 'blue', wrap='word')

create_record_label = Label(root, text='Введите запись:', font= ("Comic Sans MS", 20), fg= 'blue')
record_vvod = Entry(root)
create_record_vvod = Button(root, text='Внести запись', command=create_rec_vvod, font= ("Comic Sans MS", 20), fg= 'red', bg= 'black', activebackground='white', activeforeground='blue')

delete_rec_button = Button(root, text='удалить запись', command=delete_rec_vvod, font= ("Comic Sans MS", 15), fg= 'red', bg= 'black', activebackground='white', activeforeground='blue')
delete_label = Label(root, text='Введите номер записи:', font= ("Comic Sans MS", 15), fg= 'blue')
delete_entry = Entry(root)
delete_button = Button(root, text='удалить', command=delete_rec, font= ("Comic Sans MS", 10), fg= 'red', bg= 'black', activebackground='white', activeforeground='blue')


root.mainloop()