from locale import str
from tkinter import *
from functools import partial
import random
from statistics import mean

main = Tk()
main.geometry("480x800")
main.title("Repeated Prisoner Dilemma")
u = Label(main, text="You")
u.place(x=10, y=100)
opponent = Label(main, text="Opponent")
opponent.place(x=200, y=25)
opponent_cooperate = Label(main, text="Cooperate")
opponent_cooperate.place(x=100, y=45)
opponent_defect = Label(main, text="Defect")
opponent_defect.place(x=300, y=45)
coop_coop = Label(main, text="20, 20")
coop_coop.place(x=100, y=70)
coop_def = Label(main, text="0, 30")
coop_def.place(x=300, y=70)
def_coop = Label(main, text="30, 0")
def_coop.place(x=100, y=120)
def_def = Label(main, text="10, 10")
def_def.place(x=300, y=120)
yourPayoff = Label(main, text="Your Payoff")
yourPayoff.place(x=100, y=300)
opponentPayoff = Label(main, text="Opponent's Payoff")
opponentPayoff.place(x=300, y=300)
roundLabel = Label(main, text="Round")
roundLabel.place(x=10, y=350)
average = Label(main, text="Average:")
average.place(x=10, y=400)
totalAvg = Label(main, text="Total Average:")
totalAvg.place(x=10, y=450)
yourValue = IntVar()
opponentValue = IntVar()
yourAverage = StringVar()
OpponentAverage = StringVar()
yourTotalAverage = StringVar()
opponentTotalAverage = StringVar()
yourTextbox = Entry(main, textvariable=yourValue)
opponentTextbox = Entry(main, textvariable=opponentValue)
yourAvgTextbox = Entry(main, textvariable=yourAverage)
opponentAvgTextbox = Entry(main, textvariable=OpponentAverage)
yourTotalAvgTextbox = Entry(main, textvariable=yourTotalAverage)
opponentTotalAvgTextbox = Entry(main, textvariable=opponentTotalAverage)
yourTextbox.place(x=100, y=350)
opponentTextbox.place(x=300, y=350)
yourAvgTextbox.place(x=100, y=400)
opponentAvgTextbox.place(x=300, y=400)
yourTotalAvgTextbox.place(x=100, y=450)
opponentTotalAvgTextbox.place(x=300, y=450)
i = 1
j = 1
yourAvgList = []
yourTotalAvgList = []
opponentAvgList = []
opponentTotalAvgList = []
opponentNumber = IntVar()
opponentNumber.set(i)
opponentNumberTextbox = Entry(main, textvariable=opponentNumber, width=6)
opponentNumberTextbox.place(x=300, y=25)
roundNumber = IntVar()
roundNumber.set(j)
roundNumberTextbox = Entry(main, textvariable=roundNumber, width=6)
roundNumberTextbox.place(x=10, y=375)


def cooperate_or_defect(x):
    global i
    global j
    global yourAvgList
    global yourTotalAvgList
    global opponentAvgList
    global opponentTotalAvgList
    list1 = [20, 30]
    list2 = [0, 10]
    if x == 1:
        payoff = random.choice(list1)
        if payoff == 20:
            y = 20
            opponentValue.set(payoff)

        else:
            y = 0
            opponentValue.set(payoff)
    elif x == 2:
        payoff = random.choice(list2)
        if payoff == 0:
            y = 30
            opponentValue.set(payoff)
        else:
            y = 10
            opponentValue.set(payoff)
    yourValue.set(y)
    yourAvgList.append(y)
    opponentAvgList.append(payoff)
    if j == 25:
        yourAverage.set(str(mean(yourAvgList)))
        OpponentAverage.set(str(mean(opponentAvgList)))
        yourTotalAvgList.append(mean(yourAvgList))
        opponentTotalAvgList.append(mean(opponentAvgList))
        if i == 5:
            yourTotalAverage.set(str(mean(yourTotalAvgList)))
            opponentTotalAverage.set(str(mean(opponentTotalAvgList)))
            j = -1
        else:
            yourAvgList.clear()
            opponentAvgList.clear()
            j = 0
            i += 1
            opponentNumber.set(i)
    j += 1
    roundNumber.set(j)


cooperateButton = Button(main, text="Cooperate", command=partial(cooperate_or_defect, 1))
cooperateButton.place(x=22, y=70)
defectButton = Button(main, text="Defect", command=partial(cooperate_or_defect, 2))
defectButton.place(x=22, y=120)
mainloop()
