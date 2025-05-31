import flet as ft
import threading
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def triangular_prism():

    vertices = (
        (0.41, -1, -1.08), #B
        (0.73, -1, 0.9),  # A
        (-1.14, -1, 0.19),  # c
        (0.41, 1, -1.08),  # B1
        (0.73, 1, 0.9),  # A1
        (-1.14, 1, 0.19),  # c1
        (-0.37,-1, -0.45),

        (-0.3,-1, -0.5),
        (-0.24, -1, -0.43),
        (-0.31, -1, -0.37),


    )
    edges = (
        (0, 1), (1, 2), (2, 0),  # Нижний треугольник
        (3, 4), (4, 5), (5, 3),
        (0, 3,), (1, 4,), (2, 5,),
        (7, 8, ), (8, 9,),(9, 6,)

    )
    dashed_edges = [(1, 6), (4, 6)]
    edges2 = ((2, 4), (4, 0))
    faces = ((2, 4, 0),)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glBegin(GL_TRIANGLES)  # Отрисовка граней
    for face in faces:
        glColor4f(1, 0.5, 0, 0.3)
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    glColor3fv((1, 1, 1))
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
    glBegin(GL_LINES)
    glColor3fv((1, 0.5, 0))
    for edge in edges2:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


    for edge in dashed_edges:
        draw_dashed_line(vertices[edge[0]], vertices[edge[1]])


def draw_dashed_line(start, end, dash_length=0.03, gap_length=0.05):

    x1, y1, z1 = start
    x2, y2, z2 = end
    length = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
    dashes = int(length / (dash_length + gap_length))

    glColor3fv((1, 0.5, 0))  # Оранжевый цвет

    for i in range(dashes):
        t1 = i * (dash_length + gap_length) / length
        t2 = t1 + dash_length / length
          # Обрезаем последний сегмент
        glBegin(GL_LINES)
        glVertex3f(
            x1 + (x2 - x1) * t1,
            y1 + (y2 - y1) * t1,
            z1 + (z2 - z1) * t1
        )
        glVertex3f(
            x1 + (x2 - x1) * t2,
            y1 + (y2 - y1) * t2,
            z1 + (z2 - z1) * t2
        )
        glEnd()

def drawText3D(x, y, z, text, font_size):
    font = pygame.font.SysFont('Calibri', int(font_size))
    text_surface = font.render(text, True, (255, 255, 66, 255)).convert_alpha()
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    glRasterPos3f(x, y, z)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)

pygame_window_running = False
pygame_thread = None
stop_event = threading.Event()
def run_pygame_tip14_ygol1(e, stop_event_local):
    global pygame_window_running
    pygame_window_running = True

    pygame.init()

    screen = (800, 600)
    pygame.display.set_mode(screen, DOUBLEBUF | OPENGL)
    pygame.display.set_icon(pygame.image.load("./assets/objekte.png"))
    pygame.display.set_caption('Stereometry 360°')

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(30, (screen[0] / screen[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glTranslate(0.0, 0.0, -5)

    rot_x, rot_y, zoom = 20, -50, -5
    clock = pygame.time.Clock()
    busy = True
    vertices = (
        (0.41, -1, -1.08),  # A
        (0.73, -1, 0.9),  # B
        (-1.14, -1, 0.19),  # c
        (0.41, 1, -1.08),  # A1
        (0.73, 1, 0.9),  # B1
        (-1.14, 1, 0.19),  # c1
        (-0.37, -1, -0.45)
    )
    labels =  ["B","A", "C","B₁","A₁", "C₁", "H" ]

    while not stop_event_local.is_set() and busy:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif (event.type == pygame.MOUSEMOTION
                  and pygame.mouse.get_pressed()[0]):
                rot_x += event.rel[1]
                rot_y += event.rel[0]
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rot_x, rot_y, zoom = 20, -50, -5
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    zoom += 0.2
                if event.button == 5:
                    zoom -= 0.2

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glTranslatef(0.0, 0.0, zoom)
        glRotatef(rot_x, 1, 0, 0)
        glRotatef(rot_y, 0, 1, 0)

        triangular_prism()
        font_size = max(20, 34 * (1 + zoom))
        for i, vertex in enumerate(vertices):
            x, y, z = vertex
            if z == 0.9 and x == 0.73:
                z += 0.05
                x += 0.05
            elif z == -1.08 and x == 0.41:
                z -= 0.05
                x += 0.05
            elif z == 0.19 and x == -1.14:
                z += 0.05
                x -= 0.05

            drawText3D(x, y, z, labels[i], font_size)

        glPopMatrix()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

def start_pygame(e):
    threading.Thread(target=run_pygame_tip14_ygol1(e)).start()

def main():
    ft.app(target=app, port=8552)

def app(page: ft.Page):
    start_button = ft.ElevatedButton("Запустить Pygame", on_click=start_pygame)
    page.add(start_button)

if __name__ == '__main__':
    main()