from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

point_x = 0
point_y = 150
update_speed = 0.1

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
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    
    #   Draw points
    draw_points(250, 0)
    
    #   draw a line manully using points
    # for i in range(500):
    #     glColor3f(1, 0, 0)
    #     draw_points(i, i)
    
    #   draw lines
    # glColor3f(1, 0, 0)
    # draw_lines(250, 250, 250, 450)
    # draw_lines(50, 350, 350, 350)
    
    #   Draw a rectangle manually using lines
    # draw_lines(150, 150, 250, 150)
    # draw_lines(150, 200, 250, 200)
    # draw_lines(150, 150, 150, 200)
    # draw_lines(250, 150, 250, 200)
    
    #   Draw triangle
    # draw_triangles(100, 100, 100, 250, 150, 150)
    
    draw_points(point_x, point_y)
    
    
    glutSwapBuffers()
    
def updater():
    global point_x, point_y, update_speed
    
    point_x = point_x + update_speed
    
    if point_x >= 500:
        update_speed *= -1
    if point_x <= 0:
        update_speed *= -1
    
    glutPostRedisplay()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

#   Animate
glutIdleFunc(updater)

glutMainLoop()