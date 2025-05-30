import flet as ft
import threading
import pygame
import sys
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def piramid_3():
    vertices = (
        (1, -0.7, 0),  # Вершина A
        (-0.48, -0.7, 0.85),  # Вершина C
        (-0.48, -0.7, -0.85),  # Вершина B

        (0, 0.7, 0),  # Вершина D (верхушка)
        (-0.24, 0, 0.43),  # Вершина E
        (0.26, -0.7, -0.43),  # Вершина M
        (-0.32, -0.24, 0)  # Вершина H
    )
    edges = (
        (0, 1),  # ребро AB
        (1, 2),  # ребро BC
        (2, 0),  # ребро CA
        (0, 3),  # ребро AD
        (1, 3),  # ребро BD
        (2, 3),  # ребро CD

    )
    dashed_edges = ((4, 5), (0, 6),)
    edges2 = ((0, 4), (2, 4,))

    glBegin(GL_LINES)
    for edge in edges:
        glColor3fv((1, 1, 1))  # Белый цвет
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges2:
        glColor3fv((1, 0.5, 0))  # Белый цвет
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    # Отдельно рисуем пунктирные линии
    for edge in dashed_edges:
        draw_dashed_line(vertices[edge[0]], vertices[edge[1]])

def draw_dashed_line(start, end, dash_length=0.05, gap_length=0.02):
    x1, y1, z1 = start
    x2, y2, z2 = end
    length = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
    dashes = int(length / (dash_length + gap_length))

    glColor3fv((1, 0.5, 0))  # Оранжевый цвет

    for i in range(dashes):
        t1 = i * (dash_length + gap_length) / length
        t2 = t1 + dash_length / length

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
    font = pygame.font.SysFont('arial', int(font_size))
    text_surface = font.render(text, True, (255, 255, 66, 255)).convert_alpha()
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    glRasterPos3f(x, y, z)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)

pygame_window_running = False
pygame_thread = None
stop_event = threading.Event()
def run_pygame_tip14_rast2(e, stop_event_local):
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

    rot_x, rot_y, zoom = 20, -20, -0.5
    clock = pygame.time.Clock()
    busy = True
    vertices = (
        (1, -0.7, 0),  # Вершина A
        (-0.48, -0.7, 0.85),  # Вершина C
        (-0.48, -0.7, -0.85),  # Вершина B
        (0, 0.7, 0),  # Вершина D (верхушка)
        (-0.24, 0, 0.43),  # Вершина E
        (0.26, -0.7, -0.43),  # Вершина M
        (-0.32, -0.24, 0)  # Вершина H
    )
    labels = ["A", "C", "B", "D", "E", "M", "H"]

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
                    rot_x, rot_y, zoom = 200, -200, -0.2
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

        piramid_3()
        font_size = max(10, 20 * (1 + zoom))  # Изменение размера текста в зависимости от масштаба
        for i, vertex in enumerate(vertices):
            x, y, z = vertex
            if i == 4:  # Это вершина E
                drawText3D(x, y, z, labels[i], font_size)
            elif i == 5:  # Это вершина M
                drawText3D(x, y, z, labels[i], font_size)
            elif i == 6:  # Это вершина H
                drawText3D(x, y, z, labels[i], font_size)
            else:
                drawText3D(x, y, z, labels[i], font_size)

        glPopMatrix()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

def start_pygame(e):
    threading.Thread(target=run_pygame_tip14_rast2).start()

def main():
    ft.app(target=app, port=8550)

def app(page: ft.Page):
    start_button = ft.ElevatedButton("Запустить Pygame", on_click=start_pygame)
    page.add(start_button)

if __name__ == '__main__':
    main()