import pygame, sys, random, os

opacity = 255
i = 0

def ball_animation():
	global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
	ball.x += ball_speed_x
	ball.y += ball_speed_y

	if ball.top <= 0 or ball.bottom >= screen_height:
		ball_speed_y *= -1

	# player score	
	if ball.left <= 0:
		player_score += 1
		score_time = pygame.time.get_ticks()

	# opponent score	
	if ball.right >= screen_width:
		opponent_score += 1
		score_time = pygame.time.get_ticks()

	if ball.colliderect(player) and ball_speed_x > 0:
		if abs(ball.right - player.left) < 10:
			ball_speed_x *= -1
		elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
			ball_speed_y *= -1
		elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
			ball_speed_y *= -1

	if ball.colliderect(opponent) and ball_speed_x < 0: 
		if abs(ball.left - opponent.right) < 10:
			ball_speed_x *= -1
		elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
			ball_speed_y *= -1
		elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
			ball_speed_y *= -1

def player_animation():
	player.y += player_speed
	if player.top <= 0:
		player.top = 0
	if player.bottom >= screen_height:
		player.bottom = screen_height

def opponent_animation():
	opponent.y += opponent_speed 
	if opponent.top <= 0:
		opponent.top = 0
	if opponent.bottom >= screen_height:
		opponent.bottom = screen_height

def ball_start():
	global ball_speed_x, ball_speed_y, score_time

	current_time = pygame.time.get_ticks()
	ball.center = (screen_width/2, screen_height/2)

	if current_time - score_time < 700:
		number_three = game_font.render("3", False, white)
		screen.blit(number_three, (screen_width/2 - 10, screen_height/2 + 20))
	if 700 < current_time - score_time < 1400:
		number_number = game_font.render("2", False, white)
		screen.blit(number_number, (screen_width/2 - 10, screen_height/2 + 20))
	if 1400 < current_time - score_time < 2100:
		number_one = game_font.render("1", False, white)
		screen.blit(number_one, (screen_width/2 - 10, screen_height/2 + 20))

	if current_time - score_time < 2100:
		ball_speed_x, ball_speed_y = 0,0
	else:
		ball_speed_y = 10 * random.choice((1, -1))
		ball_speed_x = 10 * random.choice((1, -1))
		score_time = None

def game_win():
	while opponent_score == 4:
		os.system('python winscreenp2.py')
		pygame.quit()
		sys.exit()
	while player_score == 4:
		os.system('python winscreenp1.py')
		pygame.quit()
		sys.exit()

def overlay_icon(image, pos):
	arrow_surface = pygame.image.load(image)
	arrow_surface = pygame.transform.scale(arrow_surface, (150, 100))
	arrow_surface.set_alpha(opacity)
	screen.blit(arrow_surface, pos)

def mutation_1():
	global ball_speed_x, ball_speed_y, mutation_1_comp
	if mutation_1_comp == False:
		ball_speed_x *= 1.4
		ball_speed_y *= 1.4
		mutation_1_comp = True


# normal game set up
pygame.mixer.pre_init()
pygame.init()
clock = pygame.time.Clock()

# to set the screen size of the main window
screen_width = 1280
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('PONG:Reimagined')

# Rectangles for the game

ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)


bg_color = pygame.Color(0, 0, 0)
ball_color = (255, 255, 255)
line_color = (132, 132, 130)
player_color = (0, 255, 0)
opponent_color = (255, 0, 0)
white = (255, 255, 255)

# game variables
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 0

# score timer
score_time = True

# muation complete 
mutation_1_comp = False

# text variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)

  
# Set image as icon
img = pygame.image.load('ping-pong.png')
pygame.display.set_icon(img)

# condition for the game to run

while True:
	#Handling input
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
       # rest of the code	

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				player_speed += 7
			if event.key == pygame.K_UP:
				player_speed -= 7
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_DOWN:
				player_speed -= 7
			if event.key == pygame.K_UP:
				player_speed += 7

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				opponent_speed += 7
			if event.key == pygame.K_s:
				opponent_speed -= 7
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_s:
				opponent_speed += 7
			if event.key == pygame.K_w:
				opponent_speed -= 7

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_c:
				opacity = 255

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_m:
				# mutation = random.randint(1,2)
				# if mutation == 1:
				mutation_1()



    # rest of the code	

	ball_animation()
	player_animation()
	opponent_animation()
	game_win()



	
	#game visuals
	screen.fill(bg_color)
	pygame.draw.rect(screen, player_color, player)
	pygame.draw.rect(screen, opponent_color, opponent)
	pygame.draw.ellipse(screen, ball_color, ball)
	pygame.draw.aaline(screen, line_color, (screen_width/2,0), (screen_width/2, screen_height))
	if opacity > 0:
		overlay_icon("ppkeys.png", (200, 250)) # image 1
		overlay_icon("pparrow.png", (930, 250)) # image 2


	if opacity > 0:
		i += 1
		if i > 5:
			if opacity > 0:
				opacity -= 10

			i = 0

	if score_time:
		mutation_1_comp = False
		ball_start()


	player_text = game_font.render(f"{player_score}", False, white)
	screen.blit(player_text, (660, 470))

	opponent_text = game_font.render(f"{opponent_score}", False, white)
	screen.blit(opponent_text, (600, 470))


	#updating the gamme window
	pygame.display.flip()
	clock.tick(75)

