import flet as ft
import threading
import pygame
import sys
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np

pygame_window_running = False

# Отредачено
def cube():
    vertices = ((-1, -1, -1), (-1, 1, -1),
                (-1, 1, 1), (-1, -1, 1),
                (1, -1, -1), (1, 1, -1),
                (1, 1, 1), (1, -1, 1))
    edges = ((0, 1), (0, 3), (0, 4),
             (1, 2), (1, 5), (2, 3),
             (2, 6), (3, 7), (4, 5),
             (4, 7), (5, 6), (6, 7))

    dashed_edges = [(4, 2)]
    faces = ((0, 1, 2, 3), (4, 5, 6, 7),
             (0, 4, 7, 3), (1, 5, 6, 2),
             (2, 6, 7, 3), (1, 5, 4, 0))

    glBegin(GL_QUADS)
    for face in faces:
        glColor4f(0.5, 0.5, 1.0, 0.3)
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    glLineWidth(1.5)
    glBegin(GL_LINES)
    for edge in edges:
        glColor3fv((0, 0, 0))
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    for edge in dashed_edges:
        draw_dashed_line(vertices[edge[0]], vertices[edge[1]])


def draw_dashed_line(start, end, dash_length=0.1, gap_length=0.05):
    x1, y1, z1 = start
    x2, y2, z2 = end
    length = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
    dashes = int(length / (dash_length + gap_length))

    glColor3fv((0.5255, 0.0275, 0.9608))

    for i in range(dashes):
        t1 = i * (dash_length + gap_length) / length
        t2 = t1 + dash_length / length
        if t2 > 1.0:
            t2 = 1.0
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


def drawText(x, y, text, font):
    textSurface = font.render(text, True, (0, 0, 0)).convert_alpha()
    textData = pygame.image.tostring(textSurface, "RGBA", True)
    glWindowPos2d(x, y)
    glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)


def get_mouse_world_coords(HEIGHT):

    mx, my = pygame.mouse.get_pos()

    # Получаем глубину пикселя на экране
    depth = glReadPixels(mx, HEIGHT - my, 1, 1, GL_DEPTH_COMPONENT, GL_FLOAT)

    modelview = glGetDoublev(GL_MODELVIEW_MATRIX)
    projection = glGetDoublev(GL_PROJECTION_MATRIX)
    viewport = glGetIntegerv(GL_VIEWPORT)

    # Преобразуем экранные координаты в мировые
    real_x, real_y = mx, HEIGHT - my
    real_z = float(depth[0][0]) if depth is not None else 0.5

    # Получаем мировые координаты через unProject
    world_coords = gluUnProject(real_x, real_y, real_z, modelview, projection, viewport)

    return world_coords


pygame_window_running = False
pygame_thread = None
stop_event = threading.Event()

def run_pygame1_1_svetl(e, stop_event_local):
    global pygame_window_running
    pygame_window_running = True

    pygame.init()
    FPS = 60
    WIDTH, HEIGHT = 800, 600
    screen = (800, 600)
    pygame.display.set_mode(screen, DOUBLEBUF | OPENGL)
    pygame.display.set_icon(pygame.image.load("./assets/objekte.png"))
    pygame.display.set_caption('Stereometry 360°')

    font = pygame.font.SysFont('Verdana', 18)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(60, (screen[0] / screen[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glTranslate(0.0, 0.0, -5)

    rot_x, rot_y, zoom = 25, -25, -0.5
    clock = pygame.time.Clock()
    busy = True

    drawing_mode = False
    drawing_points = []
    current_line = []

    glClearColor(1.0, 1.0, 1.0, 1.0)  # Темно-серый фон
    while not stop_event_local.is_set() and busy:
        mouse_buttons = pygame.mouse.get_pressed()
        button_down = mouse_buttons[0] == 1

        time_delta = clock.tick(FPS) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                busy = False
            elif event.type == pygame.MOUSEMOTION:
                if button_down:
                    rot_x += event.rel[1]
                    rot_y += event.rel[0]
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    zoom += 0.2
                elif event.button == 5:
                    zoom -= 0.2
                elif drawing_mode and event.button == 1:
                    world_coords = get_mouse_world_coords(HEIGHT)

                    # Добавляем координаты в текущую линию
                    current_line.append(world_coords)

                    # Если линия завершена, сохраняем её
                    if len(current_line) == 2:
                        drawing_points.append(tuple(current_line))
                        current_line = []
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rot_x, rot_y, zoom = 25, -25, -0.5
                elif event.key == pygame.K_d:
                    drawing_mode = not drawing_mode
                    print("Режим рисования:", "ВКЛ" if drawing_mode else "ВЫКЛ")



        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glTranslatef(0.0, 0.0, zoom)
        glRotatef(rot_x, 1, 0, 0)
        glRotatef(rot_y, 0, 1, 0)

        cube()

        # Рисуем линии
        glLineWidth(2)
        glColor3f(1.0, 0.0, 0.0)
        glBegin(GL_LINES)
        for line in drawing_points:
            glVertex3fv(line[0])
            glVertex3fv(line[1])
        glEnd()



        glPopMatrix()

        pygame.display.flip()


    pygame.quit()
    pygame_window_running = False


def start_pygame(e):
    threading.Thread(target=run_pygame1_1_svetl, args=(e,)).start()


def main():
    ft.app(target=app, port=8550)


def app(page: ft.Page):
    start_button = ft.ElevatedButton("Запустить Pygame", on_click=start_pygame)
    page.add(start_button)


if __name__ == '__main__':
    main()