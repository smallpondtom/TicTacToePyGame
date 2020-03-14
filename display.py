import pygame, sys, random
from control import *
from pygame.locals import *

def main():
	pygame.init()
    # Open Pygame window
	screen = pygame.display.set_mode((640, 480))  # add RESIZABLE or FULLSCREEN
    # Title
	pygame.display.set_caption("TICTACTOE")

	color = pygame.color.THECOLORS["black"]
	tab2 = pygame.image.load("resources/morp_tab.png").convert()
	tab2.set_colorkey((0, 0, 0))
	tab_pos = (170, 90)

	cross = pygame.image.load("resources/cross.png").convert()
	cross.set_colorkey((0, 0, 0))
	cross_list = []

	circle = pygame.image.load("resources/circle.png").convert()
	circle.set_colorkey((0, 0, 0))
	circle_list = []

	cpu_level = 3
	cpu = 0
	player = 0
	draw = 0

	crossStone = tictactoe.getCross()
	circleStone = tictactoe.getCircle()
	turn = 'player'
	font = pygame.font.SysFont('Arial', 30)

	tab_case = [(170, 90), (270, 90), (370, 90),
                (170, 190), (270, 190), (370, 190),
                (170, 290), (270, 290), (370, 290)]

	pygame.key.set_repeat(400, 30)

	game = tictactoe()
	ai = mai(game, cpu_level, circleStone)

	while True:

        # loop speed limitation
        # 60 frames per second is enought
		pygame.time.Clock().tick(6)

		for event in pygame.event.get():  # wait for events
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

            # keyboard commands
			if event.type == KEYDOWN:
				if event.key == K_UP:
					if cpu_level < 9:
						cpu_level += 1
				elif event.key == K_DOWN:
					if cpu_level > 1:
						cpu_level -= 1
				ai.changeDepth(cpu_level)

			if event.type == MOUSEBUTTONDOWN:
				if game.done():
					if game.game(crossStone):
						player += 1
					if game.game(circleStone):
						cpu += 1
					if game.draw():
						draw += 1
					cross_list = [];
					circle_list = [];
					screen.fill(color);
					turn = "player"
					screen.blit(tab2, tab_pos);
					pygame.display.flip();
					game.clear()

				if event.button == 1:
					if turn == "player":
						for i in range(9):
							if event.pos[0] > tab_case[i][0] and event.pos[0] < tab_case[i][0] + 100 and event.pos[1] > tab_case[i][1] and event.pos[1] < tab_case[i][1] + 100:
								if not tab_case[i] in cross_list and not tab_case[i] in circle_list:
									x = int(i / 3)
									y = int(i % 3)
									game.update(x, y, crossStone)
									cross_list.append(tab_case[i])
									turn = 'cpu'

				if turn == 'cpu' and not game.done():
					move = ai.move()
					x = move[0]
					y = move[1]
					game.update(x, y, circleStone)
					i = x * 3 + y
					circle_list.append(tab_case[i])
					turn = 'player'

		screen.fill(color)

		if game.game(crossStone):
			text = font.render(("You Win"), True, (0, 250, 0))
			screen.blit(text, (270, 400))	
		if game.game(circleStone):
			text = font.render(("You Lose"), True, (250, 0, 0))
			screen.blit(text, (270, 400))
		if game.draw():
			text = font.render(("Draw"), True, (0, 0, 250))
			screen.blit(text, (285, 400))

		text = font.render(("CPU Level=" + str(cpu_level)), True, (250, 250, 250))
		screen.blit(text, (480, 0))
		text = font.render(("CPU=" + str(cpu)), True, (250, 0, 0))
		screen.blit(text, (180, 0))
		text = font.render(("Player=" + str(player)), True, (0, 250, 0))
		screen.blit(text, (0, 0))
		text = font.render(("Draw=" + str(draw)), True, (0, 0, 250))
		screen.blit(text, (340, 0))

		screen.blit(tab2, tab_pos)
		for cross_pos in cross_list:
			screen.blit(cross,cross_pos)
		for circle_pos in circle_list:
			screen.blit(circle,circle_pos)
		pygame.display.flip()

if __name__ == '__main__':
	main()

