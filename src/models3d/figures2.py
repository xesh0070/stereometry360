
import flet as ft
import threading
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def triangular_prism():
    h = 2  # Высота призмы
    a = 2  # Длина стороны равностороннего треугольника
    half_base = a / 2
    height = (3 ** 0.5) / 2 * a  # Высота треугольника

    vertices = (
        (-half_base, -1, 0), (half_base, -1, 0), (0, -1, height),  # Нижнее основание
        (-half_base, -1 + h, 0), (half_base, -1 + h, 0), (0, -1 + h, height)  # Верхнее основание
    )
    edges = (
        (0, 1), (1, 2), (2, 0),  # Нижний треугольник
        (3, 4), (4, 5), (5, 3),  # Верхний треугольник
        (0, 3), (1, 4), (2, 5)  # Соединительные рёбра
    )
    faces = (
        (0, 1, 4, 3), (1, 2, 5, 4), (2, 0, 3, 5),  # Боковые грани
        (0, 1, 2), (3, 4, 5)  # Основания
    )

    # Рисуем грани
    glBegin(GL_QUADS)
    glColor3fv((0.6471, 0.5412, 0.9843))  # Фиолетовый цвет
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3fv((0.6471, 0.5412, 0.9843))  # Фиолетовый цвет
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    # Рисуем рёбра
    glBegin(GL_LINES)
    glColor3fv((1, 1, 1))  # Белый цвет
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()





def cube():
    # Определение координат вершин
    vertices = ((-1, -1, -1), (-1, 1, -1),
                (-1, 1, 1), (-1, -1, 1),
                (1, -1, -1), (1, 1, -1),
                (1, 1, 1), (1, -1, 1))
    # Определение ребер куба
    edges = ((0, 1), (0, 3), (0, 4),
             (1, 2), (1, 5), (2, 3),
             (2, 6), (3, 7), (4, 5),
             (4, 7), (5, 6), (6, 7))
    # Определение граней куба
    faces = ((0, 1, 2, 3), (4, 5, 6, 7),
             (0, 4, 7, 3), (1, 5, 6, 2),
             (2, 6, 7, 3), (1, 5, 4, 0))
    glLineWidth(1.5)
    glBegin(GL_QUADS) # Отрисовка граней
    for face in faces:
        glColor3fv((0.6471, 0.5412, 0.9843))
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES) # Отрисовка ребер
    glColor3fv((1, 1, 1))  # Белый цвет
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def inclined_prism():
    vertices = (
        (-1, -1, -0.8),  # 0
        (-0.6, 1, -0.8),  # 1
        (0.6, -1, -0.8),  # 2
        (1, 1, -0.8),    # 3
        (0.6, -1, 0.8),   # 4
        (1, 1, 0.8),      # 5
        (-1, -1, 0.8),    # 6
        (-0.6, 1, 0.8),   # 7
    )
    edges = (
        (0, 1), (2, 3), (4, 5), (6, 7),
        (0, 2), (2, 4), (4, 6), (6, 0),
        (1, 3), (3, 5), (5, 7), (7, 1),
    )
    faces = (
        (0, 1, 3, 2),  # Передняя грань
        (4, 5, 7, 6),  # Задняя грань
        (0, 2, 4, 6),  # Левая грань
        (1, 3, 5, 7),  # Правая грань
        (0, 1, 7, 6),  # Верхняя грань
        (2, 3, 5, 4),  # Нижняя грань
    )

    # Отрисовка граней
    glBegin(GL_QUADS)
    for face in faces:
        glColor3fv((0.6471, 0.5412, 0.9843))  # Фиолетовый цвет
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    # Отрисовка рёбер
    glBegin(GL_LINES)
    glColor3fv((1, 1, 1))  # Белый цвет
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def pentagonal_prism():
    vertices = (
        (0, 1, 0.5),       # 0
        (0, -1, 0.5),      # 1
        (-0.68, 1, 0),    # 2
        (-0.68, -1, 0),    # 3
        (-0.42, 1, -0.8),  # 4
        (-0.42, -1, -0.8), # 5
        (0.43, 1, -0.8),   # 6
        (0.43, -1, -0.8),  # 7
        (0.68, 1, 0),      # 8
        (0.68, -1, 0),     # 9
    )
    # Рёбра призмы
    edges = (
        (0, 1), (2, 3), (4, 5), (6, 7), (8, 9),  # боковые рёбра
        (0, 2), (2, 4), (4, 6), (6, 8), (0, 8),  # верхний пятиугольник
        (1, 3), (3, 5), (5, 7), (7, 9), (9, 1)   # нижний пятиугольник
    )
    # Грани призмы
    faces = (
        (0, 2, 4, 6, 8),  # Верхний пятиугольник
        (1, 3, 5, 7, 9),  # Нижний пятиугольник
        (0, 1, 3, 2),     # Боковая грань 1
        (2, 3, 5, 4),     # Боковая грань 2
        (4, 5, 7, 6),     # Боковая грань 3
        (6, 7, 9, 8),     # Боковая грань 4
        (8, 9, 1, 0)      # Боковая грань 5
    )

    # Отрисовка граней
    glBegin(GL_POLYGON)
    for face in faces[:2]:  # Отрисовка верхнего и нижнего пятиугольников
        glColor3fv((0.6471, 0.5412, 0.9843))  # Фиолетовый цвет
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_QUADS)
    for face in faces[2:]:  # Отрисовка боковых граней
        glColor3fv((0.6471, 0.5412, 0.9843))  # Голубой цвет
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    # Отрисовка рёбер
    glBegin(GL_LINES)
    glColor3fv((1, 1, 1))  # Белый цвет
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def hexagonal_prism():
    vertices = (
        (0, 0.5, -0.3),  # 0
        (0, -0.5, -0.3),  # 1
        (0.26, 0.5, -0.15),  # 2
        (0.26, -0.5, -0.15),  # 3
        (0.26, 0.5, 0.15),  # 4
        (0.26, -0.5, 0.15),  # 5
        (0, 0.5, 0.3),  # 6
        (0, -0.5, 0.3),  # 7
        (-0.26, 0.5, 0.15),  # 8
        (-0.26, -0.5, 0.15),  # 9
        (-0.26, 0.5, -0.15),  # 10
        (-0.26, -0.5, -0.15),  # 11
    )

    # Рёбра призмы
    edges = (
        (0, 1), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11),  # боковые рёбра
        (0, 2), (2, 4), (4, 6), (6, 8), (8, 10), (10, 0),  # верхний шестиугольник
        (1, 3), (3, 5), (5, 7), (7, 9), (9, 11), (11, 1)   # нижний шестиугольник
    )

    # Грани призмы
    faces = (
        (0, 2, 4, 6, 8, 10),  # верхний шестиугольник
        (1, 3, 5, 7, 9, 11),   # нижний шестиугольник
        (0, 1, 3, 2),          # боковая грань 1
        (2, 3, 5, 4),           # боковая грань 2
        (4, 5, 7, 6),           # боковая грань 3
        (6, 7, 9, 8),           # боковая грань 4
        (8, 9, 11, 10),         # боковая грань 5
        (10, 11, 1, 0)          # боковая грань 6
    )

    # Отрисовка граней
    # Верхний и нижний шестиугольники
    glBegin(GL_POLYGON)
    glColor3f(0.6471, 0.5412, 0.9843)  # Фиолетовый цвет
    for vertex in faces[0]:  # Верхний шестиугольник
        glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_POLYGON)
    glColor3fv((0.6471, 0.5412, 0.9843))  # Фиолетовый цвет
    for vertex in faces[1]:  # Нижний шестиугольник
        glVertex3fv(vertices[vertex])
    glEnd()

    # Боковые грани
    glBegin(GL_QUADS)
    glColor3f(0.6471, 0.5412, 0.9843)  # Голубой цвет
    for face in faces[2:]:  # Боковые грани
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    # Отрисовка рёбер
    glBegin(GL_LINES)
    glColor3fv((1, 1, 1))  # Белый цвет
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def piramid_3():
    vertices = (
        (1, -0.7, 0),        # Вершина A (0)
        (-0.48, -0.7, 0.85),  # Вершина B (1)
        (-0.48, -0.7, -0.85), # Вершина C (2)
        (0, 0.7, 0),          # Вершина E (верхушка) (3)
    )
    edges = (
        (0, 1),  # ребро AB
        (1, 2),  # ребро BC
        (2, 0),  # ребро CA
        (0, 3),  # ребро AE
        (1, 3),  # ребро BE
        (2, 3),  # ребро CE
    )
    faces = (
        (0, 1, 2),  # Основание (треугольник ABC)
        (0, 1, 3),  # Боковая грань ABE
        (1, 2, 3),  # Боковая грань BCE
        (2, 0, 3),  # Боковая грань CAE
    )

    glBegin(GL_TRIANGLES)
    glColor3f(0.6471, 0.5412, 0.9843)  # Цвет #6A5ACD (сланцевый синий)
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()



    # Отрисовка рёбер
    glBegin(GL_LINES)
    glColor3fv((1, 1, 1))  # Белый цвет для рёбер
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def piramid_4():
    vertices = (
        (1, -1, -1),  # Вершина A (0)
        (1, -1, 1),   # Вершина B (1)
        (-1, -1, 1),  # Вершина C (2)
        (-1, -1, -1), # Вершина D (3)
        (0, 1, 0),    # Вершина E (верхушка) (4)
    )
    edges = (
        (0, 1),  # ребро AB
        (1, 2),  # ребро BC
        (2, 3),  # ребро CD
        (3, 0),  # ребро DA
        (0, 4),  # ребро AE
        (1, 4),  # ребро BE
        (2, 4),  # ребро CE
        (3, 4),  # ребро DE
    )
    faces = (
        (0, 1, 2, 3),  # Основание (квадрат ABCD)
        (0, 1, 4),     # Боковая грань ABE
        (1, 2, 4),     # Боковая грань BCE
        (2, 3, 4),     # Боковая грань CDE
        (3, 0, 4),     # Боковая грань DAE
    )

    # Отрисовка граней
    # Основание (квадрат)
    glBegin(GL_QUADS)
    glColor3f(0.6471, 0.5412, 0.9843)  # Цвет #6A5ACD (сланцевый синий)
   # glColor3f(0.1137, 0.2157, 0.3137)  # Цвет #1d3750 (тёмно-синий)
    for vertex in faces[0]:
        glVertex3fv(vertices[vertex])
    glEnd()

    # Боковые грани (треугольники)
    glBegin(GL_TRIANGLES)
    glColor3f(0.6471, 0.5412, 0.9843)  # Цвет #6A5ACD (сланцевый синий)
   # glColor3f(0.1137, 0.2157, 0.3137)  # Цвет #1d3750 (тёмно-синий)
    for face in faces[1:]:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()


    # Отрисовка рёбер
    glBegin(GL_LINES)
    glColor3fv((1, 1, 1))  # Белый цвет для рёбер
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def piramid_4_ys():
    vertices = (
        (1, -1, -1),  # Вершина A (0)
        (0.35, 0.3, -0.35),  # Вершина B (1)
        (1, -1, 1),  # Вершина C (2)
        (0.35, 0.3, 0.35),  # Вершина D (3)
        (-1, -1, 1),  # Вершина E (4)
        (-0.35, 0.3, 0.35),  # Вершина F (5)
        (-1, -1, -1),  # Вершина G (6)
        (-0.35, 0.3, -0.35),  # Вершина H (7)
    )
    edges = (
        (0, 1), (2, 3), (4, 5), (6, 7),  # вертикальные рёбра
        (1, 3), (3, 5), (5, 7), (7, 1),  # верхние рёбра
        (0, 2), (2, 4), (4, 6), (6, 0),  # нижние рёбра
    )
    faces = (
        (0, 1, 3, 2),  # Передняя боковая грань
        (2, 3, 5, 4),  # Правая боковая грань
        (4, 5, 7, 6),  # Задняя боковая грань
        (6, 7, 1, 0),  # Левая боковая грань
        (0, 2, 4, 6),  # Нижнее основание
        (1, 3, 5, 7),  # Верхнее основание
    )

    # Отрисовка граней
    glBegin(GL_QUADS)
    glColor3f(0.6471, 0.5412, 0.9843)  # Цвет #1d3750 (тёмно-синий)
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()


    # Отрисовка рёбер
    glBegin(GL_LINES)
    glColor3fv((1, 1, 1))  # Белый цвет для рёбер
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def piramid_6():
    vertices = (
        (0, -0.2, -0.3),  # 0
        (0.26, -0.2, -0.15),  # 1
        (0.26, -0.2, 0.15),  # 2
        (0, -0.2, 0.3),  # 3
        (-0.26, -0.2, 0.15),  # 4
        (-0.26, -0.2, -0.15),  # 5
        (0, 0.4, 0)  # 6 (верхушка)
    )
    edges = (
        (0, 1),  # ребро AB
        (1, 2),  # ребро BC
        (2, 3),  # ребро CD
        (3, 4),  # ребро DE
        (4, 5),  # ребро EF
        (5, 0),  # ребро FA
        (6, 0),  # ребро A-верхушка
        (6, 1),  # ребро B-верхушка
        (6, 2),  # ребро C-верхушка
        (6, 3),  # ребро D-верхушка
        (6, 4),  # ребро E-верхушка
        (6, 5),  # ребро F-верхушка
    )
    faces = (
        (0, 1, 2, 3, 4, 5),  # Основание (шестиугольник ABCDEF)
        (0, 1, 6),  # Боковая грань AB-верхушка
        (1, 2, 6),  # Боковая грань BC-верхушка
        (2, 3, 6),  # Боковая грань CD-верхушка
        (3, 4, 6),  # Боковая грань DE-верхушка
        (4, 5, 6),  # Боковая грань EF-верхушка
        (5, 0, 6),  # Боковая грань FA-верхушка
    )

    # Отрисовка граней
    # Основание (шестиугольник)
    glBegin(GL_POLYGON)
    glColor3f(0.6471, 0.5412, 0.9843)  # Цвет #1d3750 (тёмно-синий)
    for vertex in faces[0]:
        glVertex3fv(vertices[vertex])
    glEnd()

    # Боковые грани (треугольники)
    glBegin(GL_TRIANGLES)
    glColor3f(0.6471, 0.5412, 0.9843)  # Цвет #1d3750 (тёмно-синий)
    for face in faces[1:]:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()
    glLineWidth(1.5)
    # Отрисовка рёбер
    glBegin(GL_LINES)
    glColor3fv((1, 1, 1))  # Белый цвет для рёбер
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
def konys():
    num_segments = 32  # Количество граней по окружности
    num_rings = 8  # Количество горизонтальных каркасных линий (широт)
    height = 2
    radius = 1

    glEnable(GL_BLEND)  # Включаем прозрачность
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # Полупрозрачные грани боковой поверхности
    glColor4f(0.6471, 0.5412, 0.9843, 0.8)  # Цвет + прозрачность
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, height / 2, 0)  # Вершина конуса
    for i in range(num_segments + 1):  # +1 для замыкания круга
        angle = 2 * math.pi * i / num_segments
        x = radius * math.cos(angle)
        z = radius * math.sin(angle)
        glVertex3f(x, -height / 2, z)
    glEnd()

    # Полупрозрачное основание
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, -height / 2, 0)  # Центр основания
    for i in range(num_segments + 1):
        angle = 2 * math.pi * i / num_segments
        x = radius * math.cos(angle)
        z = radius * math.sin(angle)
        glVertex3f(x, -height / 2, z)
    glEnd()

    # Белый каркас
    glColor3f(0.5, 0.433, 0.72)
    glBegin(GL_LINES)

    # Боковые рёбра
    for i in range(num_segments):
        angle = 2 * math.pi * i / num_segments
        x = radius * math.cos(angle)
        z = radius * math.sin(angle)
        glVertex3f(x, -height / 2, z)
        glVertex3f(0, height / 2, 0)  # Вершина конуса

    # Круговое основание (линии по краю)
    for i in range(num_segments):
        angle1 = 2 * math.pi * i / num_segments
        angle2 = 2 * math.pi * (i + 1) / num_segments
        x1 = radius * math.cos(angle1)
        z1 = radius * math.sin(angle1)
        x2 = radius * math.cos(angle2)
        z2 = radius * math.sin(angle2)

        glVertex3f(x1, -height / 2, z1)
        glVertex3f(x2, -height / 2, z2)

    # Радиальные линии к центру основания
    for i in range(num_segments):
        angle = 2 * math.pi * i / num_segments
        x = radius * math.cos(angle)
        z = radius * math.sin(angle)
        glVertex3f(0, -height / 2, 0)
        glVertex3f(x, -height / 2, z)

    # Горизонтальные каркасные линии (широты)


    glEnd()

def sphere():
    num_segments = 32
    num_rings = 16
    radius = 1

    glEnable(GL_BLEND)  # Включаем смешивание
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # Полупрозрачные грани
    glColor4f(0.6471, 0.5412, 0.9843, 0.8)  # Цвет + прозрачность
    glBegin(GL_QUADS)
    for j in range(num_rings):
        lat1 = math.pi * j / num_rings - math.pi / 2
        lat2 = math.pi * (j + 1) / num_rings - math.pi / 2
        y1, r1 = radius * math.sin(lat1), radius * math.cos(lat1)
        y2, r2 = radius * math.sin(lat2), radius * math.cos(lat2)
        for i in range(num_segments):
            lng1 = 2 * math.pi * i / num_segments
            lng2 = 2 * math.pi * (i + 1) / num_segments
            x1, z1 = r1 * math.cos(lng1), r1 * math.sin(lng1)
            x2, z2 = r1 * math.cos(lng2), r1 * math.sin(lng2)
            x3, z3 = r2 * math.cos(lng1), r2 * math.sin(lng1)
            x4, z4 = r2 * math.cos(lng2), r2 * math.sin(lng2)

            glVertex3f(x1, y1, z1)
            glVertex3f(x2, y1, z2)
            glVertex3f(x4, y2, z4)
            glVertex3f(x3, y2, z3)
    glEnd()

    glColor3f(0.5, 0.433, 0.72)
    glBegin(GL_LINES)
    for j in range(num_rings):
        lat = math.pi * j / num_rings - math.pi / 2
        y = radius * math.sin(lat)
        r = radius * math.cos(lat)
        for i in range(num_segments):
            angle1 = 2 * math.pi * i / num_segments
            angle2 = 2 * math.pi * (i + 1) / num_segments
            x1, z1 = r * math.cos(angle1), r * math.sin(angle1)
            x2, z2 = r * math.cos(angle2), r * math.sin(angle2)

            glVertex3f(x1, y, z1)
            glVertex3f(x2, y, z2)

    for i in range(num_segments):
        lng = 2 * math.pi * i / num_segments
        x = radius * math.cos(lng)
        z = radius * math.sin(lng)
        for j in range(num_rings):
            lat1 = math.pi * j / num_rings - math.pi / 2
            lat2 = math.pi * (j + 1) / num_rings - math.pi / 2
            y1 = radius * math.sin(lat1)
            y2 = radius * math.sin(lat2)

            glVertex3f(x * math.cos(lat1), y1, z * math.cos(lat1))
            glVertex3f(x * math.cos(lat2), y2, z * math.cos(lat2))
    glEnd()

def cylinder():
    num_segments = 32
    height = 2
    radius = 1

    glEnable(GL_BLEND)  # Включаем смешивание для прозрачности
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # Полупрозрачные боковые грани
    glColor4f(0.6471, 0.5412, 0.9843, 0.4)  # Цвет боковых граней + прозрачность
    for i in range(num_segments):
        angle1 = 2 * math.pi * i / num_segments
        angle2 = 2 * math.pi * (i + 1) / num_segments
        x1 = radius * math.cos(angle1)
        z1 = radius * math.sin(angle1)
        x2 = radius * math.cos(angle2)
        z2 = radius * math.sin(angle2)

        # Рисуем боковую поверхность
        glBegin(GL_QUADS)
        glVertex3f(x1, -height / 2, z1)
        glVertex3f(x2, -height / 2, z2)
        glVertex3f(x2, height / 2, z2)
        glVertex3f(x1, height / 2, z1)
        glEnd()

    # Рисуем боковые линии
    glColor3f(0.5, 0.433, 0.72)
    glBegin(GL_LINES)
    for i in range(num_segments):
        angle = 2 * math.pi * i / num_segments
        x = radius * math.cos(angle)
        z = radius * math.sin(angle)
        glVertex3f(x, -height / 2, z)
        glVertex3f(x, height / 2, z)  # Соединяем верх и низ
    glEnd()

    # Рисуем фиолетовую поверхность нижнего основания
    glColor4f(0.6471, 0.5412, 0.9843, 0.4)
    for i in range(num_segments):
        angle1 = 2 * math.pi * i / num_segments
        angle2 = 2 * math.pi * (i + 1) / num_segments
        x1 = radius * math.cos(angle1)
        z1 = radius * math.sin(angle1)
        x2 = radius * math.cos(angle2)
        z2 = radius * math.sin(angle2)

        # Нижнее основание (фиолетовая поверхность)
        glBegin(GL_QUADS)
        glVertex3f(x1, -height / 2, z1)
        glVertex3f(x2, -height / 2, z2)
        glVertex3f(0, -height / 2, 0)  # Радиальные линии к центру основания
        glVertex3f(x1, -height / 2, z1)
        glEnd()

    # Рисуем фиолетовую поверхность верхнего основания
    for i in range(num_segments):
        angle1 = 2 * math.pi * i / num_segments
        angle2 = 2 * math.pi * (i + 1) / num_segments
        x1 = radius * math.cos(angle1)
        z1 = radius * math.sin(angle1)
        x2 = radius * math.cos(angle2)
        z2 = radius * math.sin(angle2)

        # Верхнее основание (фиолетовая поверхность)
        glBegin(GL_QUADS)
        glVertex3f(x1, height / 2, z1)
        glVertex3f(x2, height / 2, z2)
        glVertex3f(0, height / 2, 0)  # Радиальные линии к центру верхней крышки
        glVertex3f(x1, height / 2, z1)
        glEnd()

    # Рисуем каркас на основаниях
    glColor3f(0.5, 0.433, 0.72)
    for i in range(num_segments):
        angle1 = 2 * math.pi * i / num_segments
        angle2 = 2 * math.pi * (i + 1) / num_segments
        x1 = radius * math.cos(angle1)
        z1 = radius * math.sin(angle1)
        x2 = radius * math.cos(angle2)
        z2 = radius * math.sin(angle2)

        # Радиальные линии для нижнего основания
        glBegin(GL_LINES)
        glVertex3f(x1, -height / 2, z1)
        glVertex3f(x2, -height / 2, z2)
        glEnd()

        # Радиальные линии для верхнего основания
        glBegin(GL_LINES)
        glVertex3f(x1, height / 2, z1)
        glVertex3f(x2, height / 2, z2)
        glEnd()

    # Рисуем диаметры для нижнего основания
    for i in range(num_segments // 2):  # Для каждого диаметра (половина сегментов)
        angle1 = 2 * math.pi * i / num_segments
        angle2 = 2 * math.pi * (i + num_segments // 2) / num_segments  # Противоположные точки

        x1 = radius * math.cos(angle1)
        z1 = radius * math.sin(angle1)
        x2 = radius * math.cos(angle2)
        z2 = radius * math.sin(angle2)

        # Рисуем диаметр на нижнем основании
        glBegin(GL_LINES)
        glVertex3f(x1, -height / 2, z1)
        glVertex3f(x2, -height / 2, z2)
        glEnd()

        # Рисуем диаметр на верхнем основании
        glBegin(GL_LINES)
        glVertex3f(x1, height / 2, z1)
        glVertex3f(x2, height / 2, z2)
        glEnd()



pygame_window_open = False
def run_pygame(draw_function, persp):
    global pygame_window_open

    # Проверка, открыто ли уже окно Pygame
    if pygame_window_open:
        return


    pygame.init()
    pygame_window_open = True
    screen = (800, 600)
    pygame.display.set_mode(screen, DOUBLEBUF | OPENGL)
    pygame.display.set_icon(pygame.image.load("./assets/objekte.png"))
    pygame.display.set_caption('Stereometry 360°')
    glMatrixMode(GL_PROJECTION)
    gluPerspective(persp, (screen[0] / screen[1]), 0.1, 50)
    glTranslate(0.0, 0.0, -5)
    glMatrixMode(GL_MODELVIEW)
    modelMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    rot_x, rot_y, zoom = 19, -19, -0.5
    while True:
        glPushMatrix()
        glLoadIdentity()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame_window_open = False
            elif (event.type == pygame.MOUSEMOTION
                  and pygame.mouse.get_pressed()[0]):
                rot_x += event.rel[1]
                rot_y += event.rel[0]
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rot_x, rot_y, zoom = 15, -19, -0.5
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    zoom += 0.2
                if event.button == 5:
                    zoom -= 0.2

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMultMatrixf(modelMatrix)
        modelMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, zoom)
        glRotatef(rot_x, 1, 0, 0)
        glRotatef(rot_y, 0, 1, 0)
        glMultMatrixf(modelMatrix)
        draw_function()
        glPopMatrix()
        pygame.display.flip()
        pygame.time.wait(10)


def start_pygame(e):
    threading.Thread(target=run_pygame).start()


def app(page: ft.Page):
    start_button = ft.ElevatedButton("Запустить Pygame", on_click=start_pygame)
    page.add(start_button)


if __name__ == '__main__':
    ft.app(target=app, port=8550)