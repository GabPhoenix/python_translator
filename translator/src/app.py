# IMPORTING MODULES
import tkinter as tk
from tkinter.constants import END
from tkinter import ttk, messagebox
from translate import Translator
import sys

# DON'T CREATE PYCACHE FILES
sys.dont_write_bytecode = True

class UIScreens():
    def __init__(self):
        self.cyan = '#1E90FF'

        self.splash = tk.Tk()
        # WINDOW SETTINGS
        self.splash.withdraw() # HIDE WINDOW WHILE CALCULATING
        self.splash.update_idletasks()

        # CENTER WINDOW
        x = (self.splash.winfo_screenwidth() - 850) / 2
        y = (self.splash.winfo_screenheight() - 500) / 2
        self.splash.geometry("850x500+%d+%d" % (x, y))
        self.splash.deiconify() # SHOW THE WINDOW AFTER CALCULATE
        self.splash.configure(background=self.cyan) #CHANGE BACKGROUND COLOR
        # HIDE THE PERMISSON TO REDIRECT THE WINDOW
        self.splash.overrideredirect(True) 

        # LOGO SPLASH ROOT IMAGE
        _image = tk.PhotoImage(file="C:\\Users\\PC\\Desktop\\Gabriel\\ref_tradutorpy\\translator\\src\\ui_translator\\img\\logo.png") 

        # SETTING IMAGE
        self.img = tk.Label(self.splash)
        self.img.place(x=50, y=100, width=300, height=300)
        self.img.configure(image=_image)

        # SETTING TEXTS LABELS
        self.splash_name = tk.Label(self.splash)
        self.splash_name.place(x=400, y=130, width=400, height=180)
        self.splash_name.configure(
            background=self.cyan,
            foreground='#FFF',
            text='Python\nTranslator', 
            font='-family {Seoge UI} -size 60 -weight bold',
        )

        self.text2 = tk.Label(self.splash)
        self.text2.place(x=410, y=300, width=400, height=60)
        self.text2.configure(
            background=self.cyan,
            foreground='#FFF',
            text='...',
            font='-family {Tw Cen MT} -size 60 -weight bold'
        )

        self.author = tk.Label(self.splash)
        self.author.place(x=625, y=450, width=220, height=60)
        self.author.configure(
            background=self.cyan,
            foreground='#FFF',
            text='Powered by Gabriel Carvalho', 
            font='-family {Seoge UI} -size 11 -weight bold',
        )


        # CALL MAIN WINDOW AFTER SOME MILISECONDS
        self.splash.after(3000, self.main_screen)
        self.splash.mainloop()


        self.cyan = '#1E90FF'
    def main_screen(self):
        self.splash.destroy()

        self.main = tk.Tk()
        self.main.title('Python Translator')
        self.main.iconbitmap("C:\\Users\\PC\\Desktop\\Gabriel\\ref_tradutorpy\\translator\\src\\ui_translator\\img\\logo.ico")
         # CENTER WINDOW
        x = (self.main.winfo_screenwidth() - 1000) / 2
        y = ((self.main.winfo_screenheight() - 500) / 2)-30
        self.main.geometry("1000x500+%d+%d" % (x, y))
        self.main.deiconify() # SHOW THE WINDOW AFTER CALCULATE
        self.main.configure(background="#FDFDFD") #CHANGE BACKGROUND COLOR
        # HIDE THE PERMISSON TO REDIRECT THE WINDOW
        self.main.minsize(1000, 500)
        self.main.maxsize(1000, 500)

        self.top_bar = tk.Frame(self.main)
        self.top_bar.place(x=0, y=0, width=1366, height=90)
        self.top_bar.configure(background=self.cyan)

        # LOGO AND NAME
        self.logo = tk.Label(self.top_bar)
        self.logo.place(x=10, y=0, width=90, height=90)
        self.logo_img = tk.PhotoImage(file="C:\\Users\\PC\\Desktop\\Gabriel\\ref_tradutorpy\\translator\\src\\ui_translator\\img\\EN.png")
        self.logo.configure(image=self.logo_img)

        self.name = tk.Label(self.top_bar)
        self.name.place(x=110, y=0, width=400, height=90)
        self.name.configure(
            background=self.cyan,
            foreground='#FFF',
            text='Python Translator',
            font='-family {Seoge UI} -size 30 -weight bold',
            anchor='w'
        )
        # COMBOBOXIES
        self.idioms = ['en', 'pt', 'spa', 'fr', 'zh', 'ja', 'ko']
        self.combobox_one = ttk.Combobox(self.main)
        self.combobox_one.place(x=370, y=110, width=110, height=30)
        self.combobox_one.configure(
            values=self.idioms,
            background='#FDFDFD',
            foreground=self.cyan,
            font='-family {Seoge UI} -size 10 -weight bold'
        )

        self.combobox_two = ttk.Combobox(self.main)
        self.combobox_two.place(x=520, y=110, width=110, height=30)
        self.combobox_two.configure(
            values=self.idioms,
            background='#FDFDFD',
            foreground=self.cyan,
            font='-family {Seoge UI} -size 10 -weight bold'
        )

        # TEXTS
        self.text_one = tk.Text(self.main)
        self.text_one.place(x=20, y=150, width=460, height=275)
        self.text_one.configure(
            background='#dfe9f7',
            foreground=self.cyan,
            font='-family {Seoge UI} -size 12 -weight bold',
            relief='flat'      
        )

        self.text_two = tk.Text(self.main)
        self.text_two.place(x=520, y=150, width=460, height=275)
        self.text_two.configure(
            background='#dfe9f7',
            foreground=self.cyan,
            font='-family {Seoge UI} -size 12 -weight bold',
            relief='flat' 
        )
        
        # BUTTON TRANSLATE
        self.button = tk.Button(self.main)
        self.button.place(x=20, y=450, width=100, height=30)
        self.button.configure(
            background=self.cyan,
            foreground='#FDFDFD',
            relief='flat',
            activebackground='#FDFDFD',
            activeforeground=self.cyan,
            font='-family {Seoge UI} -size 14 -weight bold',
            text='Translate',
            anchor='center',
            cursor='hand2',
            command=self.on_click
        )

    # VERIFICATION IDIOMS AND COMMANDS
    def on_click(self):
        # CLEAR txt 2
        self.text_two.delete('1.0', END)

        # GETTING IDIOMS
        self.lang_one = self.combobox_one.get()
        self.lang_two = self.combobox_two.get()

        # IDIOMS VERIFICATION
        if self.lang_one == '':
            messagebox.showwarning('Select a language', 'Please, select a language\nfrom you want to translate!')
            return 0
        elif self.lang_two == '':
            messagebox.showwarning('Select a language', 'Please, select a language\nto you want to translate!')
            return 0
        
        translator = Translator(from_lang=self.lang_one, to_lang=self.lang_two)
        txt_translated =  translator.translate(self.text_one.get('1.0', END))
        self.text_two.insert('1.0', txt_translated)
        
        self.main.mainloop()

if __name__ == '__main__':
    app = UIScreens()
    sys.exit(0)