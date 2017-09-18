import pygame, random
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
clock = pygame.time.Clock()

while (True):
	clock.tick(120)
	screen.fill(white)
	
	class Sand():
		def __init__(self):
			self.image = pygame.image.load("pexplosion.jpg")
			self.rect = self.image.get_rect()
			self.velox = 0
			while (self.velox == 0):
				self.velox = random.randint(-10,10)/10
			self.veloy = 0
			while (self.veloy == 0):
				self.veloy = random.randint(-10,10)/10
			self.x = xa
			self.y = ya
		
		def Fall(self):
			self.rect.topleft = (self.x,self.y)
			self.x += self.velox
			self.y += self.veloy
			screen.blit(self.image, self.rect)
			
	
	xa, ya = pygame.mouse.get_pos()
	
	if pygame.mouse.get_pressed()[0]:
		sand = Sand()
		sandl.append(sand)
		
	for i in range(0,len(sandl)):
		sandl[i].Fall()
	
	
	
	pygame.display.flip()
	event = pygame.event.poll()
	if (event.type == pygame.QUIT):
		break
