#!/usr/bin/python
from Tkinter import *
import tkMessageBox
from urllib2 import Request, urlopen, URLError, HTTPError

class GuiWindow:

	def __init__(self):
		''' Initialize GUI window '''

		self.root = Tk()
		self.root.minsize(width=540, height=300)
		self.root.title('Live-score window')

		# GUI title
		self.l1 = Label(self.root, text="Live Score", font=('bold', 20))
		self.l1.pack()

		# URL label
		self.l2 = Label(self.root, text="Match URL", font=15)
		self.l2.pack()
		self.l2.place(x=5, y=55)

		self.textbox1 = Entry(self.root)
		self.textbox1.pack()
		self.textbox1.place(x=100, y=55, width=422)

		# Interval label
		self.l3 = Label(self.root, text="Interval (min 20 sec)", font=15)
		self.l3.pack()
		self.l3.place(x=5, y=90)

		self.textbox2 = Entry(self.root)
		self.textbox2.pack()
		self.textbox2.place(x=180, y=90, width=50)


		self.notifType = IntVar()				

		# Notification type radio buttons
		self.l4 = Label(self.root, text="Show notification : ", font=15)
		self.l4.pack()
		self.l4.place(x=5, y=130)

		self.r1 = Radiobutton(self.root, 
					text="After every interval", 
					variable=self.notifType,
					value=1)
		self.r1.pack()
		self.r1.place(x=20, y=160)


		self.r2 = Radiobutton(self.root, 
					text="When runs are scored", 
					variable=self.notifType,
					value=2)
		self.r2.pack()
		self.r2.place(x=20, y=190)

		self.r3 = Radiobutton(self.root, 
					text="When wickets fall",
					variable=self.notifType,
					value=3)
		self.r3.pack()
		self.r3.place(x=20, y=220)


		# buttons
		self.b1 = Button(self.root, 
					 text="Quit",
					 command=self.quitWindow)
		self.b1.pack()
		self.b1.place(x=15, y=260)

		self.b2 = Button(self.root, 
					 text="Start live score",
					 command=self.retrieveInput)
		self.b2.pack()
		self.b2.place(x=400, y=260)


		self.root.mainloop()

	def getUrl(self):
		url = self.textbox1.get()
		try: 
		    response = urlopen(url)
		    return url
		except HTTPError as e:
		    tkMessageBox.showerror("URL Error", "The server couldn\'t fulfill the request.")
		    return -1
		except URLError as e:
		    tkMessageBox.showerror("URL Error", "Failed to reach a server.")
		    return -1
		except ValueError:
			tkMessageBox.showerror("URL Error", "Use valid full qualified domain name")
			return -1
		    
						 
		else:				
			tkMessageBox.showerror("URL Error", "URL is empty")
			return -1
		
	def getInterval(self):
		try:
			intv = int(self.textbox2.get())
			if (intv >= 20):
				return intv 
			else:				
				tkMessageBox.showerror("Input Error", "Interval should be greater than or equal to 20 sec")
				return -1
		except ValueError:
			tkMessageBox.showerror("Input Error", "Invalid Interval input")
			return -1

	def getNotifType(self):
		ntype = int(self.notifType.get())
		if (ntype == 0):
			tkMessageBox.showerror("Input Error", "Notification type not selected")
			return -1
		else:
			return ntype	

	def retrieveInput(self):
		self.startLiveScore = True
		self.url = self.getUrl()
		if (self.url == -1):
			return

		self.interval = self.getInterval()
		if (self.interval == -1):
			return

		self.notifChoice = self.getNotifType()
		if (self.notifChoice == -1):
			return

		self.root.destroy()	

	def quitWindow(self):
		self.startLiveScore = False
		self.root.destroy()
