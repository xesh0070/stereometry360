import flet as ft
import threading
import pygame
import sys
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


# Глобальная переменная для отслеживания состояния окна Pygame
pygame_window_running = False

def cube():
    vertices = (
        (-2, 1.5, -2.5), (-2, 1.5, 2.5), (2, 1.5, 2.5), (2, 1.5, -2.5),
        (-2, -1.5, -2.5), (-2, -1.5, 2.5), (2, -1.5, 2.5), (2, -1.5, -2.5)
    )
    edges = (
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    )
    edges2 =((2, 5),)
    dashed_edges = [(4, 2), ]  # Оранжевые пунктирные линии

    faces = ((0, 1, 2, 3), (4, 5, 6, 7),
             (0, 4, 7, 3), (1, 5, 6, 2),
             (2, 6, 7, 3), (1, 5, 4, 0))

    glBegin(GL_QUADS)  # Отрисовка граней
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

    glLineWidth(1.5)
    glBegin(GL_LINES)
    for edge in edges2:
        glColor3fv(( 0.5255,  0.0275, 0.9608))
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    # Отдельно рисуем пунктирные линии
    for edge in dashed_edges:
        draw_dashed_line(vertices[edge[0]], vertices[edge[1]])

def draw_dashed_line(start, end, dash_length=0.1, gap_length=0.05):

    x1, y1, z1 = start
    x2, y2, z2 = end
    length = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
    dashes = int(length / (dash_length + gap_length))

    glColor3fv(( 0.5255,  0.0275, 0.9608))

    for i in range(dashes):
        t1 = i * (dash_length + gap_length) / length
        t2 = t1 + dash_length / length
        if t2 > 1.0:
            t2 = 1.0  # Обрезаем последний сегмент
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

def drawText(x, y, text, font):
    textSurface = font.render(text, True, (255, 255, 255, 0.)).convert_alpha()
    textData = pygame.image.tostring(textSurface, "RGBA", True)
    glWindowPos2d(x, y)
    glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)


pygame_window_running = False
pygame_thread = None
stop_event = threading.Event()

def run_pygame_tip3_par2_sv(e, stop_event_local):
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
    gluPerspective(60, (screen[0] / screen[1]), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)
    glTranslate(0.0, 0.0, -5)

    rot_x, rot_y, zoom = 30, 50, -5
    clock = pygame.time.Clock()
    busy = True
    vertices = (
        (-2, 1.5, -2.5), (-2, 1.5, 2.5), (2, 1.5, 2.5), (2, 1.5, -2.5),
        (-2, -1.5, -2.5), (-2, -1.5, 2.5), (2, -1.5, 2.5), (2, -1.5, -2.5),
        # (-1, 0.5, -0.8), (-1, 0.5, 0.8), (1, 0.5, 0.8), (1, 0.5, -0.8),
        # (-1, -0.5, -0.8), (-1, -0.5, 0.8), (1, -0.5, 0.8), (1, -0.5, -0.8)
        (0, -1.5, 2.5), (-2, -1.5, 0), (-2, 0, 2.5)
    )
    labels = ["B₁", "A₁", "D₁", "C₁", "B", "A", "D", "C", "4", "5", "3"]
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Темно-серый фон
    while not stop_event_local.is_set() and busy:
        mouse_buttons = pygame.mouse.get_pressed()
        button_down = mouse_buttons[0] == 1

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
                if event.button == 5:
                    zoom -= 0.2
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rot_x, rot_y, zoom = 30, 50, -5


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glTranslatef(0.0, 0.0, zoom)
        glRotatef(rot_x, 1, 0, 0)
        glRotatef(rot_y, 0, 1, 0)

        cube()

        font_size = max(30, 30 * (1 + zoom))  # Изменение размера текста в зависимости от масштаба
        for i, vertex in enumerate(vertices):
            x, y, z = vertex

            if z == -2.5 and y == -1.5:  # Если вершина нижняя, опускаем текст под куб
                z -= 0.2

                if x == 2:
                    x += 0.2
                else:
                    x -= 0.2
            elif i == 10:  # Если вершина нижняя, опускаем текст под куб
                z += 0.2

            elif z == 2.5 and y == -1.5:  # Если вершина нижняя, опускаем текст под куб
                z += 0.2
                if x == 2:
                    x += 0.2
                else:
                    x -= 0.2




            elif z == 2.5 and y == 1.5:  # Если вершина нижняя, опускаем текст под куб

                z += 0.2
                if x == 2:
                    x += 0.2
                else:
                    x -= 0.2


            elif z == -2.5 and y == 1.5:  # Если вершина нижняя, опускаем текст под куб

                z -= 0.2
                if x == 2:
                    x += 0.2
                else:
                    x -= 0.2

            drawText3D(x, y, z, labels[i], font_size)



        drawText(30, 750, " Тип 3. Задача №1", font)
        drawText(30, 720, " Площадь поверхности куба равна 18. Найдите его диагональ.",font)

        glPopMatrix()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    pygame_window_running = False

def start_pygame(e):
    threading.Thread(target=run_pygame_tip3_par2_sv, args=(e,)).start()

def main():
    ft.app(target=app, port=8552)

def app(page: ft.Page):
    start_button = ft.ElevatedButton("Запустить Pygame", on_click=start_pygame)
    page.add(start_button)

if __name__ == '__main__':
    main()