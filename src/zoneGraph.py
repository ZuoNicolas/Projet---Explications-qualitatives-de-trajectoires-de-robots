import sys,math,random,pygame
import pytmx
# PARAMETRES DU JEU
WIDTH = 16*16
HEIGHT = 16*16
FPS = 60
TITLE = "Mon jeu"

# INITIALISATION DU JEU
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE);
rectScreen = screen.get_rect()
tm = pytmx.load_pygame('map1.tmx', pixelalpha=True)
layer = tm.get_layer_by_name('layer1')
fond = pygame.Surface((WIDTH,HEIGHT))

for x, y, image in layer.tiles():
	fond.blit(image,(x*16,y*16))
# ... A COMPLETER AVEC LE CODE DE VOS INITIALISATIONS ...

# BOUCLE DE JEU
clock = pygame.time.Clock()
while True:
	time = clock.tick(FPS)	
	
	# GESTION DES EVENEMENTS
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			pygame.quit()
			sys.exit(0)

	# ... A COMPLETER AVEC LE CODE DE VOTRE JEU ...
	screen.blit(fond,rectScreen)	
	# MAJ DE L'AFFICHAGE
	pygame.display.update()
