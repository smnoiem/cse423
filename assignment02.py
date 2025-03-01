from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random

W_Width, W_Height = 500,500
points = [((250, 250), (1, 1), (0.5, 0.5, 0.5))]
speed = 0.1
blink_mode = False
blink = True
frozen = False

def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def draw_lines(x, y, a, b):
    glLineWidth(5)
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

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    
    for point in points:
        glColor3f(point[2][0], point[2][1], point[2][2])
        if blink_mode and blink:
            glColor3f(0, 0, 0)
        draw_points(point[0][0], point[0][1])
    
    
    glutSwapBuffers()
    
def updater():
    if frozen:
        return
    global points, speed, blink, blink_mode
    for i in range(len(points)):
        point = points[i]
        
        x, y = point[0]
        x_dir, y_dir = point[1]
        r, g, b = point[2]
        
        x += x_dir*speed
        y += y_dir*speed
        
        if x <= 0 or x>=500:
            x_dir *= -1
        if y<=0 or y>=500:
            y_dir *= -1
        
        points[i] = ((x, y), (x_dir, y_dir), (r, g, b))
    
    glutPostRedisplay()

def mouse_handler(button, state, x, y):
    if frozen:
        return
    global points
    if button==GLUT_RIGHT_BUTTON:
        if(state == GLUT_DOWN):
            
            c_x, c_y = convert_coordinate(x,y)
            
            x_dir = 1 if random.randint(0, 1000) % 2 else -1
            y_dir = 1 if random.randint(0, 1000) % 2 else -1
            
            r = random.random()
            g = random.random()
            b = random.random()
            
            points.append(((c_x, c_y), (x_dir, y_dir), (r, g, b)))


def special_key_handler(key, x, y):
    if frozen:
        return
    global speed, blink_mode, blink
    if key==GLUT_KEY_UP:
        speed *= 2
    if key== GLUT_KEY_DOWN:
        speed /= 2
    
    if key==GLUT_KEY_LEFT:
        if blink_mode:
            blink_mode = False
        else:
            blink_mode = True
            blink = True
            glutTimerFunc(1000, toggle_flag, 0)

def keyboard_handler(key, x, y):
    global frozen
    if key == b' ':
        frozen = not frozen

def toggle_flag(value):
    global blink_mode, blink
    if not frozen:
        blink = not blink
    if blink_mode:
        glutTimerFunc(1000, toggle_flag, 0)

def convert_coordinate(x,y):
    global W_Width, W_Height
    
    # a = x - (W_Width/2)
    # b = (W_Height/2) - y
        
    return x, W_Height - y


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

#   Animate
glutIdleFunc(updater)

#   Mouse interrupt
glutMouseFunc(mouse_handler)
glutSpecialFunc(special_key_handler)
glutKeyboardFunc(keyboard_handler)

glutMainLoop()