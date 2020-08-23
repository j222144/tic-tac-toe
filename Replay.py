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
