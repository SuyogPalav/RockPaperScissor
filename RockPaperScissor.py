import random;
from os import system, name;
from time import sleep;

class GameRPS:
    """initialize the required things"""
    def __init__(self):
        self.listswg=["Rock","Paper","Scissor"];
        self.listswgDict={"r":self.listswg[0], "p":self.listswg[1],"s":self.listswg[2]};
        self.chances=3;
        self.Computer=0;
        self.You=0;
        GameRPS.__recursionCount=0;


    def intro(self):
        """Introduction of Game"""
        print("\n\t\tPlay Game\n");
        print("Game Name : ", end="");
        gameName=" => ".join(self.listswg);
        print(gameName);
        print();

        print("use below keys : ");

        for i in self.listswgDict.keys():
            print(i,"for",self.listswgDict[i]);
        print();

        print("%d chances to Win.."%(self.chances));
        print();

    def ComputerWin(self):
        """Execute when Computer is Win"""
        self.Computer += 1;
        print("Computer :",self.Computer);
        print("You :",self.You);
        self.chances-=1;
        print("%d chances left" % (self.chances));
        print();

    def YouWin(self):
        """Execute when You Win"""
        self.You += 1;
        print("Computer :",self.Computer);
        print("You :",self.You);
        self.chances-=1;
        print("%d chances left" % (self.chances));
        print();

    def Draw(self):
        """Execute when play is draw"""
        print("Draw");
        print("Computer :",self.Computer);
        print("You :",self.You);
        print("%d chances left" %(self.chances));
        print();

    def Winner(self):
        """winner decision"""
        if(self.You>self.Computer):
            print("Congratulation..!! You Win..!!");
        elif(self.Computer>self.You):
            print("Oopss..!! Computer Win..!!");
        else:
            print("Match Draw");

        input("\npress enter");


    def playGame(self):
        """Playing Game"""
        while(self.chances):
            string1 = random.choice(self.listswg);
            char=(input("Enter the key: "));

            if(char not in self.listswgDict.keys()):
                print("Kindly Enter Correct Key..")
                print();
                continue;

            if(self.listswgDict[char]==string1):
                print(self.listswgDict[char],"=",string1);
                self.Draw();

            #For Rock
            elif(self.listswgDict[char]==self.listswg[0]):
                if(self.listswgDict[char] != string1 and string1 == self.listswgDict["s"]):
                    print(self.listswgDict[char], "=", string1);
                    self.YouWin();
                elif(self.listswgDict[char] != string1 and string1 == self.listswgDict["p"]):
                    print(self.listswgDict[char], "=", string1);
                    self.ComputerWin();

            #For Paper
            elif(self.listswgDict[char]==self.listswg[1]):
                if(self.listswgDict[char] != string1 and string1 == self.listswgDict["s"]):
                    print(self.listswgDict[char], "=", string1);
                    self.ComputerWin();
                elif(self.listswgDict[char] != string1 and string1 == self.listswgDict["r"]):
                    print(self.listswgDict[char], "=", string1);
                    self.YouWin();

            #For Scissor
            elif (self.listswgDict[char] == self.listswg[2]):
                if(self.listswgDict[char] != string1 and string1 == self.listswgDict["p"]):
                    print(self.listswgDict[char], "=", string1);
                    self.YouWin();
                elif(self.listswgDict[char] != string1 and string1 == self.listswgDict["r"]):
                    print(self.listswgDict[char], "=", string1);
                    self.ComputerWin();

            print();

    def playAgain(self):
        """Do you want to play again?"""
        self.screenClear();
        print("Do you want to Play Again ? : ");
        print("Enter 1 for Yes : ");
        print("Enter 2 for No : ");

        try:
            decision=int(input("\nEnter : "));
            if(decision==1):
                return(True);
            elif(decision==2):
                return(False);
            else:
                print("Kindly enter correct choice..");
                print();
                GameRPS.__recursionCount+=1;
                if(GameRPS.__recursionCount==3):
                    print("Sorry.. You Exceed the limit!\n\n");
                    return(None);

                self.playAgain();
        except ValueError:
            print("Kindly enter correct number..");
            print();
            GameRPS.__recursionCount += 1;
            if(GameRPS.__recursionCount==3):
                print("Sorry.. You Exceed the limit!\n\n");
                return(None);

            self.playAgain();

    def thanksNote(self):
        "Thanks note | Ending Note"
        print("\nThanks for Playing..!!");
        print("See You Soon...");
        input("\nPress Enter to exit.!");
        print();

    def screenClear(self):
        """Screen Clear"""
        print("\nwait...");
        sleep(0);
        # for windows (os.name is 'nt')
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')


if __name__ == '__main__':
    while(True):
        g1 = GameRPS();
        g1.intro();
        g1.playGame();
        g1.Winner();
        dicison=g1.playAgain();
        if(dicison):
            g1.screenClear();
        else:
            g1.thanksNote();
            exit();


