import flet as ft
import threading
import random
import pyperclip
import json
from pathlib import Path
# Модели для каталога моделей
from models3d.figures2 import run_pygame, hexagonal_prism

from pygame_manager import run_with_check
# Модели для задач типа 3
from models3d.tip3_cube2 import run_pygame1
from models3d.tip3_cube1 import run_pygame1_1
from models3d.tip3_cube1_svetl import run_pygame1_1_svetl
from models3d.tip3_par2_sv import run_pygame_tip3_par2_sv
from models3d.tip3_par2_dark import run_pygame_par2_dark
from models3d.tip3_pir import run_pygame_tip3_pir1
from models3d.tip3_mngg import run_pygame_tip3_mngg
from models3d.tip3_mngg_dark import run_pygame_tip3_mngg_dark


#Модели для задач типа 14
from models3d.tip14_rast import run_pygame_tip14_rast1
from models3d.tip14_rast2 import run_pygame_tip14_rast2
from models3d.ygol2 import run_pygame_tip14_ygol1
from models3d.ygol_sv import run_pygame_tip14_ygol1_sv
from models3d.tip14_sech1 import run_pygame_tip14_sech1
from models3d.tip14_V1 import run_pygame_tip14_V1

#Модели для теории
from models3d.axy import run_axy1
from models3d.axy2 import run_axy2
from models3d.axy3 import run_axy3
from models3d.sled_axy1 import run_sled1
from models3d.axy_task2 import run_axy_task2
from models3d.axy_task3 import run_axy_task3
from models3d.axy_task4 import run_axy_task4

from catalog_page import get_catalog_container
from theory_part1_axy import axy_task, sled_axy, axy
from theory_part2and3 import lines_arrangement, parallel_line_plane, parallel_line, parallel_planes, polyhedrons, perpendicular_line_plane
from theory_part4 import volumes


# Сохранение решённых задач типа 3.
SOLVED_TASKS_FILE = "solved_tasks.json"
solved_tasks = set()
def load_solved_tasks():
    global solved_tasks
    try:
        if Path(SOLVED_TASKS_FILE).exists():
            with open(SOLVED_TASKS_FILE, "r") as f:
                solved_tasks = set(json.load(f))
    except:
        solved_tasks = set()

def save_solved_tasks():
    with open(SOLVED_TASKS_FILE, "w") as f:
        json.dump(list(solved_tasks), f)

def add_solved_task(task_id):
    solved_tasks.add(task_id)
    save_solved_tasks()

def is_task_solved(task_id):
    return task_id in solved_tasks

load_solved_tasks()


def main(page: ft.Page):
    page.title = "Stereometry 360°"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_icon = "ico"

    #Функции для задач 3 типа
    def show_tip3_cube1_details0_2(e):
        details0_2.content = None
        global show_solution
        # Нахожу контейнер с полем ввода и результатом
        responsive_row = details0.content
        first_column = None
        for control in responsive_row.controls:
            if isinstance(control, ft.Column) and control.col.get("md") == 7:
                first_column = control
                break
        if show_solution:
            if len(first_column.controls) > 4:
                first_column.controls.pop()
            show_solution = False
            e.control.text = "Показать решение"
        else:
            solution_content = ft.Column(
                controls=[
                    ft.Text("Дано: S = 18", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("Найти: d ", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("Решение:", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("Пусть ребро куба равно a, тогда площадь поверхности куба S = 6a², а диагональ куба d = a√3", size=18),

                    ft.Text("Тогда диагональ куба равна:", size=18),
                    ft.Text("d = √3√(S/6) = √(3×S/6) = √(S/2) = √9 = 3", size=18),
                    ft.Text("Ответ: 3", size=18, weight=ft.FontWeight.BOLD),
                ],
                spacing=5,
                tight=True,
            )
            first_column.controls.append(solution_content)
            show_solution = True
            e.control.text = "Спрятать решение"

        page.update()

    def show_tip3_cube1(e):
        details0.content = None
        page.update()
        global show_solution
        show_solution = False
        # Галочка для хранения информации об статусе(решено/нет)
        checkmark = ft.Icon(
            name=ft.Icons.CHECK_CIRCLE_OUTLINE,
            color=ft.Colors.GREEN if is_task_solved("tip3_cube1") else ft.Colors.GREY,
            size=24
        )
        # Переменные для хранения состояния тем модели
        global light_theme_checked, dark_theme_checked, red_theme_checked
        light_theme_checked = False
        dark_theme_checked = False
        red_theme_checked = False

        def check_item_clicked(e, theme_type):
            global light_theme_checked, dark_theme_checked, red_theme_checked

            if theme_type == "light":
                light_theme_checked = not light_theme_checked
                if light_theme_checked:
                    dark_theme_checked = False
                    red_theme_checked = False
            elif theme_type == "dark":
                dark_theme_checked = not dark_theme_checked
                if dark_theme_checked:
                    light_theme_checked = False
                    red_theme_checked = False
            else:
                red_theme_checked = not red_theme_checked
                if red_theme_checked:
                    light_theme_checked = False
                    dark_theme_checked = False



            for item in theme_menu.items:
                if item.text == "Светлая тема":
                    item.checked = light_theme_checked
                elif item.text == "Темная тема":
                    item.checked = dark_theme_checked

            theme_menu.update()

        def handle_open_model(e):
            if light_theme_checked:
                start_pygame_with_cube1_sv(e)
            elif dark_theme_checked:
                start_pygame_with_cube1(e)

            else:
                start_pygame_with_cube1_sv(e)  # Светлая функция, если ничего не выбрано

        # меню выбора темы
        theme_menu = ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(
                    text="Светлая тема",
                    checked=False,
                    on_click=lambda e: check_item_clicked(e, "light"),

                ),
                ft.PopupMenuItem(
                    text="Темная тема",
                    checked=False,
                    on_click=lambda e: check_item_clicked(e, "dark"),

                ),

            ],
            icon=ft.Icons.MORE_VERT, style=ft.ButtonStyle(color="#4E426D"),
            tooltip="Выбор темы"
        )

        #поле ввода
        answer_input = ft.TextField(
            hint_text="Введите ответ",
            width=180,
            border_color="#4E426D",
            cursor_color="#4E426D",
            text_size=14,
            border_radius=20,
            content_padding=10,
            expand=True,
        )

        def check_answer(e):

            user_answer = answer_input.value.strip().replace(',', '.')
            try:
                num = int(user_answer)
                if num == 3:
                    feedback = f"Молодец! Ответ {num} верный! 🎉"
                    answer_input.border_color = ft.Colors.GREEN
                    # Добавляем задачу в решенные
                    add_solved_task("tip3_cube1")
                    # Обновляем галочку
                    update_checkmark("tip3_cube1", True)

                else:
                    feedback = f"Ответ {num} неверный. ❌"
                    answer_input.border_color = ft.Colors.RED
            except ValueError:
                feedback = "Введите число! ⚠️"
                answer_input.border_color = ft.Colors.ORANGE

            answer_input.hint_text = feedback
            answer_input.value = ""
            answer_input.width = max(180, len(feedback) * 9)
            page.update()

        def update_checkmark(task_id, is_solved=None):
            if is_solved is None:
                is_solved = is_task_solved(task_id)
            pass

        answer_input.on_submit = check_answer

        enter_icon = ft.IconButton(
            icon=ft.Icons.KEYBOARD_RETURN,
            icon_color="#4E426D",
            on_click=check_answer,
            tooltip="Проверить ответ",
        )
        # Основной контейнер задачи
        details0.content = ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={"sm": 12, "md": 7},
                    controls=[
                        ft.Text("Профильная математика. Тип 3. Стереометрия: Куб",
                                size=12, weight=ft.FontWeight.BOLD),
                        ft.Row(
                            controls=[
                                ft.OutlinedButton(
                                    "Задача 1",
                                    on_click=show_tip3_cube1,
                                    style=ft.ButtonStyle(color="black"), width=100),
                                ft.OutlinedButton(
                                    "Задача 2",
                                    on_click=show_tip3_cube2,
                                    style=ft.ButtonStyle(color="black"), width=100),
                            ],
                            spacing=10
                        ),
                        ft.Row([
                            ft.Text("Задача №1", size=24, weight=ft.FontWeight.BOLD),
                            checkmark
                        ], spacing=10),
                        ft.Text(
                            "Площадь поверхности куба равна 18. Найдите его диагональ.",
                            size=21,
                        ),
                        ft.Row(
                            controls=[
                                ft.Row(
                                    controls=[
                                        answer_input,
                                        enter_icon,
                                    ],
                                    spacing=10,
                                    alignment=ft.MainAxisAlignment.START,

                                ),
                                ft.Row([ft.TextButton(
                                    "Показать решение",
                                    on_click=show_tip3_cube1_details0_2,
                                    style=ft.ButtonStyle(color="#4E426D"),
                                ),], spacing =10,
                                ),


                            ],

                        ),

                    ],
                    spacing=10,

                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Column(
                    col={"sm": 9, "md": 5},
                    controls=[
                        ft.Container(height=5),
                        ft.Image(
                            src="assets/cube0.jpg",
                            width=190,
                            height=190,
                            fit=ft.ImageFit.SCALE_DOWN,


                        ),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    "Открыть 3d модель",
                                    on_click=handle_open_model,
                                    style=ft.ButtonStyle(color="#4E426D"),

                                    width=180
                                ),
                                theme_menu,
                            ],
                            spacing=5,
                            alignment=ft.MainAxisAlignment.CENTER,

                        ),
                    ],

                    spacing=15,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                ),
            ],
            spacing=20,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
        page.update()

    def show_tip3_cube2_details0_2(e):
        details0_2.content = None
        global show_solution

        responsive_row = details0.content
        first_column = None
        for control in responsive_row.controls:
            if isinstance(control, ft.Column) and control.col.get("md") == 7:
                first_column = control
                break

        if show_solution:

            if len(first_column.controls) > 4:
                first_column.controls.pop()
            show_solution = False
            e.control.text = "Показать решение"
        else:

            solution_content = ft.Column(
                controls=[
                    ft.Text("Дано: V = 8", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("Найти: S ", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("Решение:", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("Площадь поверхности куба выражается через его ребро a формулой S = 6a², объем формулой V = a³. Поэтому a³ = 8 откуда a = 2; ", size=18),
                    ft.Text("S = 6×2² = 24", size=18),

                    ft.Text("Ответ: 24", size=18, weight=ft.FontWeight.BOLD),
                ],
                spacing=5,
                tight=True,
            )

            first_column.controls.append(solution_content)
            show_solution = True
            e.control.text = "Спрятать решение"

        page.update()

    def show_tip3_cube2(e):
        details0.content = None
        page.update()

        global show_solution
        show_solution = False

        checkmark = ft.Icon(
            name=ft.Icons.CHECK_CIRCLE_OUTLINE,
            color=ft.Colors.GREEN if is_task_solved("tip3_cube2") else ft.Colors.GREY,
            size=24
        )
        def update_checkmark(task_id, is_solved=None):
            if is_solved is None:
                is_solved = is_task_solved(task_id)
            pass


        global light_theme_checked, dark_theme_checked
        light_theme_checked = False
        dark_theme_checked = False

        def check_item_clicked(e, theme_type):
            global light_theme_checked, dark_theme_checked

            if theme_type == "light":
                light_theme_checked = not light_theme_checked
                if light_theme_checked:
                    dark_theme_checked = False
            else:
                dark_theme_checked = not dark_theme_checked
                if dark_theme_checked:
                    light_theme_checked = False

            for item in theme_menu.items:
                if item.text == "Светлая тема":
                    item.checked = light_theme_checked
                elif item.text == "Темная тема":
                    item.checked = dark_theme_checked
            theme_menu.update()

        def handle_open_model(e):
            if light_theme_checked:
                start_pygame_with_cube1_sv(e)
            elif dark_theme_checked:
                start_pygame_with_cube1(e)
            else:
                start_pygame_with_cube1_sv(e)

        theme_menu = ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(
                    text="Светлая тема",
                    checked=False,
                    on_click=lambda e: check_item_clicked(e, "light"),

                ),
                ft.PopupMenuItem(
                    text="Темная тема",
                    checked=False,
                    on_click=lambda e: check_item_clicked(e, "dark"),

                ),
            ],
            icon=ft.Icons.MORE_VERT, style=ft.ButtonStyle(color="#4E426D"),
            tooltip="Выбор темы"
        )

        answer_input = ft.TextField(
            hint_text="Введите ответ",
            width=180,
            border_color="#4E426D",
            cursor_color="#4E426D",
            text_size=14,
            border_radius=20,
            content_padding=10,
            expand=True,
        )

        def check_answer(e):

            user_answer = answer_input.value.strip().replace(',', '.')
            try:
                num = int(user_answer)
                if num == 24:
                    feedback = f"Молодец! Ответ {num} верный! 🎉"
                    answer_input.border_color = ft.Colors.GREEN
                    # Добавляем задачу в решенные
                    add_solved_task("tip3_cube2")
                    # Обновляем галочку
                    update_checkmark("tip3_cube2", True)
                else:
                    feedback = f"Ответ {num} неверный. ❌"
                    answer_input.border_color = ft.Colors.RED
            except ValueError:
                feedback = "Введите число! ⚠️"
                answer_input.border_color = ft.Colors.ORANGE

            answer_input.hint_text = feedback
            answer_input.value = ""
            answer_input.width = max(180, len(feedback) * 9)
            page.update()

        answer_input.on_submit = check_answer

        enter_icon = ft.IconButton(
            icon=ft.Icons.KEYBOARD_RETURN,
            icon_color="#4E426D",
            on_click=check_answer,
            tooltip="Проверить ответ",
        )

        details0.content = ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={"sm": 12, "md": 7},
                    controls=[
                        ft.Text("Профильная математика. Тип 3. Стереометрия: Куб",
                                size=12, weight=ft.FontWeight.BOLD),
                        ft.Row(
                            controls=[
                                ft.OutlinedButton(
                                    "Задача 1",
                                    on_click=show_tip3_cube1,
                                    style=ft.ButtonStyle(color="black"), width=100),
                                ft.OutlinedButton(
                                    "Задача 2",
                                    on_click=show_tip3_cube2,
                                    style=ft.ButtonStyle(color="black"), width=100),
                            ],
                            spacing=10
                        ),
                        ft.Row([
                            ft.Text("Задача №2", size=24, weight=ft.FontWeight.BOLD),
                            checkmark
                        ], spacing=10),
                        ft.Text(
                            "Объем куба равен 8. Найдите площадь его поверхности.",
                            size=21,
                        ),
                        ft.Row(
                            controls=[
                                ft.Row(
                                    controls=[
                                        answer_input,
                                        enter_icon,
                                    ],
                                    spacing=10,
                                    alignment=ft.MainAxisAlignment.START,
                                ),
                                ft.TextButton(
                                    "Показать решение",
                                    on_click=show_tip3_cube2_details0_2,
                                    style=ft.ButtonStyle(color="#4E426D")
                                ),
                            ],
                        ),

                    ],
                    spacing=10,

                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Column(
                    col={"sm": 9, "md": 5},
                    controls=[
                        ft.Container(height=5),
                        ft.Image(
                            src="assets/cube0.jpg",
                            width=190,
                            height=190,
                            fit=ft.ImageFit.SCALE_DOWN
                        ),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    "Открыть 3d модель",
                                    on_click=handle_open_model,
                                    style=ft.ButtonStyle(color="#4E426D"),

                                    width=180
                                ),
                                theme_menu,
                            ],
                            spacing=5,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],

                    spacing=15,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            spacing=20,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
        page.update()

    def show_tip3_pir1_details0_2(e):
        global show_solution


        responsive_row = details0.content
        first_column = None
        for control in responsive_row.controls:
            if isinstance(control, ft.Column) and control.col.get("md") == 7:
                first_column = control
                break

        if show_solution:

            if len(first_column.controls) > 4:
                first_column.controls.pop()
            show_solution = False
            e.control.text = "Показать решение"
        else:
            solution_content = ft.Column(
                controls=[
                    ft.Text("Дано: SABCD — правильная пирамида; O − центр основания; SO = 15; BD = 16.  ",
                            size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("Найти: SA ", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("Решение:", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text(
                        "В правильной пирамиде вершина проецируется в центр основания, следовательно, \nSO является высотой пирамиды. Тогда по теореме Пифагора",
                        size=18),
                    ft.Row(
                        controls=[
                            ft.Text("SA² = SB² = SO² + BO² = SO² + (  ", size=17),
                            ft.Column(
                                controls=[
                                    ft.Text(" BD", size=17),
                                    ft.Container(width=30, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text("  2 ", size=17),
                                ],
                                spacing=0,
                            ),
                            ft.Text("  )² = 225 + 64 = 289; SA = 17", size=17),
                        ],
                        spacing=-10,
                    ),
                    ft.Text("Ответ: 17", size=18, weight=ft.FontWeight.BOLD),
                ],
                spacing=5,
            )

            first_column.controls.append(solution_content)
            show_solution = True
            e.control.text = "Спрятать решение"

        page.update()

    def show_tip3_pir1(e):
        details0.content = None
        page.update()

        global show_solution
        show_solution = False

        checkmark = ft.Icon(
            name=ft.Icons.CHECK_CIRCLE_OUTLINE,
            color=ft.Colors.GREEN if is_task_solved("tip3_pir1") else ft.Colors.GREY,
            size=24
        )
        def update_checkmark(task_id, is_solved=None):
            if is_solved is None:
                is_solved = is_task_solved(task_id)
            pass


        answer_input = ft.TextField(
            hint_text="Введите ответ",
            width=180,
            border_color="#4E426D",
            cursor_color="#4E426D",
            text_size=14,
            border_radius=20,
            content_padding=10,
            expand=True,
        )

        def check_answer(e):
            user_answer = answer_input.value.strip().replace(',', '.')
            try:
                num = int(user_answer)
                if num == 17:
                    feedback = f"Молодец! Ответ {num} верный! 🎉 "
                    answer_input.border_color = ft.Colors.GREEN
                    add_solved_task("tip3_pir1")
                    update_checkmark("tip3_pir1", True)
                else:
                    feedback = f"Ответ {num} неверный. ❌"
                    answer_input.border_color = ft.Colors.RED
            except ValueError:
                feedback = "Введите число! ⚠️"
                answer_input.border_color = ft.Colors.ORANGE

            answer_input.hint_text = feedback
            answer_input.value = ""
            answer_input.width = max(
                180,
                len(feedback) * 9
            )

            page.update()

        answer_input.on_submit = check_answer

        enter_icon = ft.IconButton(
            icon=ft.Icons.KEYBOARD_RETURN,
            icon_color="#4E426D",
            on_click=check_answer,
            tooltip="Проверить ответ",
        )

        details0.content = ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={"sm": 12, "md": 7},
                    controls=[
                        ft.Text("Профильная математика. Тип 3. Стереометрия: Пирамида",
                                size=12, weight=ft.FontWeight.BOLD),
                        ft.Row(
                            controls=[
                                ft.OutlinedButton(
                                    "Задача 1",
                                    on_click=show_tip3_pir1,
                                    style=ft.ButtonStyle(color="black"), width=100),
                                ft.OutlinedButton(
                                    "Задача 2",
                                    on_click=show_tip3_pir2,
                                    style=ft.ButtonStyle(color="black"), width=100),
                            ],
                            spacing=10
                        ),
                        ft.Row([
                            ft.Text("Задача №1", size=24, weight=ft.FontWeight.BOLD),
                            checkmark
                        ], spacing=10),
                        ft.Text(
                            "В правильной четырехугольной пирамиде SABCD точка O − центр основания, "
                            "S − вершина, SO = 15, BD = 16. Найдите боковое ребро SA.",
                            size=21,
                        ),
                        ft.Row(
                            controls=[
                                ft.Row(
                                    controls=[
                                        answer_input,
                                        enter_icon,
                                    ],
                                    spacing=10,
                                    alignment=ft.MainAxisAlignment.START,
                                ),
                                ft.TextButton(
                                    "Показать решение",
                                    on_click=show_tip3_pir1_details0_2,
                                    style=ft.ButtonStyle(color="#4E426D")
                                ),
                            ],
                        ),
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Column(
                    col={"sm": 9, "md": 5},
                    controls=[
                        ft.Container(height=5),
                        ft.Image(
                            src="assets/pir1.svg",
                            width=230,
                            height=230,
                            # fit=ft.ImageFit.SCALE_DOWN
                        ),
                        ft.ElevatedButton(
                            "Открыть 3d модель",
                            on_click=lambda e: start_pygame_with_pir1(e),
                            style=ft.ButtonStyle(color="#4E426D")
                        ),
                    ],
                    spacing=15,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            spacing=20,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
        page.update()

    def show_tip3_pir2(e):
        details0.content = None
        page.update()

        details0.content = ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={"sm": 12, "md": 7},
                    controls=[
                        ft.Text("Профильная математика. Тип 3. Стереометрия: Пирамида",
                                size=12, weight=ft.FontWeight.BOLD),

                        ft.Text("Извините, сейчас эта задача в разработке...", size=24, weight=ft.FontWeight.BOLD),
                    ]
                ),

            ],
            spacing=20,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
        page.update()

    def show_tip3_par1_details0_2(e):
        global show_solution
        responsive_row = details0.content
        first_column = None
        for control in responsive_row.controls:
            if isinstance(control, ft.Column) and control.col.get("md") == 7:
                first_column = control
                break

        if show_solution:
            if len(first_column.controls) > 4:
                first_column.controls.pop()
            show_solution = False
            e.control.text = "Показать решение"
        else:
            solution_content = ft.Column(
                controls=[
                    ft.Text("Дано:", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("ABCDA₁B₁C₁D₁ — прямоугольный параллелепипед", size=18),
                    ft.Text("BD₁ = 3; CD = 2; AD = 2; ", size=18),
                    ft.Text("Найти: AA₁ ", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("Решение:", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("Найдем диагональ BD прямоугольника ABCD по теореме Пифагора:", size=18),
                    ft.Text("BD = √(AD² + AB²) = √(AD² + CD²) = √8", size=18),
                    ft.Text("Рассмотрим прямоугольный треугольник DD₁B. По т. Пифагора:", size=18),
                    ft.Text("AA₁ = DD₁ = √(BD₁² - BD²) = √(9 - 8) = 1", size=18),
                    ft.Text("Ответ: 1", size=18, weight=ft.FontWeight.BOLD),
                ],
                spacing=5,
            )

            first_column.controls.append(solution_content)
            show_solution = True
            e.control.text = "Спрятать решение"

        page.update()

    def show_tip3_par1(e):
        details0.content = None
        page.update()

        global show_solution
        show_solution = False
        def update_checkmark(task_id, is_solved=None):
            if is_solved is None:
                is_solved = is_task_solved(task_id)
            pass
        checkmark = ft.Icon(
            name=ft.Icons.CHECK_CIRCLE_OUTLINE,
            color=ft.Colors.GREEN if is_task_solved("tip3_par1") else ft.Colors.GREY,
            size=24
        )

        answer_input = ft.TextField(
            hint_text="Введите ответ",
            width=180,
            border_color="#4E426D",
            cursor_color="#4E426D",
            text_size=14,
            border_radius=20,
            content_padding=10,
            expand=True,
        )

        def check_answer(e):
            user_answer = answer_input.value.strip().replace(',', '.')
            try:
                num = int(user_answer)
                if num == 1:
                    feedback = f"Молодец! Ответ {num} верный! 🎉"
                    answer_input.border_color = ft.Colors.GREEN
                    add_solved_task("tip3_par1")
                    update_checkmark("tip3_par1", True)
                else:
                    feedback = f"Ответ {num} неверный. ❌"
                    answer_input.border_color = ft.Colors.RED
            except ValueError:
                feedback = "Введите число! ⚠️"
                answer_input.border_color = ft.Colors.ORANGE

            answer_input.hint_text = feedback
            answer_input.value = ""
            answer_input.width = max(180, len(feedback) * 9)
            page.update()

        answer_input.on_submit = check_answer

        enter_icon = ft.IconButton(
            icon=ft.Icons.KEYBOARD_RETURN,
            icon_color="#4E426D",
            on_click=check_answer,
            tooltip="Проверить ответ",
        )

        details0.content = ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={"sm": 12, "md": 7},
                    controls=[
                        ft.Text("Профильная математика. Тип 3. Стереометрия: Параллелепипед",
                                size=12, weight=ft.FontWeight.BOLD),
                        ft.Row(
                            controls=[
                                ft.OutlinedButton(
                                    "Задача 1",
                                    on_click=show_tip3_par2,
                                    style=ft.ButtonStyle(color="black"), width=100),
                                ft.OutlinedButton(
                                    "Задача 2",
                                    on_click=show_tip3_par1,
                                    style=ft.ButtonStyle(color="black"), width=100),
                            ],
                            spacing=10
                        ),
                        ft.Row([
                            ft.Text("Задача №2", size=24, weight=ft.FontWeight.BOLD),
                            checkmark
                        ], spacing=10),
                        ft.Text(
                            "В прямоугольном параллелепипеде ABCDA₁B₁C₁D₁ известно, что BD₁=3, CD=2, AD=2. Найдите длину ребра AA₁",
                            size=21,
                        ),
                        ft.Row(
                            controls=[
                                ft.Row(
                                    controls=[
                                        answer_input,
                                        enter_icon,
                                    ],
                                    spacing=10,
                                    alignment=ft.MainAxisAlignment.START,
                                ),
                                ft.TextButton(
                                    "Показать решение",
                                    on_click=show_tip3_par1_details0_2,
                                    style=ft.ButtonStyle(color="#4E426D")
                                ),
                            ],
                        ),
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Column(
                    col={"sm": 9, "md": 5},
                    controls=[
                        ft.Container(height=5),
                        ft.Image(
                            src="assets/cube0_2.jpg",
                            width=250,
                            height=250,
                        ),
                        ft.ElevatedButton(
                            "Открыть 3d модель",
                            on_click=lambda e: start_pygame_with_cube2(e),
                            style=ft.ButtonStyle(color="#4E426D")
                        ),
                    ],
                    spacing=15,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            spacing=20,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
        page.update()

    def show_tip3_par2_details0_2(e):
        global show_solution
        responsive_row = details0.content
        first_column = None
        second_column = None
        for control in responsive_row.controls:
            if isinstance(control, ft.Column):
                if control.col.get("md") == 7:
                    first_column = control
                elif control.col.get("md") == 5:
                    second_column = control

        if show_solution:

            if len(first_column.controls) > 4:
                first_column.controls.pop()

            if len(second_column.controls) > 3:
                second_column.controls.pop()
            show_solution = False
            e.control.text = "Показать решение"
        else:
            solution_content = ft.ResponsiveRow(
                controls=[
                    ft.Column(
                        col={"sm": 12, "md": 12},
                        controls=[
                            ft.Text("Дано:", size=18, weight=ft.FontWeight.BOLD),
                            ft.Text("ABCDA₁B₁C₁D₁ — прямоугольный параллелепипед", size=18),
                            ft.Text("AB = 5; AD = 4; AA₁ = 3.", size=18),
                            ft.Text("Найти: ∠(ABD₁) ", size=18, weight=ft.FontWeight.BOLD),
                            ft.Text("Решение:", size=18, weight=ft.FontWeight.BOLD),
                            ft.Text("В прямоугольнике AA₁D₁D отрезок AD₁ является диагональю, A₁D₁ = AD. ", size=18),
                            ft.Text("По т. Пифагора: AD₁² = AA₁² + A₁D₁² = 9 + 16 = 25 ⇒ AD₁ = √25 = 5.", size=18),
                            ft.Text(
                                "Прямоугольный треугольник ABD₁ равнобедренный: AB = AD₁ = 5 значит, его острые углы равны 45°.",
                                size=18),
                            ft.Text("Ответ: 45", size=18, weight=ft.FontWeight.BOLD),
                        ]
                    )
                ],
                spacing=5,
            )

            solution_image = ft.Image(
                src="assets/par2_2.svg",
                width=245,
                height=180,
            )
            second_column.controls.append(solution_image)
            first_column.controls.append(solution_content)
            show_solution = True
            e.control.text = "Спрятать решение"

        page.update()

    def show_tip3_par2(e):
        details0.content = None
        page.update()
        global show_solution
        show_solution = False
        global light_theme_checked, dark_theme_checked
        light_theme_checked = False
        dark_theme_checked = False

        def check_item_clicked(e, theme_type):
            global light_theme_checked, dark_theme_checked

            if theme_type == "light":
                light_theme_checked = not light_theme_checked
                if light_theme_checked:
                    dark_theme_checked = False
            else:
                dark_theme_checked = not dark_theme_checked
                if dark_theme_checked:
                    light_theme_checked = False

            for item in theme_menu.items:
                if item.text == "Светлая тема":
                    item.checked = light_theme_checked
                elif item.text == "Темная тема":
                    item.checked = dark_theme_checked
            theme_menu.update()

        def handle_open_model(e):
            if light_theme_checked:
                start_pygame_with_par2_sv(e)
            elif dark_theme_checked:
                start_pygame_with_par2_dark(e)
            else:
                start_pygame_with_par2_sv(e)
        theme_menu = ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(
                    text="Светлая тема",
                    checked=False,
                    on_click=lambda e: check_item_clicked(e, "light"),

                ),
                ft.PopupMenuItem(
                    text="Темная тема",
                    checked=False,
                    on_click=lambda e: check_item_clicked(e, "dark"),

                ),
            ],
            icon=ft.Icons.MORE_VERT, style=ft.ButtonStyle(color="#4E426D"),
            tooltip="Выбор темы"
        )

        def update_checkmark(task_id, is_solved=None):
            if is_solved is None:
                is_solved = is_task_solved(task_id)
            pass

        checkmark = ft.Icon(
            name=ft.Icons.CHECK_CIRCLE_OUTLINE,
            color=ft.Colors.GREEN if is_task_solved("tip3_par2") else ft.Colors.GREY,
            size=24
        )

        answer_input = ft.TextField(
            hint_text="Введите ответ",
            width=180,
            border_color="#4E426D",
            cursor_color="#4E426D",
            text_size=14,
            border_radius=20,
            content_padding=10,
            expand=True,
        )

        def check_answer(e):

            user_answer = answer_input.value.strip().replace(',', '.')
            try:
                num = int(user_answer)
                if num == 45:
                    feedback = f"Молодец! Ответ {num} верный! 🎉"
                    answer_input.border_color = ft.Colors.GREEN
                    # Добавляем задачу в решенные
                    add_solved_task("tip3_par2")
                    # Обновляем галочку
                    update_checkmark("tip3_par2", True)
                else:
                    feedback = f"Ответ {num} неверный. ❌"
                    answer_input.border_color = ft.Colors.RED
            except ValueError:
                feedback = "Введите число! ⚠️"
                answer_input.border_color = ft.Colors.ORANGE

            answer_input.hint_text = feedback
            answer_input.value = ""
            answer_input.width = max(180, len(feedback) * 9)
            page.update()

        answer_input.on_submit = check_answer

        enter_icon = ft.IconButton(
            icon=ft.Icons.KEYBOARD_RETURN,
            icon_color="#4E426D",
            on_click=check_answer,
            tooltip="Проверить ответ",
        )
        details0.content = ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={"sm": 12, "md": 7},
                    controls=[
                        ft.Text("Профильная математика. Тип 3. Стереометрия: Параллелепипед",
                                size=12, weight=ft.FontWeight.BOLD),
                        ft.Row(
                            controls=[
                                ft.OutlinedButton(
                                    "Задача 1",
                                    on_click=show_tip3_par2,
                                    style=ft.ButtonStyle(color="black"), width=100),
                                ft.OutlinedButton(
                                    "Задача 2",
                                    on_click=show_tip3_par1,
                                    style=ft.ButtonStyle(color="black"), width=100),
                            ],
                            spacing=10
                        ),
                        ft.Row([
                            ft.Text("Задача №1", size=24, weight=ft.FontWeight.BOLD),
                            checkmark
                        ], spacing=10),
                        ft.Text(
                            "Найдите угол ABD₁ прямоугольного параллелепипеда, для которого AB=5, AD=4, AA₁=3. Дайте ответ в градусах.",

                            size=21,
                        ),
                        ft.Row(
                            controls=[
                                ft.Row(
                                    controls=[
                                        answer_input,
                                        enter_icon,
                                    ],
                                    spacing=10,
                                    alignment=ft.MainAxisAlignment.START,
                                ),
                                ft.TextButton(
                                    "Показать решение",
                                    on_click=show_tip3_par2_details0_2,
                                    style=ft.ButtonStyle(color="#4E426D")
                                ),
                            ],
                        ),
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Column(
                    col={"sm": 9, "md": 5},
                    controls=[
                        ft.Container(height=5),
                        ft.Image(
                            src="assets/par2_0.svg",
                            width=235,
                            height=185,
                        ),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    "Открыть 3d модель",
                                    on_click=handle_open_model,
                                    style=ft.ButtonStyle(color="#4E426D"),

                                    width=180
                                ),
                                theme_menu,
                            ],
                            spacing=5,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                    spacing=15,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            spacing=20,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
        page.update()

    def show_tip3_mngg1_details0_2(e):
        global show_solution
        responsive_row = details0.content
        first_column = None
        for control in responsive_row.controls:
            if isinstance(control, ft.Column) and control.col.get("md") == 7:
                first_column = control
                break

        if show_solution:

            if len(first_column.controls) > 4:
                first_column.controls.pop()
            show_solution = False
            e.control.text = "Показать решение"
        else:
            # Создаем содержимое решения
            solution_content = ft.Column(
                controls=[
                    ft.Text("Решение:", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text(
                        "Объем данного многогранника равен сумме объемов \nпрямоугольных параллелепипедов с ребрами 5, 4, 2 и 2, 2, 4:",
                        size=18),
                    ft.Text("V = V₁ + V₂ = 5×4×2 + 2×2×4 = 56", size=18),
                    ft.Text("Ответ: 56", size=18, weight=ft.FontWeight.BOLD),
                ],
                spacing=5,
            )

            first_column.controls.append(solution_content)
            show_solution = True
            e.control.text = "Спрятать решение"

        page.update()

    def show_tip3_mngg1(e):
        details0.content = None
        page.update()

        global show_solution
        show_solution = False

        def update_checkmark(task_id, is_solved=None):
            if is_solved is None:
                is_solved = is_task_solved(task_id)
            pass
        checkmark = ft.Icon(
            name=ft.Icons.CHECK_CIRCLE_OUTLINE,
            color=ft.Colors.GREEN if is_task_solved("tip3_mngg1") else ft.Colors.GREY,
            size=24
        )

        global light_theme_checked, dark_theme_checked
        light_theme_checked = False
        dark_theme_checked = False

        def check_item_clicked(e, theme_type):
            global light_theme_checked, dark_theme_checked

            if theme_type == "light":
                light_theme_checked = not light_theme_checked
                if light_theme_checked:
                    dark_theme_checked = False
            else:
                dark_theme_checked = not dark_theme_checked
                if dark_theme_checked:
                    light_theme_checked = False

            for item in theme_menu.items:
                if item.text == "Светлая тема":
                    item.checked = light_theme_checked
                elif item.text == "Темная тема":
                    item.checked = dark_theme_checked
            theme_menu.update()

        def handle_open_model(e):
            if light_theme_checked:
                start_pygame_with_mngg1(e)
            elif dark_theme_checked:
                start_pygame_with_mngg1_dark(e)
            else:
                start_pygame_with_mngg1_dark(e)

        theme_menu = ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(
                    text="Светлая тема",
                    checked=False,
                    on_click=lambda e: check_item_clicked(e, "light"),

                ),
                ft.PopupMenuItem(
                    text="Темная тема",
                    checked=False,
                    on_click=lambda e: check_item_clicked(e, "dark"),

                ),
            ],
            icon=ft.Icons.MORE_VERT, style=ft.ButtonStyle(color="#4E426D"),
            tooltip="Выбор темы"
        )

        answer_input = ft.TextField(
            hint_text="Введите ответ",
            width=180,
            border_color="#4E426D",
            cursor_color="#4E426D",
            text_size=14,
            border_radius=20,
            content_padding=10,
            expand=True,
        )

        def check_answer(e):

            user_answer = answer_input.value.strip().replace(',', '.')
            try:
                num = int(user_answer)
                if num == 56:
                    feedback = f"Молодец! Ответ {num} верный! 🎉"
                    answer_input.border_color = ft.Colors.GREEN
                    add_solved_task("tip3_mngg1")
                    update_checkmark("tip3_mngg1", True)
                else:
                    feedback = f"Ответ {num} неверный. ❌"
                    answer_input.border_color = ft.Colors.RED
            except ValueError:
                feedback = "Введите число! ⚠️"
                answer_input.border_color = ft.Colors.ORANGE

            answer_input.hint_text = feedback
            answer_input.value = ""
            answer_input.width = max(180, len(feedback) * 9)
            page.update()

        answer_input.on_submit = check_answer

        enter_icon = ft.IconButton(
            icon=ft.Icons.KEYBOARD_RETURN,
            icon_color="#4E426D",
            on_click=check_answer,
            tooltip="Проверить ответ",
        )

        details0.content = ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={"sm": 12, "md": 7},
                    controls=[
                        ft.Text("Профильная математика. Тип 3. Стереометрия: Объём многогранников",
                                size=12, weight=ft.FontWeight.BOLD),
                        ft.Row(
                            controls=[
                                ft.OutlinedButton(
                                    "Задача 1",
                                    on_click=show_tip3_mngg1,
                                    style=ft.ButtonStyle(color="black"), width=100),
                                ft.OutlinedButton(
                                    "Задача 2",
                                    on_click=show_tip3_mngg2,
                                    style=ft.ButtonStyle(color="black"), width=100),
                            ],
                            spacing=10
                        ),
                        ft.Row([
                            ft.Text("Задача №1", size=24, weight=ft.FontWeight.BOLD),
                            checkmark
                        ], spacing=10),
                        ft.Text(
                            "Найдите объем многогранника, изображенного на рисунке (все двугранные углы прямые).",
                            size=21,
                        ),
                        ft.Row(
                            controls=[
                                ft.Row(
                                    controls=[
                                        answer_input,
                                        enter_icon,
                                    ],
                                    spacing=10,
                                    alignment=ft.MainAxisAlignment.START,
                                ),
                                ft.TextButton(
                                    "Показать решение",
                                    on_click=show_tip3_mngg1_details0_2,
                                    style=ft.ButtonStyle(color="#4E426D")
                                ),
                            ],
                        ),
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Column(
                    col={"sm": 9, "md": 5},
                    controls=[
                        ft.Container(height=20),
                        ft.Image(
                            src="assets/mng1.svg",
                            width=200,
                            height=200,
                        ),
                        ft.Container(height=10),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    "Открыть 3d модель",
                                    on_click=handle_open_model,
                                    style=ft.ButtonStyle(color="#4E426D"),


                                    width=180
                                ),
                                theme_menu,
                            ],
                            spacing=5,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            spacing=20,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
        page.update()

    def show_tip3_mngg2(e):
        details0.content = None
        page.update()

        details0.content = ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={"sm": 12, "md": 7},
                    controls=[
                        ft.Text("Профильная математика. Тип 3. Стереометрия: Объём многогранников",
                                size=12, weight=ft.FontWeight.BOLD),

                        ft.Text("Извините, сейчас эта задача в разработке...", size=24, weight=ft.FontWeight.BOLD),
                    ]
                ),

            ],
            spacing=20,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
        page.update()

    def show_tip3_vprizm1_details0_2(e):
        global show_solution
        responsive_row = details0.content
        first_column = None
        for control in responsive_row.controls:
            if isinstance(control, ft.Column) and control.col.get("md") == 7:
                first_column = control
                break

        if show_solution:
            if len(first_column.controls) > 4:
                first_column.controls.pop()
            show_solution = False
            e.control.text = "Показать решение"
        else:
            solution_content = ft.Column(
                controls=[
                    ft.Text("Решение:", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text(
                        "Объем прямой призмы равен V = Sh, где S  — площадь основания, \nа h  — боковое ребро. Площадь правильного шестиугольника со стороной a, лежащего в основании, задается формулой",
                        size=18),
                    ft.Row(
                        controls=[
                            ft.Text("S = ", size=18),
                            ft.Column(
                                controls=[
                                    ft.Text(" 3√3 ", size=18),
                                    ft.Container(width=50, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text("  2 ", size=18),
                                ],
                                spacing=0,
                            ),
                            ft.Text("× a² = ", size=18),
                            ft.Column(
                                controls=[
                                    ft.Text(" 3√3 ", size=18),
                                    ft.Container(width=50, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text("  2 ", size=18),
                                ],
                                spacing=0,
                            ),
                            ft.Text("× 1² = ", size=18),
                            ft.Column(
                                controls=[
                                    ft.Text(" 3√3 ", size=18),
                                    ft.Container(width=50, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text("  2 ", size=18),
                                ],
                                spacing=0,
                            ),
                        ],
                        spacing=0,
                    ),
                    ft.Row(
                        controls=[
                            ft.Text("Тогда V призмы = Sh = ", size=18),
                            ft.Column(
                                controls=[
                                    ft.Text(" 3√3 ", size=18),
                                    ft.Container(width=50, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text("  2 ", size=18),
                                ],
                                spacing=0,
                            ),
                            ft.Text("× √3 = 4,5.", size=18),
                        ],
                        spacing=0,
                    ),
                    ft.Text("Ответ: 4,5", size=18, weight=ft.FontWeight.BOLD),
                ],
                spacing=5,
            )

            first_column.controls.append(solution_content)
            show_solution = True
            e.control.text = "Спрятать решение"

        page.update()

    def show_tip3_vprizm1(e):
        details0.content = None
        page.update()

        global show_solution
        show_solution = False
        def update_checkmark(task_id, is_solved=None):
            if is_solved is None:
                is_solved = is_task_solved(task_id)
            pass
        checkmark = ft.Icon(
            name=ft.Icons.CHECK_CIRCLE_OUTLINE,
            color=ft.Colors.GREEN if is_task_solved("tip3_vprizm1") else ft.Colors.GREY,
            size=24
        )

        answer_input = ft.TextField(
            hint_text="Введите ответ",
            width=180,
            border_color="#4E426D",
            cursor_color="#4E426D",
            text_size=14,
            border_radius=20,
            content_padding=10,
            expand=True,
        )

        def check_answer(e):

            user_answer = answer_input.value.strip().replace(',', '.')
            try:
                num = float(user_answer)
                if num == 4.5:
                    feedback = f"Молодец! Ответ {num} верный! 🎉"
                    answer_input.border_color = ft.Colors.GREEN
                    add_solved_task("tip3_vprizm1")
                    update_checkmark("tip3_vprizm1", True)
                else:
                    feedback = f"Ответ {num} неверный. ❌"
                    answer_input.border_color = ft.Colors.RED
            except ValueError:
                feedback = "Введите число! ⚠️"
                answer_input.border_color = ft.Colors.ORANGE

            answer_input.hint_text = feedback
            answer_input.value = ""
            answer_input.width = max(180, len(feedback) * 9)
            page.update()

        answer_input.on_submit = check_answer

        enter_icon = ft.IconButton(
            icon=ft.Icons.KEYBOARD_RETURN,
            icon_color="#4E426D",
            on_click=check_answer,
            tooltip="Проверить ответ",
        )

        details0.content = ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={"sm": 12, "md": 7},
                    controls=[
                        ft.Text("Профильная математика. Тип 3. Стереометрия: Объём призмы",
                                size=12, weight=ft.FontWeight.BOLD),
                        ft.Row(
                            controls=[
                                ft.OutlinedButton(
                                    "Задача 1",
                                    on_click=show_tip3_vprizm1,
                                    style=ft.ButtonStyle(color="black"), width=100),
                                ft.OutlinedButton(
                                    "Задача 2",
                                    on_click=show_tip3_vprizm2,
                                    style=ft.ButtonStyle(color="black"), width=100),
                            ],
                            spacing=10
                        ),
                        ft.Row([
                            ft.Text("Задача №1", size=24, weight=ft.FontWeight.BOLD),
                            checkmark
                        ], spacing=10),
                        ft.Text(
                            "Найдите объем правильной шестиугольной призмы, стороны основания которой равны 1, а боковые ребра равны √3",
                            size=21,
                        ),
                        ft.Row(
                            controls=[
                                ft.Row(
                                    controls=[
                                        answer_input,
                                        enter_icon,
                                    ],
                                    spacing=10,
                                    alignment=ft.MainAxisAlignment.START,
                                ),
                                ft.TextButton(
                                    "Показать решение",
                                    on_click=show_tip3_vprizm1_details0_2,
                                    style=ft.ButtonStyle(color="#4E426D")
                                ),
                            ],
                        ),
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Column(
                    col={"sm": 9, "md": 5},
                    controls=[
                        ft.Container(height=20),
                        ft.Image(
                            src="assets/sprizm1(2).svg",
                            width=180,
                            height=180,
                        ),
                        ft.ElevatedButton(
                            "Открыть 3d модель",
                            on_click=lambda e: start_pygame_with_figure(hexagonal_prism, 20),
                            style=ft.ButtonStyle(color="#4E426D")
                        ),
                    ],
                    spacing=15,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            spacing=20,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
        page.update()

    def show_tip3_vprizm2(e):
        details0.content = None
        page.update()
        details0.content = ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={"sm": 12, "md": 7},
                    controls=[
                        ft.Text("Профильная математика. Тип 3. Стереометрия: Объём призмы",
                                size=12, weight=ft.FontWeight.BOLD),

                        ft.Text("Извините, сейчас эта задача в разработке...", size=24, weight=ft.FontWeight.BOLD),
                    ]
                ),

            ],
            spacing=20,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
        page.update()

    def show_tip3_sprizm1_details0_2(e):
        global show_solution
        responsive_row = details0.content
        first_column = None
        for control in responsive_row.controls:
            if isinstance(control, ft.Column) and control.col.get("md") == 7:
                first_column = control
                break

        if show_solution:
            if len(first_column.controls) > 4:
                first_column.controls.pop()
            show_solution = False
            e.control.text = "Показать решение"
        else:
            solution_content = ft.Column(
                controls=[
                    ft.Text("Решение:", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("Площадь боковой поверхности призмы равна сумме площадей всех ее боковых граней:", size=18),
                    ft.Row(
                        controls=[
                            ft.Text("S(б.п) = 6S(гр.) = 6×5×10 = 300.", size=17),
                        ],
                        spacing=-10,
                    ),
                    ft.Text("Ответ: 300", size=18, weight=ft.FontWeight.BOLD),
                ],
                spacing=5,
            )
            first_column.controls.append(solution_content)
            show_solution = True
            e.control.text = "Спрятать решение"

        page.update()

    def show_tip3_sprizm1(e):
        details0.content = None
        page.update()

        global show_solution
        show_solution = False
        def update_checkmark(task_id, is_solved=None):
            if is_solved is None:
                is_solved = is_task_solved(task_id)
            pass
        checkmark = ft.Icon(
            name=ft.Icons.CHECK_CIRCLE_OUTLINE,
            color=ft.Colors.GREEN if is_task_solved("tip3_sprizm1") else ft.Colors.GREY,
            size=24
        )
        answer_input = ft.TextField(
            hint_text="Введите ответ",
            width=180,
            border_color="#4E426D",
            cursor_color="#4E426D",
            text_size=14,
            border_radius=20,
            content_padding=10,
            expand=True,
        )

        def check_answer(e):

            user_answer = answer_input.value.strip().replace(',', '.')
            try:
                num = int(user_answer)
                if num == 300:
                    feedback = f"Молодец! Ответ {num} верный! 🎉"
                    answer_input.border_color = ft.Colors.GREEN
                    add_solved_task("tip3_sprizm1")
                    update_checkmark("tip3_sprizm1", True)
                else:
                    feedback = f"Ответ {num} неверный. ❌"
                    answer_input.border_color = ft.Colors.RED
            except ValueError:
                feedback = "Введите число! ⚠️"
                answer_input.border_color = ft.Colors.ORANGE

            answer_input.hint_text = feedback
            answer_input.value = ""
            answer_input.width = max(180, len(feedback) * 9)
            page.update()

        answer_input.on_submit = check_answer

        enter_icon = ft.IconButton(
            icon=ft.Icons.KEYBOARD_RETURN,
            icon_color="#4E426D",
            on_click=check_answer,
            tooltip="Проверить ответ",
        )
        details0.content = ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={"sm": 12, "md": 7},
                    controls=[
                        ft.Text("Профильная математика. Тип 3. Стереометрия: Площадь боковой поверхности призмы",
                                size=12, weight=ft.FontWeight.BOLD),
                        ft.Row(
                            controls=[
                                ft.OutlinedButton(
                                    "Задача 1",
                                    on_click=show_tip3_sprizm1,
                                    style=ft.ButtonStyle(color="black"), width=100),
                                ft.OutlinedButton(
                                    "Задача 2",
                                    on_click=show_tip3_sprizm2,
                                    style=ft.ButtonStyle(color="black"), width=100),
                            ],
                            spacing=10
                        ),
                        ft.Row([
                            ft.Text("Задача №1", size=24, weight=ft.FontWeight.BOLD),
                            checkmark
                        ], spacing=10),
                        ft.Text(
                            "Найдите площадь боковой поверхности правильной шестиугольной призмы, сторона основания которой равна 5, а высота — 10.",
                            size=21,
                        ),
                        ft.Row(
                            controls=[
                                ft.Row(
                                    controls=[
                                        answer_input,
                                        enter_icon,
                                    ],
                                    spacing=10,
                                    alignment=ft.MainAxisAlignment.START,
                                ),
                                ft.TextButton(
                                    "Показать решение",
                                    on_click=show_tip3_sprizm1_details0_2,
                                    style=ft.ButtonStyle(color="#4E426D")
                                ),
                            ],
                        ),
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Column(
                    col={"sm": 9, "md": 5},
                    controls=[
                        ft.Container(height=20),
                        ft.Image(
                            src="assets/sprizm1(2).svg",
                            width=180,
                            height=180,
                        ),
                        ft.ElevatedButton(
                            "Открыть 3d модель",
                            on_click=lambda e: start_pygame_with_figure(hexagonal_prism, 20),
                            style=ft.ButtonStyle(color="#4E426D")
                        ),
                    ],
                    spacing=15,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            spacing=20,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
        page.update()

    def show_tip3_sprizm2(e):
        details0.content = None
        page.update()
        details0.content = ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={"sm": 12, "md": 7},
                    controls=[
                        ft.Text("Профильная математика. Тип 3. Стереометрия: Площидь призмы",
                                size=12, weight=ft.FontWeight.BOLD),

                        ft.Text("Извините, сейчас эта задача в разработке...", size=24, weight=ft.FontWeight.BOLD),
                    ]
                ),

            ],
            spacing=20,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
        page.update()

    def show_tip3_cyli(e):
        details0.content = None
        page.update()
        details0.content = ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={"sm": 12, "md": 7},
                    controls=[
                        ft.Text("Профильная математика. Тип 3. Стереометрия: Цилиндр (площадь)",
                                size=12, weight=ft.FontWeight.BOLD),

                        ft.Text("Извините, сейчас эти задачи в разработке...", size=24, weight=ft.FontWeight.BOLD),
                    ]
                ),

            ],
            spacing=20,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
        page.update()

    def show_tip3_sphere(e):
        details0.content = None
        page.update()

        details0.content = ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={"sm": 12, "md": 7},
                    controls=[
                        ft.Text("Профильная математика. Тип 3. Стереометрия: Сфера и шар",
                                size=12, weight=ft.FontWeight.BOLD),

                        ft.Text("Извините, сейчас эти задачи в разработке...", size=24, weight=ft.FontWeight.BOLD),
                    ]
                ),

            ],
            spacing=20,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
        page.update()




    def show_tip14_rast1_details0_2(e):
        global show_solution
        responsive_row = details0.content
        first_column = None
        for control in responsive_row.controls:
            if isinstance(control, ft.Column) and control.col.get("md") == 7:
                first_column = control
                break
        if show_solution:
            if len(first_column.controls) > 4:
                first_column.controls.pop()
            show_solution = False
            e.control.text = "Показать решение"
        else:

            solution_content = ft.Column(
                controls=[
                    ft.Text("Дано:", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("ABCDA₁B₁C₁D₁ — куб; AA₁ = 1", size=18),
                    ft.Text("a) Док-ть: BD₁ ⊥ AC", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("б) Найти: ρ(C; BD₁)", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("Решение:", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text(
                        "а) Проекция BD₁ на плоскость ABCD — это прямая BD. BD ⊥ AC (диагонали квадрата),\nпоэтому, по теореме о трех перпендикулярах, BD₁ ⊥ AC",
                        size=18),
                    ft.Text("б) Проведем отрезок CD₁ и опустим перпендикуляр CH на BD₁.", size=18),
                    ft.Text("Искомое расстояние равно высоте CH прямоугольного треугольника BCD₁ с прямым углом C:",
                            size=18),
                    ft.Row(
                        [
                            ft.Text("CH = ", size=18),
                            ft.Column(
                                [
                                    ft.Text("2S(BCD₁)", size=18),
                                    ft.Container(width=71, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text("BD", size=18),
                                ],
                                spacing=0,
                            ),
                            ft.Text(" = ", size=18),
                            ft.Column(
                                [
                                    ft.Text("CD₁ × BC", size=18),
                                    ft.Container(width=74, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text("BD₁", size=18),
                                ],
                                spacing=0,
                            ),
                            ft.Text(" = ", size=18),
                            ft.Column(
                                [
                                    ft.Text("√2", size=18),
                                    ft.Container(width=20, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text("√3", size=18),
                                ],
                                spacing=0,
                            ),
                            ft.Text(" = ", size=18),
                            ft.Column(
                                [
                                    ft.Text("√6", size=18),
                                    ft.Container(width=20, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text("3", size=18),
                                ],
                                spacing=0,
                            )
                        ],
                        spacing=0,
                    ),
                    ft.Row(
                        [
                            ft.Text("Ответ: ", size=18, weight=ft.FontWeight.BOLD),
                            ft.Column(
                                [
                                    ft.Text("√6", size=18),
                                    ft.Container(width=20, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text("3", size=18),
                                ],
                                spacing=0,
                            )
                        ],
                        spacing=0,
                    ),
                ],
                spacing=5,
            )

            first_column.controls.append(solution_content)
            show_solution = True
            e.control.text = "Спрятать решение"

        page.update()

    def show_tip14_rast(e):
        details0.content = None
        page.update()

        global show_solution
        show_solution = False

        details0.content = ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={"sm": 12, "md": 7},
                    controls=[
                        ft.Text("Профильная математика. Тип 14. Стереометрическая задача: Расстояния",
                                size=12, weight=ft.FontWeight.BOLD),
                        ft.Row(
                            controls=[
                                ft.OutlinedButton(
                                    "Задача 1",
                                    on_click=show_tip14_rast,
                                    style=ft.ButtonStyle(color="black"),
                                    width=100),
                                ft.OutlinedButton(
                                    "Задача 2",
                                    on_click=show_tip14_rast2,
                                    style=ft.ButtonStyle(color="black"),
                                    width=100),

                            ],
                            spacing=10
                        ),
                        ft.Text("Задача №1", size=24, weight=ft.FontWeight.BOLD),
                        ft.Column([
                            ft.Text("В кубе ABCDA₁B₁C₁D₁ все ребра равны 1.", size=20),
                            ft.Text("a) Докажите, что BD₁ ⊥ AC", size=20),
                            ft.Text("б) Найдите расстояние от точки C до прямой BD₁.", size=20),
                        ], spacing=3),
                        ft.Row(
                            controls=[

                                ft.TextButton(
                                    "Показать решение",
                                    on_click=show_tip14_rast1_details0_2,
                                    style=ft.ButtonStyle(color="#4E426D"))
                            ],
                        ),
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Column(
                    col={"sm": 9, "md": 5},
                    controls=[
                        ft.Container(height=5),
                        ft.Image(
                            src="assets/14кrast2.jpg",
                            width=260,
                            height=260,
                        ),
                        ft.ElevatedButton(
                            "Открыть 3d модель",
                            on_click=lambda e: start_pygame_with_rast1(e),
                            style=ft.ButtonStyle(color="#4E426D")
                        ),
                    ],
                    spacing=15,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            spacing=20,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
        page.update()

    def show_tip14_rast2_details0_2(e):
        global show_solution
        if show_solution:
            details0.content.controls[0].controls[0].controls = [
                ctrl for ctrl in details0.content.controls[0].controls[0].controls
                if not isinstance(ctrl, ft.Column) or "solution_content" not in getattr(ctrl, "id", "")
            ]
            show_solution = False
            e.control.text = "Показать решение"
        else:
            solution_content = ft.Column(
                [
                    ft.Text("Дано:", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("ABCD — тэтраэдр; AA₁ = 1, ", size=18),
                    ft.Text("DE = EC, ", size=18),
                    ft.Text("a) Док-ть: (ABE) ⊥ CD ", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("б) Найти: ρ(A; BE)  ", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("Решение:", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text(
                        "a) BE — высота равностороннего треугольника BCD. AE — высота равностороннего треугольника ACD",
                        size=18),
                    ft.Text(
                        "По­это­му BE ⊥ CD и AE ⊥ CD. Зна­чит, по при­зна­ку пер­пен­ди­ку­ляр­но­сти пря­мой и плос­ко­сти, (ABE) ⊥ CD.",
                        size=18),
                    ft.Text(
                        "б)Рас­смот­рим тре­уголь­ник AEB и его вы­со­ты AH и EM. Со­ста­вим ра­вен­ство: AH × BE = EM × AB. \n За­ме­тим те­перь, что тре­уголь­ник AEB рав­но­бед­рен­ный",
                        size=18),
                    ft.Row(
                        [
                            ft.Text("и AE = EB =  ", size=18),
                            ft.Column(
                                [
                                    ft.Text("√3 ", size=18),
                                    ft.Container(width=20, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text(" 2 ", size=18),
                                ],
                                spacing=0,
                            ),
                            ft.Text(", поэтому EM = √(  ", size=18),
                            ft.Column(
                                [
                                    ft.Text(" 3", size=18),
                                    ft.Container(width=20, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text(" 4", size=18),
                                ],
                                spacing=0,
                            ),
                            ft.Text(" - ", size=18),
                            ft.Column(
                                [
                                    ft.Text(" 1", size=18),
                                    ft.Container(width=20, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text(" 2 ", size=18),
                                ],
                                spacing=0,
                            ),
                            ft.Text(") = ", size=18),
                            ft.Column(
                                [
                                    ft.Text("√2", size=18),
                                    ft.Container(width=20, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text(" 2", size=18),
                                ],
                                spacing=0,
                            )
                        ],
                        spacing=0,
                    ),
                    ft.Row(
                        [
                            ft.Text("Тогда AH = ", size=18),
                            ft.Column(
                                [
                                    ft.Text("EM × AB", size=18),
                                    ft.Container(width=71, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text("    BE ", size=18),
                                ],
                                spacing=0,
                            ),
                            ft.Text(" = ", size=18),
                            ft.Column(
                                [
                                    ft.Text("√2", size=18),
                                    ft.Container(width=20, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text(" 2", size=18),
                                ],
                                spacing=0,
                            ),
                            ft.Text(" × 1 × ", size=18),
                            ft.Column(
                                [
                                    ft.Text(" 2 ", size=18),
                                    ft.Container(width=20, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text("√3", size=18),
                                ],
                                spacing=0,
                            ),
                            ft.Text(" = ", size=18),
                            ft.Column(
                                [
                                    ft.Text("√6", size=18),
                                    ft.Container(width=20, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text(" 3 ", size=18),
                                ],
                                spacing=0,
                            )
                        ],
                        spacing=0,
                    ),
                    ft.Row(
                        [
                            ft.Text("Ответ: ", size=18, weight=ft.FontWeight.BOLD),
                            ft.Column(
                                [
                                    ft.Text("√6", size=18),
                                    ft.Container(width=20, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text(" 3 ", size=18),
                                ],
                                spacing=0,
                            )
                        ],
                        spacing=0,
                    ),
                ],
                spacing=5,
            )

            main_column = details0.content.controls[0].controls[0]
            main_column.controls.append(solution_content)
            show_solution = True
            e.control.text = "Спрятать решение"

        page.update()

    def show_tip14_rast2(e):
        details0.content = None
        page.update()

        global show_solution
        show_solution = False

        details0.content = ft.Column(
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.ResponsiveRow(
                    controls=[
                        ft.Column(
                            col={"sm": 12, "md": 7},
                            controls=[
                                ft.Text("Профильная математика. Тип 14. Стереометрическая задача: Расстояния",
                                        size=12, weight=ft.FontWeight.BOLD),
                                ft.Row(
                                    controls=[
                                        ft.OutlinedButton(
                                            "Задача 1",
                                            on_click=show_tip14_rast,
                                            style=ft.ButtonStyle(color="black"),
                                            width=100),
                                        ft.OutlinedButton(
                                            "Задача 2",
                                            on_click=show_tip14_rast2,
                                            style=ft.ButtonStyle(color="black"),
                                            width=100),

                                    ],
                                    spacing=10
                                ),
                                ft.Text("Задача №2", size=24, weight=ft.FontWeight.BOLD),
                                ft.Column([
                                    ft.Text(
                                        "В тетраэдре ABCD, все рёбра которого равны 1, отметили середину ребра CD — точку E.",
                                        size=20),
                                    ft.Text("a) Докажите, что плоскость ABE перпендикулярна ребру CD", size=20),
                                    ft.Text("б) Найдите расстояние от точки A до прямой BE.", size=20),
                                ], spacing=3),
                                ft.Row(
                                    controls=[

                                        ft.TextButton(
                                            "Показать решение",
                                            on_click=show_tip14_rast2_details0_2,
                                            style=ft.ButtonStyle(color="#4E426D")
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                            ],
                            spacing=10,
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        ft.Column(
                            col={"sm": 12, "md": 5},
                            controls=[
                                ft.Container(
                                    content=ft.Image(
                                        src="assets/раст2.jpg",
                                        width=300,
                                        height=300,
                                        fit=ft.ImageFit.CONTAIN
                                    ),
                                    padding=10,
                                    alignment=ft.alignment.center
                                ),
                                ft.ElevatedButton(
                                    "Открыть 3d модель",
                                    on_click=lambda e: start_pygame_with_rast2(e),
                                    style=ft.ButtonStyle(color="#4E426D")
                                ),
                            ],
                            spacing=15,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ],
                    spacing=20,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                )
            ]
        )
        page.update()

    def show_tip14_ygol1_details0_2(e):
        global show_solution
        main_column = details0.content.controls[0].controls[0]
        solution_index = None
        for i, ctrl in enumerate(main_column.controls):
            if hasattr(ctrl, "id") and ctrl.id == "solution_content":
                solution_index = i
                break

        if show_solution:

            if solution_index is not None:
                main_column.controls.pop(solution_index)
            show_solution = False
            e.control.text = "Показать решение"
        else:

            solution_content = ft.Column(
                [
                    ft.Text("Дано:", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text(
                        "ABCA₁B₁C₁ — правильная треугольная призма ABCA₁B₁C₁;\nACB = 2 ; диагональ боковой грани = √5.",
                        size=18),
                    ft.Text("a) Док-ть: V(A₁BCC₁B₁) = 2V(AA₁BC)", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("б) Найти: ∠(A₁BC;ACB)  ", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("Решение:", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("a)Пусть S — площадь основания призмы, а h — её высота. Тогда V призмы равен Sh,",
                            size=18),
                    ft.Row(
                        [
                            ft.Text("а V(AA₁BC) ", size=18),
                            ft.Column(
                                [
                                    ft.Text(" 1 ", size=18),
                                    ft.Container(width=20, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text(" 3 ", size=18),
                                ],
                                spacing=0,
                            ),
                            ft.Text(" Sh. Таким образом, V(A₁BCC₁B₁) = Sh - ", size=18),
                            ft.Column(
                                [
                                    ft.Text(" 1 ", size=18),
                                    ft.Container(width=20, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text(" 3 ", size=18),
                                ],
                                spacing=0,
                            ),
                            ft.Text(" Sh = ", size=18),
                            ft.Column(
                                [
                                    ft.Text(" 2 ", size=18),
                                    ft.Container(width=20, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text(" 3 ", size=18),
                                ],
                                spacing=0,
                            ),
                            ft.Text(" Sh = 2V(AA₁BC). Ч.Т.Д.", size=18),
                        ],
                        spacing=0,

                    ),
                    ft.Text(
                        "б)Обозначим H середину ребра BC. Т.к. треугольник ABC равносторонний, а треугольник \nA₁BC — равнобедренный, AH ⊥ A₁H. Следовательно, ∠A₁HA — линейный угол двугранного угла \nс гранями BCA и BCA₁ Из треугольника A₁AB найдем A₁A = √(5 - 4) = 1 В треугольнике AHB найдем",
                        size=18),
                    ft.Row(
                        [
                            ft.Text("высоту AH = √(4 - 1) = √3. Из треугольника HAA₁ найдем: tg∠A₁HA = ", size=18),
                            ft.Column(
                                [
                                    ft.Text("AA₁", size=18),
                                    ft.Container(width=20, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text("AH", size=18),
                                ],
                                spacing=0,
                            ),
                            ft.Text(" = ", size=18),
                            ft.Column(
                                [
                                    ft.Text(" 1 ", size=18),
                                    ft.Container(width=20, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text("√3", size=18),
                                ],
                                spacing=0,
                            ),

                        ],
                        spacing=0,

                    ),
                    ft.Text(" Искомый угол = 30°", size=18),
                    ft.Row(
                        [
                            ft.Text("Ответ: 30° ", size=18, weight=ft.FontWeight.BOLD),
                        ],
                        spacing=0,
                    ),
                ],
                spacing=5,
            )
            solution_content.id = "solution_content"
            main_column.controls.append(solution_content)
            show_solution = True
            e.control.text = "Спрятать решение"

        page.update()

    def show_tip14_ygol1(e):

        details0.content = None
        page.update()

        global show_solution
        show_solution = False
        global light_theme_checked, dark_theme_checked
        light_theme_checked = False
        dark_theme_checked = False

        def check_item_clicked(e, theme_type):
            global light_theme_checked, dark_theme_checked

            if theme_type == "light":
                light_theme_checked = not light_theme_checked
                if light_theme_checked:
                    dark_theme_checked = False
            else:
                dark_theme_checked = not dark_theme_checked
                if dark_theme_checked:
                    light_theme_checked = False

            for item in theme_menu.items:
                if item.text == "Светлая тема":
                    item.checked = light_theme_checked
                elif item.text == "Темная тема":
                    item.checked = dark_theme_checked
            theme_menu.update()

        def handle_open_model(e):
            if light_theme_checked:
                start_pygame_with_ygol1_sv(e)
            elif dark_theme_checked:
                start_pygame_with_ygol1(e)
            else:
                start_pygame_with_ygol1_sv(e)

        theme_menu = ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(
                    text="Светлая тема",
                    checked=False,
                    on_click=lambda e: check_item_clicked(e, "light"),

                ),
                ft.PopupMenuItem(
                    text="Темная тема",
                    checked=False,
                    on_click=lambda e: check_item_clicked(e, "dark"),

                ),
            ],
            icon=ft.Icons.MORE_VERT, style=ft.ButtonStyle(color="#4E426D"),
            tooltip="Выбор темы"
        )

        details0.content = ft.Column(
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text("Профильная математика. Тип 14. Стереометрическая задача: Углы",
                                        size=12, weight=ft.FontWeight.BOLD),
                                ft.Row(
                                    [
                                        ft.OutlinedButton("Задача 1", on_click=show_tip14_ygol1,
                                                          style=ft.ButtonStyle(color="black"),
                                                          width=100),
                                        ft.OutlinedButton("Задача 2", on_click=show_tip14_ygol2,
                                                          style=ft.ButtonStyle(color="black"),
                                                          width=100),
                                    ],
                                    spacing=10,
                                ),
                                ft.Text("Задача №1", size=24, weight=ft.FontWeight.BOLD),
                                ft.Column([
                                    ft.Text(
                                        "Сторона основания правильной треугольной призмы ABCA₁B₁C₁ равна 2, а диагональ боковой грани равна √5. \nа)Докажите, что объем пирамиды A₁BCC₁B₁ вдвое больше объема пирамиды AA₁BC. \nб)Найдите угол между плоскостью A₁BC и плоскостью основания призмы.",
                                        size=18),
                                ], spacing=3),
                                ft.Row(
                                    [
                                        ft.TextButton(
                                            "Показать решение",
                                            on_click=show_tip14_ygol1_details0_2,
                                            style=ft.ButtonStyle(color="#4E426D")
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                ),
                            ],
                            spacing=5,
                            expand=True,
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        ft.Column(
                            [
                                ft.Image(
                                    src="assets/ygol.svg",
                                    width=250,
                                    height=250,
                                    fit=ft.ImageFit.CONTAIN
                                ),
                                ft.Row(
                                    controls=[
                                        ft.ElevatedButton(
                                            "Открыть 3d модель",
                                            on_click=handle_open_model,
                                            style=ft.ButtonStyle(color="#4E426D"),

                                            width=180
                                        ),
                                        theme_menu,
                                    ],
                                    spacing=5,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                            ],
                            spacing=15,
                            alignment=ft.MainAxisAlignment.START,
                        ),
                    ],
                    spacing=20,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                )
            ],
            alignment=ft.MainAxisAlignment.START,
        )
        page.update()

    def show_tip14_ygol2(e):
        details0.content = None
        page.update()
        details0.content = ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={"sm": 12, "md": 7},
                    controls=[
                        ft.Text("Профильная математика. Тип 3. Стереометрическая задача: Углы",
                                size=12, weight=ft.FontWeight.BOLD),

                        ft.Text("Извините, сейчас эта задача в разработке...", size=24, weight=ft.FontWeight.BOLD),
                    ]
                ),

            ],
            spacing=20,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
        page.update()


    def show_tip14_V1_details0_2(e):
        global show_solution
        global solution_content

        main_column = details0.content.controls[0].controls[0]

        if show_solution:
            if hasattr(show_tip14_V1_details0_2, 'solution_content'):
                if show_tip14_V1_details0_2.solution_content in main_column.controls:
                    main_column.controls.remove(show_tip14_V1_details0_2.solution_content)
            show_solution = False
            e.control.text = "Показать решение"
        else:

            if not hasattr(show_tip14_V1_details0_2, 'solution_content'):
                show_tip14_V1_details0_2.solution_content = ft.Column(

                                    controls=[
                                        ft.Row([
                                            ft.Text("Дано:", size=18, weight=ft.FontWeight.BOLD),
                                            ft.Text("△ABC и △MBC — правильные; (ABC)⊥(MBC);", size=18)
                                        ]),
                                        ft.Text("BC = 8; MP = PC; BT : TM  =  1 : 3.", size=18),
                                        ft.Text("a) Док-ть: CT > BP.", size=18, weight=ft.FontWeight.BOLD),
                                        ft.Text("б) Найти: Vпир.MRTA.", size=18, weight=ft.FontWeight.BOLD),
                                        ft.Text("Решение:", size=18, weight=ft.FontWeight.BOLD),
                                        ft.Text(
                                            "а)   За­ме­тим, что в тре­уголь­ни­ках TBC и PCB углы B и С равны, сто­ро­на BC общая, и BT мень­ше CP. \nТогда, за­пи­сы­вая тео­ре­му ко­си­ну­сов для сто­рон CT и BP этих тре­уголь­ни­ков, по­лу­ча­ем ис­ко­мое не­ра­вен­ство.",
                                            size=17),
                                        ft.Text(
                                            "б)   Про­ведём вы­со­ту AD тре­уголь­ни­ка ABC. В тоже время AD  — вы­со­та пи­ра­ми­ды MPTA, опу­щен­ная из ",
                                            size=17),
                                        ft.Row(
                                            [
                                                ft.Text("вер­ши­ны A на плос­кость ос­но­ва­ния MPT и AD =  ", size=17),
                                                ft.Column(
                                                    [
                                                        ft.Text("BC√3 ", size=17),
                                                        ft.Container(width=40, height=1, bgcolor=ft.Colors.BLACK),
                                                        ft.Text("  2 ", size=17),
                                                    ],
                                                    spacing=0,
                                                ),
                                                ft.Text(" = 4√3 ", size=17),
                                            ],
                                            spacing=-10,
                                        ),
                                        ft.Row(
                                            [
                                                ft.Text("S(MPT) = ", size=17),
                                                ft.Column(
                                                    [
                                                        ft.Text(" 3", size=17),
                                                        ft.Container(width=20, height=1, bgcolor=ft.Colors.BLACK),
                                                        ft.Text(" 8", size=17),
                                                    ],
                                                    spacing=0,
                                                ),
                                                ft.Text("S(BCM). Следовательно, ", size=18),
                                                ft.Text("S(MPT) = ", size=17),
                                                ft.Column(
                                                    [
                                                        ft.Text("3BC²√3", size=17),
                                                        ft.Container(width=50, height=1, bgcolor=ft.Colors.BLACK),
                                                        ft.Text("   32 ", size=17),
                                                    ],
                                                    spacing=0,
                                                ),
                                                ft.Text(" = ", size=17),
                                                ft.Column(
                                                    [
                                                        ft.Text("3 × 64√3", size=17),
                                                        ft.Container(width=70, height=1, bgcolor=ft.Colors.BLACK),
                                                        ft.Text("   32 ", size=17),
                                                    ],
                                                    spacing=0,
                                                ),
                                                ft.Text(" = 6√3 ", size=17),
                                            ],
                                            spacing=0,
                                        ),
                                        ft.Row(
                                            [
                                                ft.Text("Найдём объём пирамиды: V = ", size=17),
                                                ft.Column(
                                                    [
                                                        ft.Text(" 1", size=17),
                                                        ft.Container(width=20, height=1, bgcolor=ft.Colors.BLACK),
                                                        ft.Text(" 3", size=17),
                                                    ],
                                                    spacing=0,
                                                ),
                                                ft.Text("S(MPT) × AD = ", size=17),
                                                ft.Column(
                                                    [
                                                        ft.Text(" 1", size=17),
                                                        ft.Container(width=20, height=1, bgcolor=ft.Colors.BLACK),
                                                        ft.Text(" 3", size=17),
                                                    ],
                                                    spacing=0,
                                                ),
                                                ft.Text(" × 6√3 × 4√3 = 24 ", size=17),
                                            ],
                                            spacing=0,
                                        ),
                                        ft.Row(
                                            [
                                                ft.Text("Ответ: 24. ", size=18, weight=ft.FontWeight.BOLD),
                                            ],
                                            spacing=0,
                                        ),
                                    ],
                                    spacing=5,
                                )

            main_column.controls.append(show_tip14_V1_details0_2.solution_content)
            show_solution = True
            e.control.text = "Спрятать решение"

        page.update()

    def show_tip14_V1(e):
        details0.content = None
        page.update()

        global show_solution
        show_solution = False


        details0.content = ft.Column(
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.ResponsiveRow(
                    controls=[

                        ft.Column(
                            col={"sm": 12, "md": 7},
                            controls=[
                                ft.Text("Профильная математика. Тип 14. Стереометрическая задача: Объём",
                                        size=12, weight=ft.FontWeight.BOLD),
                                ft.Row(
                                    controls=[
                                        ft.OutlinedButton("Задача 1", on_click=show_tip14_V1,
                                                          style=ft.ButtonStyle(color="black"),
                                                          width=100),
                                        ft.OutlinedButton("Задача 2", on_click=show_tip14_V2,
                                                          style=ft.ButtonStyle(color="black"),
                                                          width=100),
                                    ],
                                    spacing=10,
                                ),
                                ft.Text("Задача №1", size=24, weight=ft.FontWeight.BOLD),
                                ft.Column([
                                    ft.Text(
                                        "Правильные треугольники ABC и MBC лежат в перпендикулярных\nплоскостях, BC  =  8. Точка P  — середина CM, а точка T\nделит отрезок BM так, что BT : TM  =  1 : 3.",
                                        size=20),
                                    ft.Text("a) Докажите, что CT > BP.", size=20),
                                    ft.Text("б) Вы­чис­ли­те объём пи­ра­ми­ды MPTA.", size=20),
                                ], spacing=3),
                                ft.Row(
                                    controls=[
                                        ft.TextButton(
                                            "Показать решение",
                                            on_click=show_tip14_V1_details0_2,
                                            style=ft.ButtonStyle(color="#4E426D"))
                                    ],
                                ),
                            ],
                            spacing=5,
                        ),

                        ft.Column(
                            col={"sm": 12, "md": 5},
                            controls=[
                                ft.Container(
                                    content=ft.Image(
                                        src="assets/v1.svg",
                                        width=250,
                                        height=250,
                                        fit=ft.ImageFit.CONTAIN,
                                    ),
                                    padding=10,
                                    alignment=ft.alignment.center,
                                ),
                                ft.ElevatedButton(
                                    "Открыть 3d модель",
                                    on_click=lambda e: start_pygame_with_V1(e),

                                    style=ft.ButtonStyle(color="#4E426D"),
                                    width=200,
                                )
                            ],
                            spacing=15,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        )
                    ],
                    spacing=20,
                )
            ]
        )
        page.update()

    def show_tip14_V2(e):
        details0.content = None
        page.update()

        details0.content = ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={"sm": 12, "md": 7},
                    controls=[
                        ft.Text("Профильная математика. Тип 14. Стереометрическая задача: Объём",
                                size=12, weight=ft.FontWeight.BOLD),

                        ft.Text("Извините, сейчас эта задача в разработке...", size=24, weight=ft.FontWeight.BOLD),
                    ]
                ),

            ],
            spacing=20,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
        page.update()
    def show_tip14_sech1_details0_2(e):
        global show_solution

        main_container = details0.content

        if show_solution:
            for control in main_container.controls[0].controls:
                if isinstance(control, ft.Column) and len(control.controls) > 4:
                    control.controls.pop()
                    break
            show_solution = False
            e.control.text = "Показать решение"
        else:
            solution_content = ft.Column(
                controls=[
                    ft.Row([
                        ft.Text("Дано:", size=18, weight=ft.FontWeight.BOLD),
                        ft.Text("ABCDA₁B₁C₁D₁ — куб; CE = EC₁; AA₁ = 2", size=18)
                    ]),
                    ft.Text("a) сечение куба плоскостью A₁BE — это равнобокая трапеция..",
                            size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("б) Найти: S(A₁BE)", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("Решение:", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text(
                        "а) Прямая BE пересекает прямую B₁C₁ в точке K. Прямая A₁K пересекает ребро C₁D₁ в его середине — точке F. \nA₁BEF — сечение куба плоскостью A₁BE. Равнобедренный треугольник A₁BK подобен треугольнику KFE, \nпоэтому FE∥A₁B, то есть A₁BEF — равнобокая трапеция.",
                        size=17),
                    ft.Text(
                        "б) Вычислим стороны треугольника A₁BK: A₁K = BK = 2BE = 2√5, A₁B = √2×AB = 2√2 и высота",
                        size=17),
                    ft.Row(
                        [
                            ft.Text("KH² = BK² - (  ", size=17),
                            ft.Column(
                                [
                                    ft.Text(" A₁B", size=17),
                                    ft.Container(width=33, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text("  2 ", size=17),
                                ],
                                spacing=0,
                            ),
                            ft.Text("  )² = 3√2. ", size=17),
                        ],
                        spacing=-10,
                    ),
                    ft.Row(
                        [
                            ft.Text("Поскольку EF — средняя линия треугольника A₁BK получаем: S(KEF) = ", size=17),
                            ft.Column(
                                [
                                    ft.Text(" 1", size=17),
                                    ft.Container(width=20, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text(" 4", size=17),
                                ],
                                spacing=0,
                            ),
                            ft.Text("S(A₁BK), ", size=18),
                        ],
                    ),
                    ft.Row(
                        [
                            ft.Text("S(A₁BEF) = S(A₁BK) - S(KEF) = ", size=17),
                            ft.Column(
                                [
                                    ft.Text(" 3", size=17),
                                    ft.Container(width=20, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text(" 4", size=17),
                                ],
                                spacing=0,
                            ),
                            ft.Text(" S(A₁BK) = ", size=17),
                            ft.Column(
                                [
                                    ft.Text(" 3", size=17),
                                    ft.Container(width=20, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text(" 4", size=17),
                                ],
                                spacing=0,
                            ),
                            ft.Text(" × ", size=17),
                            ft.Column(
                                [
                                    ft.Text(" 1", size=17),
                                    ft.Container(width=20, height=1, bgcolor=ft.Colors.BLACK),
                                    ft.Text(" 2", size=17),
                                ],
                                spacing=0,
                            ),
                            ft.Text(" × KH × A₁B = 4,5.", size=17),
                        ],
                        spacing=0,
                    ),
                    ft.Row(
                        [
                            ft.Text("Ответ: 4,5. ", size=18, weight=ft.FontWeight.BOLD),
                        ],
                        spacing=0,
                    ),
                ],
                spacing=5,
            )

            for control in main_container.controls[0].controls:
                if isinstance(control, ft.Column) and control.col.get("md") == 7:
                    control.controls.append(solution_content)
                    break

            show_solution = True
            e.control.text = "Спрятать решение"

        page.update()

    def show_tip14_sech1(e):
        details0.content = ft.Column(
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.ResponsiveRow(
                    controls=[
                        ft.Column(
                            col={"sm": 12, "md": 7},
                            controls=[
                                ft.Text("Профильная математика. Тип 14. Стереометрическая задача: Площадь сечения",
                                        size=12, weight=ft.FontWeight.BOLD),
                                ft.Row(
                                    controls=[
                                        ft.OutlinedButton("Задача 1", on_click=show_tip14_sech1,
                                                          style=ft.ButtonStyle(color="black"), width=100),
                                        ft.OutlinedButton("Задача 2", on_click=show_tip14_sech2,
                                                          style=ft.ButtonStyle(color="black"), width=100),
                                    ],
                                    spacing=10
                                ),
                                ft.Text("Задача №1", size=24, weight=ft.FontWeight.BOLD),
                                ft.Column([
                                    ft.Text("Точка E — середина ребра CC₁ куба ABCDA₁B₁C₁D₁.", size=20),
                                    ft.Text("a) Докажите, что сечение куба плоскостью A₁BE — это равнобокая трапеция.",
                                            size=20),
                                    ft.Text("б) Найдите площадь этого сечения, если ребра куба равны 2.", size=20),
                                ], spacing=3),

                                ft.Row(
                                    controls=[

                                        ft.TextButton(
                                            "Показать решение",
                                            on_click=show_tip14_sech1_details0_2,
                                            style=ft.ButtonStyle(color="#4E426D")
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                            ],
                            spacing=10,
                        ),
                        ft.Column(
                            col={"sm": 12, "md": 5},
                            controls=[
                                ft.Image(
                                    src="assets/sech1.svg",
                                    width=300,
                                    height=300,
                                    fit=ft.ImageFit.CONTAIN
                                ),
                                ft.ElevatedButton(
                                    "Открыть 3d модель",
                                    on_click=lambda e: start_pygame_with_sech1(e),
                                    style=ft.ButtonStyle(color="#4E426D")
                                ),
                            ],
                            spacing=15,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ],
                    spacing=20,
                )
            ],
            expand=True
        )
        page.update()

    def show_tip14_sech2(e):
        details0.content = None
        page.update()
        details0.content = ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={"sm": 12, "md": 7},
                    controls=[
                        ft.Text("Профильная математика. Тип 14. Стереометрическая задача: Площадь сечения",
                                size=12, weight=ft.FontWeight.BOLD),

                        ft.Text("Извините, сейчас эта задача в разработке...", size=24, weight=ft.FontWeight.BOLD),
                    ]
                ),

            ],
            spacing=20,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
        page.update()

    def show_axy(e):
       axy(a1, a2, a3, details1, page, start_pygame_with_axy1, start_pygame_with_axy2, start_pygame_with_axy3, e)

    def show_axy_sled(e):
        sled_axy(sled_a1, sled_a2, details1, page, start_pygame_with_sled1, start_pygame_with_axy2, e)

    def show_axy_task(e):
        axy_task(details0, page, details1, start_pygame_with_axy1, start_pygame_with_axy2, start_pygame_with_axy3, start_pygame_with_axy_task2,start_pygame_with_axy_task3,start_pygame_with_axy_task4, e)

    def show_parallel_line(e):
        parallel_line(e, page, details1)

    def show_parallel_line_plane(e):
        parallel_line_plane(e, page, details1)

    def show_lines_arrangement(e):
        lines_arrangement(e, page, details1)

    def show_parallel_planes(e):
        parallel_planes(e, page, details1)

    def show_polyhedrons(e):
        polyhedrons(e, page, details1)

    def show_perpendicular_line_plane(e):
        perpendicular_line_plane(e, page, details1)

    def show_volumes(e):
        volumes(e, page, details1)




    #Функции для создания выпадающих списков для задач егэ и теории
    def create_dropdown(button_text, options, button_color=ft.Colors.BLACK, ):
        dropdown_visible = False
        dropdown = ft.Column(controls=[], visible=False)

        def show_dropdown(e):
            nonlocal dropdown_visible
            dropdown_visible = True
            dropdown.visible = True
            page.update()

        def hide_dropdown(e):
            nonlocal dropdown_visible
            if not dropdown_hovered:
                dropdown.visible = False
                page.update()

        dropdown_hovered = False

        def on_dropdown_hover(e):
            nonlocal dropdown_hovered
            dropdown_hovered = e.data == "true"

        button = ft.TextButton(
            button_text,
            on_hover=show_dropdown,
            style=ft.ButtonStyle(color=button_color)
        )

        def show_random_task_0(e):
            show_random_task(e)

        dropdown.controls = [
            ft.TextButton(
                option,
                on_click=show_axy if option == "• Аксиомы" else show_axy_task if option == "• Задачи" else show_axy_sled if option == "• Следствия аксиом"
                else show_parallel_line if option =="• Параллельные прямые в пространстве" else show_parallel_line_plane if option == "• Параллельность прямой и плоскости" else show_lines_arrangement if option == "• Взаимное расположение прямых в пространстве" else show_parallel_planes if option == "• Параллельность плоскостей " else show_perpendicular_line_plane if option == "• Перпендикулярность прямой и плоскости "
                else show_volumes if option == "• Понятие объёма"
                else show_tip3_cube1 if option == "Куб" else show_tip3_pir1 if option == "Пирамида" else show_tip3_par2 if option == "Параллелепипед" else show_tip3_mngg1 if option == "Объём прямоугольных многогранников" else show_tip3_vprizm1 if option == "Призма (объём)" else show_tip3_sprizm1 if option == "Призма (площадь)" else show_tip3_cyli if option == "Цилиндр (площадь)" else show_tip3_sphere if option == "Сфера и шар" else show_random_task_0 if option == "Случайная задача"
                else show_tip14_rast if option == "Расстояния" else show_tip14_ygol1 if option == "Углы" else show_tip14_V1 if option == "Объём" else show_tip14_sech1 if option == "Площадь сечения" else None,

            ) for option in options
        ]

        container = ft.Container(
            content=ft.Column([
                button,
                ft.Container(
                    content=dropdown,
                    margin=ft.margin.only(left=20)
                )
            ]),
            on_hover=on_dropdown_hover,
            bgcolor=ft.Colors.TRANSPARENT,
        )

        return container, hide_dropdown


    container1, hide1 = create_dropdown("Тип 3. Стереометрия:",
                                        ["Куб", "Параллелепипед", "Пирамида", "Объём прямоугольных многогранников",
                                         "Призма (объём)", "Призма (площадь)", "Цилиндр (площадь)", "Сфера и шар", "Случайная задача"])

    container2, hide2 = create_dropdown("Тип 14. Стереометрическая\nзадача:", ["Углы", "Расстояния", "Площадь сечения", "Объём"])

    container3, hide3 = create_dropdown(
        "1. Аксиомы стереометрии.",
        ["• Аксиомы", "• Следствия аксиом", "• Задачи"],

        button_color=ft.Colors.BLACK,

    )
    container4, hide4 = create_dropdown(
        "2. Параллельность прямых и плоскостей",
        ["• Параллельные прямые в пространстве", "• Параллельность прямой и плоскости", "• Взаимное расположение прямых в пространстве", "• Параллельность плоскостей ", ],

        button_color=ft.Colors.BLACK,

    )
    container5, hide5 = create_dropdown(
        "3. Перпендикулярность прямых и плоскостей",
        ["• Перпендикулярность прямой и плоскости ", ],

        button_color=ft.Colors.BLACK,

    )

    container6, hide6 = create_dropdown(
        "4. Объёмы тел",
        ["• Понятие объёма", ],

        button_color=ft.Colors.BLACK,

    )


    # Функция для создания каталога фигур
    def show_catalog(e):
        main_container.content = ft.Row(
            [
                navigation,
                ft.VerticalDivider(width=1, color="#DDD"),
                get_catalog_container(page, details),
                details,
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.STRETCH,
        )
        page.update()

    # Функция главной тсраницы
    def glavn(e):

        main_container.content = ft.Row(
            [
                navigation,
                ft.VerticalDivider(width=1, color="#DDD"),
                glavn,

            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.STRETCH,
        )
        page.update()


    # Каталог ЕГЭ
    def show_catalog_ege(e):

        scrollable_content = ft.Column(
            [
                ft.Stack(
                    [
                        details0_2,
                        details0
                    ],
                    expand=True,
                )
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )

        main_container.content = ft.Row(
            [
                navigation,
                ft.VerticalDivider(width=1, color="#DDD"),
                catalog_ege,
                scrollable_content,
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.STRETCH,
            expand=True,
        )
        page.update()

    # Теория
    def show_teoria(e):

        main_container.content = ft.Row(
            [
                navigation,
                ft.VerticalDivider(width=1, color="#DDD"),
                teoria,
                details1
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.STRETCH,
        )
        page.update()


    # Вызов окна с моделями для задач егэ 3 типа
    def start_pygame_with_cube1(e):
        run_with_check(run_pygame1_1, e)
    def start_pygame_with_cube1_sv(e):
        run_with_check(run_pygame1_1_svetl, e)
    def start_pygame_with_cube2(e):
        run_with_check(run_pygame1, e)
    def start_pygame_with_par2_sv(e):
        run_with_check(run_pygame_tip3_par2_sv, e)
    def start_pygame_with_par2_dark(e):
        run_with_check(run_pygame_par2_dark, e)
    def start_pygame_with_pir1(e):
        run_with_check(run_pygame_tip3_pir1, e)
    def start_pygame_with_mngg1(e):
        run_with_check(run_pygame_tip3_mngg, e)
    def start_pygame_with_mngg1_dark(e):
        run_with_check(run_pygame_tip3_mngg_dark, e)


    # Вызов окна с моделями для задач егэ 14 типа
    def start_pygame_with_rast1(e):
        run_with_check(run_pygame_tip14_rast1, e)
    def start_pygame_with_rast2(e):
        run_with_check(run_pygame_tip14_rast2, e)
    def start_pygame_with_ygol1(e):
        run_with_check(run_pygame_tip14_ygol1, e)
    def start_pygame_with_ygol1_sv(e):
        run_with_check(run_pygame_tip14_ygol1_sv, e)
    def start_pygame_with_sech1(e):
        run_with_check(run_pygame_tip14_sech1, e)
    def start_pygame_with_V1(e):
        run_with_check(run_pygame_tip14_V1, e)
    def start_pygame_with_figure(draw_function, persp):
        threading.Thread(target=run_pygame, args=(draw_function, persp), daemon=True).start()

    # Вызов окна с моделями теории
    def start_pygame_with_axy1(e):
        run_with_check(run_axy1, e)
    def start_pygame_with_axy2(e):
        run_with_check(run_axy2, e)
    def start_pygame_with_axy3(e):
        run_with_check(run_axy3, e)

    def start_pygame_with_sled1(e):
        run_with_check(run_sled1, e)

    def start_pygame_with_axy_task2(e):
        run_with_check(run_axy_task2, e)
    def start_pygame_with_axy_task3(e):
        run_with_check(run_axy_task3, e)
    def start_pygame_with_axy_task4(e):
        run_with_check(run_axy_task4, e)

    # Изображения
    var = "assets/прекрасное творение вари 4.jpg"

    ico = "D:/pythonProject1/png/ico.ico"
    image_base64_2 = "D:/pythonProject1/png/cube0.jpg"
    cube2_2 = "assets/cube0_2.jpg"
    prism_3 = "assets/3prism.jpg"
    prism_4 = "assets/4_prism.jpg"
    prism_5 = "assets/5prism.jpg"
    prism_6 = "assets/6-2prism.jpg"
    prism_7 = "assets/nakl.prism.jpg"
    piramid_30 = "assets/3piramid.jpg"
    piramid_40 = "assets/4piramid.jpg"
    piramid_60 ="assets//6piramid.jpg"
    piramid_70 = "assets/ys_piramid.jpg"
    vrash1 ="assets/конус.jpg"
    vrash2 = "assets/илинндр.jpg"
    vrash3 = "assets/шар.jpg"
    rast14_2 = "assets/14кrast2.jpg"
    rast14_2_2 = "assets/раст2.jpg"
    sech1 = "assets/sech1.svg"
    vprizm1 = "assets/sprizm1(2).svg"
    pir1 = "assets/pir1.svg"
    mng1 = "assets/mng1.svg"
    ygol1 = "assets/ygol.svg"
    v1 =  "assets/v1.svg"
    a1 = "assets/a1.svg"
    a2 = "assets/a2.svg"
    a3 = "assets/a3_ok.svg"
    sled_a1 = "assets/sled_a1.svg"
    sled_a2 = "assets/sled_a2.svg"


    def copy_text(e):
        text_to_copy = "yanyuush@gmail.com"
        pyperclip.copy(text_to_copy)
        print("Текст скопирован!")

        if not hasattr(dlg_modal, 'original_content'):
            dlg_modal.original_content = dlg_modal.content

        dlg_modal.content = ft.Column(
            controls=[
                dlg_modal.original_content,
                ft.Text("Почта скопирована", color=ft.Colors.GREEN, size=12)
            ],
            tight=True,
        )
        e.page.update()

    def copy_text2(e):
        text_to_copy = "@yanyushh"
        pyperclip.copy(text_to_copy)
        print("Текст скопирован!")

        if not hasattr(dlg_modal, 'original_content'):
            dlg_modal.original_content = dlg_modal.content

        dlg_modal.content = ft.Column(
            controls=[
                dlg_modal.original_content,
                ft.Text("Тг скопирован", color=ft.Colors.GREEN, size=12)
            ],
            tight=True,
        )
        e.page.update()

    copy_button = ft.TextButton(
        "Почта: yanyuush@gmail.com",
        on_click=copy_text,
        icon=ft.Icons.COPY,
    )
    copy_button2 = ft.TextButton(
        "Telegram: @yanyushh",
        on_click=copy_text2,
        icon=ft.Icons.COPY,
    )
    dlg_modal = ft.AlertDialog(
        title=ft.Text("Приветствую!"),
        content=ft.Text(
            "Рада что вы заинтересовались моим проектом!\nБуду благодарна если вы отправите мне свои \nотзывы и/или предложения! \nЕсли вы обнаружили ошибку в работе моего \nприложения, прошу сообщить мне об этом!"),
        actions=[ ft.Column([copy_button,
            copy_button2,]),

        ],
        actions_alignment=ft.MainAxisAlignment.START,
    )

    def open_dlg_modal(e):

        current_page = e.page if hasattr(e, 'page') and e.page is not None else page

        if current_page is None:
            print("Ошибка: не удалось получить ссылку на страницу")
            return

        if dlg_modal not in current_page.overlay:
            current_page.overlay.append(dlg_modal)
        dlg_modal.open = True
        current_page.update()

    glavn = ft.Container(
        content=ft.Row(
            [
                ft.Container(

                    width=50,
                    height=50,
                ),
                ft.Column(
                    [
                        ft.Container(

                            width=50,
                            height=50,
                        ),
                        ft.Column([
                            ft.Text("Добро пожаловать в Stereometry 360°", size=20, weight=ft.FontWeight.BOLD,
                                    color="#837e94"),
                            ft.Column([

                                ft.Text("Изучи стереометрию", size=52, weight=ft.FontWeight.BOLD,
                                        color="#6A4C9C"),
                                ft.Text("со всех сторон!", size=52, weight=ft.FontWeight.BOLD,
                                        color="#6A4C9C"), ], spacing=-20),
                        ], spacing=-10),

                        ft.Text(
                            "Stereometry 360° — ваш надежный помощник в мире \nстереометрии! Погрузитесь в мир трёхмерных \nмоделей, исследуйте фигуры в интерактивном формате \nи освойте сложные концепции через наглядную \nвизуализацию в трёхмерном пространстве.",
                            size=20,
                            color="black"),
                        ft.Text(
                            "Предупреждение! \nПросим не открывать новые окна трёхмерных моделей при уже открытом окне!",
                            size=12, color="black"),

                        ft.Container(

                            width=25,
                            height=25,
                        ),
                        ft.Text(
                            "Что хочешь изучить сегодня?",
                            size=20,
                            color="black"),
                        ft.Row([
                            ft.OutlinedButton("Трёхмерные модели", on_click=show_catalog,
                                              style=ft.ButtonStyle(color="#6A4C9C"),
                                              width=200),
                            ft.OutlinedButton("Задачи ЕГЭ", on_click=show_catalog_ege,
                                              style=ft.ButtonStyle(color="#6A4C9C"),
                                              width=200),
                            ft.OutlinedButton("Теория", on_click=show_teoria,
                                              style=ft.ButtonStyle(color="#6A4C9C"),
                                              width=200),
                        ]),
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Column(
                    [

                        ft.Image(
                            var,
                            width=670,
                            height=670,
                            fit=ft.ImageFit.CONTAIN,
                        ),
                    ], expand=True,
                )

            ],

            spacing=0,
            alignment=ft.MainAxisAlignment.START,
            expand=True,
        ),
        expand=True,
        padding=0,
        border_radius=16,

    )

    # Функции рандомных задач типа 3
    def get_random_unsolved_task():
        # Список всех задач
        all_tasks = [
            ("tip3_cube1", "Куб: Задача 1", show_tip3_cube1),
            ("tip3_cube2", "Куб: Задача 2", show_tip3_cube2),
            ("tip3_pir1", "Пирамида: Задача 1", show_tip3_pir1),
            ("tip3_par1", "Параллелепипед: Задача 1", show_tip3_par1),
            ("tip3_par2", "Параллелепипед: Задача 2", show_tip3_par2),
            ("tip3_mngg1", "Многогранники: Задача 1", show_tip3_mngg1),
            ("tip3_vprizm1", "Призма (объем): Задача 1", show_tip3_vprizm1),
            ("tip3_sprizm1", "Призма (площадь): Задача 1", show_tip3_sprizm1)
        ]

        # Фильтр задач
        unsolved_tasks = [task for task in all_tasks if not is_task_solved(task[0])]

        if not unsolved_tasks:
            return None

        # Выбор случайной
        return random.choice(unsolved_tasks)

    def show_random_task(e):
        task = get_random_unsolved_task()
        if task:
            task_id, task_name, task_func = task
            task_func(e)

        else:
            # Если все задачи решены
            details0.content = ft.Column(
                controls=[
                    ft.Text("Поздравляем!", size=24, weight=ft.FontWeight.BOLD),
                    ft.Text("Вы решили все доступные задачи типа 3!", size=18),

                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
            page.update()


    catalog_ege = ft.Container(
        content=ft.Column(
            [
                ft.Column(
                    [
                        ft.Text("Каталог ЕГЭ:", size=24, weight=ft.FontWeight.BOLD,
                                color="#6A4C9C"),
                        ft.Text("Профильная математика", size=18, weight=ft.FontWeight.BOLD,
                                color="#6A4C9C"),
                    ],
                    spacing=3,
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Text("Первая часть:", size=16, color="black"),
                ft.Container(content=container1, on_hover=hide1),

                ft.Text("Вторая часть:", size=16, color="black"),
                ft.Container(content=container2, on_hover=hide2),

            ],
            spacing=5,
            alignment=ft.MainAxisAlignment.START,

        ),
        width=300,
        padding=20,
        border_radius=16,

    )
    teoria = ft.Container(
        content=ft.Column(
            [
                ft.Column(
                    [
                        ft.Text("Теория стереометрии:", size=24, weight=ft.FontWeight.BOLD,
                                color="#6A4C9C"),
                    ],
                    spacing=3,
                    alignment=ft.MainAxisAlignment.START,
                ),

                ft.Container(content=container3, on_hover=hide3),
                ft.Container(content=container4, on_hover=hide4),
                ft.Container(content=container5, on_hover=hide5),
                ft.Container(content=container6, on_hover=hide6),

            ],
            spacing=5,
            alignment=ft.MainAxisAlignment.START,
        ),
        width=300,
        padding=20,
        border_radius=16,

    )

    details = ft.Container(
        content=ft.Text("", size=16, color="#666"),
        expand=True,
        padding=20,
    )

    details0 = ft.Container(
        content=None,
        expand=True,
        padding=25,

    )
    details1 = ft.Container(
        content=None,
        expand=True,
        padding=25,

    )
    details0_2 = ft.Container(
        content=None,
        expand=True,
        padding=25,

    )
    details_main = ft.Container(
        content=None,
        expand=True,
        padding=25,

    )

    catalog = get_catalog_container(page, details)

    navigation = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Image(
                            src="assets/objekte.png",
                            width=35,
                            height=35
                        ),
                        ft.Text("Stereometry 360°", size=19, weight=ft.FontWeight.BOLD, color="#6A4C9C"),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10,
                ),

                ft.Column(
                    [
                        ft.TextButton("Главная", icon="home", on_click=glavn, icon_color="#4E426D",
                                      style=ft.ButtonStyle(color="#4E426D")),
                        ft.TextButton("Каталог моделей", on_click=show_catalog, icon="grid_view", icon_color="#4E426D",
                                      style=ft.ButtonStyle(color="#4E426D")),
                        ft.TextButton("Каталог ЕГЭ", on_click=show_catalog_ege, icon="school", icon_color="#4E426D",
                                      style=ft.ButtonStyle(color="#4E426D")),
                        ft.TextButton("Теория", on_click=show_teoria, icon="calculate", icon_color="#4E426D",
                                      style=ft.ButtonStyle(color="#4E426D")),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),

                # Добавляю расширяющийся контейнер для выравнивания кнопок внизу
                ft.Container(expand=True),
                ft.TextButton("Информация от автора", on_click=open_dlg_modal, style=ft.ButtonStyle(color="#4E426D"))
            ],
            spacing=20,
            expand=True,
        ),
        width=250,
        padding=20,
        bgcolor="#ECEAF1",
        border_radius=20,
    )

    main_container = ft.Container(
        content=ft.Row(
            [navigation, glavn, ],

            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.STRETCH,
        ),
        expand=True,
    )

    page.add(main_container)

ft.app(target=main, assets_dir="assets")
