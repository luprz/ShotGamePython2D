import pygame
import random

pygame.init()
disparo=pygame.mixer.Sound("disparo.wav")
grito=pygame.mixer.Sound("grito.wav")
pantalla=pygame.display.set_mode((480,500))
fuente=pygame.font.SysFont("Arial",20,True,False)
fuente2=pygame.font.SysFont("Arial",12,True,False)
info=fuente2.render("Tienes 10 segundo para destruir los rectandulos",0,(255,255,255))
pygame.display.set_caption("Tutorial de Pygame 2!")
salir=False
reloj1=pygame.time.Clock()
listarec=[]
segundoint=0
termino=False
rotos=0


for x in range(25):
	w=random.randrange(5,25)
	h=random.randrange(5,25)
	x=random.randrange(450)
	y=random.randrange(450)
	listarec.append(pygame.Rect(x,y,w,h))
	r1=pygame.Rect(0,0,5,25)
	r2=pygame.Rect(0,0,25,5)
	
while salir!=True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			salir=True 
		if event.type==pygame.MOUSEBUTTONDOWN:
			disparo.play()
			for recs in listarec:
				if termino==False:
					if r1.colliderect(recs):
						grito.play()
						recs.width=0
						recs.height=0
						rotos+=1	
	
	reloj1.tick(20)	
	(r2.left,r2.top)=pygame.mouse.get_pos()
	(r1.left,r1.top)=pygame.mouse.get_pos()	 
	r1.top-=r1.height/2
	r2.right-=r1.width*2 
	pantalla.fill((0,0,0))
	
	for recs in listarec:
		pygame.draw.rect(pantalla, (0,200,0),recs)
			
	pygame.draw.rect(pantalla,(200,20,20),r1)
	pygame.draw.rect(pantalla,(200,20,20),r2)
	pantalla.blit(info,(5,5))
	
	if segundoint>=10:
		termino=True
		
	if termino==False:	
		segundoint = pygame.time.get_ticks()/1000
		segundos = "Time: "+str (segundoint)
		contador=fuente.render(segundos,0,(0,0,230))
	else:
		mensaje = str(" Game Over! ")		
		contador=fuente.render(segundos,0,(0,0,230))
		gameover=fuente.render(mensaje,0,(0,0,230))	
		pantalla.blit(gameover,(190, 220))
		
	rotos2 = "Objetivos: "+str(rotos)
	puntaje= fuente.render(rotos2,0,(200,20,50))	
	pantalla.blit(puntaje,(280,5))		
	pantalla.blit(contador,(400,5))
	pygame.display.update()
	
pygame.quit()			
