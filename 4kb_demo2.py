import pygame as p,math as m,random as r,os,tempfile,wave,struct,time
p.init();p.mixer.init(22050,-16,1,512);X=p.display.Info();W,H=X.current_w,X.current_h
s=p.display.set_mode((W,H),p.FULLSCREEN);S,C,ta,I=m.sin,m.cos,m.tau,int;d=p.draw
clk=p.time.Clock();gt=p.time.get_ticks;g=os.path.join(tempfile.gettempdir(),'d.wav')
U,V=[p.Surface((W,H)).convert_alpha() for _ in'12'];f=p.font.SysFont('Arial',24)
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
