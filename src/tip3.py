import flet as ft
import threading
import random
import json
from pathlib import Path


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
from models3d.figures2 import run_pygame, triangular_prism, pentagonal_prism,piramid_6, piramid_4, piramid_3, piramid_4_ys, konys, cylinder, inclined_prism, cube, hexagonal_prism, sphere
from пробую import run_pygame_cube

# Сохранение решённых задач типа 3.
SOLVED_TASKS_FILE = "solved_tasks.json"
solved_tasks = set()


# Вызов окна с моделями фигур
def start_pygame_with_figure(draw_function, persp):
    threading.Thread(target=run_pygame, args=(draw_function, persp), daemon=True).start()

def load_solved_tasks():
    global solved_tasks
    try:
        if Path(SOLVED_TASKS_FILE).exists():
            with open(SOLVED_TASKS_FILE, "r") as f:
                solved_tasks = set(json.load(f))
    except:
        solved_tasks = set()

#Сохранять решённые задачи
def save_solved_tasks():
    with open(SOLVED_TASKS_FILE, "w") as f:
        json.dump(list(solved_tasks), f)


def add_solved_task(task_id):
    solved_tasks.add(task_id)
    save_solved_tasks()

def is_task_solved(task_id):
    return task_id in solved_tasks

load_solved_tasks()


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


def start_pygame_with_red_cube(e):
    run_with_check(run_pygame_cube, e)
    
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

def show_tip3_cube1_details0_2(page, e):
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
        if len(first_column.controls) > 4:  # Проверяю, есть ли решение в контейнере
            first_column.controls.pop()
        show_solution = False
        e.control.text = "Показать решение"
    else:
        solution_content = ft.Column(
            controls=[
                ft.Text("Дано: S = 18", size=18, weight=ft.FontWeight.BOLD),
                ft.Text("Найти: d ", size=18, weight=ft.FontWeight.BOLD),
                ft.Text("Решение:", size=18, weight=ft.FontWeight.BOLD),
                ft.Text("Пусть ребро куба равно a, тогда площадь поверхности куба S = 6a², а диагональ куба d = a√3",
                        size=18),

                ft.Text("Тогда диагональ куба равна:", size=18),
                ft.Text("d = √3√(S/6) = √(3×S/6) = √(S/2) = √9 = 3", size=18),
                ft.Text("Ответ: 3", size=18, weight=ft.FontWeight.BOLD),
            ],
            spacing=5,
            tight=True,
        )

        # Добавляю решение после всех существующих элементов в колонне
        first_column.controls.append(solution_content)
        show_solution = True
        e.control.text = "Спрятать решение"

    page.update()


def show_tip3_cube1(page):
    details0.content = None
    page.update()
    global show_solution
    show_solution = False

    # Галочка для хранения информации об статусе задачи (решено/нет)
    checkmark = ft.Icon(
        name=ft.icons.CHECK_CIRCLE_OUTLINE,
        color=ft.colors.GREEN if is_task_solved("tip3_cube1") else ft.colors.GREY,
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
            elif item.text == "Редактировать":
                item.checked = red_theme_checked
        theme_menu.update()

    def handle_open_model(page, e):
        if light_theme_checked:
            start_pygame_with_cube1_sv(e)  # Если выбрана светлая тема вызывать функцию светлой темы
        elif dark_theme_checked:
            start_pygame_with_cube1(e)
            # Если выбрана тёмная тема вызывать функцию тёмной темы
        elif red_theme_checked:
            start_pygame_with_red_cube(e)
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
            ft.PopupMenuItem(
                text="Редактировать",
                checked=False,
                on_click=lambda e: check_item_clicked(e, "red"),

            ),
        ],
        icon=ft.icons.MORE_VERT, style=ft.ButtonStyle(color="#4E426D"),
        tooltip="Выбор темы"
    )

    # поле ввода
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
                answer_input.border_color = ft.colors.GREEN
                # Добавляем задачу в решенные
                add_solved_task("tip3_cube1")
                # Обновляем галочку
                update_checkmark("tip3_cube1", True)

            else:
                feedback = f"Ответ {num} неверный. ❌"
                answer_input.border_color = ft.colors.RED
        except ValueError:
            feedback = "Введите число! ⚠️"
            answer_input.border_color = ft.colors.ORANGE

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
        icon=ft.icons.KEYBOARD_RETURN,
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
                            ), ], spacing=10,
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


def show_tip3_cube2_details0_2(page, e):
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
                ft.Text(
                    "Площадь поверхности куба выражается через его ребро a формулой S = 6a², объем формулой V = a³. Поэтому a³ = 8 откуда a = 2; ",
                    size=18),
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


def show_tip3_cube2(page, e):
    details0.content = None
    page.update()

    global show_solution
    show_solution = False

    checkmark = ft.Icon(
        name=ft.icons.CHECK_CIRCLE_OUTLINE,
        color=ft.colors.GREEN if is_task_solved("tip3_cube2") else ft.colors.GREY,
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
        icon=ft.icons.MORE_VERT, style=ft.ButtonStyle(color="#4E426D"),
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
                answer_input.border_color = ft.colors.GREEN
                # Добавляем задачу в решенные
                add_solved_task("tip3_cube2")
                # Обновляем галочку
                update_checkmark("tip3_cube2", True)
            else:
                feedback = f"Ответ {num} неверный. ❌"
                answer_input.border_color = ft.colors.RED
        except ValueError:
            feedback = "Введите число! ⚠️"
            answer_input.border_color = ft.colors.ORANGE

        answer_input.hint_text = feedback
        answer_input.value = ""
        answer_input.width = max(180, len(feedback) * 9)
        page.update()

    answer_input.on_submit = check_answer

    enter_icon = ft.IconButton(
        icon=ft.icons.KEYBOARD_RETURN,
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


def show_tip3_pir1_details0_2(page, e):
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
                                ft.Container(width=30, height=1, bgcolor=ft.colors.BLACK),
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


def show_tip3_pir1(page, e):
    details0.content = None
    page.update()

    global show_solution
    show_solution = False

    checkmark = ft.Icon(
        name=ft.icons.CHECK_CIRCLE_OUTLINE,
        color=ft.colors.GREEN if is_task_solved("tip3_pir1") else ft.colors.GREY,
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
                answer_input.border_color = ft.colors.GREEN
                add_solved_task("tip3_pir1")
                update_checkmark("tip3_pir1", True)
            else:
                feedback = f"Ответ {num} неверный. ❌"
                answer_input.border_color = ft.colors.RED
        except ValueError:
            feedback = "Введите число! ⚠️"
            answer_input.border_color = ft.colors.ORANGE

        answer_input.hint_text = feedback
        answer_input.value = ""
        answer_input.width = max(
            180,
            len(feedback) * 9
        )

        page.update()

    answer_input.on_submit = check_answer

    enter_icon = ft.IconButton(
        icon=ft.icons.KEYBOARD_RETURN,
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


def show_tip3_pir2(page, e):
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


def show_tip3_par1_details0_2(page, e):
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


def show_tip3_par1(page, e):
    details0.content = None
    page.update()

    global show_solution
    show_solution = False

    def update_checkmark(task_id, is_solved=None):
        if is_solved is None:
            is_solved = is_task_solved(task_id)
        pass

    checkmark = ft.Icon(
        name=ft.icons.CHECK_CIRCLE_OUTLINE,
        color=ft.colors.GREEN if is_task_solved("tip3_par1") else ft.colors.GREY,
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
                answer_input.border_color = ft.colors.GREEN
                add_solved_task("tip3_par1")
                update_checkmark("tip3_par1", True)
            else:
                feedback = f"Ответ {num} неверный. ❌"
                answer_input.border_color = ft.colors.RED
        except ValueError:
            feedback = "Введите число! ⚠️"
            answer_input.border_color = ft.colors.ORANGE

        answer_input.hint_text = feedback
        answer_input.value = ""
        answer_input.width = max(180, len(feedback) * 9)
        page.update()

    answer_input.on_submit = check_answer

    enter_icon = ft.IconButton(
        icon=ft.icons.KEYBOARD_RETURN,
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


def show_tip3_par2_details0_2(page, e):
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


def show_tip3_par2(page, e):
    # https: // math - ege.sdamgia.ru / problem?id = 245361

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

        # Обновляем состояние элементов меню
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
        icon=ft.icons.MORE_VERT, style=ft.ButtonStyle(color="#4E426D"),
        tooltip="Выбор темы"
    )

    def update_checkmark(task_id, is_solved=None):
        if is_solved is None:
            is_solved = is_task_solved(task_id)
        pass

    checkmark = ft.Icon(
        name=ft.icons.CHECK_CIRCLE_OUTLINE,
        color=ft.colors.GREEN if is_task_solved("tip3_par2") else ft.colors.GREY,
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
            if num == 45:  # Правильный ответ 1 с учетом погрешности
                feedback = f"Молодец! Ответ {num} верный! 🎉"
                answer_input.border_color = ft.colors.GREEN
                # Добавляем задачу в решенные
                add_solved_task("tip3_par2")
                # Обновляем галочку
                update_checkmark("tip3_par2", True)
            else:
                feedback = f"Ответ {num} неверный. ❌"
                answer_input.border_color = ft.colors.RED
        except ValueError:
            feedback = "Введите число! ⚠️"
            answer_input.border_color = ft.colors.ORANGE

        answer_input.hint_text = feedback
        answer_input.value = ""
        answer_input.width = max(180, len(feedback) * 9)
        page.update()

    answer_input.on_submit = check_answer

    enter_icon = ft.IconButton(
        icon=ft.icons.KEYBOARD_RETURN,
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


def show_tip3_mngg1_details0_2(page, e):
    global show_solution
    responsive_row = details0.content
    first_column = None
    for control in responsive_row.controls:
        if isinstance(control, ft.Column) and control.col.get("md") == 7:
            first_column = control
            break

    if show_solution:
        # Если решение отображается, удаляем его
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


def show_tip3_mngg1(page, e):
    details0.content = None
    page.update()

    global show_solution
    show_solution = False

    def update_checkmark(task_id, is_solved=None):
        if is_solved is None:
            is_solved = is_task_solved(task_id)
        pass

    checkmark = ft.Icon(
        name=ft.icons.CHECK_CIRCLE_OUTLINE,
        color=ft.colors.GREEN if is_task_solved("tip3_mngg1") else ft.colors.GREY,
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
        icon=ft.icons.MORE_VERT, style=ft.ButtonStyle(color="#4E426D"),
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
                answer_input.border_color = ft.colors.GREEN
                add_solved_task("tip3_mngg1")
                update_checkmark("tip3_mngg1", True)
            else:
                feedback = f"Ответ {num} неверный. ❌"
                answer_input.border_color = ft.colors.RED
        except ValueError:
            feedback = "Введите число! ⚠️"
            answer_input.border_color = ft.colors.ORANGE

        answer_input.hint_text = feedback
        answer_input.value = ""
        answer_input.width = max(180, len(feedback) * 9)
        page.update()

    answer_input.on_submit = check_answer

    enter_icon = ft.IconButton(
        icon=ft.icons.KEYBOARD_RETURN,
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


def show_tip3_mngg2(page, e):
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


def show_tip3_vprizm1_details0_2(page, e):
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
                                ft.Container(width=50, height=1, bgcolor=ft.colors.BLACK),
                                ft.Text("  2 ", size=18),
                            ],
                            spacing=0,
                        ),
                        ft.Text("× a² = ", size=18),
                        ft.Column(
                            controls=[
                                ft.Text(" 3√3 ", size=18),
                                ft.Container(width=50, height=1, bgcolor=ft.colors.BLACK),
                                ft.Text("  2 ", size=18),
                            ],
                            spacing=0,
                        ),
                        ft.Text("× 1² = ", size=18),
                        ft.Column(
                            controls=[
                                ft.Text(" 3√3 ", size=18),
                                ft.Container(width=50, height=1, bgcolor=ft.colors.BLACK),
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
                                ft.Container(width=50, height=1, bgcolor=ft.colors.BLACK),
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


def show_tip3_vprizm1(page, e):
    details0.content = None
    page.update()

    global show_solution
    show_solution = False

    def update_checkmark(task_id, is_solved=None):
        if is_solved is None:
            is_solved = is_task_solved(task_id)
        pass

    checkmark = ft.Icon(
        name=ft.icons.CHECK_CIRCLE_OUTLINE,
        color=ft.colors.GREEN if is_task_solved("tip3_vprizm1") else ft.colors.GREY,
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
                answer_input.border_color = ft.colors.GREEN
                add_solved_task("tip3_vprizm1")
                update_checkmark("tip3_vprizm1", True)
            else:
                feedback = f"Ответ {num} неверный. ❌"
                answer_input.border_color = ft.colors.RED
        except ValueError:
            feedback = "Введите число! ⚠️"
            answer_input.border_color = ft.colors.ORANGE

        answer_input.hint_text = feedback
        answer_input.value = ""
        answer_input.width = max(180, len(feedback) * 9)
        page.update()

    answer_input.on_submit = check_answer

    enter_icon = ft.IconButton(
        icon=ft.icons.KEYBOARD_RETURN,
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


def show_tip3_vprizm2(page, e):
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


def show_tip3_sprizm1_details0_2(page, e):
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


def show_tip3_sprizm1(page, e):
    details0.content = None
    page.update()

    global show_solution
    show_solution = False

    def update_checkmark(task_id, is_solved=None):
        if is_solved is None:
            is_solved = is_task_solved(task_id)
        pass

    checkmark = ft.Icon(
        name=ft.icons.CHECK_CIRCLE_OUTLINE,
        color=ft.colors.GREEN if is_task_solved("tip3_sprizm1") else ft.colors.GREY,
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
                answer_input.border_color = ft.colors.GREEN
                add_solved_task("tip3_sprizm1")
                update_checkmark("tip3_sprizm1", True)
            else:
                feedback = f"Ответ {num} неверный. ❌"
                answer_input.border_color = ft.colors.RED
        except ValueError:
            feedback = "Введите число! ⚠️"
            answer_input.border_color = ft.colors.ORANGE

        answer_input.hint_text = feedback
        answer_input.value = ""
        answer_input.width = max(180, len(feedback) * 9)
        page.update()

    answer_input.on_submit = check_answer

    enter_icon = ft.IconButton(
        icon=ft.icons.KEYBOARD_RETURN,
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


def show_tip3_sprizm2(page, e):
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


def show_tip3_cyli(page, e):
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


def show_tip3_sphere(page, e):
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


