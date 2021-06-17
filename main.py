from tkinter import *
from tkinter.font import *
from levelPage import LevelPage
from components.buttons import MainButton


class MainApplication(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.Main = Main(self)
        self.LevelPage = LevelPage(self)
        self.Game = None
        self.Main.pack()


class Main(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.title = Label(self, text="지구정복", font=Font(size=50))
        self.title.grid(row=0, column=0, padx=10, pady=150)

        self.startButton = MainButton(self, "시작하기", self.startCommand)
        self.startButton.grid(row=1, column=0, padx=10, pady=10)

        self.endButton = MainButton(self, "종료하기", self.endCommand)
        self.endButton.grid(row=2, column=0, padx=10, pady=10)

    def startCommand(self):
        self.pack_forget()
        self.parent.LevelPage.pack()

    def endCommand(self):
        self.parent.parent.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("지구정복")
    root.geometry("1200x800")
    root.resizable(False, False)
    MainApplication(root).pack()
    root.mainloop()
