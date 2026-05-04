import tkinter as tk
from tkinter import messagebox
import random
import json
import os

quotes = [
    {"text": "Будь лучше, чем вчера.", "author": "Алексей Иванов", "topic": "Мотивация"},
    {"text": "Только тот, кто рискует, пьет шампанское.", "author": "Владимир Войнович", "topic": "Жизнь"},
    {"text": "Учение — свет, а неучение — тьма.", "author": "Пётр Лавров", "topic": "Образование"},
    {"text": "Успех — это сумма маленьких усилий, повторяющихся изо дня в день.", "author": "Роберт Коллиер", "topic": "Успех"},
    {"text": "Не бойся, что не получится. Бойся, что не попробуешь.", "author": "Максим Горький", "topic": "Мотивация"},
    {"text": "Жизнь — это то, что происходит, пока ты строишь планы.", "author": "Джон Леннон", "topic": "Жизнь"},
    {"text": "Образование — это не заполнение ведра, а зажигание огня.", "author": "Уильям Батлер Йейтс", "topic": "Образование"},
    {"text": "Творчество — это позволять себе делать ошибки. Искусство — это знать, какие из них оставить.", "author": "Скотт Адамс", "topic": "Творчество"},
    {"text": "Мы — то, что мы делаем постоянно. Поэтому совершенство — это не действие, а привычка.", "author": "Аристотель", "topic": "Философия"},
    {"text": "Величайшая слава не в том, чтобы никогда не падать, а в том, чтобы подниматься каждый раз, когда падаешь.", "author": "Конфуций", "topic": "Мотивация"},
    {"text": "Единственный способ сделать выдающуюся работу — любить то, чем занимаешься.", "author": "Стив Джобс", "topic": "Успех"},
    {"text": "Время — это то, чего мы хотим больше всего, но используем хуже всего.", "author": "Уильям Пенн", "topic": "Жизнь"},
    {"text": "Мудрый человек учится на чужих ошибках, умный — на своих, а глупый не учится вовсе.", "author": "Народная мудрость", "topic": "Образование"},
]

HISTORY_FILE = 'quotes_history.json'

if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        history = json.load(f)
else:
    history = []

root = tk.Tk()
root.title("Random Quote Generator")

# Область для истории
history_listbox = tk.Listbox(root, width=80, height=15)
history_listbox.pack(pady=10)

def update_history():
    history_listbox.delete(0, tk.END)
    for item in history:
        display_text = f"\"{item['text']}\" - {item['author']} ({item['topic']})"
        history_listbox.insert(tk.END, display_text)

def save_history():
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=4)

def generate_quote():
    if not filtered_quotes_list:
        messagebox.showinfo("Информация", "Нет цитат для отображения после фильтрации.")
        return
    quote = random.choice(filtered_quotes_list)
    history.append(quote)
    save_history()
    update_history()

generate_button = tk.Button(root, text="Сгенерировать цитату", command=generate_quote)
generate_button.pack(pady=10)

# Фильтры
filter_frame = tk.Frame(root)
filter_frame.pack(pady=5)

tk.Label(filter_frame, text="Автор:").grid(row=0, column=0, padx=5)
author_entry = tk.Entry(filter_frame)
author_entry.grid(row=0, column=1, padx=5)

tk.Label(filter_frame, text="Тема:").grid(row=0, column=2, padx=5)
topic_entry = tk.Entry(filter_frame)
topic_entry.grid(row=0, column=3, padx=5)

def apply_filter():
    author_filter = author_entry.get().strip().lower()
    topic_filter = topic_entry.get().strip().lower()
    global filtered_quotes_list
    filtered_quotes_list = [
        q for q in quotes
        if (author_filter in q['author'].lower() if author_filter else True) and
           (topic_filter in q['topic'].lower() if topic_filter else True)
    ]

filter_button = tk.Button(filter_frame, text="Применить фильтр", command=apply_filter)
filter_button.grid(row=0, column=4, padx=5)

filtered_quotes_list = quotes.copy()

# Проверка и запуск
update_history()
root.mainloop()