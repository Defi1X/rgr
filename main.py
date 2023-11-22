#!/usr/bin/python3
import pathlib
import pygubu
from tkinter import filedialog
from CTkMessagebox import CTkMessagebox
import customtkinter as tk

from modules.utilities import unlockProcedure, isTextValid

from modules.atbash import atbash_decode, atbash_encode 
from modules.viginere import vigenere_decode, vigenere_encode, is_valid_vigenere_key
from modules.gronsfeld import gronsfeld_decode, gronsfeld_encode, is_valid_gronsfeld_key

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "design.ui"

class DesignApp:
    def __init__(self, master=None):    
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("app", master)
        
        self.cypher_choice = None
        builder.import_variables(self, ['cypher_choice'])

        builder.connect_callbacks(self)

        self.vigenere_key = "123"
        self.gronsfeld_sequence = "asd"


    def run(self):
        self.mainwindow.mainloop()

    def openFileHandler(self):
        path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if path:
            with open(path, "r") as file:
                content = file.read()
                self.builder.get_object("inputTextBox").delete("1.0", "end")
                self.builder.get_object("inputTextBox").insert("1.0", content)
                # self.builder.get_object("inputTextBox").configure(state="disabled")

    def resetProgramStateHandle(self):
        self.builder.get_object("inputTextBox").configure(state="normal")
        self.builder.get_object("outputTextBox").configure(state="normal")
        self.builder.get_object("inputTextBox").delete("1.0", "end")
        self.builder.get_object("outputTextBox").delete("1.0", "end")

        
    def saveFileHandler(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt",
                                            initialfile="end_Output.txt",
                                            filetypes=[("Text Files", "*.txt")])
        if path:
            with open(path, 'w') as file:
                content = self.builder.get_object("outputTextBox").get("1.0", "end")
                file.write(content)


    def radio1Handle(self):
        toplevel = tk.CTkToplevel(master=self.mainwindow)
        toplevel.title("Viginere cypher")
        
        label = tk.CTkLabel(toplevel, text="Provide a key-phrase:")
        label.pack()
        
        entry = tk.CTkEntry(toplevel)
        entry.pack()
        self.vigenere_key_entry = entry

        def close_window():
            self.vigenere_key = self.vigenere_key_entry.get()  # после закрытия окна сохраняем значение в атрибут класса
            toplevel.destroy()

        button = tk.CTkButton(toplevel, text="Close", command=close_window)
        button.pack()

        toplevel.focus()

    def radio2Handle(self):
        pass

    def radio3Handle(self):
        toplevel = tk.CTkToplevel(master=self.mainwindow)
        toplevel.title("Gronsfeld cypher")
        
        label = tk.CTkLabel(toplevel, text="Provide a key-phrase:")
        label.pack()
        
        entry = tk.CTkEntry(toplevel)
        entry.pack()
        self.gronsfeld_entry = entry

        def close_window():
            self.gronsfeld_sequence = self.gronsfeld_entry.get()  
            toplevel.destroy()

        button = tk.CTkButton(toplevel, text="Close", command=close_window)
        button.pack()

        toplevel.focus()

    def encryptHandle(self):
        cipher_choice = self.cypher_choice.get()  # Получаем выбранный шифр
        input_text = self.builder.get_object("inputTextBox").get("1.0", "end").strip()  # Получаем текст для шифрования

        if not isTextValid(input_text):
            CTkMessagebox(title="Error", icon="cancel", message="Incorrect input text. Make sure to use to use english letters, printable special characters.")
            return

        # Здесь вызываем соответствующую функцию шифрования на основе выбранного шифра и передаем параметры
        if cipher_choice == 1:
            key = self.vigenere_key  # Получаем ключ для шифра Виженера
            if is_valid_vigenere_key(key):
                encrypted_text = vigenere_encode(input_text, key)  
            else:
                CTkMessagebox(title="Error", icon="cancel", message="Invalid key provided. Make sure to use only english letters[a-z].")
                return
        elif cipher_choice == 2:
            encrypted_text = atbash_encode(input_text) 
        elif cipher_choice == 3:
            sequence = self.gronsfeld_sequence  # Получаем последовательность чисел для шифра Гронсфельда
            if is_valid_gronsfeld_key(sequence):
                encrypted_text = gronsfeld_encode(input_text, sequence)  
            else:
                CTkMessagebox(title="Error", icon="cancel", message="Invalid key provided. Make sure to use only digits[0-9].")
                return
        else:
            encrypted_text = ""  # Выбор стандартного значения

        self.builder.get_object("outputTextBox").configure(state="normal") 
        self.builder.get_object("outputTextBox").delete("1.0", "end")  
        self.builder.get_object("outputTextBox").insert("1.0", encrypted_text)  # Вставляем зашифрованный текст
        self.builder.get_object("outputTextBox").configure(state="disabled")  # Блокируем поле для редактирования

    def decryptHandle(self):
        cipher_choice = self.cypher_choice.get()  # Получаем выбранный шифр 
        input_text = self.builder.get_object("inputTextBox").get("1.0", "end").strip()  # Получаем текст для дешифрования

        if not isTextValid(input_text):
            CTkMessagebox(title="Error", icon="cancel", message="Incorrect input text. Make sure to use to use english letters, printable special characters.")
            return
        

        # Здесь вызываем соответствующую функцию дешифрования на основе выбранного шифра и передаем параметры
        if cipher_choice == 1:
            key = self.vigenere_key  # Получаем ключ для шифра Виженера
            if is_valid_vigenere_key(key):
                decrypted_text = vigenere_decode(input_text, key) 
            else:
                CTkMessagebox(title="Error", icon="cancel", message="Invalid key provided. Make sure to use only english letters[a-z].")
                return
        elif cipher_choice == 2:
            decrypted_text = atbash_decode(input_text) 
        elif cipher_choice == 3:
            sequence = self.gronsfeld_sequence  # Получаем последовательность чисел для шифра Гронсфельда
            if is_valid_gronsfeld_key(sequence):
                decrypted_text = gronsfeld_decode(input_text, sequence)  
            else:
                CTkMessagebox(title="Error", icon="cancel", message="Invalid key provided. Make sure to use only digits[0-9].")
                return
        else:
            decrypted_text = ""  # Выбор стандартного значения

        self.builder.get_object("outputTextBox").configure(state="normal") 
        self.builder.get_object("outputTextBox").delete("1.0", "end")
        self.builder.get_object("outputTextBox").insert("1.0", decrypted_text)  # Вставляем расшифрованный текст
        self.builder.get_object("outputTextBox").configure(state="disabled")  # Блокируем поле для редактирования

    def on_quit(self):
        self.mainwindow.quit()



if __name__ == "__main__":
    # call authorization function
    if unlockProcedure():
        # start main cycle
        app = DesignApp()
        app.run()
    

