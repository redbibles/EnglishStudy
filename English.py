import tkinter as tk
import time
import random
from threading import Timer

Nlines=0
line=[]
f = open('English.dat','r')
while True:
    line.append( f.readline() )
    if not line[Nlines]: break
    Nlines=Nlines+1
f.close()

TestOrder  = list(range(0,Nlines))
TestNumber = Nlines
Stime      = time.time()
Qus = ''

class MyInfiniteTimer():

    def __init__(self, t, hFunction):
        self.t = t
        self.hFunction = hFunction
        self.thread = Timer(self.t, self.handle_function)
        
    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.t, self.handle_function)
        self.thread.start()
        
    def start(self):
        self.thread = Timer(self.t, self.handle_function)
        self.thread.start()
        
    def cancel(self):
        self.thread.cancel()

def TimerFunction():
    ScoreLabel.configure(text = 'Time : {0:3d}'.format(int(time.time()-Stime)))
    

TimerThread = MyInfiniteTimer(1,TimerFunction)    
    
def Answer(event):
    global TestNumber
    global Qus

    if TestNumber >= 5:
        TimerThread.cancel()
        btn['state']=tk.ACTIVE
        AnswerEntry.config(state=tk.DISABLED)
    else:    
        
        Ans = AnswerEntry.get()
        Ans = Ans.rstrip()
        Qus = Qus.rstrip()
        Ans = Ans.rstrip(' ')
        Qus = Qus.rstrip(' ')

        if(Ans == Qus):
            TestNumber = TestNumber+1
            print('OK')
            Question = Qus.split(' ')
            QuestionLabel.config(text = Question[0])
        else:
            print('False')
            QuestionLabel.config(text = Qus)

        Qus =line[TestOrder[TestNumber]]
        AnswerEntry.delete(0,100)

def Start():
    global Stime
    global TestNumber
    global Qus
    ScoreLabel.configure(text = '0')
    Stime=time.time()
    btn['state']=tk.DISABLED
    AnswerEntry.config(state=tk.NORMAL)
    AnswerEntry.delete(0,100)
    AnswerEntry.icursor(1)
    random.shuffle(TestOrder)
    TestNumber = 0
    Qus =line[TestOrder[TestNumber]]
    Qus = Qus.rstrip()
    Qus = Qus.rstrip(' ')
    
    QuestionLabel.config(text = Qus)
    TimerThread.start()

winWidth  = 800
winHeight = 400

win=tk.Tk()
win.geometry(str(winWidth)+'x'+str(winHeight))
win.title('English Study')
win.option_add('*Font','맑은고딕 10')

btn=tk.Button(win,text='Start')
btn.config(width=10,height=2)
btn.config(command=Start)
btn.place(x=(winWidth)/2-5*12,y=winHeight-50)

ScoreLabel = tk.Label(win,text='Score')
ScoreLabel.pack()

QuestionLabel = tk.Label(win,text='Start New Game')
QuestionLabel.pack()

AnswerEntry = tk.Entry(win,text='Answer')
AnswerEntry.bind("<Return>", Answer)
AnswerEntry.pack()
AnswerEntry.config(state=tk.DISABLED)

win.mainloop()