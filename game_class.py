import pygame
import time
from settings import *
from sprites import *

pygame.init()
pygame.mixer.init()
pygame.font.init()

class game:
	def __init__(self):
		self.win = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption('PingPong')
		self.clock = pygame.time.Clock()
		self.running = True
		self.playing = True
		self.font_name = pygame.font.match_font(FONT_NAME)
		self.sprites()
		self.score_value = 0
		self.score_value2 = 0

	def sprites(self):
		self.all_sprites = pygame.sprite.Group()
		self.player1 = p1()
		self.player2 = p2()
		self.ball = ball()
		self.c = collision()
		self.all_sprites.add(self.player1, self.player2, self.ball)

	def new(self):
		self.run()

	def run(self):
		self.clock.tick(FPS)
		self.win.blit(bg, (0, 0))
		self.events()
		self.draw()
		self.update()
		self.counter()
		while self.playing:
			self.clock.tick(FPS)
			self.win.blit(bg, (0, 0))
			self.events()
			self.draw()
			self.update()

	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				if self.playing:
					self.playing = False
				self.running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					self.pause_screen()

		# player1 in grief
		if self.ball.rect.right >= WIDTH:
			self.ball.rect.center = (WIDTH / 2, HEIGHT / 2)
			self.ball.x_vel *= -1
			self.score_value += 1
			self.player2.rect.y = 0
			time.sleep(2)
		# player2 in grief
		if self.ball.rect.left <= 0:
			self.ball.rect.center = (WIDTH / 2, HEIGHT / 2)
			self.ball.x_vel *= -1
			self.score_value2 += 1
			self.player2.rect.y = 0
			time.sleep(2)

		self.player1.event()
		self.player2.event()

		self.ball.update()

		# player1 in grief
		if self.ball.rect.right >= WIDTH:
			self.ball.rect.center = (WIDTH / 2, HEIGHT / 2)
			self.ball.x_vel *= -1
			self.score_value += 1
			self.player2.rect.y = 0
		# player2 in grief
		if self.ball.rect.left <= 0:
			self.ball.rect.center = (WIDTH / 2, HEIGHT / 2)
			self.ball.x_vel *= -1
			self.score_value2 += 1
			self.player2.rect.y = 0

		self.show_score(220, 10, 500, 10)

		# player1 or player2 hits the ball
		if self.c.checkCollision(self.player1, self.ball):
			self.ball.x_vel *= -1
		if self.c.checkCollision(self.player2, self.ball):
			self.ball.x_vel *= -1

	def draw(self):
		self.all_sprites.draw(self.win)
		self.show_score(220, 10, 500, 10)

	def update(self):
		pygame.display.flip()

	def show_score(self, x, y, x2, y2):
		self.score = font.render('Player1 : ' + str(self.score_value), True, (255, 255, 255))
		self.score_2 = font.render('Player2 : ' + str(self.score_value2), True, (255, 0, 0))
		self.win.blit(self.score, (x, y))
		self.win.blit(self.score_2, (x2, y2))

	def start_screen(self):
		self.draw_text('PingPong', 70, RED, 270, 150)
		self.draw_text('Press any key to start', 40, WHITE, 320, 250)
		self.draw_text('Developer = Aadish Saini @karn', 30, CYAN, 500, 530)
		pygame.display.flip()
		self.waiting_for_key()

	def pause_screen(self):
		self.draw_text('Paused', 30, BLACK, 270, 150)
		self.draw_text('Press any key to resume', 40, WHITE, 320, 250)
		self.draw_text('Developer = Aadish Saini @karn', 30, CYAN, 500, 530)
		pygame.display.flip()
		self.waiting_for_key()

	def game_over_screen(self):
		self.win.fill(WHITE)
		self.draw_text('PingPong', 70, RED, 270, 150)
		self.draw_text('GAME OVER press anykey to play again', 40, RED, 80, 250)
		self.draw_text('Developer = Aadish Saini @karn', 30, CYAN, 500, 530)
		self.draw_text('Player1 = '+str(self.score_value), 25, CYAN, 100, 530)
		self.draw_text('Player2 = '+str(self.score_value2), 25, CYAN, 250, 530)
		pygame.display.flip()
		self.waiting_for_key()

	def waiting_for_key(self):
		waiting = True
		while waiting:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					waiting = False
					self.running = False
				if event.type == pygame.KEYDOWN:
					waiting = False

	def draw_text(self, text, size, color, x, y):
		font = pygame.font.Font(self.font_name, size)
		text_surface = font.render(text, True, color)
		text_rect = text_surface.get_rect()
		text_rect.x = x
		text_rect.y = y
		self.win.blit(text_surface, text_rect)
	
	def counter(self):
		time.sleep(2)

