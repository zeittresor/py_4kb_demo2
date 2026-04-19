import pygame as p,math as m,random as r,os,tempfile,wave,struct
p.init();p.mixer.init(22050,-16,1,512);i=p.display.Info();W,H=i.current_w,i.current_h;s=p.display.set_mode((W,H),p.FULLSCREEN)
S,C,ta=m.sin,m.cos,m.tau;d=p.draw;I=int;clk=p.time.Clock();gt=p.time.get_ticks;U=p.Surface((W,H)).convert_alpha();V=p.Surface((W,H)).convert_alpha();g=tempfile.gettempdir()+os.sep+'d.wav'
def mus():
 sr=22050;dur=64;n=sr*dur;sc=[0,3,7,10,12,7,3,0]
 with wave.open(g,'wb')as w:
  w.setparams((1,2,sr,n,'NONE',''))
  for i in range(n):
   t=i/sr;b=t*2.5;o=[1,.5,2,1.5][I(t/8)%4];f=55*o*2**(sc[I(b)%8]/12);e=(1-b%1)**1.2;x=S(ta*f*t+S(ta*f*1.02*t))*.28*e
   x+=.22*(b%4<.08)*e;x+=.04*r.random()*(t>8)*(1-(b*4%1))**8;x+=.08*S(ta*f*4*t)*(t>24)*e;x+=.1*r.random()*(t>32)*(abs(b%4-2)<.05)
   w.writeframes(struct.pack('<h',I(max(-1,min(1,x))*32767)))
try:mus();p.mixer.music.load(g);p.mixer.music.play(-1)
except:pass
def hc(h,q=0):
 h=(h+q*.11)%1;a=[abs(h*6-3)-1,2-abs(h*6-2),2-abs(h*6-4)]
 if q&1:a=a[2],a[0]*.7,a[1]
 if q&2:a=a[0]*.4,a[1],a[2]*.9
 return[max(0,min(255,I(x*255)))for x in a]
def pl(T,t,q):
 cx=W*(.5+.35*S(q));cy=H*(.5+.35*C(q*2));z=6+(q&3)*2
 for y in range(0,H,z):
  for x in range(0,W,z):
   v=S(x*.012+t)+S((x*S(t/3)+y*C(t/4))*.01)+S(m.hypot(x-cx,y-cy)*.015-t)
   d.rect(T,hc(v*.25+t*.08,q),(x,y,z,z))
def sf(T,t,q):
 fx=W*(.5+.45*S(t*.4+q));fy=H*(.5+.45*C(t*.3+q));sp=.18+(q&3)*.06
 for i in range(170):
  x=(S(i*12.989)*.5+.5)*W;y=(S(i*78.233)*.5+.5)*H;z=.08+(i*.017+t*sp)%1;X=I(fx+(x-fx)/z);Y=I(fy+(y-fy)/z)
  if 0<X<W and 0<Y<H:d.circle(T,hc(z+t,q),(X,Y),1+(z<.2))
def cu(T,t,q):
 P=[];A=t*(1+(q&3)*.12);B=t*.7;R=H*(.35+.07*S(q))
 for i in range(8):
  x=((i&1)*2-1)*(1+.4*S(q));y=((i&2)-1)*(1+.3*C(q));z=((i&4)//2-1)
  X=x*C(A)-z*S(A);z=x*S(A)+z*C(A);x=X;Y=y*C(B)-z*S(B);z=y*S(B)+z*C(B);P.append((I(W/2+x*R/(z+3)),I(H/2+Y*R/(z+3))))
 for i,j in((0,1),(1,3),(3,2),(2,0),(4,5),(5,7),(7,6),(6,4),(0,4),(1,5),(2,6),(3,7)):d.line(T,hc(t,q),P[i],P[j],1+(q&1))
def kn(T,t,q):
 P=[];R=H*(.22+.06*(q&3));n=70+q%4*18
 for i in range(n):
  a=i*ta/n;r1=R*(1+.35*S((3+q%3)*a+t));x=r1*C((2+q%2)*a+t);y=r1*S(3*a+t*.7);z=r1*S(2*a+t);P.append((I(W/2+x/(z/H+2)),I(H/2+y/(z/H+2))))
 d.lines(T,hc(t*.5,q),1,P,1+(q&1))
def ob(T,t,q):
 for j in range(6+q%8):
  a=t*(1+j*.02)+j;R=H*.18*(1+.4*S(t+j));d.circle(T,hc(t+j*.07,q),(I(W/2+S(a)*R*(2+S(j))),I(H/2+C(a*1.3)*R)),I(8+18*abs(S(t*2+j))),1+(j&1))
def dr(k,T,t):
 q=k%12;T.fill(0)
 if q%3==0:pl(T,t,q)
 if q%3==1:sf(T,t,q)
 if q%4==0:cu(T,t,q)
 elif q%4==1:kn(T,t,q)
 else:ob(T,t,q)
k,N,run,D,F,tm=0,12,1,6,1.4,0
while run:
 for e in p.event.get():
  if e.type==p.KEYDOWN and e.key==p.K_ESCAPE:run=0
 dt=clk.tick(60)/1000;tm+=dt;a=min(1,max(0,(tm-D+F)/F));t=gt()*1e-3
 dr(k,U,t);dr(k+1,V,t);U.set_alpha(I(255*(1-a)));V.set_alpha(I(255*a));s.blit(U,(0,0));s.blit(V,(0,0));p.display.flip()
 if tm>D:k+=1;tm=0
