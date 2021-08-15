import random
lst=['  ']*53
alst=['  ']*6
blst=['  ']*6
dlst=['  ']*6
clst=['  ']*6
#dlst[5]='a1'
def board():
  print('+--------------------------------------------------------+')
  print('|                      |'+lst[25]+' |'+lst[26]+' |'+lst[27]+' |'+'                     |')
  print('+                      +---+---+---+                     +')
  print('|  (b1)           (b3) |'+lst[24]+' |'+clst[0]+' |'+lst[28]+' |'+'  (c1)           (c3)|')
  print('+                      +---+---+---+                     +')
  print('|                      |'+lst[23]+' |'+clst[1]+' |'+lst[29]+' |'+'                     |')
  print('+                      +---+---+---+                     +')
  print('|                      |'+lst[22]+' |'+clst[2]+' |'+lst[30]+' |'+'                     |')
  print('+                      +---+---+---+                     +')
  print('|  (b2)           (b4) |'+lst[21]+' |'+clst[3]+' |'+lst[31]+' |'+'  (c2)           (c4)|')
  print('+                      +---+---+---+                     +')
  print('|                      |'+lst[20]+' |'+clst[4]+' |'+lst[32]+' |'+'                     |')
  print('+---+---+---+---+---+--+-----------+--+---+---+---+---+--+')
  print('|'+lst[14]+' |'+lst[15]+' |'+lst[16]+' |'+lst[17]+' |'+lst[18]+' |'+lst[19]+'| \  '+clst[5]+'   / |'+lst[33]+'|'+lst[34]+' |'+lst[35]+' |'+lst[36]+' |'+lst[37]+' |'+lst[38]+'|')
  print('+---+---+---+---+---+--+  \     /  +--+---+---+---+---+--+')
  print('|'+lst[13]+' |'+blst[0]+' |'+blst[1]+' |'+blst[2]+' |'+blst[3]+' |'+blst[4]+'|'+blst[5]+' - - - '+dlst[5]+'|'+dlst[4]+'|'+dlst[3]+' |'+dlst[2]+' |'+dlst[1]+' |'+dlst[0]+' |'+lst[39]+'|')
  print('+---+---+---+---+---+--+  /     \  +--+---+---+---+---+--+')
  print('|'+lst[12]+' |'+lst[11]+' |'+lst[10]+' |'+lst[9]+' |'+lst[8]+' |'+lst[7]+'| /  '+alst[5]+'   \ |'+lst[45]+'|'+lst[44]+' |'+lst[43]+' |'+lst[42]+' |'+lst[41]+' |'+lst[40]+'|')
  print('+---+---+---+---+---+--+-----------+--+---+---+---+---+--+')
  print('|                      |'+lst[6]+' |'+alst[4]+' |'+lst[46]+' |'+'                     |')
  print('+                      +---+---+---+                     +')
  print('|  (a1)           (a3) |'+lst[5]+' |'+alst[3]+' |'+lst[47]+' |'+'  (d1)           (d3)|')
  print('+                      +---+---+---+                     +')
  print('|                      |'+lst[4]+' |'+alst[2]+' |'+lst[48]+' |'+'                     |')
  print('+                      +---+---+---+                     +')
  print('|                      |'+lst[3]+' |'+alst[1]+' |'+lst[49]+' |'+'                     |')
  print('+                      +---+---+---+                     +')
  print('|  (a2)           (a4) |'+lst[2]+' |'+alst[0]+' |'+lst[50]+' |'+'  (d2)           (d4)|')
  print('+                      +---+---+---+                     +')
  print('|                      |'+lst[1]+' |'+lst[52]+' |'+lst[51]+' |'+'                     |')
  print('+----------------------+---+---+---+---------------------+')

def homecheck(alst,blst,clst,dlst,t):
    if i==0:
        if t[i]>=6:
          t[i]=5
        alst[t[i]]='A '
        #lst[t[i]-52]='  '
        print("a")
       
    elif i==1:
        if t[i]>=18:
          t[i]=5
          blst[t[i]]='B '
        else:  
          blst[t[i]-13]='B '
        #lst[t[i]]='  '
        print("b")
        
    elif i==2:
        if t[i]>=31:
          t[i]=5
          clst[t[i]]='C '
        else:  
          clst[t[i]-26]='C '
        #lst[t[i]]='  '
        print("c")
        
    elif i==3:
        if t[i]>=44:
          t[i]=5
          dlst[t[i]]='D '
        else:  
          dlst[t[i]-39]='D '
        #lst[t[i]]='  '
        print("d")
        
    user[i]='  '
    #bcd[i]=0
    #board()
    return alst,blst,clst,dlst,bcd;

def killcheck(t,ic):
  hd=[2,15,28,41]
  for j in range(4):
    if t[i]==t[j]:
      if i!=j:
        if t[i]!=hd[j]:
          ic[j]=' '
          t[j]=hd[j]
          print("\n",user[j],"killed")
          print("\n","ic:",ic)
          print("\n","t:",t)
  return ic,t;      





ic=[' ',' ',' ',' ']
glst=['a1','b1','c1','d1']
#glst2=['','','','']
#['','','',''],['','','',''],['','','',''],['','','','']
user=['A1','B1','C1','D1']
dice='*'
bcd=[0,0,0,0]
t=[2,15,28,41]

while True:
    i=0
    while (dice=='*'):
        dice=' '
        #board()
        di=random.randint(1,6)
        print("\nDice rolled for",user[i],":",di)
        if i not in ic:
            if di==6:
                ic[i]=i
                lst[t[i]]=user[i] #placing in first position in first six
                lst[t[i]]='  '
                di=random.randint(1,6)
                print("\nDice Rolled Again for",user[i],":",di)
                lst[t[i]+di]=user[i]
                t[i]+=di
                if di==6:
                    di=random.randint(1,6)
                    print("\nDice Rolled Again for",user[i],":",di)
                    if di==6:
                        print('no more than 2 sixes')
                    else:
                        lst[t[i]]='  '
                        lst[t[i]+di]=user[i]
                        t[i]+=di
            board()            
        else:
            lst[t[i]]='  '
            t[i]+=di
            if di==6:
                di=random.randint(1,6)
                print("\nDice Rolled Again for",user[i],":",di)
                t[i]+=di
                if di==6:
                    di=random.randint(1,6)
                    print("\nDice Rolled Again for",user[i],":",di)
                    if di==6:
                        print('no more than 2 sixes')
                    else:
                        t[i]+=di
            print(t)
            
            #alst,blst,clst,dlst=homecheck(t)
            if t[i]>52:
              t[i]-=52
              bcd[i]=1
            ic,t=killcheck(t,ic)  
            if i==0 and t[i]>1 and bcd[i]==1:
              alst,blst,clst,dlst,bcd=homecheck(alst,blst,clst,dlst,t)
            elif i==1 and t[i]>13 and bcd[i]==1:
              alst,blst,clst,dlst,bcd=homecheck(alst,blst,clst,dlst,t)
            elif i==2 and t[i]>26 and bcd[i]==1:
              alst,blst,clst,dlst,bcd=homecheck(alst,blst,clst,dlst,t)
            elif i==3 and t[i]>39 and bcd[i]==1:
              alst,blst,clst,dlst,bcd=homecheck(alst,blst,clst,dlst,t)       
            lst[t[i]]=user[i]##
            board()
        i+=1
        #print("\n",t)
        if i==4:
            i=0
        dice=str(input("\nPress * to roll dice:"))    
    break
