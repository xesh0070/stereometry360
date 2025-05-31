import flet as ft
import threading
import pygame

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *




def cube():
    vertices = (
        (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
        (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1),
        (1, 1, -3), (0, 1, -1), (1, 0 ,-1)
    )
    edges = (
        (0, 1), (0, 3), (0, 4), (2, 1), (2, 3), (2, 7),
        (6, 3), (6, 4), (6, 7), (5, 1), (5, 4), (5, 7), (9, 8), (10, 8)
    )
    dashed_edges = [(4, 7), (4, 10), (7, 9), (9, 10)]  # Оранжевые пунктирные линии


    glBegin(GL_LINES)
    for edge in edges:
        glColor3fv((1, 1, 1))  # Белый цвет
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in dashed_edges:
        glColor3fv((1, 0.5, 0))  # Белый цвет
        for vertex in edge:
            glVertex3fv(vertices[vertex])
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
def run_pygame_tip14_sech1(e, stop_event_local):
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
    gluPerspective(60, (screen[0] / screen[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glTranslate(0.0, 0.0, -5)

    rot_x, rot_y, zoom = 0, 0, -0.5
    clock = pygame.time.Clock()
    busy = True
    vertices = (
        (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
        (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1),
         (1, 1, -3), (0, 1, -1), (1, 0 ,-1)
    )
    labels = ["C", "C₁",  "D₁", "D","B", "B₁", "A", "A₁", "K", "F","E"]

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


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glTranslatef(0.0, 0.0, zoom)
        glRotatef(rot_x, 1, 0, 0)
        glRotatef(rot_y, 0, 1, 0)

        cube()
        font_size = max(10, 24 * (1 + zoom))  # Изменение размера текста в зависимости от масштаба
        for i, vertex in enumerate(vertices):
            x, y, z = vertex
            if y == -1 and x == 1:
                y -= 0.1
                x += 0.1
            elif y == -1 and x == -1:
                y -= 0.1
                x -= 0.2
            elif y == 1 and x == 1:
                y += 0.1
                x += 0.1
            elif y == 1 and x == -1:
                y += 0.1
                x -= 0.1
            elif i == 10:
                y -= 0.1
                x += 0.1
            elif i == 9:
                y += 0.1

            drawText3D(x, y, z, labels[i], font_size)


        glPopMatrix()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def start_pygame(e):
    threading.Thread(target=run_pygame_tip14_sech1(e)).start()


def main():
    ft.app(target=app, port=8550)


def app(page: ft.Page):
    start_button = ft.ElevatedButton("Запустить Pygame", on_click=start_pygame)
    page.add(start_button)


if __name__ == '__main__':
    main()