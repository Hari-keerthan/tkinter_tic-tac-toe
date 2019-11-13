import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.title("tic tac toe")

global bclick,drw
blclick = True
drw = 1

btn1 = tk.Button(window,text='',fg='black', height=3, width=15 , command = lambda : btnclick(btn1)) 
btn1.grid(column=0,row=1)
btn2 = tk.Button(window,text='',fg='black', height=3, width=15, command = lambda  : btnclick(btn2)) 
btn2.grid(column=1,row=1)  
btn3 = tk.Button(window,text='',fg='black', height=3, width=15, command = lambda : btnclick(btn3)) 
btn3.grid(column=2,row=1)  
btn4 = tk.Button(window,text='',fg='black', height=3, width=15, command = lambda : btnclick(btn4)) 
btn4.grid(column=0,row=2)
btn5 = tk.Button(window,text='',fg='black', height=3, width=15, command = lambda : btnclick(btn5)) 
btn5.grid(column=1,row=2)  
btn6 = tk.Button(window,text='',fg='black', height=3, width=15, command = lambda : btnclick(btn6)) 
btn6.grid(column=2,row=2)  
btn7 = tk.Button(window,text='',fg='black', height=3, width=15, command = lambda  : btnclick(btn7)) 
btn7.grid(column=0,row=3)  
btn8 = tk.Button(window,text='',fg='black', height=3, width=15, command = lambda  : btnclick(btn8)) 
btn8.grid(column=1,row=3)  
btn9 = tk.Button(window,text='',fg='black', height=3, width=15, command = lambda  : btnclick(btn9)) 
btn9.grid(column=2,row=3)

def reset():
    global bclick,drw
    btn1['text'] = ''
    btn2['text'] = ''
    btn3['text'] = ''
    btn4['text'] = ''
    btn5['text'] = ''
    btn6['text'] = ''
    btn7['text'] = ''
    btn8['text'] = ''
    btn9['text'] = ''
    bclick = True
    lbl = tk.Label(window, text='Player 1 turn')
    lbl.grid(column = 1 , row = 6)
    drw = 1
    lbl = tk.Label(window, text='                     ')
    lbl.grid(column = 2 , row = 6)
    lbl = tk.Label(window, text='                     ')
    lbl.grid(column = 2 , row = 8)
    butt_chnge_state('active')

def chkwin(): 
    print(btn1['text'])
    if(	btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X' or 
	btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X' or  
	btn7['text'] == 'X' and btn8['text'] == 'X' and btn9['text'] == 'X' or  
	btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X' or  
	btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X' or  
	btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X' or  
	btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X' or  
	btn3['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X'):
        lbl = tk.Label(window, text='player 1 won')
        lbl.grid(column = 2 , row = 6)
        lbl = tk.Label(window, text='player 2 lost')
        lbl.grid(column = 2 , row = 8)
        butt_chnge_state('disable')
    elif (btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O' or 
	btn4['text'] == 'O' and btn5['text'] == 'O' and btn6['text'] == 'O' or  
	btn7['text'] == 'O' and btn8['text'] == 'O' and btn9['text'] == 'O' or  
	btn1['text'] == 'O' and btn5['text'] == 'O' and btn9['text'] == 'O' or  
	btn3['text'] == 'O' and btn5['text'] == 'O' and btn7['text'] == 'O' or  
	btn1['text'] == 'O' and btn4['text'] == 'O' and btn7['text'] == 'O' or  
	btn2['text'] == 'O' and btn5['text'] == 'O' and btn8['text'] == 'O' or  
	btn3['text'] == 'O' and btn6['text'] == 'O' and btn9['text'] == 'O'):
        lbl = tk.Label(window, text='player 2 won')
        lbl.grid(column = 2 , row = 6)
        lbl = tk.Label(window, text='player 1 lost')
        lbl.grid(column = 2 , row = 8)
        butt_chnge_state('disable')
    else :
        if drw == 10:
            lbl = tk.Label(window, text='its a draw')
            lbl.grid(column = 2 , row = 6)
            butt_chnge_state('disable')
                
def butt_chnge_state(x):
    btn1['state'] = x
    btn2['state'] = x
    btn3['state'] = x
    btn4['state'] = x
    btn5['state'] = x
    btn6['state'] = x
    btn7['state'] = x
    btn8['state'] = x
    btn9['state'] = x
    



def btnclick(butt):
    global bclick,drw
    if butt['text'] == '' and bclick == True:
            butt['text'] = 'X'
            bclick = False
            lbl = tk.Label(window, text='Player 2 turn')
            lbl.grid(column = 1 , row = 6)
            drw = drw + 1
            chkwin()
    elif butt['text'] == '' and bclick == False:
            butt['text'] = 'O'
            bclick = True
            lbl = tk.Label(window, text='Player 1 turn')
            lbl.grid(column = 1 , row = 6)
            drw = drw + 1
            chkwin()
    else:
        messagebox.showinfo('tic tac toe','button already pressed')

 
        


lbl = tk.Label(window, text ='tic tac toe',font=('',30))
lbl.grid(column = 1 , row =0)
lbl = tk.Label(window, text='Player 1 turn')
lbl.grid(column = 1 , row = 6)
playr_won = tk.Label(window, text='')
playr_won.grid(column = 2 , row = 6)
playr_loss = tk.Label(window, text='')
playr_loss.grid(column = 2 , row = 8)
player1 = tk.Label(window, text='player1 - X')
player1.grid(column = 0 , row = 6)
player1 = tk.Label(window, text='player2 - O')
player1.grid(column = 0 , row = 8)

btn_reset = tk.Button(window,text = 'reset game',command=lambda : reset())
btn_reset.grid(column=1,row=10)

window.mainloop()

