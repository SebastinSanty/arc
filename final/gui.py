import tkinter as tk
import tkinter.filedialog as filedialog
import os
import subprocess

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		# CheckVar1 = IntVar()
		# CheckVar2 = IntVar()
		# CheckVar3 = IntVar()
		# self.c1 = tk.Checkbutton(top, text = "Run Coursedata", variable = CheckVar1, onvalue = 1, offvalue = 0, height=5,width = 20)
		# self.c2 = tk.Checkbutton(top, text = "Run No. of Course", variable = CheckVar2, onvalue = 1, offvalue = 0, height=5, width = 20)
		# self.c3 = tk.Checkbutton(top, text = "Run Student Data", variable = CheckVar2, onvalue = 1, offvalue = 0, height=5, width = 20)
		# self.c1.pack()
		# self.c2.pack()
		# self.c3.pack()

		# self.dir_opt = {'initialdir' : '.'}

		self.coursetype_btn = tk.Button(self, text="Attach Coursetype", command=self.browse_coursetype).pack()
		self.coursetype_lbl = tk.Label(self)
		self.coursetype_lbl.pack()

		self.noofcourse_btn = tk.Button(self, text="Attach No. of Course", command=self.browse_noofcourse).pack()
		self.noofcourse_lbl = tk.Label(self)
		self.noofcourse_lbl.pack()

		self.studentdata_btn = tk.Button(self, text="Attach Student Data", command=self.browse_studentdata).pack()
		self.studentdata_lbl = tk.Label(self)
		self.studentdata_lbl.pack()

		def shcallback(filearg):
			os.system(filearg + self.coursetype_lbl['text'] + ' '+ self.noofcourse_lbl['text'] + ' ' + self.studentdata_lbl['text'] + ' 1 1 1')

		self.tag = tk.Button(self, text = "Output Tag File", command=shcallback('./tag.sh')).pack()
		self.pending = tk.Button(self, text = "Output Pending File", command=shcallback('./pending.sh')).pack()

		self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
		self.quit.pack(side="bottom")

	def browse_coursetype(self):
		filename = filedialog.askopenfilename(initialdir = os.path.dirname(os.path.abspath(__file__)))
		self.coursetype_lbl.config(text = filename[len((os.path.dirname(os.path.abspath(__file__))))+1:])

	def browse_noofcourse(self):
		filename = filedialog.askopenfilename(initialdir = os.path.dirname(os.path.abspath(__file__)))
		self.noofcourse_lbl.config(text = filename[len((os.path.dirname(os.path.abspath(__file__))))+1:])

	def browse_studentdata(self):
		filename = filedialog.askopenfilename(initialdir = os.path.dirname(os.path.abspath(__file__)))
		self.studentdata_lbl.config(text = filename[len((os.path.dirname(os.path.abspath(__file__))))+1:])

root = tk.Tk()
root.geometry('600x400')
app = Application(master=root)
app.mainloop()