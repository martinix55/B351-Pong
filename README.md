B351-Pong
=========
Pong Final Report

CSCI-B351
Professor Hauser
18 Dec 2013

Cole Martin
Antonio Thundy
Matt Alsop

Introduction

  Released in 1972, Pong is one of the more well-known and entertaining games in history. The creator, Allan Alcorn, 
was assigned this game as a training exercise by Atari’s co-founder Nolan Bushnell. Known to be revolutionary to the 
video game world, Pong was the first commercially prosperous video game. It is essentially a two-dimensional sports 
game that is mirrored to simulate table tennis. The user controls the right side of the screen, where it has its 
paddle. The paddle is designed to move up and down only. The object of the game is to hit the ball back and forth 
until someone lets the ball past his or her paddle, in which the opponent will score a point.

  Playing against the computer is one way to turn this two-player game into a single user. This is where the project 
starts to get a lot more interesting. Taking into account the speed of the ball and the speed of the paddle, we have 
created a game

Problem Description

	The problem that we were trying to solve would be creating an AI opponent to play against the computer that got 
more difficult to beat as the paddle speed increased. We first started out with a big problem, trying to figure 
Pygame out. We spent about a week just getting down the necessities for creating the Pygame. Once we overcame 
this challenge and were familiar with the Pygame syntax, we started to take a look at our methods.
 
Methods

  We start off by essentially setting up the Pygame screen and all of our variables. The variables portion of the 
project is one of the most important things we have set up, as we refer to them throughout all of our methods. 
Located in the variables respective to the ball, we have the speed at which it moves, acceleration, dimensions 
for Pygame to run, the start position of the ball, and actually drawing the ball on the screen. Inside the paddle 
variables, we have its dimensions and start position for each the user and the AI component, along with the speed. 
To start off, when you first start the game from your command line, you enter “python filename argument,” in which 
the argument is the level you want to play on: easy, medium, or hard. Typing which level you are going to play on is 
essential, as it won’t run without this. When you play on easy, the speed of the paddles is 2, which means that each 
time it moves 2 pixels out of the 700 x 500 board. When it is on medium, the paddle speed is 3 and hard means that 
the paddle speed is 5. We came up with these numbers by trial and error and lost a lot of games to the computer at 
speed 5, so we stuck with that as our hardest level. Finally, our last little set of variables is the background of 
the pong table, which is a bunch of different lines and circles and the fonts that we use when showing the score of 
the AI and the user.

  To start off the actually coding portion of the project, we look to our while statement, which includes our 
entire portion of coding. While the variable exit is False, we run our entire code, until the user hits the ‘q’ 
button on their keyboard. While the variable exit is False, the first thing we must check is whether or not the 
user has typed ‘q’. To do so, we have an if statement that checks this throughout the entire game, so you can quit 
at any point. The next thing we must do would be to set up to see if a winner has been determined after somebody 
scores a point. To become the winner, either the user or the AI must reach a score of 10 before their opponent.

  To start the game, the user has to manually hit the ‘s’ button on their keyboard. Once this is pressed, the ball 
starts moving at a random speed in the y coordinate and a negative direction in the x coordinate, which just means 
that it starts off moving towards the AI player. Lastly, we have our user controls located here, which allows the 
user to move his paddle at any point throughout the game, even if the ball isn’t moving. To set this up, we have 
to create an event type in which if the up directional arrow on the keyboard is pressed down, the paddle moves up 
until the up directional arrow is released, which makes the paddle stop moving. The same exact thing happens with 
the down directional arrow, as it moves down when the key is held down and once it is released it stops moving. 
All of the above is located in a for statement that allows any of these things to happen at any point while the 
screen is up.

  Now we get to the meat and potatoes of our coding, the actual gameplay part. All of the following occurs while 
the ball_move variable is set to True. If during the course of movement the ball happens to hit the top of the 
screen, we must redirect it and get it to bounce away at the same angle, we just have to make the y coordinate 
become negative so it knows to move in the opposite direction. The same thing happens when the ball hits the 
bottom of the screen, as it will follow the same path, it just goes in the opposite y coordinate direction.

  Up next, we check to see if somebody scores. To check this, we must see if the ball hits either the right or 
left walls. If the user scores, we print out a statement that states that the user has scored and it gives you 
an update on what the current scores is. When the AI component scores it does the same exact thing. After someone 
scores, the ball is placed back in the center of the screen, and ball_move is set back to False, meaning that the 
ball doesn’t start moving until the user hits the ‘s’ button on their keyboard. 

  Now came the most interesting and challenging part of the coding, checking to see if the ball made contact with 
the paddle. This is the part that we struggled on the most throughout this project. Essentially when the ball 
collides with the paddle, it counts the number of hits just because we needed a variable for this and it seemed 
like the most logical. When it does hit either the AI or users paddle, we check the speed and make it hit off at 
the same speed. Again, we must include the paddle movement for the AI and user in this if statement as well, so the
paddles will be available to move throughout the course of the ball moving.

  Lastly, we have some more Pygame screen variables to enter, including displaying the scores at the top of the 
screen during the gameplay and actually drawing the paddles, boundaries, and background.

Evaluation Criteria

  When evaluating our criteria, we always must take into account the ball speed and the paddle speed. We allow for 
the ball to move faster than the paddle because it makes the game a lot more challenging for the AI component. When 
we first started the project, this wasn’t something we were really thinking about until we gave our initial 
presentation and got some very good feedback from our peers.

  We also implemented our random-type function, which is essentially adding some depth to our ‘hit’ variable. What 
the hit variable does is actually keep a running count of the amount of times the ball hits the paddle. When it 
reaches numbers past 2, the ball speed starts to increase. This is where we used the hit variable to our advantage. 
Randomly, when the ball hits the tops of either of the paddles, it starts to go in crazy directions. This is because 
the hit variable is just counting all the hits. When this happens, it’s impossible for the user to predict where 
the ball is going to go or at what speed.

Results

  The more that we played around with the ball speed and the paddle speed, the more our numbers actually started 
making sense to us. We let people play on easy, medium, and hard difficulty and our numbers were spot on. Out of 
the 21 friends and family members we let play, all 21 beat the computer set on difficulty easy. This is what you’d 
expect though, so the medium we hoped to get around the 50-55% range in terms of people beating the AI, but for all
of the games to be a lot closer than the easy games. We ended up getting a 62% win percentage, so we were pretty 
spot on with our assumptions. Honestly, our level difficulty is so hard that we didn’t expect anybody to win, but 
were very surprised when we received 3 winners, which is only a measly 15%. Granted we do have a small variable size, 
but this goes to show that our assumptions were correct and that we succeeded in creating an AI that gets better as 
the paddle speed increases. Below we have the scores of each of the 21 users in terms of what they scored first and 
what the computer scored second.

	          Easy Medium	Hard
User 1	    10-1	10-8	4-10
User 2	    10-1	10-7	5-10
User 3	    10-5	6-10	4-10
User 4	    10-2	10-7	10-9
User 5	    10-3	10-8	5-10
User 6	    10-3	10-6	6-10
User 7	    10-4	8-10	4-10
User 8	    10-3	9-10	5-10
User 9	    10-2	10-7	5-10
User 10	    10-4	10-6	7-10
User 11	    10-4	8-10	5-10
User 12	    10-5	9-10	4-10
User 13	    10-3	9-10	5-10
User 14	    10-2	10-7	10-8
User 15	    10-3	10-6	5-10
User 16	    10-5	9-10	5-10
User 17	    10-3	10-8	7-10
User 18	    10-2	10-7	3-10
User 19	    10-3	8-10	10-9
User 20	    10-2	10-8	5-10
User 21	    10-2	10-8	5-10
			
% Win	      100%	62%	  15%

  As you can see, our easy scores represent that it is really simple because everybody won fairly simple. When it 
comes to medium, it was a lot closer of a game because the margin of victory was a lot slimmer than it was when the 
AI component was set to easy. When we take a look at hard, some people came close to beating it, but for the most 
part the AI had easy victories over the users it was competing against.

Conclusion

  In conclusion, we learned that we could create an AI component to play against that got better as the paddle speed 
got quicker. We also enjoyed playing around with our hit variable and getting that to work when it hits the paddle 
was fun to watch and try to predict the direction it shoots off into. Working with Pygame for the first time was 
pretty challenging, but overall we enjoyed it. It will definitely help us in the future to know that we can branch 
out and work on something that is new to us and something that we all had never programmed on before. The hit 
variable was something that we used to our advantage, knowing that if the ball hit either the top or bottom of the 
paddle it would rack up the hit variable, therefore increasing the speed of the ball and shooting it out in a random 
direction.
