from googletranslator import custom as cs, data as d
import customtkinter as ctk
from tkinter import messagebox, END, INSERT
from PIL import ImageTk, Image
from googletrans import Translator
import pyttsx3

ctk.set_appearance_mode("light")


class GoogleTranslate(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Settings
        self.detectedLang = None
        self.geometry("900x540")
        self.title(" Myles' Language Translator")
        self.resizable(width=True, height=True)
        self.configure(bg_color=cs.color1)

        # A Frame: For showing the GoogleTranslate Logo
        self.frame = ctk.CTkFrame(self, width=180, height=100)
        self.frame.pack(pady=20)
        self.frame.place(x=20, y=20)

        # DisplayLogo method definition
        self.DisplayLogo()

        # ========Header Buttons========
        # About Button
        def About():
            messagebox.showinfo("Google Translate - Python", "Developed by Myles Petu")

        aboutBtn = ctk.CTkButton(self, text="About",
                                 font=(cs.font1, 10, 'bold'), bg_color=cs.color4,
                                 fg_color=cs.color4, width=13, command=About)

        aboutBtn.pack(pady=5)
        aboutBtn.place(x=800, y=20)

        # Exit Button
        exitBtn = ctk.CTkButton(self, text="Exit",
                                font=(cs.font4, 10, 'bold'), bg_color=cs.color4,
                                fg_color=cs.color4, width=13, command=self.Exit)
        exitBtn.pack(pady=5)
        exitBtn.place(x=800, y=50)
        self.MainWindow()

    def DisplayLogo(self):

        image = ctk.CTkImage(Image.open('LangLogo.png'),
                             size=(190, 100))  # WidthxHeight

        # image = Image.open('GoogleTranslate.png')
        # Resizing the image
        # resized_image = image.resize((160, 100))

        # self.img1 = ImageTk.PhotoImage(image=image)
        # A Label Widget to display the Image
        label = ctk.CTkLabel(self.frame, bg_color=cs.color1, fg_color=cs.color1, image=image)
        label.pack()

    def MainWindow(self):
        # String Variable
        self.currLang = ctk.StringVar()
        self.currLang.set("Type Here")

        # Label: For showing the name of detected language
        self.detectedLang = ctk.CTkLabel(self, width=150, height=10,
                                         textvariable=self.currLang, font=(cs.font3, 20),
                                         bg_color=cs.color1, fg_color=cs.color1)
        self.detectedLang.pack(pady=50)
        self.detectedLang.place(x=160, y=155)

        # Combobox: To select the language to be translated
        self.toLang = ctk.CTkComboBox(self, values=d.lang_list)
        self.toLang.pack(pady=10)
        self.toLang.place(x=550, y=130)

        self.fromText_Box = ctk.CTkTextbox(self, width=400, height=200)
        self.fromText_Box.pack(pady=10)
        self.fromText_Box.place(x=80, y=190)

        self.toText_Box = ctk.CTkTextbox(self, width=400, height=200)
        self.toText_Box.pack(pady=10)
        self.toText_Box.place(x=490, y=190)

        # Translate Button
        translateBtn = ctk.CTkButton(self, text="Translate",
                                     font=(cs.font4, 14, "bold"), bg_color=cs.color4,
                                     fg_color=cs.color4, command=self.Translator)
        translateBtn.pack(pady=10)
        translateBtn.place(x=290, y=430)
        # Speak Button
        speakBtn = ctk.CTkButton(self, text="Speak",
                                 font=(cs.font4, 14, "bold"), bg_color=cs.color4,
                                 fg_color=cs.color4, command=self.Speak)
        speakBtn.pack(pady=10)
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

                    self.currLang.set("Detected Language: " + langType.lang)

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
        self.destroy()


if __name__ == "__main__":
    # Instance of GoogleTranslator Class
    obj = GoogleTranslate()
    obj.mainloop()
