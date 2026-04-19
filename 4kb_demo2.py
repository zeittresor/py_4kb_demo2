import pygame as p,math as m,random as r,os,tempfile,wave,struct
p.init();p.mixer.init(22050,-16,1,512);X=p.display.Info();W,H=X.current_w,X.current_h;s=p.display.set_mode((W,H),p.FULLSCREEN);S,C,T,I=m.sin,m.cos,m.tau,int;d=p.draw;cl=p.time.Clock();gt=p.time.get_ticks;g=os.path.join(tempfile.gettempdir(),'d4.wav')
U,V=[p.Surface((W,H)).convert_alpha()for _ in'12']
def hc(h,q=0):
 h=(h+q*.071)%1;a=[abs(h*6-3)-1,2-abs(h*6-2),2-abs(h*6-4)];return tuple(max(0,min(255,I(x*255)))for x in a)
td=os.path.join(tempfile.gettempdir(),'4kv_tex');os.makedirs(td,exist_ok=True);Q=[]
for j in range(10):
 fn=os.path.join(td,str(j)+'.bmp')
 try:q=p.image.load(fn).convert()
 except Exception:
  q=p.Surface((48,48))
  for y in range(48):
   for x in range(48):
    v=S((x*x+y*j+13*j)*.04)+C((y*y+x*j)*.05)+r.random()*.9;q.set_at((x,y),hc(v*.12+r.random()*.08,j))
  try:p.image.save(q,fn)
  except Exception:pass
 Q+=q.convert(),
F=p.font.SysFont('Segoe UI Emoji',92);E=[]
for c in'☻★!?@#AI':
 try:E+=F.render(c,1,(255,255,255)).convert_alpha(),
 except Exception:E+=p.Surface((10,10),p.SRCALPHA),
def mus():
 sr,du=22050,210;n=sr*du;P=[0,3,5,7,10,8,5,7,12,10,7,3];M=[0,2,3,7,10,12,14,15,12,10,7,5,3,2,7,10,17,15,14,10,7,5,2,0];B=[0,0,7,0,10,7,5,3]
 with wave.open(g,'wb')as w:
  w.setparams((1,2,sr,n,'NONE',''))
  for i in range(n):
   t=i/sr;b=t*2.85;bt=I(b);f=b%1;ba=bt//4;ro=P[(ba//4)%12];x=0;e=(1-f)**.68;hz=55*2**((ro+B[(bt+ba)%8])/12)
   x+=S(T*hz*t+.55*S(T*hz*2*t))*e*.26
   st=I(b*2);no=ro+M[(st+ba*5+bt//13)%24]+(12 if ba>8 and st%9==0 else 0);le=(1-(b*2%1))**2.35;fq=220*2**(no/12);x+=S(T*fq*t+S(T*fq*t)*.7)*le*.18
   for o in(0,3,7,12):x+=S(T*110*2**((ro+o)/12)*t+S(t*.23+o))*.026
   if bt>8:k=(1-f)**8;x+=S(T*(35+145*k)*t)*k*.62
   z=r.random()*2-1
   if bt>16 and bt%4==2:x+=z*(1-f)**13*.27
   if bt>24:x+=z*(1-(b*2%1))**30*.085
   if bt>56 and bt%16>13:x+=S(T*(660+55*(bt%12))*t)*(1-f)*.09
   w.writeframes(struct.pack('<h',I(max(-1,min(1,x))*32767)))
mus();p.mixer.music.load(g);p.mixer.music.play(-1)
def proj(x,y,z,a,b,c,cx,cy,sc):
 y,z=y*C(a)-z*S(a),y*S(a)+z*C(a);x,z=x*C(b)+z*S(b),-x*S(b)+z*C(b);x,y=x*C(c)-y*S(c),x*S(c)+y*C(c);z+=4.2;q=H*sc/z;return I(cx+x*q),I(cy+y*q),z
def obj(A,cx,cy,t,k,bt):
 M=k%5
 if M==0:V=[(-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)];F=[(0,1,2,3),(4,5,6,7),(0,1,5,4),(2,3,7,6),(1,2,6,5),(0,3,7,4)]
 elif M==1:V=[(0,-1.4,0),(1,1,1),(-1,1,1),(-1,1,-1),(1,1,-1)];F=[(0,1,2),(0,2,3),(0,3,4),(0,4,1),(1,2,3,4)]
 elif M==2:V=[(0,-1.4,0),(1,0,1),(0,1.4,0),(-1,0,1),(0,0,-1.4)];F=[(0,1,4),(1,2,4),(2,3,4),(3,0,4),(0,1,2,3)]
 elif M==3:V=[(-1.4,-.8,-.3),(1.4,-.8,-.3),(1.4,.8,-.3),(-1.4,.8,-.3),(-1.2,-.6,.35),(1.2,-.6,.35),(1.2,.6,.35),(-1.2,.6,.35)];F=[(0,1,2,3),(4,5,6,7),(0,4,7,3),(1,5,6,2),(0,1,5,4),(3,2,6,7)]
 else:V=[(S(i*T/9)*(1+.4*(i%2)),C(i*T/9)*(1+.2*((i+1)%3)),S(i*2.2))for i in range(9)];F=[tuple(range(9))]+[(i,(i+1)%9,(i+4)%9)for i in range(9)]
 P=[proj(x*(1+.35*S(k)),y*(1+.25*C(k*.7)),z,t*.7+k,t*.43+k*.2,t*.31,cx,cy,.78)for x,y,z in V]
 for fa in sorted(F,key=lambda f:sum(P[i][2]for i in f)):
  pts=[P[i][:2]for i in fa];col=hc(t*.05+sum(fa)*.04,k)
  if (k+len(fa))&1:d.polygon(A,tuple(min(255,I(v*(.55+bt*.7)))for v in col),pts,0)
  d.polygon(A,(255,255,255),pts,1+I(bt*3))
def dr(k,A,t):
 q,bt=(k*7+1)%13,(1-(t*2.85%1))**2;A.fill(0);cx,cy=W/2+S(t*.29+k)*W*.24,H/2+C(t*.23+k)*H*.23
 if q==0:
  ox=I((S(t+k)+1)*17);oy=I((C(t*.7+k)+1)*17)
  for y in range(0,H,24):
   for x in range(0,W,24):v=S((x+ox)*.012+t)+S((y+oy)*.014*C(t*.6))+S(m.hypot(x-cx,y-cy)*.013);d.rect(A,hc(v*.17,k),(x,y,24,24))
 elif q==1:
  P=[];vp=(cx+S(t*.7)*W*.3,cy+C(t*.5)*H*.25)
  for i in range(230):
   z=(i*.017-t*(.45+k%6*.12))%1+.018;a=i*12.989+k*9.1;x=(S(a)*W*.58+S(i*3.1)*W*.08)/z+vp[0];y=(C(a*1.37)*H*.36+C(i*2.4)*H*.08)/z+vp[1];P+=(I(x),I(y),z),;d.circle(A,(255,255,255),P[-1][:2],max(1,I(1.8/z)))
  for i in range(0,60,2):d.line(A,(220,230,255),P[i][:2],P[(i*7+k)%230][:2],1)
 elif q==2:
  for j in range(1,24):z=j-t%1;ay=cy+H/(z*.34);c=hc(j*.04+t*.05,k);d.line(A,c,(0,I(ay)),(W,I(ay)),I(1+bt*4));xx=I(cx+S(t+k)*W/z);d.line(A,c,(xx,0),(xx,H),1)
 elif q==3:obj(A,cx,cy,t,k,bt)
 elif q==4:
  for i in range(95):
   z=(i*.041-t*.28)%3+.55;x=((i*61+k*13)%260-130)*W/420;y=((i*97+k*7)%170-85)*H/260;a=max(6,I((50+30*bt)/z));qv=Q[(i+k)%10];xo=(i*7+I(t*17)+k*5)%24;yo=(i*11+I(t*13)+k*3)%24;R=p.transform.rotate(p.transform.scale(qv.subsurface((xo,yo,24,24)),(a,a)),t*30+i*9);A.blit(R,(I(cx+x/z-R.get_width()/2),I(cy+y/z-R.get_height()/2)))
 elif q==5:
  for i,e in enumerate(E*3):
   z=(i*.12-t*.18)%3+.7;ang=t*70+i*29+k*13;R=p.transform.rotozoom(e,ang,(.22+bt*.18)/z);x=cx+S(i*1.7+t*.9)*W*.42/z;y=cy+C(i*1.3+t*.7)*H*.25/z;A.blit(R,(I(x-R.get_width()/2),I(y-R.get_height()/2)))
 elif q==6:
  N=6+k%8;P=[]
  for i in range(N):a=i*T/N+t*.75;P+=(I(cx+S(a)*H*.55/(1.4+C(t+i))),I(cy+C(a*1.7)*H*.38/(1.6+S(t+i*.7)))),
  if k&2:d.polygon(A,hc(t,k),P,0)
  for i in range(N):
   d.circle(A,(255,255,255),P[i],3+I(bt*4))
   for j in range(i):
    if(i*j+k)%3<2:d.line(A,hc((i+j)*.03+t,k),P[i],P[j],1+I(bt*2))
 elif q==7:
  for i in range(32):R=H*(.035+i*.03+bt*.035);x=cx+S(t+i)*R;y=cy+C(t*.7+i)*R;d.rect(A,hc(i*.04+t,k),(I(x-R),I(y-R),I(R*2),I(R*2)),I(1+bt*5))
 elif q==8:
  for x in range(0,W,18):
   y=I((t*230+x*(k%9+1))%H)
   for j in range(7):d.rect(A,hc(.33+j*.03+t*.05,k),(x,(y-j*30)%H,12,22),1)
 elif q==9:
  for y in range(-7,8):
   for x in range(-9,10):
    X,Y,Z=x*.25,y*.25,S(x*.7+t)+C(y*.6+t*.8);P=proj(X,Y,Z,t*.55,t*.3,t*.2,cx,cy,1.3);R=5+I(10/(P[2]*.35));d.circle(A,hc(Z*.08+t*.04,k),P[:2],R)
 elif q==10:
  for i in range(70):a=i*T/70+t*(1+k%3);r1=H*.25+bt*340;d.line(A,hc(i*.02+t*.1,k),(I(cx),I(cy)),(I(cx+S(a)*r1),I(cy+C(a)*r1)),I(1+bt*7))
 elif q==11:
  for i in range(18):R=65+i*35+bt*120;d.circle(A,hc(t+i*.03,k),(I(cx+S(t+i)*R),I(cy+C(t+i)*R)),I(15+bt*95),I(1+bt*9))
 else:
  for i in range(30):
   a=t+i*.33;P=[proj(S(a+j*T/5)*(1+i*.015),C(a*1.3+j*T/5)*(1+i*.01),S(a+j)*1.5,t+i*.01,t*.6,t*.2,cx,cy,.95)[:2]for j in range(5)]
   d.polygon(A,hc(i*.025+t,k),P,i%3==0)
 return bt
k=tm=0
while 1:
 if any(e.type in(p.QUIT,p.KEYDOWN)for e in p.event.get()):p.quit();exit()
 dt=cl.tick(60)/1000;tm+=dt;t=gt()*1e-3;a=min(1,max(0,(tm-8.5)/1.5));bt=dr(k,U,t);dr(k+1,V,t);U.set_alpha(I(255*(1-a)));V.set_alpha(I(255*a));s.fill(0);s.blit(U,(0,0));s.blit(V,(0,0))
 if bt>.92:z=1.05+bt*.04;R=p.transform.scale(s,(I(W*z),I(H*z)));s.blit(R,(-I(W*(z-1)/2),-I(H*(z-1)/2)),special_flags=p.BLEND_RGB_ADD)
 p.display.flip()
 if tm>10:k+=1;tm=0
