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
