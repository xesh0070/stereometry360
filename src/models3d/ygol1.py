import flet as ft
import threading
import pygame

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def piramid_3():
    vertices = (
        (0, -1, -0.96),  # Вершина A
        (-0.83, -1, 0.48),  # Вершина b
        (0.83, -1, 0.48),  # Вершина c
        (0, 1, -0.96),  # Вершина A
        (-0.83, 1, 0.48),  # Вершина b
        (0.83, 1, 0.48),  # Вершина c
        (0, -1, 0.48),  # Вершина H
    )
    edges = (
        (0, 1), (1, 2), (2, 0),  # Нижний треугольник
        (3, 4), (4, 5), (5, 3),  # Верхний треугольник
        (0, 3), (1, 4), (2, 5)  # Соединительные рёбра
    )
    faces = ((1, 2, 3),)  # Note the comma to make it a tuple with one element
    dashed_edges = ((0, 6),)
    dashed_edges2 = ((6, 3),)
    edges2 = ((1, 3), (2, 3))


    glBegin(GL_TRIANGLES)
    glColor3f(0.6471, 0.5412, 0.9843)
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()


    glBegin(GL_LINES)
    for edge in edges:
        glColor3fv((1, 1, 1))
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
    glBegin(GL_LINES)
    glColor3f(0.3137, 0.1333, 0.3333)
    for edge in edges2:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


    for edge in dashed_edges:
        draw_dashed_line(vertices[edge[0]], vertices[edge[1]])


    for edge in dashed_edges2:
        draw_dashed_line2(vertices[edge[0]], vertices[edge[1]])


def draw_dashed_line(start, end, dash_length=0.05, gap_length=0.02):
    x1, y1, z1 = start
    x2, y2, z2 = end
    length = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
    dashes = int(length / (dash_length + gap_length))

    glColor3f(0.4863, 0.7098, 0.8784)

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


def draw_dashed_line2(start, end, dash_length=0.05, gap_length=0.02):
    x1, y1, z1 = start
    x2, y2, z2 = end
    length = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
    dashes = int(length / (dash_length + gap_length))

    glColor3f(0.3137, 0.1333, 0.3333)

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
    font = pygame.font.SysFont('Verdana', int(font_size))
    text_surface = font.render(text, True, (0xA5, 0x8A, 0xFB, 255))
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    glRasterPos3f(x, y, z)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)

pygame_window_running = False
pygame_thread = None
stop_event = threading.Event()
def run_pygame_tip14_ygol1(e, stop_event_local):
    try:
        pygame.init()

        screen = (800, 600)
        pygame.display.set_mode(screen, DOUBLEBUF | OPENGL)
        pygame.display.set_icon(pygame.image.load("./assets/objekte.png"))
        pygame.display.set_caption('Stereometry 360°')

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        glMatrixMode(GL_PROJECTION)
        gluPerspective(40, (screen[0] / screen[1]), 0.1, 50.0)

        glMatrixMode(GL_MODELVIEW)
        glTranslate(0.0, 0.0, -5)

        rot_x, rot_y, zoom = 30, 165, -0.5
        clock = pygame.time.Clock()

        vertices = (
            (0, -1, -0.96),  # Вершина A
            (-0.83, -1, 0.48),  # Вершина C
            (0.83, -1, 0.48),  # Вершина B
            (0, 1, -0.96),  # Вершина A
            (-0.83, 1, 0.48),  # Вершина C
            (0.83, 1, 0.48),  # Вершина B
            (0, -1, 0.48),  # Вершина H
        )

        labels = ["A", "B", "C", "A₁", "B₁", "C₁", "H"]

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif (event.type == pygame.MOUSEMOTION and
                      pygame.mouse.get_pressed()[0]):
                    rot_x += event.rel[1]
                    rot_y += event.rel[0]
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        rot_x, rot_y, zoom = 30, 165, -0.5
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
            font_size = max(10, 27 * (1 + zoom))

            for i, vertex in enumerate(vertices):
                x, y, z = vertex
                if i == 6:  # Вершина H
                    if y == -1:
                        y -= 0.1
                    drawText3D(x, y, z, labels[i], font_size)
                else:
                    if y == -1:
                        y -= 0.1
                    if y == 1:
                        y += 0.05
                    drawText3D(x, y, z, labels[i], font_size)

            glPopMatrix()
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


def start_pygame(e):

    threading.Thread(target=run_pygame_tip14_ygol1, daemon=True).start()


def main(page: ft.Page):
    start_button = ft.ElevatedButton("Запустить Pygame", on_click=start_pygame)
    page.add(start_button)


if __name__ == '__main__':
    ft.app(target=main)