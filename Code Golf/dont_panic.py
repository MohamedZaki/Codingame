v,I,T={},input,int
_,w,_,o,x,_,_,n=map(T,I().split())
for i in[1]*n:f,p=map(T,I().split());v[f]=p
while 1:
 f,p,d=I().split();f,p=T(f),T(p);s=d=='LEFT';t=x;c=f in v
 if c:t=v[f]
 if c|~f-o:r=((p>t)*~s)|(p<t*s)
 print(['WAIT','BLOCK'][r])
