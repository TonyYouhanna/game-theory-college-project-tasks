from tkinter import *
from tkinter import Radiobutton
from tkinter import messagebox
from statistics import mean

main = Tk()
main.title("Task 2")
number_of_player1_moves_value = IntVar()
number_of_player1_moves_textbox = Entry(main, textvariable=number_of_player1_moves_value)
number_of_player1_moves_Label = Label(main, text="Enter number of moves for player 1:")
number_of_player1_moves_Label.grid(row=1, column=0)
number_of_player1_moves_textbox.grid(row=1, column=1)
number_of_player2_moves_Label = Label(main, text="Enter number of moves for player 2:")
number_of_player2_moves_Label.grid(row=1, column=2)
number_of_player2_moves_value = IntVar()
number_of_player2_moves_textbox = Entry(main, textvariable=number_of_player2_moves_value)
number_of_player2_moves_textbox.grid(row=1, column=3)
be_zerosum_bool = IntVar(main, value=2)
zerosum_RB = Radiobutton(main, text="zerosum", variable=be_zerosum_bool, value=1)
non_zerosum_RB = Radiobutton(main, text="non-zerosum", variable=be_zerosum_bool, value=0)
zerosum_RB.grid(row=0, column=1)
non_zerosum_RB.grid(row=0, column=2)
payoff_entries = []


def take():
    minimum_payoffs11 = []
    minimum_payoffs21 = []
    minimum_payoffs12 = []
    minimum_payoffs22 = []
    if be_zerosum_bool.get() == 1:
        for i in range(int(number_of_player1_moves_value.get())):
            payoffs = []
            for j in range(int(number_of_player2_moves_value.get())):
                payoffs.append(payoff_entries[i][j].get())
            minimum_payoffs11.append(min(payoffs))
        player1_minmaxLabel = Label(main, text="Minmax payoff for player 1:")
        player1_minmaxLabel.grid(row=number_of_player1_moves_value.get() + 5, column=0)
        player1_minmaxText = IntVar()
        player1_minmaxTextbox = Entry(main, textvariable=player1_minmaxText)
        player1_minmaxTextbox.grid(row=number_of_player1_moves_value.get() + 5, column=1)
        player1_minmaxText.set(max(minimum_payoffs11))
        player1_moveLabel = Label(main, text="when he/she plays move")
        player1_moveLabel.grid(row=number_of_player1_moves_value.get() + 5, column=2)
        player1_moveValue = IntVar()
        player1_moveTextbox = Entry(main, textvariable=player1_moveValue)
        player1_moveTextbox.grid(row=number_of_player1_moves_value.get() + 5, column=3)
        player1_moveValue.set(minimum_payoffs11.index(max(minimum_payoffs11)) + 1)
        player2_indices = []
        for i in range(int(number_of_player1_moves_value.get())):
            br_list = []
            for j in range(int(number_of_player2_moves_value.get())):
                br_list.append(payoff_entries[i][j].get() * -1)
            player2_BrLabel = Label(main, text="Player 2 best response for player 1 move")
            player2_BrLabel.grid(row=number_of_player1_moves_value.get() + i + 7, column=0)
            player2_BrText = IntVar()
            player2_BrTextbox = Entry(main, textvariable=player2_BrText)
            player2_BrTextbox.grid(row=number_of_player1_moves_value.get() + i + 7, column=1)
            player2_BrText.set(i + 1)
            player2_BrText2 = IntVar()
            player2_BrTextbox2 = Entry(main, textvariable=player2_BrText2)
            player2_BrTextbox2.grid(row=number_of_player1_moves_value.get() + i + 7, column=2)
            player2_BrText2.set(br_list.index(max(br_list)) + 1)
            player2_BrLabel2 = Label(main, text="with payoff")
            player2_BrLabel2.grid(row=number_of_player1_moves_value.get() + i + 7, column=3)
            player2_BrText3 = IntVar()
            player2_BrTextbox3 = Entry(main, textvariable=player2_BrText3)
            player2_BrTextbox3.grid(row=number_of_player1_moves_value.get() + i + 7, column=4)
            player2_BrText3.set(max(br_list))
            player2_indices.append(str(i) + str(br_list.index(max(br_list))))
        for i in range(int(number_of_player2_moves_value.get())):
            payoffs = []
            for j in range(int(number_of_player1_moves_value.get())):
                payoffs.append(payoff_entries[j][i].get() * -1)
            minimum_payoffs21.append(min(payoffs))
        player2_minmaxLabel = Label(main, text="Minmax payoff for player 2:")
        player2_minmaxLabel.grid(row=number_of_player1_moves_value.get() + 6, column=0)
        player2_minmaxText = IntVar()
        player2_minmaxTextbox = Entry(main, textvariable=player2_minmaxText)
        player2_minmaxTextbox.grid(row=number_of_player1_moves_value.get() + 6, column=1)
        player2_minmaxText.set(max(minimum_payoffs21))
        player2_moveLabel = Label(main, text="when he/she plays move")
        player2_moveLabel.grid(row=number_of_player1_moves_value.get() + 6, column=2)
        player2_moveValue = IntVar()
        player2_moveTextbox = Entry(main, textvariable=player2_moveValue)
        player2_moveTextbox.grid(row=number_of_player1_moves_value.get() + 6, column=3)
        player2_moveValue.set(minimum_payoffs21.index(max(minimum_payoffs21)) + 1)
        player1_indices = []
        for i in range(int(number_of_player2_moves_value.get())):
            br_list2 = []
            for j in range(int(number_of_player1_moves_value.get())):
                br_list2.append(payoff_entries[j][i].get())
            player1_BrLabel = Label(main, text="Player 1 best response for player 2 move")
            player1_BrLabel.grid(row=number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + i + 8,
                                 column=0)
            player1_BrText = IntVar()
            player1_BrTextbox = Entry(main, textvariable=player1_BrText)
            player1_BrTextbox.grid(
                row=number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + i + 8, column=1)
            player1_BrText.set(i + 1)
            player1_BrText2 = IntVar()
            player1_BrTextbox2 = Entry(main, textvariable=player1_BrText2)
            player1_BrTextbox2.grid(
                row=number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + i + 8, column=2)
            player1_BrText2.set(br_list2.index(max(br_list2)) + 1)
            player1_BrLabel2 = Label(main, text="with payoff")
            player1_BrLabel2.grid(row=number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + i + 8,
                                  column=3)
            player1_BrText3 = IntVar()
            player1_BrTextbox3 = Entry(main, textvariable=player1_BrText3)
            player1_BrTextbox3.grid(
                row=number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + i + 8, column=4)
            player1_BrText3.set(max(br_list2))
            player1_indices.append(str(br_list2.index(max(br_list2))) + str(i))
        k = 0
        common = 0
        for i in player1_indices:
            if i in player2_indices:
                common = 1
                nash_Label = Label(main, text="Nash equilibrium occurs when player 1 plays move")
                nash_Label.grid(
                    row=number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + k + 9,
                    column=0)
                player1_nashText = IntVar()
                player1_nashTextbox = Entry(main, textvariable=player1_nashText)
                player1_nashTextbox.grid(
                    row=number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + k + 9,
                    column=1)
                player1_nashText.set(int(i[0]) + 1)
                nash_Label2 = Label(main, text="and player 2 plays move")
                nash_Label2.grid(
                    row=number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + k + 9,
                    column=2)
                player2_nashText = IntVar()
                player2_nashTextbox = Entry(main, textvariable=player2_nashText)
                player2_nashTextbox.grid(
                    row=number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + k + 9,
                    column=3)
                player2_nashText.set(int(i[1]) + 1)
                k += 1
        if (not common):
            no_nash_Label = Label(main, text="There is no nash equilibrium")
            no_nash_Label.grid(
                row=number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + k + 9,
                column=0)




    elif be_zerosum_bool.get() == 0:
        for i in range(int(number_of_player1_moves_value.get())):
            payoffs1 = []
            for j in range(int(number_of_player2_moves_value.get())):
                payoffs1.append(int(payoff_entries[i][j].get().split()[0]))
            minimum_payoffs12.append(min(payoffs1))
        player1_minmaxLabel = Label(main, text="Minmax payoff for player 1:")
        player1_minmaxLabel.grid(row=number_of_player1_moves_value.get() + 5, column=0)
        player1_minmaxText = IntVar()
        player1_minmaxTextbox = Entry(main, textvariable=player1_minmaxText)
        player1_minmaxTextbox.grid(row=number_of_player1_moves_value.get() + 5, column=1)
        player1_minmaxText.set(max(minimum_payoffs12))
        player1_moveLabel = Label(main, text="when he/she plays move")
        player1_moveLabel.grid(row=number_of_player1_moves_value.get() + 5, column=2)
        player1_moveValue = IntVar()
        player1_moveTextbox = Entry(main, textvariable=player1_moveValue)
        player1_moveTextbox.grid(row=number_of_player1_moves_value.get() + 5, column=3)
        player1_moveValue.set(minimum_payoffs12.index(max(minimum_payoffs12)) + 1)
        player2_indices = []
        for i in range(int(number_of_player1_moves_value.get())):
            br_list = []
            for j in range(int(number_of_player2_moves_value.get())):
                br_list.append(int(payoff_entries[i][j].get().split()[1]))
            player2_BrLabel = Label(main, text="Player 2 best response for player 1 move")
            player2_BrLabel.grid(row=number_of_player1_moves_value.get() + i + 7, column=0)
            player2_BrText = IntVar()
            player2_BrTextbox = Entry(main, textvariable=player2_BrText)
            player2_BrTextbox.grid(row=number_of_player1_moves_value.get() + i + 7, column=1)
            player2_BrText.set(i + 1)
            player2_BrText2 = IntVar()
            player2_BrTextbox2 = Entry(main, textvariable=player2_BrText2)
            player2_BrTextbox2.grid(row=number_of_player1_moves_value.get() + i + 7, column=2)
            player2_BrText2.set(br_list.index(max(br_list)) + 1)
            player2_BrLabel2 = Label(main, text="with payoff")
            player2_BrLabel2.grid(row=number_of_player1_moves_value.get() + i + 7, column=3)
            player2_BrText3 = IntVar()
            player2_BrTextbox3 = Entry(main, textvariable=player2_BrText3)
            player2_BrTextbox3.grid(row=number_of_player1_moves_value.get() + i + 7, column=4)
            player2_BrText3.set(max(br_list))
            player2_indices.append(str(i) + str(br_list.index(max(br_list))))
        for i in range(int(number_of_player2_moves_value.get())):
            payoffs2 = []
            for j in range(int(number_of_player1_moves_value.get())):
                payoffs2.append(int(payoff_entries[j][i].get().split()[1]))
            minimum_payoffs22.append(min(payoffs2))
        player2_minmaxLabel = Label(main, text="Minmax payoff for player 2:")
        player2_minmaxLabel.grid(row=number_of_player1_moves_value.get() + 6, column=0)
        player2_minmaxText = IntVar()
        player2_minmaxTextbox = Entry(main, textvariable=player2_minmaxText)
        player2_minmaxTextbox.grid(row=number_of_player1_moves_value.get() + 6, column=1)
        player2_minmaxText.set(max(minimum_payoffs22))
        player2_moveLabel = Label(main, text="when he/she plays move")
        player2_moveLabel.grid(row=number_of_player1_moves_value.get() + 6, column=2)
        player2_moveValue = IntVar()
        player2_moveTextbox = Entry(main, textvariable=player2_moveValue)
        player2_moveTextbox.grid(row=number_of_player1_moves_value.get() + 6, column=3)
        player2_moveValue.set(minimum_payoffs22.index(max(minimum_payoffs22)) + 1)
        player1_indices = []
        for i in range(int(number_of_player2_moves_value.get())):
            br_list2 = []
            for j in range(int(number_of_player1_moves_value.get())):
                br_list2.append(int(payoff_entries[j][i].get().split()[0]))
            player1_BrLabel = Label(main, text="Player 1 best response for player 2 move")
            player1_BrLabel.grid(row=number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + i + 8,
                                 column=0)
            player1_BrText = IntVar()
            player1_BrTextbox = Entry(main, textvariable=player1_BrText)
            player1_BrTextbox.grid(
                row=number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + i + 8, column=1)
            player1_BrText.set(i + 1)
            player1_BrText2 = IntVar()
            player1_BrTextbox2 = Entry(main, textvariable=player1_BrText2)
            player1_BrTextbox2.grid(
                row=number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + i + 8, column=2)
            player1_BrText2.set(br_list2.index(max(br_list2)) + 1)
            player1_BrLabel2 = Label(main, text="with payoff")
            player1_BrLabel2.grid(row=number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + i + 8,
                                  column=3)
            player1_BrText3 = IntVar()
            player1_BrTextbox3 = Entry(main, textvariable=player1_BrText3)
            player1_BrTextbox3.grid(
                row=number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + i + 8, column=4)
            player1_BrText3.set(max(br_list2))
            player1_indices.append(str(br_list2.index(max(br_list2))) + str(i))
        k = 0
        common = 0
        for i in player1_indices:
            if i in player2_indices:
                common = 1
                nash_Label = Label(main, text="Nash equilibrium occurs when player 1 plays move")
                nash_Label.grid(
                    row=number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + k + 9,
                    column=0)
                player1_nashText = IntVar()
                player1_nashTextbox = Entry(main, textvariable=player1_nashText)
                player1_nashTextbox.grid(
                    row=number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + k + 9,
                    column=1)
                player1_nashText.set(int(i[0]) + 1)
                nash_Label2 = Label(main, text="and player 2 plays move")
                nash_Label2.grid(
                    row=number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + k + 9,
                    column=2)
                player2_nashText = IntVar()
                player2_nashTextbox = Entry(main, textvariable=player2_nashText)
                player2_nashTextbox.grid(
                    row=number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + k + 9,
                    column=3)
                player2_nashText.set(int(i[1]) + 1)
                k += 1
        if (not common):
            no_nash_Label = Label(main, text="There is no nash equilibrium")
            no_nash_Label.grid(
                row=number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + number_of_player1_moves_value.get() + k + 9,
                column=0)


def payoff_matrix():
    global payoff_entries
    if be_zerosum_bool.get() != 0 and be_zerosum_bool.get() != 1:
        messagebox.showerror("Error", "You have to choose the type of the game")
    elif be_zerosum_bool.get() == 1:
        payoff_label = Label(main, text="Payoffs:")
        payoff_label.grid(row=3, column=0)
        for i in range(int(number_of_player1_moves_value.get())):
            row = []
            for j in range(int(number_of_player2_moves_value.get())):
                e_value = IntVar()
                e = Entry(main, textvariable=e_value)
                e.grid(row=i + 4, column=j + 1)
                row.append(e_value)
            payoff_entries.append(row)
    elif be_zerosum_bool.get() == 0:
        payoff_label = Label(main,
                             text="Payoffs (Enter the payoffs of players 1 & 2 in a textbox with space between them):")
        payoff_label.grid(row=3, column=0)
        for i in range(int(number_of_player1_moves_value.get())):
            row = []
            for j in range(int(number_of_player2_moves_value.get())):
                e_value = StringVar()
                e = Entry(main, textvariable=e_value)
                e.grid(row=i + 4, column=j + 1)
                row.append(e_value)
            payoff_entries.append(row)


payoff_matrix = Button(main, text="Payoff Matrix", command=payoff_matrix)
payoff_matrix.grid(row=0, column=3)
Result = Button(main, text="Result", command=take)
Result.grid(row=0, column=4)
mainloop()
