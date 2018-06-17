# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
suits=['D','H','C','S']
rankings=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
used_cards=set()
initial_chips=0
playing=True
class Dealer:
    def __init__(self):
        self.dcards=[]
        self.dvalue=0
class Player:
    def __init__(self,chip=100):
        Dealer.__init__(self)
        self.chip=0
        self.add_chip(chip)
        self.pcards=[]
        self.pvalue=0
    def add_chip(self,amount):
        global initial_chips
        initial_chips = int(initial_chips) - int(amount)
        self.chip = int(self.chip) + int(amount)
    def win_chip(self):
        global initial_chips
        initial_chips += 2 * int(self.chip)
        self.chip = 0
    def lose_chip(self):
        self.chip = 0
    def game_start(self):
        for i in range(2):
            a=random.randint(1,4)
            b=random.randint(1,13)
            for i in used_cards:
                if i==(suits[a-1]+rankings[b-1]):
                    a=random.randint(1,4)
                    b=random.randint(1,13)
                    i=0
            self.pcards.append((suits[a-1]+rankings[b-1]))
            used_cards.add((suits[a-1]+rankings[b-1]))
        for i in range(2):
            c=random.randint(1,4)
            d=random.randint(1,13)
            for i in used_cards:
                if i==(suits[c-1]+rankings[d-1]):
                    c=random.randint(1,4)
                    d=random.randint(1,13)
                    i=0
            self.dcards.append((suits[c-1]+rankings[d-1]))
            used_cards.add((suits[c-1]+rankings[d-1]))
    def card_value(self):
        self.dvalue=0
        self.pvalue=0
        for i in self.pcards:
            if i[1:]=='A':
                self.pvalue += 11
            elif i[1:]== 'J' or i[1:]=='Q' or i[1:]=='K':
                 self.pvalue += 10
            else:
                 self.pvalue += int(i[1:])
        if int(self.pvalue) > 21:
            for i in self.pcards:
                if i[1:]=='A':
                    self.pvalue -= 10
        for i in self.dcards:
            if i[1:]=='A':
                self.dvalue += 11
            elif i[1:]== 'J' or i[1:]=='Q' or i[1:]=='K':
                 self.dvalue += 10
            else:
                 self.dvalue += int(i[1:])
        if int(self.dvalue) > 21:
            for i in self.dcards:
                if i[1:]=='A':
                    self.dvalue -= 10
    def hit(self):
        a=random.randint(1,4)
        b=random.randint(1,13)
        for i in used_cards:
            if i==(suits[a-1]+rankings[b-1]):
                a=random.randint(1,4)
                b=random.randint(1,13)
                i=0
        self.pcards.append((suits[a-1]+rankings[b-1]))
        used_cards.add((suits[a-1]+rankings[b-1]))
        self.card_value()
    def win_loss(self):
        global initial_chips
        if self.pvalue < self.dvalue:
            print("\t\tYou have lost the Bet!!!")
            self.display_cards()
            self.lose_chip()
        elif self.pvalue > 21:
            print("\t\tYou have been Busted!!!")
            self.lose_chip()
        elif self.pvalue == self.dvalue:
            print("\t\tIts a Tie!!!")
            initial_chips += int(self.chip)
            self.display_cards()
            self.chip=0
        else:
            print("\t\tYOU HAVE WON!!!")
            self.display_cards()
            self.win_chip()
    def display_cards(self):
        print("Dealer Cards are: {}".format(self.dcards))
        print("Player Cards are: {}".format(self.pcards))
    def stand(self):
        while True:
            if self.dvalue < 18:
                c=random.randint(1,4)
                d=random.randint(1,13)
                for i in used_cards:
                    if i==(suits[c-1]+rankings[d-1]):
                        c=random.randint(1,4)
                        d=random.randint(1,13)
                        i=0
                self.dcards.append((suits[c-1]+rankings[d-1]))
                used_cards.add((suits[c-1]+rankings[d-1]))
                self.card_value()
            elif self.dvalue > 21:
                self.dcards=self.dcards[:-1]
                self.card_value()
                self.display_cards()
                break
            else:
                self.display_cards()
                break 
        
def main():
    global initial_chips
    global playing
    initial_chips=input("Enter your total amount:")
    while playing:
        while True:
            amount=0
            amount=input("Enter you betting amount:")
            if int(amount) > int(initial_chips):
                print("Not enough Chips!!!Try Again!!!")
                continue
            sam=Player(amount)
            sam.game_start()
            sam.display_cards()
            sam.card_value()
            while True:
                io=input("Do you want to Hit('H') or Stand('S'):")
                if io == 'h' or io == 'H':
                    sam.hit()
                    sam.display_cards()
                    if sam.pvalue > 21:
                        sam.lose_chip()
                        break
                elif io == 's' or io == 'S':
                    sam.stand()
                    break
                else:
                    print("\t\t\tError!!! Retry!")
            sam.win_loss()
            print("Your total Chips: {}".format(initial_chips))
            break
        p=input("Do you want to play again(y/n):")
        if p=='y' or p=='Y':
            continue
        elif p=='n' or p=='N':
            break
        else:
            print("Try Again")
if __name__=='__main__':
    main()