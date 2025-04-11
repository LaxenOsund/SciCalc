import customtkinter
class Buttons(customtkinter.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        self.Bopen = customtkinter.CTkButton(self, text="(",width=40,height=40)
        self.Bopen.grid(row=2, column=0, padx=2, pady=(0, 0), sticky="e")
        self.Bclose = customtkinter.CTkButton(self, text=")",width=40,height=40)
        self.Bclose.grid(row=2, column =1, padx=2, pady=(0, 0), sticky="e")
        self.Bmc = customtkinter.CTkButton(self, text="mc",width=40,height=40)
        self.Bmc.grid(row=2, column =2, padx = 2, pady=(0,0), sticky = "e")
        self.Bmadd = customtkinter.CTkButton(self, text="m+",width=40,height=40)
        self.Bmadd.grid(row=2, column=3, padx=2, pady=(0, 0), sticky="e")
        self.Bmneg = customtkinter.CTkButton(self, text="m-",width=40,height=40)
        self.Bmneg.grid(row=2, column=4, padx=2, pady=(0, 0), sticky="e")
        self.Bdel = customtkinter.CTkButton(self, text="del",width=40,height=40)
        self.Bdel.grid(row=2, column=5, padx=2, pady=(0,0), sticky="e")
        self.Bchange = customtkinter.CTkButton(self, text="+/-",width=40,height=40)
        self.Bchange.grid(row=2, column=6, padx=2, pady=(0, 0), sticky="e")
        self.Bmod = customtkinter.CTkButton(self, text="%",width=40,height=40)
        self.Bmod.grid(row=2, column=7, padx=2, pady=(0, 0), sticky="e")
        self.Bdiv = customtkinter.CTkButton(self, text="/",width=40,height=40,fg_color="orange")
        self.Bdiv.grid(row=2, column=8, padx=2, pady=(0,0), sticky="e")
        
        self.Bopen = customtkinter.CTkButton(self, text="(",width=40,height=40)
        self.Bopen.grid(row=3, column=0, padx=2, pady=4, sticky="ne")
        self.Bclose = customtkinter.CTkButton(self, text=")",width=40,height=40)
        self.Bclose.grid(row=3, column =1, padx=2, pady=4, sticky="ne")
        self.Bmc = customtkinter.CTkButton(self, text="mc",width=40,height=40)
        self.Bmc.grid(row=3, column =2, padx = 2, pady=(0,0), sticky = "e")
        self.Bmadd = customtkinter.CTkButton(self, text="m+",width=40,height=40)
        self.Bmadd.grid(row=3, column=3, padx=2, pady=(0, 0), sticky="e")
        self.Bmneg = customtkinter.CTkButton(self, text="m-",width=40,height=40)
        self.Bmneg.grid(row=3, column=4, padx=2, pady=(0, 0), sticky="e")
        self.bdel = customtkinter.CTkButton(self, text="del",width=40,height=40)
        self.bdel.grid(row=3, column=5, padx=2, pady=(0,0), sticky="e")
        self.Bchange = customtkinter.CTkButton(self, text="+/-",width=40,height=40)
        self.Bchange.grid(row=3, column=6, padx=2, pady=(0, 0), sticky="e")
        self.Bmod = customtkinter.CTkButton(self, text="%",width=40,height=40)
        self.Bmod.grid(row=3, column=7, padx=2, pady=(0, 0), sticky="e")
        self.Bdiv = customtkinter.CTkButton(self, text="/",width=40,height=40,fg_color="orange")
        self.Bdiv.grid(row=3, column=8, padx=2, pady=(0,0), sticky="e")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("420x180")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        self.checkbox_frame = Buttons(self)
        self.checkbox_frame.grid(row = 0, column = 0, padx = 10, pady = (10,0), sticky = "nsw")
        
        
        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")


    def button_callback(self):
        print("button pressed")

app = App()
app.mainloop()