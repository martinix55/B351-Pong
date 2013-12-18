import pygame
import random
import sys

dimensions = (700, 500)
user_score = 0
ai_score = 0
red = (255, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 205)
ball_move = False
exit = False
user_start = False
move_user_up = False
move_user_down = False
user = False
ai = True

pygame.init()
screen = pygame.display.set_mode(dimensions)
pygame.display.set_caption("B351 AI Pong")

ball_start = (((dimensions[0] / 2) - 8.5) , (dimensions[1] / 2))
ball_x_speed = 0
ball_x_acc = 1
ball_y_speed = 0
ball_y_acc = 1
ball_dimensions = (17, 17)
hit = 0
ball = pygame.Rect(ball_start, ball_dimensions)

paddle_dimensions = (16, 65)
user_paddle_start = ((dimensions[0] - 40 ), (dimensions[1] / 2 - (paddle_dimensions[1] / 2)))
ai_paddle_start = ((dimensions[0] - 673 ), (dimensions[1] / 2 - (paddle_dimensions[1] / 2)))
if sys.argv[1] == "easy":
	ai_paddle_speed = 2
elif sys.argv[1] == "medium":
	ai_paddle_speed = 3
elif sys.argv[1] == "hard":
	ai_paddle_speed = 5
else:
	ai_paddle_speed = 8
user_paddle_speed = ai_paddle_speed + 1
user_paddle = pygame.Rect(user_paddle_start, paddle_dimensions)
ai_paddle = pygame.Rect(ai_paddle_start, paddle_dimensions)

half_court_size = (8, 500)
wall_size = (700, 8)
half_court = pygame.Rect((dimensions[0] / 2 - 4, 0), half_court_size)
right_wall = pygame.Rect((dimensions[0] - 7, 0), half_court_size)
left_wall = pygame.Rect((dimensions[0] - 701, 0), half_court_size)
bottom_wall = pygame.Rect((0, 493), wall_size)
top_wall = pygame.Rect((0, -1), wall_size)

user_font_position = ((dimensions[0] / 2 + 30) , dimensions[1] / 200)
ai_font_position = ((dimensions[0] / 2 - 75) , dimensions[1] / 200)
font = pygame.font.SysFont("Comic Sans MS", 65)

if user_score == 0 and ai_score == 0:
	print
	print("You are playing the AI set on " + sys.argv[1] + ". Good luck!")

while exit == False:
	for event in pygame.event.get():

       	        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
			print
			print("User has quit the game.")
			print
                        exit = True

		if (user_score) == 10:
			exit = True
			print
			print("The user has won the game.")
			print
		elif (ai_score) == 10:
			exit = True
			print
			print("The AI has won the game.")
			print

	        if event.type == pygame.KEYDOWN and event.key == pygame.K_s and (user_start == True or user_start == False) and ball_move == False:
                        ball_x_speed = -(ai_paddle_speed + 1)
                        ball_y_speed = random.randint(-4, 4)
                        ball_move = True

                if user == False:
                        #paddle moving up
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                                move_user_up = True
                        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
                                move_user_up = False

                        #paddle moving down        
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                                move_user_down = True
                        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                                move_user_down = False

	if ball_move == True:
                if ball.y + ball_y_speed < 0:
                        ball_y_speed *= -1

                if ball.y + ball_y_speed + ball_dimensions[1] > dimensions[1]:
                        ball_y_speed *= -1

                if ball.x + ball_x_speed < 0:
			print
			print("The user has scored!")
                        print("User Score: " + str((user_score + 1)) )
                        print("AI Score: " + str(ai_score) )
			print
                        ball_move = False
                        user_start = True
			ball.x = ((dimensions[0] / 2) - 8.5)
			ball.y = (dimensions[1] / 2)
                        user_score += 1
                        hit = 0

                if ball.x + ball_x_speed + ball_dimensions[0] > dimensions[0]:
			print
			print("The AI has scored!")
                        print("User Score: " + str(user_score) )
                        print("AI Score: " + str((ai_score + 1)) )
			print
               	        ball_move = False
			user_start = False
			ball.x = ((dimensions[0] / 2) - 8.5)
			ball.y = (dimensions[1] / 2)
                       	ai_score += 1        
                       	hit = 0

                if ball.colliderect(ai_paddle):
                        if ball.y + ball_y_speed > ai_paddle.y and ball.y + ball_y_speed < ai_paddle.y + paddle_dimensions[1]:
                                ball_x_speed *= -1
                                hit += 1
                                if hit % 2 == 0:
                                        if ball_x_speed < 0:
                                                ball_x_speed -= ball_x_acc
                                        else:
                                                ball_x_speed += ball_x_acc
                                        if ball_y_speed < 0:
                                                ball_y_speed -= ball_y_acc
                                        else:
                                                ball_y_speed += ball_y_acc
                        else:
                                ball_y_speed *= -1

                if ball.colliderect(user_paddle):
                        if ball.y + ball_y_speed > user_paddle.y and ball.y + ball_y_speed < user_paddle.y + paddle_dimensions[1]:
                                ball_x_speed *= -1
                                hit += 1
                                if hit % 2 == 0:
                                        if ball_x_speed < 0:
                                                ball_x_speed -= ball_x_acc
                                        else:
                                                ball_x_speed += ball_x_acc
                                        if ball_y_speed < 0:
                                                ball_y_speed -= ball_y_acc
                                        else:
                                                ball_y_speed += ball_y_acc
                        else:
                                ball_y_speed *= -1

                ball = ball.move(ball_x_speed, ball_y_speed)
                
        if move_user_up == True:
                if user_paddle.y > 0:
                        user_paddle = user_paddle.move(0, -user_paddle_speed)
        if move_user_down == True:
                if user_paddle.y + paddle_dimensions[1] < dimensions[1]:
                        user_paddle = user_paddle.move(0, user_paddle_speed)
        
        if ai == True:
                if ball.y < ai_paddle.y + (paddle_dimensions[1] / 2) and ai_paddle.y > 0:
                        ai_paddle = ai_paddle.move(0, -ai_paddle_speed)
                if ball.y > ai_paddle.y + (paddle_dimensions[1] / 2) and ai_paddle.y + paddle_dimensions[1] < dimensions[1]:
                        ai_paddle = ai_paddle.move(0, ai_paddle_speed)

        user_font = font.render(str(user_score), True, white)
        ai_font = font.render(str(ai_score), True, white)        

        screen.fill(blue)
        pygame.draw.rect(screen, red, right_wall)
        pygame.draw.rect(screen, red, half_court)
        pygame.draw.rect(screen, red, left_wall)
        pygame.draw.rect(screen, red, top_wall)
        pygame.draw.rect(screen, red, bottom_wall)
        pygame.draw.circle(screen, red, (350, 250), 85)
        pygame.draw.circle(screen, blue, (350, 250), 78)
	pygame.draw.ellipse(screen, white, ball)
        pygame.draw.ellipse(screen, white, user_paddle)
        pygame.draw.ellipse(screen, white, ai_paddle)

        screen.blit(user_font, user_font_position)
        screen.blit(ai_font, ai_font_position)

        pygame.display.flip()

pygame.quit()
