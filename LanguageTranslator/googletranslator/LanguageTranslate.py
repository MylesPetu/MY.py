from googletranslator import custom as cs, data as d
from tkinter import *
from PIL import ImageTk, Image
from googletrans import Translator
from tkinter import ttk, messagebox
import pyttsx3




class GoogleTranslate:

    def __init__(self, root):
        # Window Settings
        self.toText_Box = None
        self.fromText_Box = None
        self.img1 = None
        self.toLang = None
        self.detectedLang = None
        self.currLang = None
        self.window = root
        self.window.geometry("900x540")
        self.window.title('Language Translator')
        self.window.resizable(width=True, height=True)
        self.window.configure(bg="white")

        # A Frame: For showing the GoogleTranslate Logo
        self.frame = Frame(self.window, width=300, height=60)
        self.frame.pack()
        self.frame.place(x=20, y=20)

        # DisplayLogo method definition
        self.DisplayLogo()

        # ========Header Buttons========
        def About():
            messagebox.showinfo("Google Translate - Python", "Developed by Myles Petu")

        # About Button
        aboutBtn = Button(self.window, text="About",
                          font=(cs.font2, 8, 'bold'), bg=cs.color2,
                          fg="white", width=5, command=About)
        aboutBtn.place(x=800, y=20)

        # Exit Button
        exitBtn = Button(self.window, text="Exit",
                         font=(cs.font2, 8, 'bold'), bg=cs.color2,
                         fg="white", width=5, command=self.Exit)
        exitBtn.place(x=800, y=60)

        self.MainWindow()
# opens and resizes the logo(image)

    def DisplayLogo(self):
        # Opening the image
        image = Image.open('Logo-removebg-preview.png')
        # Resizing the image
        resized_image = image.resize((160, 100))

        self.img1 = ImageTk.PhotoImage(resized_image)
        # A Label Widget to display the Image
        label = Label(self.frame, bg=cs.color1, image=self.img1)
        label.pack()

    def MainWindow(self):
        # String Variable
        self.currLang = StringVar()
        self.currLang.set("Type Here")
        # Label: For showing the name of detected language
        self.detectedLang = Label(self.window,
                                  textvariable=self.currLang, font=(cs.font3, 20),
                                  bg=cs.color1)
        self.detectedLang.place(x=160, y=155)

        # Combobox: To select the language to be translated
        text = StringVar()
        self.toLang = ttk.Combobox(self.window, textvariable=text,
                                   font=(cs.font1, 15))
        self.toLang['values'] = d.lang_list
        self.toLang.current(0)
        self.toLang.place(x=550, y=130)

        self.fromText_Box = Text(self.window, bg=cs.color3,
                                 font=(cs.font1, 15), height=9, width=34)
        self.fromText_Box.place(x=80, y=190)

        self.toText_Box = Text(self.window, bg=cs.color3,
                               relief=GROOVE, font=(cs.font1, 15), height=9, width=34)
        self.toText_Box.place(x=480, y=190)

        translateBtn = Button(self.window, text="Translate",
                              font=(cs.font2, 14, "bold"), bg=cs.color4, fg=cs.color1,
                              command=self.Translator)
        translateBtn.place(x=290, y=430)

        speakBtn = Button(self.window, text="Speak",
                          font=(cs.font2, 14, "bold"), bg=cs.color4, fg=cs.color1,
                          command=self.Speak)
        speakBtn.place(x=500, y=430)

    def Translator(self):
        try:
            fromText = self.fromText_Box.get("1.0", "end-1c")

            # Instance of Translator class
            translator = Translator()

            dest_lang = self.toLang.get()

            if dest_lang == '':
                messagebox.showwarning("Nothing has chosen!", "Please Select a Language")
            else:
                if fromText != '':
                    langType = translator.detect(fromText)

                    # Translating the text
                    result = translator.translate(fromText, dest=dest_lang)

                    self.currLang.set(d._language[langType.lang.lower()])

                    self.toText_Box.delete("1.0", END)

                    self.toText_Box.insert(INSERT, result.text)
        except Exception as es:
            messagebox.showerror("Error!", f"Error due to {es}")

    def Speak(self):
        try:
            toText = self.toText_Box.get("1.0", "end-1c")
            if toText != '':
                engine = pyttsx3.init()
                engine.say(toText)
                engine.runAndWait()
            else:
                messagebox.showwarning("Nothing to speak!", "Please translate some text first")
        except Exception as es:
            messagebox.showerror("Error!", f"Error due to {es}")

    def Exit(self):
        self.window.destroy()


if __name__ == "__main__":
    # Instance of Tk Class
    root = Tk()
    # Object of GoogleTranslator Class
    obj = GoogleTranslate(root)
    root.mainloop()
