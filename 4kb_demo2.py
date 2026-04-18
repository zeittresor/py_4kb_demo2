import pygame as p,math as m,random as r,os,tempfile,wave,struct
p.init();p.mixer.init(22050,-16,1,512);i=p.display.Info();W,H=i.current_w,i.current_h;s=p.display.set_mode((W,H),p.FULLSCREEN)
sn,co,pi=m.sin,m.cos,m.pi;C=p.time.Clock();t0=p.time.get_ticks;U=p.Surface((W,H)).convert_alpha();V=p.Surface((W,H)).convert_alpha()
g=tempfile.gettempdir()+os.sep+'d.wav'
def mus():
 sr=22050;d=64;n=int(sr*d)
 with wave.open(g,'wb') as w:
  w.setparams((1,2,sr,n,'NONE',''))
  for i in range(n):
   t=i/sr;bt=t*2.5;oct=[1,.5,2,1.5][int(t/8)%4];sq=[0,3,7,10,12,7,3,0]
   f=55*oct*(2**(sq[int(bt)%8]/12));x=sn(2*pi*f*t+sn(2*pi*f*1.02*t))*.3
   x*=(1-(bt%1))**1.2;x+=.05*r.random()*(1-(bt*4%1))**9 # Kick+Hat
   y=int(max(-1,min(1,x))*32767);w.writeframes(struct.pack('<h',y))
try:mus();p.mixer.music.load(g);p.mixer.music.play(-1)
except:pass
def hue(h):
 h%=1;return [max(0,min(255,int(x*255)))for x in(abs(h*6-3)-1,2-abs(h*6-2),2-abs(h*6-4))]
def plasma(T,t):
 for y in range(0,H,8):
  for x in range(0,W,8):
   v=sn(x*.01+t)+sn(.01*(x*sn(t/2)+y*co(t/3)))+sn(.01*m.sqrt(x*x+y*y)+t)
   p.draw.rect(T,hue(v*.3+t*.1),(x,y,8,8))
def knot(T,t):
 T.fill((0,0,0));pts=[];R=H*.3
 for i in range(100):
  phi=i*.0628;r1=R+R*.3*sn(3*phi+t);x=r1*co(2*phi+t);y=r1*sn(3*phi+t);z=r1*sn(2*phi)
  pz=1/(z/H+2);pts.append((int(W/2+x*pz),int(H/2+y*pz)))
 if len(pts)>1:p.draw.lines(T,hue(t*.5),True,pts,3)
def cube(T,t):
 T.fill((0,0,0));pts=[]
 for i in range(8):
  x,y,z=((i&1)*2-1,(i&2)-1,(i&4)//2-1);ry=t;rz=t*.7;nx=x*co(ry)-z*sn(ry);nz=x*sn(ry)+z*co(ry);x,z=nx,nz
  ny=y*co(rz)-z*sn(rz);nz=y*sn(rz)+z*co(rz);y,z=ny,nz;pz=1/(z+3);pts.append((int(W/2+x*pz*H*.5),int(H/2+y*pz*H*.5)))
 for i,j in [(0,1),(1,3),(3,2),(2,0),(4,5),(5,7),(7,6),(6,4),(0,4),(1,5),(2,6),(3,7)]:p.draw.line(T,hue(t),pts[i],pts[j],2)
def draw(md,T,t):
 if md==0:plasma(T,t)
 elif md==1:cube(T,t)
 elif md==2:knot(T,t)
 else:
  T.fill((10,0,20));[p.draw.circle(T,hue(t+j*.1),(int(W/2+sn(t+j)*200),int(H/2+co(t*1.3+j)*200)),int(20+10*sn(t*2+j)))for j in range(8)]
k,N,run,D,F,tm=0,4,1,6,1.5,0
while run:
 for e in p.event.get():
  if e.type==p.KEYDOWN and e.key==p.K_ESCAPE:run=0
 dt=C.tick(60)/1000;tm+=dt;a=min(1,max(0,(tm-(D-F))/F));t=t0()*1e-3
 draw(k%N,U,t);draw((k+1)%N,V,t);U.set_alpha(int(255*(1-a)));V.set_alpha(int(255*a))
 s.blit(U,(0,0));s.blit(V,(0,0));p.display.flip()
 if tm>D:k+=1;tm=0
