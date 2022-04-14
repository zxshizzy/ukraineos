import wikipedia
from tkinter import *
from tkinter import messagebox
import time

window = Tk()
window.configure(bg="#3C3C3C")
window.attributes("-fullscreen", True)

def loading_anim():
    def end():
        load.place(relx=1000)
        ico.place(relx=1000)

        #chrome

        def chromeopen():
            def show_message():
                print("searching")
                wikipedia.set_lang("uk")
                parsed = wikipedia.summary(message.get())
                print(parsed)
                messagebox.showinfo("BanderaSearch", parsed)

            def close_browser():
                label_name.place(relx=1000)
                message_entry.place(relx=1000)
                message_button.place(relx=1000)
                close_button.place(relx=1000)
            message = StringVar()
            getinfo = message.get()
    
            label_name = Label(text="Bandera", fg="#ffffff", bg="#0000ff", font="bold")
            label_name.place(relx=0.483, rely=0.350)
    
    
            message_entry = Entry(textvariable=message)
            message_entry.place(relx=.5, rely=0.4, anchor="c")

            message_button = Button(text="Search", command=show_message)
            message_button.place(relx=.480, rely=.450, anchor="c")

            close_button = Button(text="Close", command=close_browser)
            close_button.place(relx=.520, rely=.450, anchor="c")

        def settings_open():
            def settings_def():
                window.config(bg=settings_color.get())

            def settings_close():
                settings_label.place(relx=1000)
                settings_entry.place(relx=1000)
                settings_button.place(relx=1000)
                settings_close_btn.place(relx=1000)

            settings_label = Label(text="Background color(html):", bg='white')
            settings_label.place(relx=0.405, rely=0.350)

            settings_color = StringVar()
            settings_entry = Entry(textvariable=settings_color)
            settings_entry.place(relx=0.405, rely=0.4)

            settings_button = Button(text="Ok", command=settings_def)
            settings_button.place(relx=0.405, rely=0.430)
            
            settings_close_btn = Button(text="Close", command=settings_close)
            settings_close_btn.place(relx=0.420, rely=0.430)
        
        chrome = Button(window, text="BanderaBrowser", command=chromeopen)
        chrome.place(relx=0.030, rely=0.050, height=100, width=100)

        settings = Button(window, text="Settings", command=settings_open)
        settings.place(relx=0.030, rely=0.220, width=100, height=100)



    load.after(5000, end)

load = Label(text="Loading...", font=("Bolt", 30), background="#3c3c3c")
load.place(relx=0.455, rely=0.440)

ico = Label(text="𝓤𝓴𝓻𝓪𝓲𝓷𝓮 𝓞𝓢", font=("Arial", 50), background="#3C3C3C")
ico.place(relx=0.405, rely=0.350)

loading_anim()

window.mainloop()
