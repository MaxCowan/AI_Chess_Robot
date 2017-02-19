from tkinter import *
import datetime
import time

class Start(Frame):

    def createWidgets(self):
        self.Start = Button(self)
        self.Start["text"] = "Start"
        self.Start["fg"]   = "green"
        self.Start["width"] = 30
        self.Start["font"] = ("Times New Roman", 130)
        self.Start["command"] =  self.onclose
        self.Start.pack()

    def __init__(self, master=None, type = "Black"):
        Frame.__init__(self, master)
        self.master = master
        master.minsize(width=480, height=320)
        master.maxsize(width=480, height=320)
        self.pack()
        self.createWidgets()

    def onclose(self):
        self.destroy()
        SignIn(self.master)

class SignIn(Frame):

    def createWidgets(self):
        self.Guest = Button(self)
        self.Guest["text"] = "Guest"
        self.Guest["fg"]   = "black"
        self.Guest["width"] = 30
        self.Guest["font"] = ("Times New Roman", 62)
        self.Guest["command"] =  self.onclose
        self.Guest.pack()


        self.btnSignIn = Button(self)
        self.btnSignIn["text"] = "Sign in"
        self.btnSignIn["fg"]   = "green"
        self.btnSignIn["width"] = 30
        self.btnSignIn["font"] = ("Times New Roman", 62)
        self.btnSignIn["command"] =  self.signedIn
        self.btnSignIn.pack()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        master.minsize(width=480, height=320)
        master.maxsize(width=480, height=320)
        self.pack()
        self.createWidgets()

    def onclose(self):
        self.destroy()
        Options(self.master)

    def signedIn(self):
        self.destroy()
        SignInOptions(self.master)

class SignInOptions(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        master.minsize(width=480, height=320)
        master.maxsize(width=480, height=320)
        self.pack()
        self.createWidgets()


    def createWidgets(self):

        self.Welcome = Label(self)
        self.Welcome["text"] = "Welcome " #TODO +USER
        self.Welcome["font"] = "Times New Roman", 20
        self.Welcome.pack()

        self.Stats = Button(self)
        self.Stats["text"] = "Your Stats  "
        self.Stats["font"] = "Times New Roman", 30
        self.Stats["command"] = lambda: self.StatsPage()
        self.Stats.pack()

        self.Play = Button(self)
        self.Play["text"] = "Play a game"
        self.Play["font"] = "Times New Roman", 30
        self.Play["command"] = self.onclose
        self.Play.pack()

    def StatsPage(self):
        self.destroy()
        Stats(self.master)

    def onclose(self):
        self.destroy()
        Options(self.master)

class Options(Frame):

    def createWidgets(self):
        timings = ["3:00", "3:00 5s Delay", "5:00", "5:00 5s Delay", "10:00", "10:00 5s Delay", "30:00", "30:00 3s Delay",
                   "60:00", "60:00 3s Delay"]
        self.vartime = StringVar(self)
        self.vartime.set("Timings")

        self.time = OptionMenu(self, self.vartime, *timings)
        self.time["font"] = ("Times New Roman", 28)
        self.time.children["menu"]["font"] = ("Times New Roman", 15)
        self.time.grid(row=0, column = 3)

        self.PlayAI = Button(self)
        self.PlayAI["text"] = ("  Play against an AI ")
        self.PlayAI.grid(row = 0, column = 1)
        self.PlayAI["font"] = ("Times New Roman", 20)
        self.PlayAI["command"] = self.StartGame

        self.PlayGuest = Button(self)
        self.PlayGuest["text"] = ("Play against a Guest")
        self.PlayGuest.grid(row = 1, column = 1)
        self.PlayGuest["font"] = ("Times New Roman", 20)
        self.PlayGuest["command"] = self.StartGame

        self.PlayUser = Button(self)
        self.PlayUser["text"] = ("Play against an User")
        self.PlayUser.grid(row = 2, column = 1)
        self.PlayUser["font"] = ("Times New Roman", 20)
        self.PlayUser["command"] = self.StartGame

        self.Cancel = Button(self)
        self.Cancel["text"] = ("Logout")
        self.Cancel["fg"] = ("red")
        self.Cancel["font"] = ("Times New Roman", 15)
        self.Cancel.grid(row = 3, column = 1)
        self.Cancel["command"] = self.GoBack

    def GoBack(self):
        self.destroy()
        Start(self.master)

    def StartGame(self):
        if self.vartime.get() != "Timings":
            self.destroy()
            Clock(self.master, self.vartime.get())

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        master.minsize(width=480, height=320)
        master.maxsize(width=480, height=320)
        self.pack()
        self.createWidgets()

    def onclose(self):
        self.destroy()
        SignIn(self.master, self.vartime.get())

class Stats(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        master.minsize(width=480, height=320)
        master.maxsize(width=480, height=320)
        self.pack()
        self.createWidgets()

    def createWidgets(self):

        self.Wins = Label(self)
        self.Wins["text"] = "Insert stats"
        self.Wins["font"] = "Times New Roman", 40
        self.Wins.pack()

        self.Losses = Label(self)
        self.Losses["text"] = "Insert stats"
        self.Losses["font"] = "Times New Roman", 40
        self.Losses.pack()

        self.Smate = Label(self)
        self.Smate["text"] = "Insert stats"
        self.Smate["font"] = "Times New Roman", 40
        self.Smate.pack()

        self.Cancel = Button(self)
        self.Cancel["text"] = ("Cancel")
        self.Cancel["fg"] = ("red")
        self.Cancel["font"] = ("Times New Roman", 15)
        self.Cancel.pack()
        self.Cancel["command"] = self.onclose

    def onclose(self):
        self.destroy()
        SignInOptions(self.master)

class Clock(Frame):

    def createWidgets(self):

        self.Switch = Button(self)
        self.Switch["bg"] = "red"
        self.Switch["width"] = 180
        self.Switch["height"] = 10
        self.Switch.pack()
        self.Switch["command"] = self.buttonPressed

        self.TimeLeft = Label(self)
        self.TimeLeft["textvar"] = self.strTime
        self.TimeLeft["font"] = "Times New Roman", 100
        self.TimeLeft.pack()


    def __init__(self, master=None, timing="5:00"):
        Frame.__init__(self, master)
        self.master = master
        master.minsize(width=480, height=320)
        master.maxsize(width=480, height=320)
        self.timerRunning = False

        self.intTime = 0
        self.Delay = 0
        self.strTime = StringVar()
        self.strTime.set("")
        self.delay = 0

        if "3:00" in timing:
            self.intTime = 180
            self.strTime.set("3:00")
        elif "5:00" in timing:
            self.intTime = 300
            self.strTime.set("5:00")
        elif "10:00" in timing:
            self.intTime = 600
            self.strTime.set("10:00")
        elif "30:00" in timing:
            self.intTime = 1800
            self.strTime.set("30:00")
        elif "60:00" in timing:
            self.intTime = 3600
            self.strTime.set("60:00")
        if "5s" in timing:
            self.delay = 5
        elif "3s" in timing:
            self.delay = 3
        self.pack()
        self.createWidgets()
        self.TimeOne = datetime.datetime.now()


    def buttonPressed(self):
        self.timerRunning = True
        time.sleep(self.delay)
        self.after(100, self.timeHandler)

    def timeHandler(self):
        if self.timerRunning:
            self.TimeTwo = datetime.datetime.now()
            #print((self.TimeTwo-self.TimeOne).seconds)
            if (self.TimeTwo-self.TimeOne).seconds >= 1:
                self.intTime -= 1
                # print(self.intTime)
                # print("New time:", str(self.intTime//60) + ":" + str(self.intTime % 60))
                self.strTime.set(str(self.intTime//60) + ":" + str(self.intTime % 60).zfill(2))
                self.TimeOne = self.TimeTwo
            self.after(100, self.timeHandler)

root = Tk()
app = Start(master=root)
app.mainloop()
root.destroy()
