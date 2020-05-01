import string
import random
#creating a list of characters
symbol=[] 
#appending the characters in the symbol list
symbol=list(string.ascii_letters) 
#Making two lists having fixed(7) characters 
card1=[0]*7
card2=[0]*7
#Making positions to be variable
pos1=random.randint(0,6)
pos2=random.randint(0,6)
#selecting a symbol randomly from the symbol list
samesymbol=random.choice(symbol)
#Removing that same symbol from the symbol list
symbol.remove(samesymbol)
#
if(pos1==pos2):
    card2[pos2]=samesymbol
    card1[pos1]=samesymbol
else:
    card1[pos1]=samesymbol
    card2[pos2]=samesymbol
    card1[pos2]=random.choice(symbol)
    symbol.remove(card1[pos2])
    card2[pos1]=random.choice(symbol)
    symbol.remove(card2[pos1])
i=0
while(i<7):
    if(i!=pos1 and i!=pos2):
        alphabet1=random.choice(symbol)
        symbol.remove(alphabet1)
        alphabet2=random.choice(symbol)
        symbol.remove(alphabet2)
        card1[i]=alphabet1
        card2[i]=alphabet2
    i=i+1
print(card1)
print(card2)
Key=input("Spot the same character")
if Key==samesymbol:
    print("Hurray!")
else:
    print("Fuck off!")
        
    
