import flet as ft
import threading
from models3d.figures2 import run_pygame, triangular_prism, pentagonal_prism, piramid_6, piramid_4, piramid_3, piramid_4_ys, konys, cylinder,inclined_prism, cube, hexagonal_prism, sphere
from pygame_manager import run_with_check


VRASH2_IMG = "assets/илинндр.jpg"
VRASH1_IMG = "assets/конус.jpg"
VRASH3_IMG = "assets/шар.jpg"
PIRAMID3_IMG = "assets/3piramid.jpg"
PIRAMID4_IMG = "assets/4piramid.jpg"
PIRAMID6_IMG = "assets/6piramid.jpg"
PIRAMID7_IMG = "assets/ys_piramid.jpg"
PRISM3_IMG = "assets/3prism.jpg"
PRISM4_IMG = "assets/4_prism.jpg"
PRISM5_IMG = "assets/5prism.jpg"
PRISM6_IMG = "assets/6-2prism.jpg"
PRISM7_IMG = "assets/nakl.prism.jpg"


def show_vrash(e, details_container):
    figures = [
        (VRASH2_IMG, "Цилиндр", lambda e: start_pygame_with_figure(cylinder, 70), 100),
        (VRASH1_IMG, "Конус", lambda e: start_pygame_with_figure(konys, 70), 100),
        (VRASH3_IMG, "Шар", lambda e: start_pygame_with_figure(sphere, 80), 100)
    ]

    figures_row = ft.Row(
        [
            ft.Column(
                [
                    ft.Image(
                        src=image,
                        width=150,
                        height=150,
                        fit=ft.ImageFit.CONTAIN
                    ),
                    ft.ElevatedButton(
                        text=title,
                        on_click=on_click,
                        style=ft.ButtonStyle(color="black"),
                        width=button_width
                    )
                ],
                spacing=10,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
            for image, title, on_click, button_width in figures
        ],
        spacing=30,
        wrap=True,
        run_spacing=30,
        scroll=ft.ScrollMode.AUTO,
        alignment=ft.MainAxisAlignment.CENTER
    )

    details_container.content = ft.Column(
        [
            ft.Text("Тела вращения", size=28, weight=ft.FontWeight.BOLD),
            ft.Text(
                "Тела вращения — объёмные тела, возникающие при вращении плоской геометрической фигуры, "
                "ограниченной кривой, вокруг оси, лежащей в той же плоскости.",
                size=20,
            ),
            ft.Text("Цилиндр", size=24, weight=ft.FontWeight.BOLD),
            ft.Text(
                "Цилиндр – фигура, полученная в результате вращения прямоугольника вокруг одной из его сторон.",
                size=20,
            ),
            ft.Text("Конус", size=24, weight=ft.FontWeight.BOLD),
            ft.Text(
                "Конус – фигура, полученная в результате вращения прямоугольного треугольника вокруг одного из катетов",
                size=20,
            ),
            ft.Text("Шар", size=24, weight=ft.FontWeight.BOLD),
            ft.Text(
                "Шар – фигура, полученная вращением полукруга вокруг его диаметра.",
                size=20,
            ),
            figures_row,
            ft.Container(height=5)
        ],
        spacing=12,
        scroll=ft.ScrollMode.AUTO
    )
    e.page.update()


def show_piramid(e, details_container):
    figures = [
        (PIRAMID3_IMG, "Треугольная", lambda e: start_pygame_with_figure(piramid_3, 40)),
        (PIRAMID4_IMG, "Четырёхугольная", lambda e: start_pygame_with_figure(piramid_4, 70)),
        (PIRAMID6_IMG, "Шестиугольная", lambda e: start_pygame_with_figure(piramid_6, 20)),
        (PIRAMID7_IMG, "Усеченная", lambda e: start_pygame_with_figure(piramid_4_ys, 70))
    ]

    figures_row = ft.Row(
        [
            ft.Column(
                [
                    ft.Image(
                        src=image,
                        width=150,
                        height=150,
                        fit=ft.ImageFit.CONTAIN
                    ),
                    ft.ElevatedButton(
                        text=title,
                        on_click=on_click,
                        style=ft.ButtonStyle(color="black"),
                        width=150
                    )
                ],
                spacing=10,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
            for image, title, on_click in figures
        ],
        spacing=30,
        wrap=True,
        run_spacing=30,
        scroll=ft.ScrollMode.AUTO,
        alignment=ft.MainAxisAlignment.CENTER
    )

    details_container.content = ft.Column(
        [
            ft.Text("Пирамида", size=28, weight=ft.FontWeight.BOLD),
            ft.Text(
                "N-угольная пирамида – многогранник, одна грань которого – n-угольник, а остальные грани – треугольники с общей вершиной.",
                size=20,
            ),
            ft.Text("Правильная пирамида", size=24, weight=ft.FontWeight.BOLD),
            ft.Text(
                "Правильная пирамида – пирамида, основанием которой является правильный многоугольник, а высота опускается в центр вписанной и описанной окружности многоугольника, лежащего в основании пирамиды.",
                size=20,
            ),
            ft.Text("Усеченная", size=24, weight=ft.FontWeight.BOLD),
            ft.Text(
                "Усеченная пирамида – многогранник, вершинами которого служат вершины основания пирамиды и вершины её сечения плоскостью, параллельной основанию.",
                size=20,
            ),
            figures_row,
            ft.Container(height=5)
        ],
        spacing=12,
        scroll=ft.ScrollMode.AUTO
    )
    e.page.update()


def show_prism(e, details_container):
    straight_prisms = [
        (PRISM3_IMG, "Треугольная", lambda e: start_pygame_with_figure(triangular_prism, 70)),
        (PRISM4_IMG, "Четырёхугольная", lambda e: start_pygame_with_figure(cube, 70)),
        (PRISM5_IMG, "Пятиугольная", lambda e: start_pygame_with_figure(pentagonal_prism, 50)),
        (PRISM6_IMG, "Шестиугольная", lambda e: start_pygame_with_figure(hexagonal_prism, 20))
    ]

    straight_prisms_row = ft.Row(
        [
            ft.Column(
                [
                    ft.Image(
                        src=image,
                        width=150,
                        height=150,
                        fit=ft.ImageFit.CONTAIN
                    ),
                    ft.ElevatedButton(
                        text=title,
                        on_click=on_click,
                        style=ft.ButtonStyle(color="black"),
                        width=150
                    )
                ],
                spacing=10,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
            for image, title, on_click in straight_prisms
        ],
        spacing=30,
        wrap=True,
        run_spacing=30,
        scroll=ft.ScrollMode.AUTO,
        alignment=ft.MainAxisAlignment.CENTER
    )

    inclined_prism_row = ft.Row(
        [
            ft.Column(
                [
                    ft.Image(
                        src=PRISM7_IMG,
                        width=190,
                        height=190,
                        fit=ft.ImageFit.CONTAIN
                    ),
                    ft.ElevatedButton(
                        text="Наклонная",
                        on_click=lambda e: start_pygame_with_figure(inclined_prism, 60),
                        style=ft.ButtonStyle(color="black"),
                        width=150
                    )
                ],
                spacing=5,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
        spacing=30,
        wrap=True,
        alignment=ft.MainAxisAlignment.CENTER
    )

    details_container.content = ft.Column(
        [
            ft.Text("Призма", size=28, weight=ft.FontWeight.BOLD),
            ft.Text(
                "Призма – это многогранник, две грани которого являются равными многоугольниками, находящимися в параллельных плоскостях, а остальные грани – параллелограммами.",
                size=20,
            ),
            ft.Text("Прямые призмы", size=24, weight=ft.FontWeight.BOLD),
            ft.Text(
                "Прямая призма – призма, боковые рёбра которой перпендикулярны основаниям.",
                size=20,
            ),
            straight_prisms_row,
            ft.Text("Наклонная призма", size=24, weight=ft.FontWeight.BOLD),
            ft.Text(
                "Наклонная призма – это призма, боковые рёбра которой не перпендикулярны основаниям.",
                size=20,
            ),
            inclined_prism_row,
            ft.Container(height=10)
        ],
        spacing=15,
        alignment=ft.MainAxisAlignment.START,
        scroll=ft.ScrollMode.AUTO
    )
    e.page.update()

def start_pygame_with_figure(draw_function, persp):
    threading.Thread(target=run_pygame, args=(draw_function, persp), daemon=True).start()

def get_catalog_container(page, details_container):
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Каталог моделей", size=28, weight=ft.FontWeight.BOLD, color="#6A4C9C"),
                ft.Text("Основные стереометрические фигуры:", size=16, color="black"),
                ft.ElevatedButton(
                    "Призмы",
                    on_click=lambda e: show_prism(e, details_container),
                    style=ft.ButtonStyle(color="#6A4C9C"),
                    width=200
                ),
                ft.ElevatedButton(
                    "Пирамиды",
                    on_click=lambda e: show_piramid(e, details_container),
                    style=ft.ButtonStyle(color="#6A4C9C"),
                    width=200
                ),
                ft.ElevatedButton(
                    "Тела вращения",
                    on_click=lambda e: show_vrash(e, details_container),
                    style=ft.ButtonStyle(color="#6A4C9C"),
                    width=200
                ),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.START,
        ),
        width=300,
        padding=20,
        border_radius=16,
    )