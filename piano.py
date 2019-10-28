import vlc
import time
from tkinter import * 
from PIL import Image, ImageTk
import PIL
from collections import deque
notesWhite = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
notesBlack = ['C#', 'D#', '-', 'F#', 'G#', 'A#', '-']
notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G','G#', 'A', 'A#', 'B']
amountOfNotes = 61
curMel = []
playerMel = deque()

from random import randint

def generateMelody():
	global numOfNotes
	global curMel
	print("I am here to generate")
	n = int(numOfNotes.get())
	begOfMel = randint(0, amountOfNotes - 9)
	mel = []
	for i in range(n):
		mel.append(randint(begOfMel, begOfMel + 9))
	print(list(map(lambda x : str(x // 12 + 1) + 'o' + notes[x % 12], mel)))
	curMel = list(map(lambda x : str(x // 12 + 1) + 'o' + notes[x % 12], mel))

def playMel():
	global curMel, lenInterval
	for i in curMel:
		p = vlc.MediaPlayer('notes/' + i + ".mp3")
		p.play()
		time.sleep(float(lenInterval.get()))


def isDigit(char):
	print(char)
	return char.isdigit()


def checkMel():
	global curMel, playerMel
	global greatLabel, imgGreat
	while(len(curMel) < len(playerMel)):
		playerMel.popleft()
	print(curMel, list(playerMel))
	if curMel == list(playerMel):
		greatLabel.configure(image=imgGreat)

def callback(event):
    global panel
    global notesWhite, notesBlack, root, greatLabel
    greatLabel.configure(image='')
    #print([method_name for method_name in dir(panel) if callable(getattr(panel, method_name))])
    #print ("clicked at", event.x, event.y, panel.winfo_x())

    numWhite = (event.x - panel.winfo_x() - 13) // 34
    numBlack = (event.x - panel.winfo_x() - 36) // 34
    print(numWhite, numBlack, panel.winfo_y())
    x = 0
#    print(event.y, panel.winfo_y())
    if (event.y < 132 and (event.x - panel.winfo_x() - 36) % 34 < 20 and notesBlack[numBlack % 7] != '-'):
    	x = str(numBlack // 7 + 1) + 'o' + notesBlack[numBlack % 7]
    else:
    	x = str(numWhite // 7 + 1) + 'o' + notesWhite[numWhite % 7]
    print(x)
    playerMel.append(x)
    p = vlc.MediaPlayer("notes/" + x + ".mp3")
    p.play()
    checkMel()
    return x



root = Tk()
root.geometry("1248x500")
img = Image.open("great.png")
img.thumbnail((200, 200))
imgPiano = ImageTk.PhotoImage(Image.open("pianoStup.png"))
imgGreat = ImageTk.PhotoImage(img)

greatLabel = Label(root, anchor="center", image='')
greatLabel.place(relx=0.5, y=400, width=200, height=200, anchor="center")

labelInterval = Label(root, text="Length of interval")
labelInterval.place(x=10, y=40)

lenInterval = StringVar()
lenInterval.set("0.5")
entryInterval = Entry(root, validate="key", vcmd=(root.register(isDigit), "%S"), textvariable=lenInterval)
entryInterval.place(x=130, y=40, width="30")

labelNotes = Label(root, text="Number of notes")
labelNotes.place(x=10, y=10)

numOfNotes = StringVar()
numOfNotes.set("1")
entryNotes = Entry(root, validate="key", vcmd=(root.register(isDigit), "%S"), textvariable=numOfNotes)
entryNotes.place(x=130, y=10, width="30")




buttonGenerate = Button(root, text="Generate", command=generateMelody)
buttonGenerate.place(y=30, relx=0.5, anchor="center")

buttonPlay = Button(root, text="Play", command=playMel)
buttonPlay.place(y=70, relx=0.5, anchor="center")




panel = Label(root, image=imgPiano)
panel.img = imgPiano
panel.bind("<Button-1>", callback)
panel.place(x=0, y = 100)




root.mainloop()

#padx = 13px
#whiteLength = 34
#blackLength = 20
