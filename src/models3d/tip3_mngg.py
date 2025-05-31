import flet as ft
import threading
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Глобальная переменная для отслеживания состояния окна Pygame
pygame_window_running = False

def mngg():
    vertices = (
        (-2.5, 2, -2),  # A 0
        (-2.5, -2, -2),  # B 1
        (2.5, -2, -2),   # D 2
        (-2.5, -2, 2),   # H 3
        (2.5, -2, 2),    # C 4
        (-2.5, 2, 2),    # E 5
        (2.5, 0, -2),    # N 6
        (2.5, 0, 2),     # Q 7
        (-0.5, 2, -2),   # F 8
        (-0.5, 0, -2),   # S 9
        (-0.5, 0, 2),    # R 10
        (-0.5, 2, 2),     # P 11
        (-0.5, -2, -2),  # u 12
        (-0.5, -2, 2)  # v 13
    )

    # Правильно определенные грани (полигоны)
    faces = [

        [0, 1, 12, 8],
        [12, 2, 6, 9],

        [5, 3, 13, 11],
        [13, 10, 7, 4],

        # Левая грань (A-E-H-B)
        [0, 5, 3, 1],
        # Правая грань (D-C-Q-N)
        [2, 4, 7, 6],
        # Верхняя грань (A-F-P-E)
        [0, 8, 11, 5],
        # Нижняя грань (B-H-C-D)
        [1, 3, 4, 2],
        # Центральный верхний полигон (F-S-R-P)
        [8, 9, 10, 11],
        # Центральный нижний полигон (N-Q-R-S)
        [6, 7, 10, 9]
    ]

    # Включаем прозрачность
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # Рисуем полупрозрачные грани
    glColor4f(0.5, 0.5, 1.0, 0.3)  # Голубой с прозрачностью
    for face in faces:
        glBegin(GL_POLYGON)
        for vertex in face:
            glVertex3fv(vertices[vertex])
        glEnd()

    # Рисуем белый каркас
    edges = (
        (0,1), (0,8), (8,9), (9,6), (6,2), (2,1),  # Передняя часть
        (5,11), (11,10), (10,7), (7,4), (4,3), (3,5),  # Задняя часть
        (0,5), (8,11), (9,10), (6,7), (2,4), (1,3)  # Соединяющие ребра
    )

    glLineWidth(1.5)
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def drawText3D(x, y, z, text, font_size):
    font = pygame.font.SysFont('arial', int(font_size))
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
def run_pygame_tip3_mngg(e, stop_event_local):
    global pygame_window_running
    pygame_window_running = True

    pygame.init()

    screen = (800, 600)
    pygame.display.set_mode(screen, DOUBLEBUF | OPENGL)
    pygame.display.set_icon(pygame.image.load("./assets/objekte.png"))
    pygame.display.set_caption('Stereometry 360°')

    font = pygame.font.SysFont('Verdana', 18)
    font2 = pygame.font.SysFont('Calibri', 20)
    font3 = pygame.font.SysFont('Calibri', 24)



    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (screen[0] / screen[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glTranslate(0.0, 0.0, -5)

    rot_x, rot_y, zoom = 20, -15, -10
    clock = pygame.time.Clock()
    busy = True
    vertices = (
        (-2.5,0,2), # HE 4
        (0, -2, 2),  # HC 5
        (-1.5, 2, -2),  # PE 2
        (-0.5, 1, -2),  # PR 2
        (-2.5, 2, 0),  # PR 4
    )
    labels = ["4","5","2","2", "4"]
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
                # Обработка нажатия кнопки
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rot_x, rot_y, zoom = 20, -15, -10

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glTranslatef(0.0, 0.0, zoom)
        glRotatef(rot_x, 1, 0, 0)
        glRotatef(rot_y, 0, 1, 0)

        mngg()
        font_size = max(12, 24 * (6 + zoom))  # Изменение размера текста в зависимости от масштаба
        for i, vertex in enumerate(vertices):
            x, y, z = vertex
            if   x == -2.5:

                x -= 0.25
            elif  x == 0:
                y -= 0.45

            elif  x == -0.5:
                x += 0.15

            drawText3D(x, y, z, labels[i], font_size)

        glPopMatrix()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    pygame_window_running = False

def start_pygame(e):
    threading.Thread(target=run_pygame_tip3_mngg, args=(e,)).start()

def main():
    ft.app(target=app, port=8550)

def app(page: ft.Page):
    start_button = ft.ElevatedButton("Запустить Pygame", on_click=start_pygame)
    page.add(start_button)

if __name__ == '__main__':
    main()