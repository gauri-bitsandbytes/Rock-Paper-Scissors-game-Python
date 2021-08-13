# GUI VERSION OF ROCK PAPER SCISSORS GAME

from tkinter import *
from PIL import Image, ImageTk
from random import randint

# pip install PILLOW (in console)

# main window
root = Tk()
root.title("Rock Paper Scissors")
root.configure(background="cyan")


# giving link for picture
rock_img_player1 = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_player1 = ImageTk.PhotoImage(Image.open("paper.png"))
scissors_img_player1 = ImageTk.PhotoImage(Image.open("scissors.png"))
rock_img_player2 = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_player2 = ImageTk.PhotoImage(Image.open("paper.png"))
scissors_img_player2 = ImageTk.PhotoImage(Image.open("scissors.png"))


# insert picture
player1_label = Label(root, image=rock_img_player1, bg="cyan")
player2_label = Label(root, image=rock_img_player2, bg="cyan")
player1_label.grid(row=1, column=0)
player2_label.grid(row=1, column=4)


# scores
player1_score = Label(root, text=0, font=100, bg="cyan")
player2_score = Label(root, text=0, font=100, bg="cyan")
player1_score.grid(row=1, column=1)
player2_score.grid(row=1, column=3)


# indicators
player1_indicator = Label(root, font=50, text="COMPUTER", bg="cyan")
player2_indicator = Label(root, font=50, text="USER", bg="cyan")
player1_indicator.grid(row=0, column=1)
player2_indicator.grid(row=0, column=3)


# messages
msg = Label(root, font=50, bg="cyan")
msg.grid(row=3, column=2)


# buttons
rock = Button(root, width=20, height=2, text="ROCK", bg="blue",
              command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER", bg="red",
               command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissors = Button(root, width=20, height=2, text="SCISSORS", bg="green",
                  command=lambda: updateChoice("scissors")).grid(row=2, column=3)

# list of 3 options
choices = ["rock","paper","scissors"]

# function to change the images 
def updateChoice(x):

#for player1 (comp)
    player1_choice = choices[randint(0,2)]
    if player1_choice == "rock":
        player1_label.configure(image=rock_img_player1)
    elif player1_choice == "paper":
        player1_label.configure(image=paper_img_player2)
    else:
        player1_label.configure(image=scissors_img_player1)


# for player 2
    if x == "rock":
        player2_label.configure(image=rock_img_player2)
    elif x == "paper":
        player2_label.configure(image=paper_img_player2)
    else:
        player2_label.configure(image=scissors_img_player2)
    
    checkWinner(x, player1_choice)


# update message
def updateMessage(x):
    msg['text'] = x


# updating player1 score (comp)
def update_player1_score():
    player_score = int(player1_score["text"])
    player_score += 1
    player1_score["text"] = str(player_score)
    
    
# updating player2 score
def update_player2_score():
    player_score = int(player2_score["text"])
    player_score += 1
    player2_score["text"] = str(player_score)


# checking which player gets points
def checkWinner(player,computer):
    if player == computer:
        updateMessage("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("Computer gets +1")
            update_player1_score()
        else:
            updateMessage("Player gets +1")
            update_player1_score()

    elif player == "paper":
        if computer == "scissors":
            updateMessage("Computer gets +1")
            update_player1_score()
        else:
            updateMessage("Player gets +1")
            update_player2_score()

    elif player == "scissors":
        if computer == "rock":
            updateMessage("Computer gets +1")
            update_player1_score()
        else:
            updateMessage("Player gets +1")
            update_player2_score()

root.mainloop()
