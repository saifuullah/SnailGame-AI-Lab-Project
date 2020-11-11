import arcade
import random
import os

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)


snail1 = arcade.load_texture("snail_1.png")
snail2 = arcade.load_texture("snail_2.png")
back = arcade.load_texture("back.jpg")
sp1 = arcade.load_texture("splashes.png")
sp2 = arcade.load_texture("splash2.png")
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
MARGIN = 5
boxSize = SCREEN_HEIGHT // 10 

class Game(arcade.View):
    def __init__(self):
        super().__init__()
        self.board = []
        self.human = 1
        self.bot = 2
        self.turn = "HUMAN"
        self.win = "0"
        self.state = "GameMenu"
        self.botScore = 0
        self.humanScore = 0
        self.initilizeBoard(10, 10)


    #Function for initilization of backend 2D board array
    def initilizeBoard(self, rows, cols):
        for i in range(cols):
            tempBoard = []
            for i in range(0, rows):
                tempBoard.append(0)
            self.board.append(tempBoard)
        self.board[0][9] = 2
        self.board[9][0] = 1




    def on_key_press(self, key, modifiers):
        if self.state == "GameMenu":
            if key:
                self.human = 1
                self.bot = 2
                self.state = "GameInstruction"
        elif self.state == "GameInstruction":
            if key == arcade.key.SPACE:
                self.human = 1
                self.bot = 2
                self.state = "GameOn"
        elif self.state == "GameOver":
            if key == arcade.key.R:
                self.human = 1
                self.bot = 2
                self.state = "GameOn"
                self.botScore = 0
                self.humanScore = 0
                self.initilizeBoard(10, 10)



    def evalBoard(self):
        if self.state == "GameOn":
            if self.botScore > 49:
                self.state = "GameOver"
                self.win = "BOT"

            elif self.humanScore > 49:
                self.state = "GameOver"
                self.win = "HUMAN"
            elif self.humanScore == self.botScore and self.humanScore + self.botScore == 98:
                self.state = "DRAW"




    def on_show(self):
        arcade.set_background_color(arcade.color.PERSIAN_INDIGO)

    def draw_horizental(self, grid_size, box_size, pixel):
        temp = box_size
        for i in range(1, grid_size):
            arcade.draw_line(0, box_size, (box_size*grid_size), box_size,  arcade.color.BLACK, pixel)
            box_size = box_size + temp #temp is box size


    def draw_vertical(self, grid_size, box_size, pixel):
        temp = box_size
        for i in range(1, grid_size):
            arcade.draw_line(box_size, 0, box_size, (box_size*grid_size),  arcade.color.BLACK, pixel)
            box_size = box_size + temp #temp is box size


    def on_draw(self):
        arcade.start_render()
        if self.state == "GameMenu":
            arcade.draw_text("Welcome to snails game", 450, 400, arcade.color.WHITE, font_size=40, anchor_x="center")
            arcade.draw_text("Welcome to snails game", 450, 400, arcade.color.WHITE, font_size=40, anchor_x="center")
            arcade.draw_text("Welcome to snails game", 450, 400, arcade.color.WHITE, font_size=40, anchor_x="center")
            arcade.draw_text("Welcome to snails game", 450, 400, arcade.color.WHITE, font_size=40, anchor_x="center")
            arcade.draw_text("Welcome to snails game", 452, 400, arcade.color.WHITE, font_size=40, anchor_x="center")
            arcade.draw_text("Welcome to snails game", 452, 400, arcade.color.WHITE, font_size=40, anchor_x="center")


            arcade.draw_text("===> Press any key to continue", 480, 350, arcade.color.WHITE, font_size=20, anchor_x="center")
            arcade.draw_text("===> Press any key to continue", 480, 350, arcade.color.WHITE, font_size=20, anchor_x="center")
            arcade.draw_text("===> Press any key to continue", 480, 350, arcade.color.WHITE, font_size=20, anchor_x="center")
        

            arcade.draw_text("DEVELOPED BY: WISHA KHURSHID, SAIF ULLAH, SYED WAJEH", 500, 150, arcade.color.WHITE, font_size=20, anchor_x="center")
            arcade.draw_text("DEVELOPED BY: WISHA KHURSHID, SAIF ULLAH, SYED WAJEH", 500, 150, arcade.color.WHITE, font_size=20, anchor_x="center")
            arcade.draw_text("DEVELOPED BY: WISHA KHURSHID, SAIF ULLAH, SYED WAJEH", 500, 150, arcade.color.WHITE, font_size=20, anchor_x="center")

        elif self.state == "GameOn":
            # self.shape_list = arcade.ShapeElementList()
            arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,back)

            self.draw_horizental(10, boxSize, 4)
            self.draw_vertical(10, boxSize, 4)
            arcade.draw_lrwh_rectangle_textured(600, 0,1000, SCREEN_HEIGHT,back)
            
            arcade.draw_line(605, 0, 605, 605,  arcade.color.WHITE, 7)

            arcade.draw_rectangle_filled(820, 530, 230,
                                     55, arcade.color.WHITE)
            arcade.draw_text(self.turn + " TURN", 720, 515, arcade.color.BLACK, font_size=25)
            arcade.draw_text(self.turn + " TURN", 721, 516, arcade.color.BLACK, font_size=25)
            arcade.draw_text(self.turn + " TURN", 721, 516, arcade.color.BLACK, font_size=25)
            arcade.draw_text(self.turn + " TURN", 720, 515, arcade.color.BLACK, font_size=25)

            
            #Score of both players
            # LABEL SCORE BOARD FOR BOT
            arcade.draw_text("BOT SCORE" , 630, 310, arcade.color.WHITE, font_size=20)
            arcade.draw_text("BOT SCORE" , 630, 310, arcade.color.WHITE, font_size=20)
            arcade.draw_text("BOT SCORE" , 630, 310, arcade.color.WHITE, font_size=20)

            arcade.draw_rectangle_filled(700, 260, 70,
                                     55, arcade.color.WHITE)
            arcade.draw_text(str(self.botScore) , 690, 245, arcade.color.BLACK, font_size=20)
            arcade.draw_text(str(self.botScore) , 690, 245, arcade.color.BLACK, font_size=20)
            arcade.draw_text(str(self.botScore) , 690, 245, arcade.color.BLACK, font_size=20)
            
            # LABEL SCORE BOARD FOR HUMAN
            arcade.draw_text("HUMAN SCORE" , 800, 310, arcade.color.WHITE, font_size=20)
            arcade.draw_text("HUMAN SCORE" , 800, 310, arcade.color.WHITE, font_size=20)
            arcade.draw_text("HUMAN SCORE" , 800, 310, arcade.color.WHITE, font_size=20)

            arcade.draw_rectangle_filled(870, 260, 70,
                                     55, arcade.color.WHITE)
            arcade.draw_text(str(self.humanScore) , 859, 245, arcade.color.BLACK, font_size=20)
            arcade.draw_text(str(self.humanScore) , 859, 245, arcade.color.BLACK, font_size=20)
            arcade.draw_text(str(self.humanScore) , 859, 245, arcade.color.BLACK, font_size=20)

            Y = boxSize
            temp = 0
            #print(self.board)
            for row in range (0, len(self.board)):
                X = 0
                for col in range (0, len(self.board)):
                    # print("Found : " + str(self.board[temp][col]))
                    if self.board[row][col] == 1 : #Human snail
                        arcade.draw_lrwh_rectangle_textured( X+MARGIN, SCREEN_HEIGHT-Y, boxSize-MARGIN, boxSize-MARGIN, snail1)
                    
                    elif self.board[row][col] == 2 : #Human snail
                        arcade.draw_lrwh_rectangle_textured( X+MARGIN, SCREEN_HEIGHT-Y, boxSize-MARGIN, boxSize-MARGIN, snail2)
                    
                    elif self.board[row][col] == 11 : #Human snail
                        arcade.draw_lrwh_rectangle_textured( X+MARGIN, SCREEN_HEIGHT-Y, boxSize-MARGIN, boxSize-MARGIN, sp1)
                    
                    elif self.board[row][col] == 22 : #Human snail
                        arcade.draw_lrwh_rectangle_textured( X+MARGIN, SCREEN_HEIGHT-Y, boxSize-MARGIN, boxSize-MARGIN, sp2)
                    
                    X += boxSize
                temp += 1
                Y += boxSize
                

        elif self.state == "GameOver":
            if self.win == "HUMAN":
                arcade.draw_text("Congratulations, you won !", 300, 300, arcade.color.WHITE, font_size=40, anchor_x="center")
                arcade.draw_text("Click to continue", 300, 250, arcade.color.WHITE, font_size=20, anchor_x="center")

            elif self.win == "BOT":
                arcade.draw_text("Computer wins :(", 300, 300, arcade.color.WHITE, font_size=50, anchor_x="center")
                arcade.draw_text("Press R to continue", 300, 250, arcade.color.WHITE, font_size=20, anchor_x="center")


            elif self.win == "DRAW":
                arcade.draw_text("It's a draw..", 300, 300, arcade.color.WHITE, font_size=50, anchor_x="center")
                arcade.draw_text("Click to continue", 300, 250, arcade.color.WHITE, font_size=20, anchor_x="center")


        elif self.state == "GameInstruction":
                arcade.draw_text("GAME INSTRUCTION:", 100, 520, arcade.color.WHITE, font_size=20)
                arcade.draw_text("GAME INSTRUCTION:", 100, 520, arcade.color.WHITE, font_size=20)
                arcade.draw_text("GAME INSTRUCTION:", 100, 520, arcade.color.WHITE, font_size=20)
                
                arcade.draw_text("1- Capture maximum space to win the Game.", 150, 480, arcade.color.WHITE, font_size=14)
                arcade.draw_text("1- Capture maximum space to win the Game.", 150, 480, arcade.color.WHITE, font_size=14)

                arcade.draw_text("2- You can roll back through your own splashes.", 150, 460, arcade.color.WHITE, font_size=14)
                arcade.draw_text("2- You can roll back through your own splashes.", 150, 460, arcade.color.WHITE, font_size=14)

                arcade.draw_text("3- Any Player that capture 50 boxes will be winner.", 150, 440, arcade.color.WHITE, font_size=14)
                arcade.draw_text("3- Any Player that capture 50 boxes will be winner.", 150, 440, arcade.color.WHITE, font_size=14)


##############################################
####### RETURN THE INDEX VALUE OF 2D BACK-END
####### BOARD ACCORDING TO X,Y VALUES
##############################################

    def calcRowCol(self, x, y):
        x1 = y // boxSize
        y1 = x // boxSize
        return 9-x1, y1

    def checkValidClick(self, x, y):
        if 0 <= x <= SCREEN_WIDTH and 0 <= y <= SCREEN_HEIGHT:
            return True
        elif 0 > x > SCREEN_WIDTH and 0 > y > SCREEN_HEIGHT:
            return False

############################################
#---------- GET HUMAN AND BOT POSITION
############################################
    def getHumanPosition(self):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board)):
                if self.board[i][j] == 2:
                    return i,j


    def getBotPosition(self):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board)):
                if self.board[i][j] == 1:
                    return i,j
#####################################################################
##################################################################### 
#                   RIGHT RAILS Function

    def rightRail(self, x, y, turn):
        if turn== "HUMAN":
            self.board[x][y] = 22
            i = 1
            while(True):
                if self.board[x][y+i] == 22 and y+i < 9:
                    i += 1
                else:
                    break
            if y+i == 9 and self.board[x][y+i] == 22:
                self.board[x][y+i] = 2    
            else:
                self.board[x][y+i-1] = 2
        elif turn== "BOT":
            #print("BOT RAIL")
            self.board[x][y] = 11
            i = 1
            while(True):
                if self.board[x][y+i] == 11 and y+i < 9:
                    i += 1
                else:
                    break
            if y+i == 9 and self.board[x][y+i]:
                self.board[x][y+i] = 1    
            else:
                self.board[x][y+i-1] = 1

#####################################################################
#####################################################################
#                LEFT RAILS Function

    def leftRail(self, x, y, turn):
        if turn== "HUMAN":
            self.board[x][y] = 22
            i = 1
            while(True):
                if self.board[x][y-i] == 22 and y-i > 0:
                    i += 1
                else:
                    break
            if y-i == 0 and self.board[x][y-i] == 22:
                self.board[x][y-i] = 2    
            else:
                self.board[x][y-i+1] = 2
        elif turn== "BOT":
            #print("BOT RAIL")
            self.board[x][y] = 11
            i = 1
            while(True):
                if self.board[x][y-i] == 11 and y-i > 0:
                    i += 1
                else:
                    break
            if y-i == 0 and self.board[x][y-i] ==11:
                self.board[x][y-i] = 1    
            else:
                self.board[x][y-i+1] = 1
#####################################################################
#####################################################################


#####################################################################
#                UP RAILS Function

    def upRail(self, x, y, turn):
        if turn== "HUMAN":
           
            self.board[x][y] = 22
            i = 1
            while(True):
                if self.board[x-i][y] == 22 and x-i > 0:
                    i += 1
                else:
                    break
                
            if x-i == 0 and self.board[x-i][y] == 22:
                self.board[x-i][y] = 2   
            else:
                 self.board[x-i+1][y] = 2
        elif turn== "BOT":
            #print("BOT RAIL")
            self.board[x][y] = 11
            i = 1
            while(True):
                if self.board[x-i][y] == 11 and x-i > 0:
                    i += 1
                else:
                    break
            if x-i == 0 and self.board[x-i][y] == 11:
                self.board[x-i][y] = 1    
            else:
                self.board[x-i+1][y] = 1


############################################
# ------------------------------------------
############################################


#####################################################################
#                Down RAILS Function

    def DownRail(self, x, y, turn):
        if turn== "HUMAN":
           
            self.board[x][y] = 22
            i = 1
            while(True):
                if self.board[x+i][y] == 22 and x+i < 9:
                    i += 1
                else:
                    break
            if x+i == 9 and self.board[x+i][y] == 22:
                self.board[x+i][y] = 2    
            else:
                self.board[x+i-1][y] = 2
        elif turn== "BOT":
            #print("BOT RAIL")
            self.board[x][y] = 11
            i = 1
            while(True):
                if self.board[x+i][y] == 11 and x+i < 9:
                    i += 1
                else:
                    break
            if x+i == 9 and self.board[x+i][y] == 11:
                self.board[x+i][y] = 1    
            else:
                self.board[x+i-1][y] = 1


############################################
# ------------------------------------------
############################################





    def on_mouse_press(self, x, y, _button, _modifiers):
        if self.state == "GameOn":
            row, col = self.calcRowCol(x,y)
            print("Clicked on : (" + str(row) + "," + str(col) + ")")
            #Check for valid moves
            if self.checkValidClick(x, y): # Click should be in the BOX
                # Now check weather the clicked space is next to the Position of player
                if self.turn == "HUMAN":
                    
                    x,y = self.getHumanPosition()
                    print("Human on : (" + str(x) + "," + str(y) + ")")
                    
                    if   row==x and y+1==col and self.board[row][col]==0: #Right Move
                        self.board[row][col], self.board[x][y] = 2, 22
                        self.turn = "BOT"
                        self.humanScore += 1
                    elif row==x and y-1==col and self.board[row][col]==0: #Left Move
                        self.board[row][col], self.board[x][y] = 2, 22
                        self.turn = "BOT"
                        self.humanScore += 1
                    elif x+1==row and y==col and self.board[row][col]==0: #Up Move
                        self.board[row][col], self.board[x][y] = 2, 22
                        self.turn = "BOT"
                        self.humanScore += 1
                    elif x-1==row and y==col and self.board[row][col]==0: #Down Move
                        self.board[row][col], self.board[x][y] = 2, 22
                        self.turn = "BOT"
                        self.humanScore += 1
                    
                    ########################### ############################
                    #-------------- RAILING CODE ---------------------------

                    elif row==x and y+1==col and self.board[row][col]==22: #Right rails
                        self.rightRail(x, y, self.turn)
                        self.turn = "BOT"
                        
                    elif row==x and y-1==col and self.board[row][col]==22:  #Left Rail
                        self.leftRail(x, y, self.turn)
                        self.turn = "BOT"

                    elif x-1==row and y==col and self.board[row][col]==22:  #Up Rails
                        self.upRail(x, y, self.turn)
                        self.turn = "BOT"
                        
                    elif x+1==row and y==col and self.board[row][col]==22: #Down Move
                        self.DownRail(x, y, self.turn)
                        self.turn = "BOT"
                        


                    else:
                        self.turn = "BOT"
                        print("INVALID CLICK, HUMAN TURN LOST !!!!")

                elif self.turn == "BOT":
                    
                    x, y = self.getBotPosition()
                    print("Bot on : (" + str(x) + "," + str(y) + ")")
                    
                    if   row==x and y+1==col and self.board[row][col]==0: #Right Move
                        self.board[row][col], self.board[x][y] = 1, 11
                        self.turn = "HUMAN"
                        self.botScore += 1
                    elif row==x and y-1==col and self.board[row][col]==0: #Left Move
                        self.board[row][col], self.board[x][y] = 1, 11
                        self.turn = "HUMAN"
                        self.botScore += 1
                    elif x+1==row and y==col and self.board[row][col]==0: #Up Move
                        self.board[row][col], self.board[x][y] = 1, 11
                        self.turn = "HUMAN"
                        self.botScore += 1
                    elif x-1==row and y==col and self.board[row][col]==0: #Down Move
                        self.board[row][col], self.board[x][y] = 1, 11
                        self.turn = "HUMAN"
                        self.botScore += 1
                    
                    ############################ Railss
                    elif row==x and y+1==col and self.board[row][col]==11: #Right rails
                        self.rightRail(x, y, self.turn)
                        self.turn = "HUMAN"

                    elif row==x and y-1==col and self.board[row][col]==11: # Left rails
                        self.leftRail(x, y, self.turn)
                        self.turn = "HUMAN"
                    elif x-1==row and y==col and self.board[row][col]==11: #Up Rail
                        self.upRail(x, y, self.turn)
                        self.turn = "HUMAN"
                    elif x+1==row and y==col and self.board[row][col]==11: #Down Move
                        self.DownRail(x, y, self.turn)
                        self.turn = "HUMAN"
                        
                    else:
                        self.turn = "HUMAN"
                        print("INVALID CLICK, BOT TURN LOST !!!!")
                self.evalBoard()




if __name__ == "__main__":
    window = arcade.Window(SCREEN_HEIGHT+400, SCREEN_WIDTH, "SNAILS GAME")
    game_view = Game()
    window.show_view(game_view)
    arcade.run()




    