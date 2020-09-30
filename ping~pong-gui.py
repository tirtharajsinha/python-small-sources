#import simplegui
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
import time

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
SIDE = LEFT
count=0
msg1="tied"
msg2="tied"

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]	# position the ball at the centre of the canvas
    if direction == RIGHT:
        ball_vel = [random.randrange(120, 240) / 60, -(random.randrange(60, 180) /60)]
    else:
        ball_vel = [-(random.randrange(120, 240) / 60), -(random.randrange(60, 180) / 60)]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    global SIDE #this is a boolean
    paddle1_pos, paddle2_pos = (HEIGHT - PAD_HEIGHT)/2, (HEIGHT - PAD_HEIGHT)/2
    paddle1_vel = paddle2_vel = 0
    score1, score2 = 0, 0
    SIDE = not SIDE
    spawn_ball(SIDE)
def level():
    global ball_vel
    ball_vel[0] = - 1.1 * ball_vel[0]
    print("level up!")

def draw(canvas):
    global msg1,msg2,score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,count
    
    
      
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    #canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    #canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if paddle1_pos <= ball_pos[1] <= (paddle1_pos+PAD_HEIGHT):
            ball_vel[0] = - 1.0 * ball_vel[0]
        else:
            #spawn_ball(RIGHT)
            ball_vel[0] = - 1.0 * ball_vel[0]
            score2 += 1
            count+=1
            
    if ball_pos[0] >= (WIDTH - BALL_RADIUS - PAD_WIDTH):
        if paddle2_pos <= ball_pos[1] <= (paddle2_pos+PAD_HEIGHT):
            ball_vel[0] = - 1.0 * ball_vel[0]
        else:
            #spawn_ball(LEFT)
            ball_vel[0] = - 1.0 * ball_vel[0]
            score1 += 1
            count+=1
            
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 0.1, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    if 0 <= (paddle1_pos + paddle1_vel) <= HEIGHT - PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    if 0 <= (paddle2_pos + paddle2_vel) <= HEIGHT - PAD_HEIGHT:
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_line([PAD_WIDTH / 2, paddle1_pos],[PAD_WIDTH / 2, paddle1_pos + PAD_HEIGHT], PAD_WIDTH, "black")
    canvas.draw_line([WIDTH - PAD_WIDTH / 2, paddle2_pos],[WIDTH- PAD_WIDTH / 2, paddle2_pos + PAD_HEIGHT], PAD_WIDTH, "White")
    if score1==score2:
        msg1="tied"
        msg2="tied"
    elif score1>score2:
        msg1="leading"
        msg2=""
    elif score1<score2:
        msg1=""
        msg2="leading"
    # draw scores
    canvas.draw_text(str(score1), (150, 40), 40, "black")
    canvas.draw_text("player 1  "+msg1, (145, 55), 20, "black")
    canvas.draw_text("Vs", (275, 45), 55, "red")
    canvas.draw_text(str(score2), (400, 40), 40, "White")
    canvas.draw_text("player 2  "+msg2, (395, 55), 20, "White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    vel = 3
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -vel   
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -vel
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0   
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
        
def game_restart():
    time.sleep(5)
    new_game()

# create frame
frame = simplegui.create_frame("2-side Ping~Pong", WIDTH, HEIGHT)
frame.set_canvas_background('green')
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", game_restart, 100)
frame.add_button("start game", new_game, 100)
frame.add_button("level up",level, 100)
time.sleep(5)
# start frame
new_game()

frame.start()
