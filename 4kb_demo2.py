import pygame as p,math as m,random as r,os,tempfile,wave,struct,time
p.init();p.mixer.init(22050,-16,1,512);X=p.display.Info();W,H=X.current_w,X.current_h;s=p.display.set_mode((W,H),p.FULLSCREEN);S,C,T,I=m.sin,m.cos,m.tau,int;d=p.draw;cl=p.time.Clock();gt=p.time.get_ticks;g=os.path.join(tempfile.gettempdir(),'d2.wav')
U,V=[p.Surface((W,H)).convert_alpha()for _ in'12'];F=p.font.SysFont('Arial',58);Q=[]
def hc(h,q):
 h=(h+q*.07)%1;a=[abs(h*6-3)-1,2-abs(h*6-2),2-abs(h*6-4)];return tuple(max(0,min(255,I(x*255)))for x in a)
for j in range(6):
 q=p.Surface((16,16))
 for y in range(16):
  for x in range(16):q.set_at((x,y),hc((x*y+j*19+r.random()*9)/64,j))
 Q+=q.convert(),
def mus():
 sr,du=22050,190;n=sr*du;P=[0,3,5,7,10,8,5,7];M=[0,2,3,7,10,12,14,15,12,10,7,5,3,2,7,10];B=[0,0,7,0,10,7,5,3]
 with wave.open(g,'wb')as w:
  w.setparams((1,2,sr,n,'NONE',''))
  for i in range(n):
   if i%90000==0:s.fill(0);s.blit(F.render(str(I(i/n*100)),1,(99,99,99)),(W//2,H//2));p.display.flip()
   t=i/sr;b=t*2.8;bt=I(b);f=b%1;ba=bt//4;ro=P[(ba//4)%8];x=0;e=(1-f)**.7;hz=55*2**((ro+B[bt%8])/12)
   x+=S(T*hz*t+.5*S(T*hz*2*t))*e*.26
   st=I(b*2);no=ro+M[(st+ba*3+bt//16)%16]+(12 if ba&4 and st%7==0 else 0);le=(1-(b*2%1))**2.3;fq=220*2**(no/12);x+=S(T*fq*t+S(T*fq*t)*.7)*le*.18
   for o in(0,3,7):x+=S(T*110*2**((ro+o)/12)*t+S(t*.25+o))*.035
   if bt>8:k=(1-f)**8;x+=S(T*(40+120*k)*t)*k*.6
   z=r.random()*2-1
   if bt>16 and bt%4==2:x+=z*(1-f)**13*.26
   if bt>24:x+=z*(1-(b*2%1))**30*.08
   if bt>64 and bt%16>13:x+=S(T*(660+55*(bt%12))*t)*(1-f)*.08
   w.writeframes(struct.pack('<h',I(max(-1,min(1,x))*32767)))
mus();time.sleep(.5);p.mixer.music.load(g);p.mixer.music.play(-1)
def dr(k,A,t):
 q,bt=(k*7+k//3)%11,(1-(t*2.8%1))**2;A.fill(0);cx,cy=W/2+S(t*.31+k)*W*.22,H/2+C(t*.27+k)*H*.22
 if q==0:
  for y in range(0,H,24):
   for x in range(0,W,24):v=S(x*.01+t)+S(y*.013*C(t*.6))+S(m.hypot(x-cx,y-cy)*.012);d.rect(A,hc(v*.18,k),(x,y,24,24))
 elif q==1:
  for i in range(260):z=(i*.004-t*(1 if k&1 else -.7))%1+.01;a=i*2.4+k;r1=H/z*.35;d.circle(A,hc(z,k),(I(cx+C(a)*r1),I(cy+S(a)*r1)),max(1,I(2/z)))
 elif q==2:
  for j in range(1,18):z=j-t%1;ay=cy+H/(z*.38);c=hc(j*.04+t*.05,k);d.line(A,c,(0,I(ay)),(W,I(ay)),I(1+bt*4));xx=I(cx+S(t+k)*W/z);d.line(A,c,(xx,0),(xx,H),1)
 elif q==3:
  R=H*.18+bt*130;N=3+k%7
  for i in range(N):a=t+i*T/N;P=[(I(cx+S(a+j*T/3)*R*(1+.3*S(t+j))),I(cy+C(a+j*T/3)*R*(1+.3*C(t+j))))for j in range(3)];d.polygon(A,hc(i/N+t*.1,k),P,i&1)
 elif q==4:
  n=4+I(bt*7)+k%3;R=H*.22+bt*140;P=[(I(cx+S(i*T/n+t)*R*(1 if i%2 else .37)),I(cy+C(i*T/n+t)*R*(1 if i%2 else .37)))for i in range(n*2)];d.polygon(A,hc(t,k),P,0)
 elif q==5:
  for i in range(80):a=i*T/80+t*(1+k%3);r1=H*.25+bt*330;d.line(A,hc(i*.02+t*.1,k),(I(cx),I(cy)),(I(cx+S(a)*r1),I(cy+C(a)*r1)),I(1+bt*7))
 elif q==6:
  for i in range(16):R=70+i*34+bt*120;d.circle(A,hc(t+i*.03,k),(I(cx+S(t+i)*R),I(cy+C(t+i)*R)),I(15+bt*90),I(1+bt*9))
 elif q==7:
  for i in range(75):z=(i*.05-t*.25)%3+.7;x=((i*47)%220-110)*W/420;y=((i*83)%150-75)*H/260;a=max(3,I(65/z));R=p.transform.scale(Q[(i+k)%6],(a,a));A.blit(R,(I(cx+x/z),I(cy+y/z)))
 elif q==8:
  for i in range(28):z=(i*.04-t*.18)%1+.05;a=i*2.2+k;R=H/z*.33;x=I(cx+C(a)*R);y=I(cy+S(a)*R);L=I(35/z);P=[(x,y-L),(x-L//2,y+L),(x+L//2,y+L)];d.polygon(A,hc(z+t,k),P,0);d.polygon(A,(255,255,255),P,1)
 elif q==9:
  for i in range(24):R=H*(.04+i*.035+bt*.03);x=cx+S(t+i)*R;y=cy+C(t*.7+i)*R;d.rect(A,hc(i*.04+t,k),(I(x-R),I(y-R),I(R*2),I(R*2)),I(1+bt*5))
 else:
  for x in range(0,W,18):
   y=I((t*220+x*(k%9+1))%H)
   for j in range(6):d.rect(A,hc(.33+j*.03+t*.05,k),(x,(y-j*28)%H,12,20),1)
 return bt
k=tm=0
while 1:
 if any(e.type in(p.QUIT,p.KEYDOWN)for e in p.event.get()):p.quit();exit()
 dt=cl.tick(60)/1000;tm+=dt;t=gt()*1e-3;a=min(1,max(0,(tm-10)/2));bt=dr(k,U,t);dr(k+1,V,t);U.set_alpha(I(255*(1-a)));V.set_alpha(I(255*a));s.fill(0);s.blit(U,(0,0));s.blit(V,(0,0))
 if bt>.93:z=1.05+bt*.03;R=p.transform.scale(s,(I(W*z),I(H*z)));s.blit(R,(-I(W*(z-1)/2),-I(H*(z-1)/2)),special_flags=p.BLEND_RGB_ADD)
 p.display.flip()
 if tm>12:k+=1;tm=0
import pygame as p,math as m,random as r,os,tempfile,wave,struct,time
p.init();p.mixer.init(22050,-16,1,512);X=p.display.Info();W,H=X.current_w,X.current_h
s=p.display.set_mode((W,H),p.FULLSCREEN);S,C,ta,I=m.sin,m.cos,m.tau,int;d=p.draw
clk=p.time.Clock();gt=p.time.get_ticks;g=os.path.join(tempfile.gettempdir(),'d.wav')
U,V=[p.Surface((W,H)).convert_alpha() for _ in'12'];f=p.font.SysFont('Arial',58)
def mus():
 sr,du=22050,160;n=sr*du
 with wave.open(g,'wb')as w:
  w.setparams((1,2,sr,n,'NONE',''))
  for i in range(n):
   if i%80000==0:
    s.fill(0);s.blit(f.render(str(I(i/n*100)),1,(99,99,99)),(W//2,H//2));p.display.flip()
   t=i/sr;b=t*2.4;bt=I(b);x=0;sq=[0,3,7,10];hz=27.5*(2**(sq[bt%4]/12))
   x+=S(ta*hz*t+S(ta*hz*t)*.6)*(1-b%1)*.5
   if bt>16:x+=S(ta*max(30,160*(1-(b%1)**.3))*t)*(1-(b%1)**.1)
   if bt>32 and bt%2:x+=r.random()*(1-b%1)**16*.12
   w.writeframes(struct.pack('<h',I(max(-1,min(1,x))*32767)))
mus();time.sleep(.5);p.mixer.music.load(g);p.mixer.music.play(-1)
def hc(h,q):
 a=[abs(((h+q*.1)%1)*6-3)-1,2-abs(((h+q*.1)%1)*6-2),2-abs(((h+q*.1)%1)*6-4)]
 return tuple(max(0,min(255,I(x*255)))for x in a)
def dr(k,T,t):
 q,bt=k%7,(1-(t*2.4%1))**2;T.fill(0);cx,cy=W/2+S(t*.4)*W*.2,H/2+C(t*.3)*H*.2
 if q==0:
  for y in range(0,H,24):
   for x in range(0,W,24):
    v=S(x*.01+t)+S(y*.01*C(t*.5))+S(m.sqrt((x-cx)**2+(y-cy)**2)*.01);d.rect(T,hc(v*.2,k),(x,y,24,24))
 elif q==1:
  for i in range(200):z=(i*.005-t)%1+.01;r1=H/z*.45;a=i*137.5;d.circle(T,hc(z,k),(I(cx+C(a)*r1),I(cy+S(a)*r1)),max(1,I(2/z)))
 elif q==2:
  for j in range(1,15):
   z=j-t%1;ay=cy+H/(z*.4);c=hc(j*.06,k);d.line(T,c,(0,I(ay)),(W,I(ay)),I(1+bt*3));xx=I(cx+S(t)*W/z);d.line(T,c,(xx,0),(xx,H),1)
 elif q==3:
  R=H*.15+bt*120
  for i in range(5):
   a=t+i*ta/5;pts=[(I(cx+S(a+j*ta/3)*R),I(cy+C(a+j*ta/3)*R))for j in range(3)];d.polygon(T,hc(i*.1,k),pts,2)
 elif q==4:
  n=4+I(bt*6);R=H*.2+bt*100;pts=[(I(cx+S(i*ta/n+t)*R*(1 if i%2 else .4)),I(cy+C(i*ta/n+t)*R*(1 if i%2 else .4)))for i in range(n*2)];d.polygon(T,hc(t,k),pts,0)
 elif q==5:
  for i in range(60):a=i*ta/60+t;r1=H*.3+bt*250;d.line(T,hc(i*.02,k),(I(cx),I(cy)),(I(cx+S(a)*r1),I(cy+C(a)*r1)),I(1+bt*6))
 else:
  for i in range(12):R=100+i*30+bt*100;d.circle(T,hc(t,i),(I(cx+S(t+i)*R),I(cy+C(t+i)*R)),I(20+bt*80),I(1+bt*10))
 return bt
k,tm=0,0
while 1:
 if any(e.type in(p.QUIT,p.KEYDOWN)for e in p.event.get()):p.quit();exit()
 dt=clk.tick(60)/1000;tm+=dt;t=gt()*1e-3;a=min(1,max(0,(tm-10)/2));bt=dr(k,U,t);dr(k+1,V,t);U.set_alpha(I(255*(1-a)));V.set_alpha(I(255*a));s.fill(0);s.blit(U,(0,0));s.blit(V,(0,0))
 if bt>.94:
  z=1.07;tmp=p.transform.scale(s,(I(W*z),I(H*z)));s.blit(tmp,(-I(W*(z-1)/2),-I(H*(z-1)/2)),special_flags=p.BLEND_RGB_ADD)
 p.display.flip()
 if tm>12:k+=1;tm=0
