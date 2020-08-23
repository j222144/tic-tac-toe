import random

class Assigned:
    def __init__(self,whom_with, x_o):
        self.whom_with = whom_with
        self.x_o = x_o
        self.test = None
        self.test2 = None

    def xoro(self):
        o = "O"
        x = "X"
        if self.x_o == o or self.x_o == x:
            self.test2 = True
        else:
            self.test2 = False
                
        while self.test2 == False:
            self.x_o = input("Player 1) please select to be either X's Or O's :").upper()
            if self.x_o == o or self.x_o == x:
                self.test2 = True 
            else:
                self.test2 == False
                
        if self.test2 == True:
            if o == self.x_o:
                self.test2 = True
            else:
                self.test2 = False
        return self.test2

        

    def vs(self):
        
        friend = "FRIEND"
        ai = "AI"
        
        if self.whom_with == friend or self.whom_with == ai:
            self.test = True
        else:
            self.test = False
                
        while self.test == False:
            print(self.whom_with)
            self.whom_with = input("Please enter either 'Friend' or 'AI' :").upper()
            if self.whom_with == friend or self.whom_with == ai:
                self.test = True 
            else:
                self.test == False

        if self.test == True:
            if friend == self.whom_with:
                self.test = True
            else:
                self.test = False
        return self.test



    

    def role(self):
        user1.vs()
        user1.xoro()

        
        if self.test is True and self.test2 is True:
            player1 = 'O'
            player2 = 'X'
        elif self.test is True and self.test2 is False:
            player1 = 'X'
            player2 = 'O'
        elif self.test is False and self.test2 is True:
            player1 = 'O'
            player2 = 'X'
        else:
            player1 = 'X'
            player2 = 'O'

        return player1,player2
            

class Re_run:
    def re_play():
        replay = True
        user = input("Would you like to play again? : Yes / No ").upper()

        while user != "YES" and user != "NO":
            user = input("Would you like to play again? : Yes / No ").upper()

        
        if user == "YES":
            replay = True
        else:
            replay = False
            print("\n\n Have a Great day!")
        return replay


    def test_re_play():
        while Re_run.re_play() == True:
            ai_f = input("Please select whether you wnat to play with AI or Friend: ").upper()
            x_or_o = input("Player1 please select to be O's or X's : ").upper()
            user1 = Assigned(ai_f,x_or_o)
            Game.play()



class Game:

    def random():
        ai = random.randrange(1,9)
        return ai
        
    def play():
        pos = ['1','2','3','4','5','6','7','8','9']
        p1, p2 = user1.role()
        draw = True
        friend = user1.vs()
        ai_nums = Game.random()

        print(pos[0]+" | "+pos[1]+" | "+pos[2]+"\n--|---|--\n"+pos[3]+" | "+pos[4]+" | "+pos[5]+"\n--|---|--\n"+pos[6]+" | "+pos[7]+" | "+pos[8]+"\n\n")
        if friend == True:
            for i in range(5):
                user = int(input("Player 1 Select your position : "))
                char = str(user)
                position_check = True
                
                if char == pos[user-1]:
                    pos[user-1] = p1
                    position_check = False
                    print(pos[0]+" | "+pos[1]+" | "+pos[2]+"\
                    \n--|---|--\n"+pos[3]+" | "+pos[4]+" | "+pos[5]+"\
                    \n--|---|--\n"+pos[6]+" | "+pos[7]+" | "+pos[8]+"\n\n")
                    
                while position_check == True:
                    user = int(input("Player 1) please select emply position : "))
                    char = str(user)
                    if char == pos[user-1]:    
                        pos[user-1] = p1
                        print(pos[0]+" | "+pos[1]+" | "+pos[2]+"\
                        \n--|---|--\n"+pos[3]+" | "+pos[4]+" | "+pos[5]+"\
                        \n--|---|--\n"+pos[6]+" | "+pos[7]+" | "+pos[8]+"\n\n")
                        break
                
                if (p1 == pos[0]) and (p1== pos[1]) and (p1== pos[2]) or (p1 == pos[3]) and (p1== pos[4]) and (p1== pos[5]):
                    print("Player 1) Wins")
                    draw = False
                    break
                elif (p1 == pos[6]) and (p1== pos[7]) and (p1== pos[8]) or (p1 == pos[0]) and (p1== pos[3]) and (p1== pos[6]) or (p1 == pos[1]) and (p1 == pos[4]) and (p1 == pos[7]):
                    print("Player 1) Wins")
                    draw = False
                    break

                elif (p1 == pos[0]) and (p1== pos[4]) and (p1== pos[8]) or (p1 == pos[2]) and (p1== pos[4]) and (p1== pos[6]) or (p1 == pos[2]) and (p1== pos[5]) and (p1== pos[8]):
                    print("Player 1) Wins")
                    draw = False
                    break
                else:
                    if i < 4:
                        user2 = int(input("Player 2 select your position : "))
                        char2 = str(user2)
                        position_check = True
                        
                        if char2 == pos[user2-1]:
                            pos[user2-1] = p2
                            position_check = False
                            print(pos[0]+" | "+pos[1]+" | "+pos[2]+"\
                            \n--|---|--\n"+pos[3]+" | "+pos[4]+" | "+pos[5]+"\
                            \n--|---|--\n"+pos[6]+" | "+pos[7]+" | "+pos[8]+"\n\n")
                            
                        while position_check == True:
                            user2 = int(input("Player 2) please select emply position : "))
                            char2 = str(user2)
                            if char2 == pos[user2-1]:    
                                pos[user2-1] = p2
                                print(pos[0]+" | "+pos[1]+" | "+pos[2]+"\
                                \n--|---|--\n"+pos[3]+" | "+pos[4]+" | "+pos[5]+"\
                                \n--|---|--\n"+pos[6]+" | "+pos[7]+" | "+pos[8]+"\n\n")
                                break
                            
                        if (p2 == pos[0]) and (p2== pos[1]) and (p2== pos[2]) or (p2 == pos[3]) and (p2== pos[4]) and (p2== pos[5]):
                            print("Player 2) Wins")
                            draw = False
                            break
                        elif (p2 == pos[6]) and (p2== pos[7]) and (p2== pos[8]) or (p2 == pos[0]) and (p2== pos[3]) and (p2== pos[6]) or (p2 == pos[1]) and (p2 == pos[4]) and (p2 == pos[7]):
                            print("Player 2) Wins")
                            draw = False
                            break

                        elif (p2 == pos[0]) and (p2== pos[4]) and (p2== pos[8]) or (p2 == pos[2]) and (p2== pos[4]) and (p2== pos[6]) or (p2 == pos[2]) and (p2== pos[5]) and (p2== pos[8]):
                            print("Player 2) Wins")
                            draw = False
                            break

                if i == 4 and draw == True:
                    print("Draw")
                    
        else:
            for i in range(5):
                user = int(input("Player 1 Select your position : "))
                char = str(user)
                position_check = True
                if char == pos[user-1]:
                    pos[user-1] = p1
                    position_check = False
                    print(pos[0]+" | "+pos[1]+" | "+pos[2]+"\
                    \n--|---|--\n"+pos[3]+" | "+pos[4]+" | "+pos[5]+"\
                    \n--|---|--\n"+pos[6]+" | "+pos[7]+" | "+pos[8]+"\n\n")
                while position_check == True:
                    user = int(input("Player 1) please select emply position : "))
                    char = str(user)
                    if char == pos[user-1]:    
                        pos[user-1] = p1
                        print(pos[0]+" | "+pos[1]+" | "+pos[2]+"\
                        \n--|---|--\n"+pos[3]+" | "+pos[4]+" | "+pos[5]+"\
                        \n--|---|--\n"+pos[6]+" | "+pos[7]+" | "+pos[8]+"\n\n")
                        break
                
                if (p1 == pos[0]) and (p1== pos[1]) and (p1== pos[2]) or (p1 == pos[3]) and (p1== pos[4]) and (p1== pos[5]):
                    print("Player 1) Wins")
                    draw = False
                    break
                elif (p1 == pos[6]) and (p1== pos[7]) and (p1== pos[8]) or (p1 == pos[0]) and (p1== pos[3]) and (p1== pos[6]) or (p1 == pos[1]) and (p1 == pos[4]) and (p1 == pos[7]):
                    print("Player 1) Wins")
                    draw = False
                    break

                elif (p1 == pos[0]) and (p1== pos[4]) and (p1== pos[8]) or (p1 == pos[2]) and (p1== pos[4]) and (p1== pos[6]) or (p1 == pos[2]) and (p1== pos[5]) and (p1== pos[8]):
                    print("Player 1) Wins")
                    draw = False
                    break
                else:
                    if i < 4:
                        Game.random()
                        num = Game.random()
                        a = Game.random()
                        char2 = str(a)
                        position_check = True
                        if char2 == pos[num-1]:
                            pos[Game.random()-1] = p2
                            position_check = False
                            print("AI Turn")
                            print(pos[0]+" | "+pos[1]+" | "+pos[2]+"\
                            \n--|---|--\n"+pos[3]+" | "+pos[4]+" | "+pos[5]+"\
                            \n--|---|--\n"+pos[6]+" | "+pos[7]+" | "+pos[8]+"\n\n")

                        while position_check == True:
                            Game.random()
                            num = Game.random()
                            a = Game.random()
                            char2 = str(a)
                            if char2 == pos[num-1]:    
                                pos[num-1] = p2
                                print("AI Turn")
                                print(pos[0]+" | "+pos[1]+" | "+pos[2]+"\
                                \n--|---|--\n"+pos[3]+" | "+pos[4]+" | "+pos[5]+"\
                                \n--|---|--\n"+pos[6]+" | "+pos[7]+" | "+pos[8]+"\n\n")
                                break
                        if (p2 == pos[0]) and (p2== pos[1]) and (p2== pos[2]) or (p2 == pos[3]) and (p2== pos[4]) and (p2== pos[5]):
                            print("AI Wins")
                            draw = False
                            break
                        elif (p2 == pos[6]) and (p2== pos[7]) and (p2== pos[8]) or (p2 == pos[0]) and (p2== pos[3]) and (p2== pos[6]) or (p2 == pos[1]) and (p2 == pos[4]) and (p2 == pos[7]):
                            print("AI Wins")
                            draw = False
                            break

                        elif (p2 == pos[0]) and (p2== pos[4]) and (p2== pos[8]) or (p2 == pos[2]) and (p2== pos[4]) and (p2== pos[6]) or (p2 == pos[2]) and (p2== pos[5]) and (p2== pos[8]):
                            print("AI Wins")
                            draw = False
                            break

                if i == 4 and draw == True:
                    print("Draw")


ai_f = input("Please select whether you wnat to play with AI or Friend: ").upper()
x_or_o = input("Player1 please select to be O's or X's : ").upper()
user1 = Assigned(ai_f,x_or_o)

Game.play()
Re_run.test_re_play()

print(user1.vs())

