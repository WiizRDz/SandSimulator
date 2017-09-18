import pygame
screen = pygame.display.set_mode((1000,750))
pygame.display.set_caption("Sand")
pygame.font.init()
pygame.init()

#Colours
if (True):
	black = (0,0,0)
	white = (255,255,255)
	red = (255,0,0)
	green = (0,255,0)
	dark_green = (30,140,47)
	blue = (0,0,255)
	brown = (83,67,27)
	yellow = (255,255,0)
	gray = (150, 150, 150)

sandl = []
sandloc = []

while (True):
	screen.fill(white)
	
	class Sand():
		def __init__(self):
			self.image = pygame.image.load("pexplosion.jpg")
			self.x = xa
			self.y = ya
			
		def ID(self):
			self.loc = sandl.index(sand)
		
		def Fall(self):
			screen.blit(self.image, (self.x,self.y))
			try:
				sandloc[self.loc] = (self.x,self.y)
			except IndexError:
				sandloc.append("")
				sandloc[self.loc] = (self.x,self.y)
			if self.loc != 0:
				try:
					pygame.draw.line(screen, black, (sandloc[self.loc]),(sandloc[self.loc-1]), 6)
				except IndexError:
					pass
			
	
	xa, ya = pygame.mouse.get_pos()
	
	if pygame.mouse.get_pressed()[0]:
		sand = Sand()
		sandl.append(sand)
		sand.ID()
		
	for i in range(0,len(sandl)):
		sandl[i].Fall()
	
	
	
	pygame.display.flip()
	event = pygame.event.poll()
	if (event.type == pygame.QUIT):
		break
