import threading
import random
import json
from pathlib import Path
import flet as ft
import pyperclip
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

# Модели для задач типа 14
from models3d.tip14_rast import run_pygame_tip14_rast1
from models3d.tip14_rast2 import run_pygame_tip14_rast2
from models3d.ygol2 import run_pygame_tip14_ygol1
from models3d.ygol_sv import run_pygame_tip14_ygol1_sv
from models3d.tip14_sech1 import run_pygame_tip14_sech1
from models3d.tip14_V1 import run_pygame_tip14_V1

# Сохранение решённых задач
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

# Функции для задач типа 3
def show_tip3_cube1_details0_2(e):
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

    checkmark = ft.Icon(
        name=ft.Icons.CHECK_CIRCLE_OUTLINE,
        color=ft.Colors.GREEN if is_task_solved("tip3_cube1") else ft.Colors.GREY,
        size=24
    )

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

    def handle_open_model(e):
        if light_theme_checked:
            start_pygame_with_cube1_sv(e)
        elif dark_theme_checked:
            start_pygame_with_cube1(e)
        else:
            start_pygame_with_cube1_sv(e)

    theme_menu = ft.PopupMenuButton(
        items=[
            ft.PopupMenuItem(text="Светлая тема", checked=False, on_click=lambda e: check_item_clicked(e, "light")),
            ft.PopupMenuItem(text="Темная тема", checked=False, on_click=lambda e: check_item_clicked(e, "dark")),
            ft.PopupMenuItem(text="Редактировать", checked=False, on_click=lambda e: check_item_clicked(e, "red")),
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
            if num == 3:
                feedback = f"Молодец! Ответ {num} верный! 🎉"
                answer_input.border_color = ft.Colors.GREEN
                add_solved_task("tip3_cube1")
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

    details0.content = ft.ResponsiveRow(
        controls=[
            ft.Column(
                col={"sm": 12, "md": 7},
                controls=[
                    ft.Text("Профильная математика. Тип 3. Стереометрия: Куб",
                            size=12, weight=ft.FontWeight.BOLD),
                    ft.Row(
                        controls=[
                            ft.OutlinedButton("Задача 1", on_click=show_tip3_cube1, style=ft.ButtonStyle(color="black"), width=100),
                            ft.OutlinedButton("Задача 2", on_click=show_tip3_cube2, style=ft.ButtonStyle(color="black"), width=100),
                        ],
                        spacing=10
                    ),
                    ft.Row([
                        ft.Text("Задача №1", size=24, weight=ft.FontWeight.BOLD),
                        checkmark
                    ], spacing=10),
                    ft.Text("Площадь поверхности куба равна 18. Найдите его диагональ.", size=21),
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
                            ft.Row([
                                ft.TextButton(
                                    "Показать решение",
                                    on_click=show_tip3_cube1_details0_2,
                                    style=ft.ButtonStyle(color="#4E426D"),
                                ),
                            ], spacing=10),
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
                    ft.Image(src="assets/cube0.jpg", width=190, height=190, fit=ft.ImageFit.SCALE_DOWN),
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

# Остальные функции задач (show_tip3_cube2, show_tip3_pir1 и т.д.) должны быть перенесены аналогично

# Функции для запуска 3D моделей
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

# Функция для создания выпадающих списков задач ЕГЭ
def create_ege_dropdown(button_text, options, button_color=ft.Colors.BLACK):
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

    dropdown.controls = [
        ft.TextButton(
            option,
            on_click=show_tip3_cube1 if option == "Куб"
            else show_tip3_pir1 if option == "Пирамида"
            else show_tip3_par2 if option == "Параллелепипед"
            else show_tip3_mngg1 if option == "Объём прямоугольных многогранников"
            else show_tip3_vprizm1 if option == "Призма (объём)"
            else show_tip3_sprizm1 if option == "Призма (площадь)"
            else show_tip3_cyli if option == "Цилиндр (площадь)"
            else show_tip3_sphere if option == "Сфера и шар"
            else show_random_task if option == "Случайная задача"
            else show_tip14_rast if option == "Расстояния"
            else show_tip14_ygol1 if option == "Углы"
            else show_tip14_V1 if option == "Объём"
            else show_tip14_sech1 if option == "Площадь сечения"
            else None,
        ) for option in options
    ]

    container = ft.Container(
        content=ft.Column([
            button,
            ft.Container(content=dropdown, margin=ft.margin.only(left=20))
        ]),
        on_hover=on_dropdown_hover,
        bgcolor=ft.Colors.TRANSPARENT,
    )

    return container, hide_dropdown

# Функция для случайных задач
def get_random_unsolved_task():
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

    unsolved_tasks = [task for task in all_tasks if not is_task_solved(task[0])]

    if not unsolved_tasks:
        return None

    return random.choice(unsolved_tasks)

def show_random_task(e):
    task = get_random_unsolved_task()
    if task:
        task_id, task_name, task_func = task
        task_func(e)
    else:
        details0.content = ft.Column(
            controls=[
                ft.Text("Поздравляем!", size=24, weight=ft.FontWeight.BOLD),
                ft.Text("Вы решили все доступные задачи типа 3!", size=18),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        page.update()

# Инициализация глобальных переменных
page = None
details0 = None
details0_2 = None
show_solution = False
light_theme_checked = False
dark_theme_checked = False
red_theme_checked = False

def init_ege_tasks(pg, dt0, dt0_2):
    global page, details0, details0_2
    page = pg
    details0 = dt0
    details0_2 = dt0_2