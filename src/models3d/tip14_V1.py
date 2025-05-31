
import flet as ft
import threading
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def triangular_prism():
    vertices = (
        (-3.99, -4, -2.3),  # Вершина A (0)
        (3.99, -4, -2.3),  # Вершина c (1)
        (0, -4, 4.62),  # Вершина B (2)
        (0, 2.54, 0),  # Вершина M (верхушка) (3)
        (0, -1.82, 3.08), # T
        (2, -0.73, -1.15), # P
        (2, -4, 1.16),  # D
    )
    edges = (
        (2, 4), # BT
        (2, 0),  # BA
        (1, 2),  # BC
        (1, 0),  # CA
        (3, 6), # MD
        (6, 0),  # AD
        (5, 1)  # PC
    )
    edges2 = (

        (4, 5), # TP
        (5, 0),  # PA
        (0, 4),  # AM
        (4, 5),  # MP
        (0, 4), # AT
        (3, 4),  # MT
        (3, 0) , # MT
        (3, 5),  # MP
    )
    faces = (
        (0, 1, 2),
        (0, 1, 3),
        (1, 2, 3),
        (2, 0, 3),
    )

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # Отрисовка граней призмы
    glBegin(GL_TRIANGLES)
    for face in faces[:2]:  # Рисуем верхнюю и нижнюю грани
        glColor4f(0.5, 0.5, 1.0, 0.3)
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()


    # Отрисовка боковых граней
    glBegin(GL_QUADS)
    for face in faces[2:]:
        glColor4f(0.7, 0.7, 1.0, 0.3)
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    # Отрисовка дополнительных граней

    glLineWidth(2)
    # Отрисовка ребер
    glBegin(GL_LINES)
    glColor3fv((0, 0, 0))
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


    glLineWidth(2)
    # Отрисовка ребер
    glBegin(GL_LINES)
    glColor3fv(( 0.5255,  0.0275, 0.9608))
    for edge in edges2:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_dashed_line(start, end, dash_length=0.03, gap_length=0.05):
    x1, y1, z1 = start
    x2, y2, z2 = end
    length = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
    dashes = int(length / (dash_length + gap_length))

    glColor3fv(( 0.5255,  0.0275, 0.9608))  # Оранжевый цвет

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
    text_surface = font.render(text, True, (0, 0, 0, 0)).convert_alpha()
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    glRasterPos3f(x, y, z)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)

pygame_window_running = False
pygame_thread = None
stop_event = threading.Event()
def run_pygame_tip14_V1(e, stop_event_local):
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
        (-3.99, -4, -2.3),  # Вершина A (0)
        (3.99, -4, -2.3),  # Вершина B (1)
        (0, -4, 4.62),  # Вершина C (2)
        (0, 2.54, 0),  # Вершина M (верхушка) (3)
        (0, -1.82, 3.08),  # T
        (2, -0.73, -1.15),  # P
        (2, -4, 1.16),  # D
    )
    labels =  ["A","C", "B","M","T", "P", "D" ]
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Темно-серый фон
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
        font_size = max(20, 34 * (1 + zoom))  # Изменение размера текста в зависимости от масштаба
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
    threading.Thread(target=run_pygame_tip14_V1).start()

def main():
    ft.app(target=app, port=8550)

def app(page: ft.Page):
    start_button = ft.ElevatedButton("Запустить Pygame", on_click=start_pygame)
    page.add(start_button)

if __name__ == '__main__':
    main()