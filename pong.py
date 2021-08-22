import pygame
from random import randint, choice
# ----------- Game Initialization -------------------
pygame.init()

displayWidth, displayHeight = 1000, 800

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

# ----------- Constants ---------------
FPS = 30
backgroundColor = "black"
ballSize = 20
ballStart = ((displayWidth/2), displayHeight/2)

scoreFont = pygame.font.SysFont(None, 75)




class Ball:
	""" Class for the ball """
	def __init__(self):
		self.x, self.y = ballStart
		self.size = ballSize
		self.Xspeed = choice([-10, 10]) # Sets horizontal movement to be 10 going left or right
		self.Yspeed = randint(-10, 10) # Gives random vertical movement going up or down 
		self.color = "white"
		self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

	def draw(self): # Method for drawing the ball
		# gameDisplay.blit(self.color, (self.x, self.y))
		pygame.draw.rect(gameDisplay, self.color, self.rect)



class Paddle:
	""" Class for the paddles"""
	def __init__(self, side):
		self.color = "white"
		self.w = ballSize
		self.h = ballSize * 3
		if side == "right":
			self.x = displayWidth - ballSize*2
		else:
			self.x = ballSize
		self.y = ballStart[1]
		print(self.x, self.y, self.w, self.h)
		self.rect = pygame.Rect(self.x, self.y, self.w, self.h)


	def draw(self):
		pygame.draw.rect(gameDisplay, self.color, self.rect)

	def moveUp(self):
		pass

	def moveDown(self):
		pass


class Scores:
	def __init__(self, font):
		self.leftScore = 0
		self.rightScore = 0
		self.leftScoreMessage = font.render(f'{self.leftScore}', True, "white")
		self.rightScoreMessage = font.render(f'{self.rightScore}', True, "white")
	
	def scoreUpdate(self, currentPlayer):
		if currentPlayer == 'left':
			self.leftScore += 1
			self.leftScoreMessage = font.render(f'{self.leftScore}', True, "white")
		else:
			self.rightScore += 1
			self.rightScoreMessage = font.render(f'{self.rightScore}', True, "white")

# Initiate Scores Class Outside Of Main Loop 
# So That The Scores Are Saved
scores = Scores(scoreFont)

# ----------- Main Game Function ---------------
def runGame():
	# Game Variables
	gameRunning = True
	gameOver = False

	paddleLeft, paddleRight = Paddle("left"), Paddle("right")
	ball = Ball()

# ----------- Start Of Game Loop ---------------
	while gameRunning:
		gameDisplay.fill(backgroundColor)

# ----------- Game Over Menu -------------------
		while gameOver == True:
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameOver = False
					gameRunning = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameRunning = False
						gameOver = False
					if event.key == pygame.K_c:
						runGame()

# ----------- Gameplay Handling -------------------
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameRunning = False
			if event.type == pygame.MOUSEBUTTONUP:
				pass
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT or event.key == ord('a'):
					print('left')
				if event.key == pygame.K_RIGHT or event.key == ord('d'):
					print('right')
				if event.key == pygame.K_UP or event.key == ord('w'):
					print('jump')
				if event.key == pygame.K_DOWN or event.key == ord('s'):
					print('down')

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == ord('a'):
					print('left stop')
				if event.key == pygame.K_RIGHT or event.key == ord('d'):
					print('right stop')
				if event.key == pygame.K_DOWN or event.key == ord('s'):
					print('down stop')
				if event.key == ord('q'):
					pygame.quit()
					sys.exit()
					gameRunning = False

#  ----------- Game Code -------------------
		# Draw
		gameDisplay.blit(scores.leftScoreMessage, (displayWidth/2 - 100, 10))
		gameDisplay.blit(scores.rightScoreMessage, (displayWidth/2, 10))

		paddleLeft.draw()
		paddleRight.draw()
		ball.draw()


		# Update
		pygame.display.update()
		clock.tick(FPS)
		
if __name__ == "__main__":
	runGame()