from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random

sky_color = (0, 0, 0)
color_change_rate = 0.01
direction = 0
drop_length = 50
speed = 3
total_drops = 100
rain_drops = [ (random.randint(0, 500), random.randint(0, 500)) for i in range(total_drops)]

def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def draw_lines(x, y, a, b, width = 5):
    glLineWidth(width)
    glBegin(GL_LINES)
    glVertex2f(x, y)
    glVertex2f(a, b)
    glEnd()
    
def draw_triangles(a, b, c, d, e, f):
    
    glBegin(GL_TRIANGLES)
    glVertex2f(a, b)
    glVertex2f(c, d)
    glVertex2f(e, f)
    glEnd()

def draw_rectangle(a, b, height, width):
    draw_triangles(a, b, a+width, b, a, b+height)
    draw_triangles(a+width, b, a, b+height, a+width, b+height)

def draw_triangle_single_point(x, y, base=20, height=80):
    c = x + base
    d = y
    e = x + (base // 2)
    f = y + height
    draw_triangles(x, y, c, d, e, f)

def draw_triangles_practice(a, b, c, d, e, f):
    glLineWidth(5)
    
    glBegin(GL_LINES)
    
    glVertex2f(a, b)
    glVertex2f(c, d)
    
    glVertex2f(c, d)
    glVertex2f(e, f)
    
    glVertex2f(e, f)
    glVertex2f(a, b)
    
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(sky_color[0], sky_color[1], sky_color[2], 1.0)
    glLoadIdentity()
    iterate()

    #   Draw areas
    for i in range(270):
        glColor3f(0.478, 0.357, 0.059)
        draw_lines(0, i, 500, i, width=10)
    
    for i in range(270):
        glColor3f(0.478, 0.357, 0.059)
        draw_lines(0, i, 500, i, width=10)
    
    for i in range(270, 350):
        glColor3f(0.294, 0.180, 0.086)
        draw_lines(0, i, 500, i, width=10)
    
    glColor3f(0.565, 0.933, 0.565)
    for i in range(0, 500, 50):
        draw_triangle_single_point(i, 270, base=50, height=80)
        
    #   house rectangle
    glColor3f(0.992, 0.965, 0.922)
    draw_rectangle(100, 180, height=120, width=300)
    
    #   roof
    glColor3f(0.306, 0.090, 0.690)
    draw_triangles(100-10, 300, 100+300+10, 300, 100+(300//2), 350+40)
    
    #   door
    glColor3f(0.184, 0.584, 0.992)
    draw_rectangle(240, 180, height=80, width=40)
    
    #   window
    glColor3f(0.184, 0.584, 0.992)
    edge_distance = 40
    draw_rectangle(100+edge_distance, 180+40, height=40, width=30)
    draw_rectangle(400-edge_distance-30, 180+40, height=40, width=30)
    
    
    #   let it rain
    display_rain()
    
    glutSwapBuffers()

def display_rain():
    global rain_drops, total_drops, direction, drop_length
    for i in range(total_drops):
        x = rain_drops[i][0]
        y = rain_drops[i][1]
        x2 = x + drop_length*direction
        y2 = y - drop_length
        
        draw_lines(x, y, x2, y2)

def update_position():
    global rain_drops, total_drops, direction, speed, drop_length
    for i in range(total_drops):
        x = rain_drops[i][0] + speed*direction
        y = rain_drops[i][1] - speed
        
        if y <= 0:
            y = (y + 500)
        if x>500:
            x = x % 500
        if x<0:
            x = x + 500
        
        rain_drops[i] = (x, y)
        

def updater():
    global rain_drops, total_drops
    
    update_position()
    
    glutPostRedisplay()

def keyboard_handler(key, x, y):
    global update_speed, sky_color, color_change_rate
    r, g, b = sky_color
    
    if key == b'l':
        r = min(1.0, r+color_change_rate)
        g = min(1.0, g+color_change_rate)
        b = min(1.0, b+color_change_rate)
    if key == b'd':
        r = max(0.0, r - color_change_rate)
        g = max(0.0, g - color_change_rate)
        b = max(0.0, b - color_change_rate)
    
    sky_color = (r, g, b)

def special_key_handler(key, x, y):
    global direction
    if key==GLUT_KEY_RIGHT:
        direction = min(1, direction+1)
    if key== GLUT_KEY_LEFT:
        direction = max(-1, direction-1)
    glutPostRedisplay()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

#   Animate
glutIdleFunc(updater)

#   Keyboard interrupt
glutKeyboardFunc(keyboard_handler)
glutSpecialFunc(special_key_handler)

glutMainLoop()