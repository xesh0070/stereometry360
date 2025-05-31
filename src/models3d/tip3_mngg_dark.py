import flet as ft
import threading
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


pygame_window_running = False

def mngg():
    vertices = (
        (-2.5, 2, -2),  # A
        (-2.5, -2, -2),  # B
        (2.5, -2, -2),  # D
        (-2.5, -2, 2),  # H
        (2.5, -2, 2),  # C
        (-2.5, 2, 2),  # E 5

        (2.5, 0, -2),  # N
        (2.5, 0, 2),  # Q
        (-0.5, 2, -2),  # F
        (-0.5, 0, -2),  # S
        (-0.5, 0, 2),  # R
        (-0.5, 2, 2),  # P
    )
    edges = ( #ЛИЦЕВОЙ МНОГОУГОЛЬНИК
              (0,1), # AB
              (0, 8),  # AF
              (8, 9),  # FS
              (9, 6),  # SN
              (6, 2),  # ND
              (2, 1),  # DB
              # ЗАДНИЙ МНОГОУГОЛЬНИК
              (5,11 ),  #  EP
              (11,10 ),  # PR
              (10,7 ),  # RQ
              (7,4 ),  # QC
              (4,3 ),  # CH
              (3, 5),  # HE
              # СОЕДИНЕНИЕ
              (0, 5),  # AE
              (8,11 ),  # FP
              (9,10 ),  # SR
              (6, 7),  # NQ
              (2,4 ),  # DC
              (1,3 ),  # BH

    )



    glBegin(GL_LINES)
    for edge in edges:
        glColor3fv((1, 1, 1))  # Белый цвет
        for vertex in edge:
            glVertex3fv(vertices[vertex])
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
def run_pygame_tip3_mngg_dark(e, stop_event_local):
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
    gluPerspective(45, (screen[0] / screen[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glTranslate(0.0, 0.0, -5)

    rot_x, rot_y, zoom = 20, -15, -10
    clock = pygame.time.Clock()
    busy = True
    vertices = (
        (-2.5, 0, 2),  # HE 4
        (0, -2, 2),  # HC 5
        (-1.5, 2, -2),  # PE 2
        (-0.5, 1, -2),  # PR 2
        (-2.5, 2, 0),  # PR 4
    )
    labels = ["4", "5", "2", "2", "4"]

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
            if x == -2.5:

                x -= 0.25
            elif x == 0:
                y -= 0.45

            elif x == -0.5:
                x += 0.15

            drawText3D(x, y, z, labels[i], font_size)



        glPopMatrix()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    pygame_window_running = False

def start_pygame(e):
    threading.Thread(target=run_pygame_tip3_mngg_dark, args=(e,)).start()

def main():
    ft.app(target=app, port=8558)

def app(page: ft.Page):
    start_button = ft.ElevatedButton("Запустить Pygame", on_click=start_pygame)
    page.add(start_button)

if __name__ == '__main__':
    main()