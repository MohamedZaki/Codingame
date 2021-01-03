x,y,X,Y=map(int,input().split())
while 1:
 d=''
 if Y<y:d='S';Y+=1
 if Y>y:d='N';Y-=1
 if X<x:d+='E';X+=1
 if X>x:d+='W';X-=1
 print(d)
