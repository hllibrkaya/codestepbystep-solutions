import random

def play_roulette(money,bet):
    print("start with $ "+str(money)+" and bet up to $ "+str(bet))
    print("bet\t"+"spin\t"+"money")
    max = money
    
    while money!=0:
        temp=bet
        spin = random.randint(0,36)
        if money>bet:
            temp=bet
        if money<=bet:
            temp=money 
        
        if(spin%2==0 and spin!=0):
            money=money+temp
            if max<money:
                max = money
            print(str(temp)+"\t"+str(spin)+"\t"+ str(money))
        else:
            money=money-temp
            print(str(temp)+"\t"+str(spin)+"\t"+ str(money))
        
    print("max money: $ "+str(max))