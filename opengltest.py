# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:07:13 2020

@author: robin
"""

import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def draw_gun():
    # Setting up materials, ambient, diffuse, specular and shininess properties are all
    # different properties of how a material will react in low/high/direct light for
    # example.
    ambient_coeffsGray = [0.3, 0.3, 0.3, 1]
    diffuse_coeffsGray = [0.5, 0.5, 0.5, 1]
    specular_coeffsGray = [0, 0, 0, 1]
    glMaterialfv(GL_FRONT, GL_AMBIENT, ambient_coeffsGray)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse_coeffsGray)
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular_coeffsGray)
    glMateriali(GL_FRONT, GL_SHININESS, 1)

    # OpenGL is very finicky when it comes to transformations, for all of them are global,
    # so it's good to seperate the transformations which are used to generate the object
    # from the actual global transformations like animation, movement and such.
    # The glPushMatrix() ----code----- glPopMatrix() just means that the code in between
    # these two functions calls is isolated from the rest of your project.
    # Even inside this push-pop (pp for short) block, we can use nested pp blocks,
    # which are used to further isolate code in it's entirety.
    glPushMatrix()

    glPushMatrix()
    glTranslatef(3.1, 0, 1.75)
    glRotatef(90, 0, 1, 0)
    glScalef(1, 1, 5)
    glScalef(0.2, 0.2, 0.2)
    glutSolidTorus(0.2, 1, 10, 10)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(2.5, 0, 1.75)
    glScalef(0.1, 0.1, 1)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1, 0, 1)
    glRotatef(10, 0, 1, 0)
    glScalef(0.1, 0.1, 1)
    glutSolidCube(1)

    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.8, 0, 0.8)
    glRotatef(90, 1, 0, 0)
    glScalef(0.5, 0.5, 0.5)
    glutSolidTorus(0.2, 1, 10, 10)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1, 0, 1.5)
    glRotatef(90, 0, 1, 0)
    glScalef(1, 1, 4)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glRotatef(8, 0, 1, 0)
    glScalef(1.1, 0.8, 3)
    glutSolidCube(1)
    glPopMatrix()

    glPopMatrix()

def main():
    # Initialization of PyGame modules
    pg.init()
    # Initialization of Glut library
    glutInit(sys.argv)
    # Setting up the viewport, camera, backgroud and display mode
    display = (800,600)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)
    glClearColor(0.1,0.1,0.1,0.3)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    gluLookAt(5,5,3,0,0,0,0,0,1)

    glTranslatef(0.0,0.0, -5)
    while True:
        # Listener for exit command
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        # Clears the screen for the next frame to be drawn over
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        ############## INSERT CODE FOR GENERATING OBJECTS ##################
        draw_gun()
        ####################################################################
        # Function used to advance to the next frame essentially
        pg.display.flip()
        pg.time.wait(10)
        
main()
