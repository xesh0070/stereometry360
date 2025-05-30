import flet as ft
import threading
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math



def axy():
    # Определение координат вершин
    vertices = ((-1, 0, 0.8), (1, 0, 0.8),
                (1, 0, -0.8), (-1, 0, -0.8),
                (0.6, 0, -0.6), (-0.6, 0, 0.6)
                )
    edges = ((4, 5), (4, 5))

    faces = ((0, 1, 2, 3),)

    # Включаем прозрачность
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glBegin(GL_QUADS)  # Отрисовка граней
    for face in faces:
        glColor4fv((0.6471, 0.5412, 0.9843, 0.6))
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    glLineWidth(4)
    glBegin(GL_LINES)
    for edge in edges:
        glColor3fv((0.282, 0.820, 0.839))
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def draw_spheres():
    # Параметры шаров: (x, y, z)
    spheres = [
        (0.7, 0.0, 0.5),  # Шар 1

    ]

    radius = 0.015
    quadric = gluNewQuadric()
    glColor3fv(( 0.5255,  0.0275, 0.9608))  #

    for x, y, z in spheres:
        glPushMatrix()
        glTranslatef(x, y, z)
        gluSphere(quadric, radius, 20, 20)
        glPopMatrix()

def drawText3D(x, y, z, text, font_size):
    font = pygame.font.SysFont('Calibri', int(font_size))
    text_surface = font.render(text, True, (134, 7, 245, 0.)).convert_alpha()
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
def run_sled1(e, stop_event_local):
    global pygame_window_running
    pygame_window_running = True


    pygame.init()
    FPS = 60
    WIDTH, HEIGHT = 800, 600
    screen = (800, 600)
    pygame.display.set_mode(screen, DOUBLEBUF | OPENGL)
    pygame.display.set_icon(pygame.image.load("./assets/objekte.png"))
    pygame.display.set_caption('Stereometry 360°')

    font = pygame.font.SysFont('LaTeX', 20)


    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(35, (screen[0] / screen[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glTranslate(0.0, 0.0, -5)

    rot_x, rot_y, zoom =25, -25, -0.5
    clock = pygame.time.Clock()
    busy = True
    vertices = (
        (0.6, 0, -0.6), (0.7, 0.0, 0.5),  # Шар 1

    )
    labels = ["a", "M"]
    glClearColor(1.0, 1.0, 1.0, 1.0)
    while busy:
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
                    rot_x, rot_y, zoom = 25, -25, -0.5


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glTranslatef(0.0, 0.0, zoom)
        glRotatef(rot_x, 1, 0, 0)
        glRotatef(rot_y, 0, 1, 0)

        axy()
        draw_spheres()
        font_size = max(20, 20 * (1 + zoom))  # Изменение размера текста в зависимости от масштаба
        for i, vertex in enumerate(vertices):
            x, y, z = vertex
            if y == 0 :  # Если вершина нижняя, опускаем текст под куб
                y -= 0.04



            drawText3D(x, y, z, labels[i], font_size)

        drawText(30, 750, " Тип 3. Задача №1", font)
        drawText(30, 720, " Площадь поверхности куба равна 18. Найдите его диагональ.",font)

        glPopMatrix()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    pygame_window_running = False

def start_pygame(e):
    threading.Thread(target=run_sled1, args=(e,)).start()

def main():
    ft.app(target=app, port=8551)

def app(page: ft.Page):
    start_button = ft.ElevatedButton("Запустить Pygame", on_click=start_pygame)
    page.add(start_button)

if __name__ == '__main__':
    main()