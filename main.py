from tkinter import *

class Human:

    alphabeth = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                 'P', 'Q', 'R','S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ']

    morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
              '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----', ' ']

root = Tk()
root.title('Morse Code')
root.configure(background='#675355')
root.geometry('600x800')
canvas = Canvas(root, bg='#675355', height=600, width=400)
word = Entry(root)
word.place(x=360, y=160)
image = PhotoImage(file=r'C:\Users\TOSHIBA\OneDrive\Masaüstü/image_1.png')
label1 = Label(root, text='Write some word to translate in Morse Code  ', background='#ffe5b2').place(x=100 ,y=160)
label_img = Label(image=image).place(x=100 ,y=280)


new_word = []

def clear():
    new_word.clear()
    word.delete(0, END)
    mylabel2.destroy()
def change():
    global mylabel2
    for i in (word.get()).upper():
        number_word = Human.alphabeth.index(i)
        new_word.append(Human.morse_code[number_word])
    mylabel2 = Label(root, text=new_word, background='#f8770e', padx=20, pady=8, foreground='blue')
    mylabel2.place(x=280, y=240)



mybutton = Button(root, text='Translate', padx=20, pady=8, command=change, background='#9ec2e2').place(x=280 ,y=200)
again_button = Button(root, text='Try Again', padx=20, pady=8, command=clear, background='#8ec2e2').place(x=360 ,y=200)


root.mainloop()