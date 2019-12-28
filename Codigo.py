from visual import *
from visual.graph import *	

scene=display(title=("Movimiento Parabolico"),background=color.white,
              x=800, y=0, width=700, height=700)
scene.range = 60
scene.forward=(-0.41,-0.34,-0.85)
suelo=box(pos=(0,-26.4,0), size=(3200,1,100),material=materials.wood, color=color.orange)

#Cañon
f=frame()
can1=extrusion(pos=[(-18,0,0),(-14,0,0)], shape=shapes.ngon(np=15, length=3),
                 color=color.black,material=materials.wood,scale=[(0.6,0.6),(0.87,0.87)],frame=f)
can2=extrusion(pos=[(-14,0,0),(-9,0,0)], shape=shapes.ngon(np=15, length=3.2),
                 color=color.black,material=materials.wood,scale=[(0.81,0.81),(0.79,0.79)],frame=f)
can3=extrusion(pos=[(-9,0,0),(-5,0,0)], shape=shapes.ngon(np=15, length=2.9),
                 color=color.black,material=materials.wood,scale=[(0.85,0.85),(0.75,0.75)],frame=f)
can4=extrusion(pos=[(-5,0,0),(-2,0,0)], shape=shapes.ngon(np=15, length=2.7),
                 color=color.black,material=materials.wood,scale=[(0.8,0.8),(0.75,0.75)],frame=f)
can5=extrusion(pos=[(-2,0,0),(38,0,0)], shape=shapes.ngon(np=15, length=2)-shapes.ngon(np=15, length=1.2),
                 color=color.black,material=materials.wood,scale=[(1,1),(0.45,0.45)],frame=f)

f1=frame()
#Base 
plat1=extrusion(pos=[(0,-25,0),(0,-24,0)], shape=shapes.ngon(np=15, length=8.4),
                 color=(0.40, 0.22, 0.09),material=materials.wood,frame=f1)
plat2=extrusion(pos=[(0,-26,0),(0,-25,0)], shape=shapes.ngon(np=15, length=8.4),
                 color=(0.40, 0.22, 0.09),scale=[(1,1),(0.98,0.98)],material=materials.wood,frame=f1)
plat3=extrusion(pos=[(0,-25,0),(0,-23.5,0)], shape=shapes.ngon(np=15, length=8),
                 color=(0.40, 0.22, 0.09), material=materials.wood,frame=f1)

plat4=box(pos=(0,-22.5,0), size=(4,2,20),frame=f1,
                 color=color.gray(0.3),material=materials.wood)
plat5=box(pos=(-15,-22.5,0), size=(4,2,20),frame=f1,
                 color=color.gray(0.3),material=materials.wood)
plat6=box(pos=(15,-22.5,0), size=(4,2,20),frame=f1,
                 color=color.gray(0.3),material=materials.wood)
plat7=box(pos=(0,-20.5,0), size=(40,2,20),frame=f1,
                 color=color.gray(0.3),material=materials.wood) 
plat8=box(pos=(-4.5,-20.5,8), size=(50,2,5),frame=f1,
                 color=color.gray(0.3),material=materials.wood)
plat9=box(pos=(-4.5,-20.5,-8), size=(50,2,5),frame=f1,
                 color=color.gray(0.3),material=materials.wood)
#Izquierda
plat10=box(pos=(-4.5,-20,-9), size=(50,2,1),frame=f1,
                 color=color.gray(0.3),material=materials.wood)
plat11=box(pos=(-4.5,-20,-7), size=(50,2,1),frame=f1,
                 color=color.gray(0.3),material=materials.wood)

#Derecha
plat12=box(pos=(-4.5,-20,9), size=(50,2,1),frame=f1,
                 color=color.gray(0.3),material=materials.wood)
plat13=box(pos=(-4.5,-20,7), size=(50,2,1),frame=f1,
                 color=color.gray(0.3),material=materials.wood)

#Ruedas Izquierdas
plat14=extrusion(pos=[(0,-17,-7.6),(0,-17,-8.6)], shape=shapes.ngon(np=10, length=1.5),
                 color=(color.gray(0.5)),material=materials.wood,frame=f1)
plat15=extrusion(pos=[(-20,-17,-7.6),(-20,-17,-8.6)], shape=shapes.ngon(np=10, length=1.5),
                 color=color.gray(0.5),material=materials.wood,frame=f1)

plat16=box(pos=(-10,-17,-6.5),size=(26,4,2),frame=f1,
                 color=color.gray(0.1),material=materials.wood)
#Ruedas Derechas
plat28=extrusion(pos=[(0,-17,7.6),(0,-17,8.6)], shape=shapes.ngon(np=10, length=1.5),
                 color=(color.gray(0.5)),material=materials.wood,frame=f1)
plat29=extrusion(pos=[(-20,-17,7.6),(-20,-17,8.6)], shape=shapes.ngon(np=10, length=1.5),
                 color=(color.gray(0.5)),material=materials.wood,frame=f1)

plat30=box(pos=(-10,-17,6.5),size=(26,4,2),frame=f1,color=color.gray(0.1))

#base para el cañon
plat17=cylinder(pos=(-20,-17,-9),axis=(0,0,4), color=color.gray(1), radius=0.5,frame=f1,material=materials.wood)
plat18=cylinder(pos=(-20,-17,5),axis=(0,0,4), color=color.gray(1), radius=0.5,frame=f1,material=materials.wood)
plat19=cylinder(pos=(0,-17,-9),axis=(0,0,4), color=color.gray(1), radius=0.5,frame=f1,material=materials.wood)
plat20=cylinder(pos=(0,-17,5),axis=(0,0,4), color=color.gray(1), radius=0.5,frame=f1,material=materials.wood)

plat21=cylinder(pos=(0,0,-6), axis=(0,0,12),radius=2,frame=f1,
                 color=color.gray(1),material=materials.wood)
plat22=cylinder(pos=(0,0,-7), axis=(0,0,14), radius=1.5,frame=f1,
                 color=color.gray(1),material=materials.wood)
plat23=cylinder(pos=(0,0,-7.5), axis=(0,0,15), radius=0.2,frame=f1,
                 color=color.gray(1),material=materials.wood)
plat24=box(pos=(0,-9,-6), size=(5,18,1),frame=f1,
                 color=color.gray(1),material=materials.wood)
plat25=box(pos=(0,-9,6), size=(5,18,1),frame=f1,
                 color=color.gray(1),material=materials.wood)

plat26=box(pos=(-10,-10,6), size=(5,27,1),
                 color=color.gray(1),material=materials.wood)
plat26.rotate(angle=(-pi/4),axis=(0,0,1),
                 color=color.gray(1),material=materials.wood)
plat27=box(pos=(-10,-10,-6), size=(5,27,1),
                 color=color.gray(1),material=materials.wood)
plat27.rotate(angle=(-pi/4),axis=(0,0,1),
                 color=color.gray(1),material=materials.wood)

plat28=box(pos=(0,-18,-5),size=(1,5,0.5),
                 color=color.gray(1),material=materials.wood),
plat29=box(pos=(0,-18,5),size=(1,5,0.5),
                 color=color.gray(1),material=materials.wood)


T=gcurve(color=color.white)
#Movimiento
while True:
      angulo=int(raw_input("Entre el angulo= "))
      if angulo<0 or angulo>180:
            print("El angulo debe estar entre 0 y 180")
      else:
            break
      
instrucion = """
    Haga click 
aqui para continuar
"""
Boton=label(xoffset=1, yoffset=100, opacity=0.5, text=instrucion,color=color.blue)

sw=0 
while sw==0:
    rate(70)
    if scene.mouse.clicked:
        Boton.visible=False     
        for i in range(angulo):
            rate(20)
            f.rotate(angle=(2*pi)/360, axis=(0,0,1))
            sw=1  


alturainicial=0
velocidadinicial=int(raw_input("Entre la Velocidad incial= "))


bola=sphere(pos=(0,alturainicial,0), radius=3, 
                 color=(0.06,0.05,0.04),material=materials.rough, make_trail=true)

t=0; dt=0.01; g=9.8

aceleracion=vector(0,-g,0)

velocidad=vector(velocidadinicial*cos(angulo*pi/180), 
             velocidadinicial*sin(angulo*pi/180),0)

z=60
while true:
      rate(100)
      x=bola.pos.y
      T.plot(pos=(t,x))
      velocidad=velocidad+(aceleracion*t)
      bola.pos=(velocidadinicial*cos(angulo*pi/180)*t,
                  alturainicial+velocidadinicial*sin(angulo*pi/180)*t-4.9*t**2)
      scene.range=z
      if bola.y <=suelo.pos.y+3.5:
            break
      t+=dt
      z=z+1
