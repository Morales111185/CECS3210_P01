import random 
import graphics
from graphics import *


while True:
    
    win = GraphWin('Shapes',1000,1000)
    label = Text(Point(497.0, 140.0),"Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")
    label.draw(win)
    label_1 = Text(Point(485.0, 230.0),"Enter the number of your selection \n 1. Rock \n 2. paper \n 3. scissor \n") 
    label_1.draw(win)
    rock= Rectangle(Point(338.0, 291.0),Point(414.0, 352.0))
    rock.setFill("red")
    rock.draw(win)
    paper = Rectangle(Point(444.0, 293.0),Point(518.0, 355.0))
    paper.setFill("yellow")
    paper.draw(win)
    scissors = Rectangle(Point(552.0, 294.0),Point(646.0, 354.0))
    scissors.setFill("green")
    scissors.draw(win)
    label_X = Text(Point(375.0, 321.0),"ROCK")
    label_X.draw(win)
    label_Y = Text(Point(480.0, 325.0),"PAPER")
    label_Y.draw(win)
    label_Z = Text(Point(598.0, 319.0),"SCISSORS")
    label_Z.draw(win)
    choice_get = win.getKey()
    choice = choice_get
    label_2 = Text(Point(488.0, 227.0),"Users turn")
    label_2.draw(win)
    
    if choice == '1': 
        choice_name = 'Rock'
    elif choice == '2': 
        choice_name = 'Paper'
    else: 
        choice_name = 'Scissors'
          
    win.close()
    win = GraphWin('Shapes',1000,1000)
    label = Text(Point(497.0, 45.0),"Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")
    label.draw(win)
    label_2 = Text(Point(488.0, 145.0),"Users turn: " + choice)
    label_2.draw(win)
    label_3 = Text(Point(485.0, 227.0),"Users choice is "+ choice_name)
    label_3.draw(win)
    if choice == '1': 
       square = Rectangle(Point(427.0, 264.0),Point(538.0, 329.0))
       square.setFill("red")
       square.draw(win)
       label_Q = Text(Point(478.0, 301.0),"ROCK")
       label_Q.draw(win)
    elif choice == '2': 
        square = Rectangle(Point(427.0, 264.0),Point(538.0, 329.0))
        square.setFill("yellow")
        square.draw(win)
        label_Q = Text(Point(478.0, 301.0),"PAPER")
        label_Q.draw(win)
    else: 
        square = Rectangle(Point(427.0, 264.0),Point(538.0, 329.0))
        square.setFill("green")
        square.draw(win)
        label_Q = Text(Point(478.0, 301.0),"SCISSORS")
        label_Q.draw(win)
    label_4 = Text(Point(479.0, 354.0),"\nNow its the computers turn......")
    label_4.draw(win) 
  
  
    comp_choice = random.randint(1, 3) 
      
 
    while comp_choice == choice: 
        comp_choice = random.randint(1, 3) 
  
    if comp_choice == 1: 
        comp_choice_name = 'Rock'
    elif comp_choice == 2: 
        comp_choice_name = 'Paper'
    else: 
        comp_choice_name = 'Scissors'
    label_5 = Text(Point(473.0, 396.0),"Computers choice is: "+comp_choice_name)
    label_5.draw(win)
    if comp_choice == 1: 
       square2 = Rectangle(Point(432.0, 441.0),Point(534.0, 505.0))
       square2.setFill("red")
       square2.draw(win)
       label_W = Text(Point(482.0, 471.0),"ROCK")
       label_W.draw(win)
    elif comp_choice == 2: 
        square2 = Rectangle(Point(432.0, 441.0),Point(534.0, 505.0))
        square2.setFill("yellow")
        square2.draw(win)
        label_W = Text(Point(482.0, 471.0),"PAPER")
        label_W.draw(win)
    else: 
        square2 = Rectangle(Point(432.0, 441.0),Point(534.0, 505.0))
        square2.setFill("green")
        square2.draw(win)
        label_W = Text(Point(482.0, 471.0),"SCISSORS")
        label_W.draw(win)
    label_6 = Text(Point(484.0, 530.0),choice_name + ' V/S ' + comp_choice_name)
    label_6.draw(win)
    if((choice == '1' and comp_choice == 2) or
      (choice == '2' and comp_choice ==1 )):
        label_7 = Text(Point(486.0, 585.0),"Paper Wins!")
        label_7.draw(win)
        result = "Paper"
          
    elif((choice == '1' and comp_choice == 3) or
        (choice == '3' and comp_choice == 1)):
        label_8 = Text(Point(486.0, 585.0),"Rock Wins!")
        label_8.draw(win)
        result = "Rock"
    else:
        if ((choice == '1' and comp_choice == 1) or
        (choice == '2' and comp_choice == 2) or (choice == '3' and comp_choice == 3)):
            label_9 = Text(Point(486.0, 585.0),"Its a Draw!")
            label_9.draw(win)
        else:
             label_9 = Text(Point(486.0, 585.0),"Scissors Win!")
             label_9.draw(win)
             result = "Scissor"
       
  
   
    if result == choice_name:
         label_10 = Text(Point(486.0, 650.0),"User Wins!")
         label_10.draw(win)
    elif result == comp_choice_name:
        label_11 = Text(Point(486.0, 650.0),"Computer Wins")
        label_11.draw(win) 
    else:
        label_13 = Text(Point(486.0, 650.0),"No winner this round!")
        label_13.draw(win)
        
              
          
    label_12 = Text(Point(488.0, 694.0),"Do you want to play again? (Y/N)")
    label_12.draw(win)
    ans_get = win.getKey()
    win.close()
  
  
 
    if ans_get == 'n' or ans_get == 'N': 
        win.close()
        break
      
win = GraphWin('Shapes',1000,1000)
label_13 = Text(Point(500,400),"\nTHANKS FOR PLAYING")
label_13.draw(win)
 
