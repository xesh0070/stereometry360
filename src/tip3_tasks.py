import flet as ft
import random
from models3d.tip3_cube2 import run_pygame1
from models3d.tip3_cube1 import run_pygame1_1
from models3d.tip3_cube1_svetl import run_pygame1_1_svetl
from models3d.tip3_par2_sv import run_pygame_tip3_par2_sv
from models3d.tip3_par2_dark import run_pygame_par2_dark
from models3d.tip3_pir import run_pygame_tip3_pir1
from models3d.tip3_mngg import run_pygame_tip3_mngg
from models3d.tip3_mngg_dark import run_pygame_tip3_mngg_dark
from pygame_manager import run_with_check


def get_tip3_tasks(solved_tasks, is_task_solved, add_solved_task, page, details0, details0_2, show_solution):
    def show_tip3_cube1_details0_2(e):
        details0_2.content = None
        nonlocal show_solution
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
                    ft.Text(
                        "Пусть ребро куба равно a, тогда площадь поверхности куба S = 6a², а диагональ куба d = a√3",
                        size=18),
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
        nonlocal show_solution
        show_solution = False
        checkmark = ft.Icon(
            name=ft.Icons.CHECK_CIRCLE_OUTLINE,
            color=ft.Colors.GREEN if is_task_solved("tip3_cube1") else ft.Colors.GREY,
            size=24
        )

        light_theme_checked = False
        dark_theme_checked = False
        red_theme_checked = False

        def check_item_clicked(e, theme_type):
            nonlocal light_theme_checked, dark_theme_checked, red_theme_checked
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
                run_with_check(run_pygame1_1_svetl, e)
            elif dark_theme_checked:
                run_with_check(run_pygame1_1, e)
            else:
                run_with_check(run_pygame1_1_svetl, e)

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
                                ft.OutlinedButton("Задача 1", on_click=show_tip3_cube1,
                                                  style=ft.ButtonStyle(color="black"), width=100),

                            ],
                            spacing=10
                        ),
                        ft.Row([ft.Text("Задача №1", size=24, weight=ft.FontWeight.BOLD), checkmark], spacing=10),
                        ft.Text("Площадь поверхности куба равна 18. Найдите его диагональ.", size=21),
                        ft.Row(
                            controls=[
                                ft.Row(controls=[answer_input, enter_icon], spacing=10,
                                       alignment=ft.MainAxisAlignment.START),
                                ft.Row([ft.TextButton("Показать решение", on_click=show_tip3_cube1_details0_2,
                                                      style=ft.ButtonStyle(color="#4E426D"))], spacing=10),
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
                                ft.ElevatedButton("Открыть 3d модель", on_click=handle_open_model,
                                                  style=ft.ButtonStyle(color="#4E426D"), width=180),
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

    # Аналогично реализовать другие функции задач типа 3 (show_tip3_cube2, show_tip3_pir1 и т.д.)

    return {
        "show_tip3_cube1": show_tip3_cube1,
        # "show_tip3_cube2": show_tip3_cube2,
        # "show_tip3_pir1": show_tip3_pir1,
        # "show_tip3_par1": show_tip3_par1,
        # "show_tip3_par2": show_tip3_par2,
        # "show_tip3_mngg1": show_tip3_mngg1,
        # "show_tip3_vprizm1": show_tip3_vprizm1,
        # "show_tip3_sprizm1": show_tip3_sprizm1
    }