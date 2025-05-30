import flet
import flet as ft


def axy_task(details0, page, details1, start_pygame_with_axy1, start_pygame_with_axy2, start_pygame_with_axy3, e):
    details0.content = None
    page.update()
    global show_solution
    show_solution = False

    # Функции проверки ответов для существующих задач
    def check_answer(e):
        user_answer = answer_input.value.strip().lower()
        if user_answer in ["да", "да."]:
            answer_input.border_color = ft.Colors.GREEN
            answer_input.hint_text = " Ответ верный! 🎉"
        else:
            answer_input.border_color = ft.Colors.RED
            answer_input.hint_text = f"Ответ '{user_answer}' неверный. ❌"
        answer_input.value = ""
        page.update()

    def check_answer2(e):
        user_answer = answer_input2.value.strip().lower()
        if user_answer in ["нет", "нет."]:
            answer_input2.border_color = ft.Colors.GREEN
            answer_input2.hint_text = " Ответ верный! 🎉"
        else:
            answer_input2.border_color = ft.Colors.RED
            answer_input2.hint_text = f"Ответ '{user_answer}' неверный. ❌"
        answer_input2.value = ""
        page.update()

    def check_answer3(e):
        user_answer = answer_input3.value.strip().lower()
        if user_answer in ["нет", "нет."]:
            answer_input3.border_color = ft.Colors.GREEN
            answer_input3.hint_text = " Ответ верный! 🎉"
        else:
            answer_input3.border_color = ft.Colors.RED
            answer_input3.hint_text = f"Ответ '{user_answer}' неверный. ❌"
        answer_input3.value = ""
        page.update()

    # Элементы интерфейса для существующих задач
    answer_input = ft.TextField(
        hint_text="Введите ответ",
        width=180,
        border_color="#4E426D",
        cursor_color="#4E426D",
        text_size=14,
        border_radius=20,
        content_padding=10,
        expand=True,
        on_submit=check_answer
    )

    answer_input2 = ft.TextField(
        hint_text="Введите ответ",
        width=180,
        border_color="#4E426D",
        cursor_color="#4E426D",
        text_size=14,
        border_radius=20,
        content_padding=10,
        expand=True,
        on_submit=check_answer2
    )

    answer_input3 = ft.TextField(
        hint_text="Введите ответ",
        width=180,
        border_color="#4E426D",
        cursor_color="#4E426D",
        text_size=14,
        border_radius=20,
        content_padding=10,
        expand=True,
        on_submit=check_answer3
    )

    check_button = ft.IconButton(
        icon=ft.Icons.KEYBOARD_RETURN,
        icon_color="#4E426D",
        on_click=check_answer,
        tooltip="Проверить ответ",
    )

    check_button2 = ft.IconButton(
        icon=ft.Icons.KEYBOARD_RETURN,
        icon_color="#4E426D",
        on_click=check_answer2,
        tooltip="Проверить ответ",
    )

    check_button3 = ft.IconButton(
        icon=ft.Icons.KEYBOARD_RETURN,
        icon_color="#4E426D",
        on_click=check_answer3,
        tooltip="Проверить ответ",
    )

    # Контейнеры с решениями для существующих задач
    task1_ansv = ft.Container(
        content=ft.Column([
            ft.Text(
                "Через 3 точки, если они не лежат на одной прямой, можно провести плоскость, и притом только одну, в силу аксиомы А1.",
                size=18,
                weight=ft.FontWeight.W_400
            ),
            ft.Column(
                controls=[
                    ft.ElevatedButton(
                        "Открыть 3D модель",
                        on_click=lambda e: start_pygame_with_axy1(e),
                        style=ft.ButtonStyle(color="#4E426D"),
                        width=180,
                        visible=False
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            )
        ]),
        visible=False
    )

    task2_ansv = ft.Container(
        content=ft.Column([
            ft.Text(
                "Через 3 точки можно провести плоскость, а 4 точку можно взять и в этой плоскости, и вне нее. Значит, ответ отрицательный.",
                size=18,
                weight=ft.FontWeight.W_400
            ),
            ft.Column(
                controls=[
                    ft.ElevatedButton(
                        "Открыть 3D модель",
                        on_click=lambda e: start_pygame_with_axy2(e),
                        style=ft.ButtonStyle(color="#4E426D"),
                        width=180,
                        visible=False
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            )
        ]),
        visible=False
    )

    task3_ansv = ft.Container(
        content=ft.Column([
            ft.Text(
                "Приведем конкретный пример. Рассмотрим плоский четырехугольник, в плоскости этого четырехугольника лежат 4 точки. Итак, ответ на этот вопрос отрицательный, нет.",
                size=18,
                weight=ft.FontWeight.W_400
            ),
            ft.Column(
                controls=[
                    ft.ElevatedButton(
                        "Открыть 3D модель",
                        on_click=lambda e: start_pygame_with_axy2(e),
                        style=ft.ButtonStyle(color="#4E426D"),
                        width=180,
                        visible=False
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            )
        ]),
        visible=False
    )

    #задача №2 с доказательством
    task4_ansv = ft.Container(
        content=ft.Column([
            ft.Text(
                "Пусть нам даны три точки: А, В, и С. Нужно доказать, что отрезки АВ, ВС, СА лежат в одной плоскости\n"
                "Если точка С лежит на прямой АВ, то ответ очевиден. Предположим, что точка С не принадлежит прямой АВ. "
                "Тогда через три точки A, B, C, не лежащие на одной прямой, проходит плоскость, и притом только одна, "
                "в силу аксиомы 1. Обозначим эту плоскость α.\n"
                "Прямая АВ целиком лежит в плоскости α, потому что две ее точки лежат в этой плоскости. "
                "Но, значит, и отрезок АВ лежит в плоскости α.\n"
                "Аналогично и с другими отрезками. Прямая ВС лежит в плоскости α, потому что две ее точки В и С "
                "лежат в плоскости, значит, и отрезок ВС лежит в плоскости α.\n"
                "И аналогично, отрезок АС лежит в плоскости α. Что и требовалось доказать.",
                size=18,
                weight=ft.FontWeight.W_400
            ),
            ft.Column(
                controls=[
                    ft.ElevatedButton(
                        "Открыть 3D модель",
                        on_click=lambda e: start_pygame_with_axy3(e),
                        style=ft.ButtonStyle(color="#4E426D"),
                        width=180,
                        visible=False
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            )
        ]),
        visible=False
    )

    # Кнопки для показа решений
    solution_button1 = ft.TextButton(
        "Показать решение",
        style=ft.ButtonStyle(color="#4E426D"),
    )

    solution_button2 = ft.TextButton(
        "Показать решение",
        style=ft.ButtonStyle(color="#4E426D"),
    )

    solution_button3 = ft.TextButton(
        "Показать решение",
        style=ft.ButtonStyle(color="#4E426D"),
    )

    solution_button4 = ft.TextButton(
        "Показать решение",
        style=ft.ButtonStyle(color="#4E426D"),
    )

    # Функции для показа/скрытия решений
    def show_solution(e):
        task1_ansv.visible = not task1_ansv.visible
        for control in task1_ansv.content.controls[1].controls:
            control.visible = task1_ansv.visible
        solution_button1.text = "Спрятать решение" if task1_ansv.visible else "Показать решение"
        page.update()

    def show_solution2(e):
        task2_ansv.visible = not task2_ansv.visible
        for control in task2_ansv.content.controls[1].controls:
            control.visible = task2_ansv.visible
        solution_button2.text = "Спрятать решение" if task2_ansv.visible else "Показать решение"
        page.update()

    def show_solution3(e):
        task3_ansv.visible = not task3_ansv.visible
        for control in task3_ansv.content.controls[1].controls:
            control.visible = task3_ansv.visible
        solution_button3.text = "Спрятать решение" if task3_ansv.visible else "Показать решение"
        page.update()

    def show_solution4(e):
        task4_ansv.visible = not task4_ansv.visible
        for control in task4_ansv.content.controls[1].controls:
            control.visible = task4_ansv.visible
        solution_button4.text = "Спрятать решение" if task4_ansv.visible else "Показать решение"
        page.update()

    solution_button1.on_click = show_solution
    solution_button2.on_click = show_solution2
    solution_button3.on_click = show_solution3
    solution_button4.on_click = show_solution4

    # Основной контейнер с задачами
    details1.content = ft.Container(
        content=ft.Column(
            [
                ft.Column([
                    ft.Text("Теория стереометрии. Аксиомы стереометрии: Задачи",
                            size=12, weight=ft.FontWeight.BOLD),
                    ft.Text("Аксиомы стереометрии", size=28, weight=ft.FontWeight.BOLD)
                ], spacing=5),

                ft.ResponsiveRow(
                    controls=[
                        ft.Column(
                            col={"sm": 12, "md": 12},
                            controls=[
                                ft.Text("Задача №1", size=24, weight=ft.FontWeight.BOLD),
                                ft.Text(
                                    "а) Верно ли, что любые 3 точки лежат в одной плоскости?",
                                    size=20, weight=ft.FontWeight.W_500
                                ),
                                task1_ansv,
                                ft.Row(
                                    controls=[
                                        ft.Row(
                                            controls=[answer_input, check_button],
                                            spacing=10,
                                            alignment=ft.MainAxisAlignment.START,
                                        ),
                                        solution_button1,
                                    ],
                                ),

                                ft.Text(
                                    "б) Верно ли, что любые 4 точки лежат в одной плоскости?",
                                    size=20, weight=ft.FontWeight.W_500
                                ),
                                task2_ansv,
                                ft.Row(
                                    controls=[
                                        ft.Row(
                                            controls=[answer_input2, check_button2],
                                            spacing=10,
                                            alignment=ft.MainAxisAlignment.START,
                                        ),
                                        solution_button2,
                                    ],
                                ),

                                ft.Text(
                                    "в) Верно ли, что любые 4 точки не лежат в одной плоскости?",
                                    size=20, weight=ft.FontWeight.W_500
                                ),
                                task3_ansv,
                                ft.Row(
                                    controls=[
                                        ft.Row(
                                            controls=[answer_input3, check_button3],
                                            spacing=10,
                                            alignment=ft.MainAxisAlignment.START,
                                        ),
                                        solution_button3,
                                    ],
                                ),

                                # задача №2
                                ft.Text("Задача №2", size=24, weight=ft.FontWeight.BOLD),
                                ft.Text(
                                    "Три данные точки соединены попарно отрезками. Докажите, что все отрезки лежат в одной плоскости.",
                                    size=20, weight=ft.FontWeight.W_500
                                ),
                                task4_ansv,
                                ft.Row(
                                    controls=[solution_button4],
                                    alignment=ft.MainAxisAlignment.START,
                                ),
                            ],
                            spacing=5,
                        ),
                    ],
                    spacing=20,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),
            ],
            spacing=15,
            scroll=ft.ScrollMode.AUTO
        ),
        expand=True
    )
    page.update()


def sled_axy(sled_a1, sled_a2, details1, page, start_pygame_with_sled1, start_pygame_with_axy2, e):
    # Создаем контейнеры для пруфоф, которые будут скрыты/показаны
    proof_container1 = ft.Column([], spacing=5)
    proof_container2 = ft.Column([], spacing=5)

    # Доказательства
    doc_1 = ft.Column(
            controls=[
                ft.Text("Дано: Прямая a, M ∉ a.", size=18, weight=ft.FontWeight.BOLD),
                ft.Text("Доказать:", size=18, weight=ft.FontWeight.BOLD),
                ft.Text("1) Cуществует плоскость α, a ∈ α, M ∈ α.", size=18),

                ft.Text("2) Плоскость α единственна.", size=18),

                ft.Text("Доказательство 1:", size=18, weight=ft.FontWeight.BOLD),
                ft.Text("Докажем, что существует плоскость α, a ∈ α, M ∈ α. На прямой а выберем любые две точки Р и Q: P,Q ∈ α. Тогда имеем 3 точки – Р, Q, M, которые не лежат на одной прямой."

"По аксиоме А1, через три точки, не лежащие на одной прямой, проходит плоскость, и притом только одна, т.е. плоскость α, которая содержит и прямую a, и точку М, существует.", size=18),
                ft.Text("Доказательство 2:", size=18, weight=ft.FontWeight.BOLD),
                ft.Text(
                    "Следует доказать единственность такой плоскости."

"Предположим, что существует иная плоскость α¹, которая проходит и через точку М, и через прямую a. Например, это будет плоскость, проходящая через точки Q¹ P¹,  прямой a, и точку M. Но тогда эта плоскость α¹ проходит и через прямую a, и через точку М, а значит, и через точки Р, Q. А через три точки Р, Q, M, не лежащие на одной прямой, в силу 1 аксиомы, проходит только одна плоскость. Значит, эта плоскость α¹ совпадает с плоскостью α. Значит, единственность доказана. Вся теорема доказана.",
                    size=18),
            ],
            spacing=5,
            tight=True,
        )

    doc_2 = ft.Column(
            controls=[
                ft.Text("Дано: a ∩ b = M", size=18, weight=ft.FontWeight.BOLD),
                ft.Text("Доказать:", size=18, weight=ft.FontWeight.BOLD),
                ft.Text("1) Cуществует плоскость α, a ∈ α, b ∈ α.", size=18),

                ft.Text("2) Плоскость α единственна.", size=18),

                ft.Text("Доказательство 1:", size=18, weight=ft.FontWeight.BOLD),
                ft.Text("На прямой b возьмем точку N, которая не совпадает с точкой М, то есть N ∈ b, N  НЕ РАВНО  M"

"Тогда имеем точку N, которая не принадлежит прямой a. По предыдущей теореме, через прямую и не лежащую на ней точку проходит плоскость. Назовем ее плоскостью α. Значит, такая плоскость, которая проходит через прямую a и точку N, существует. Но эта плоскость также проходит и через всю прямую b, так как две точки М и N прямой b лежат в этой плоскости. То есть и прямая a и прямая b принадлежат плоскости α. Значит, существует такая плоскость, которая проходит через две пересекающиеся прямые, что и требовалось доказать в первом пункте.", size=18),
                ft.Text("Доказательство 2:", size=18, weight=ft.FontWeight.BOLD),
                ft.Text(
                    "Следует доказать единственность такой плоскости."

"Предположим противное. Пусть существует иная плоскость α¹, такая, которая проходит и через прямую a, и через прямую b. Но тогда она также проходит и через прямую a, и точку N. Но по предыдущей теореме эта плоскость единственна, т.е. плоскость α¹ совпадает с плоскостью α. "

"Значит, мы доказали существование единственной плоскости, проходящей через две пересекающиеся прямые.",
                    size=18),
            ],
            spacing=5,
            tight=True,
        )

    # Функции для показа/скрытия пруфоф
    def toggle_proof1(e):
        if proof_container1.controls:
            proof_container1.controls.clear()
            e.control.text = "Показать доказательство"
        else:
            proof_container1.controls.append(doc_1)
            e.control.text = "Скрыть доказательство"
        page.update()

    def toggle_proof2(e):
        if proof_container2.controls:
            proof_container2.controls.clear()
            e.control.text = "Показать доказательство"
        else:
            proof_container2.controls.append(doc_2)
            e.control.text = "Скрыть доказательство"
        page.update()

    # показ пруфоф
    proof_button1 = ft.TextButton(
        "Показать доказательство",
        on_click=toggle_proof1,
        style=ft.ButtonStyle(color="#4E426D")
    )

    proof_button2 = ft.TextButton(
        "Показать доказательство",
        on_click=toggle_proof2,
        style=ft.ButtonStyle(color="#4E426D")
    )

    details1.content = ft.Container(
        content=ft.Column(
            [
                ft.Column([ft.Text("Теория стереометрии. Аксиомы стереометрии: Некоторые следствия из аксиом",
                                   size=12, weight=ft.FontWeight.BOLD),
                           ft.Text("Некоторые следствия из аксиом", size=28, weight=ft.FontWeight.BOLD)], spacing=5),

                ft.ResponsiveRow(
                    controls=[
                        ft.Column(
                            col={"sm": 12, "md": 7},
                            controls=[
                                ft.Text("Теорема 1", size=24, weight=ft.FontWeight.BOLD),
                                ft.Text(
                                    "Через прямую и не лежащую на ней точку проходит плоскость, и притом только одна.",
                                    size=20, weight=ft.FontWeight.W_500
                                ),
                                proof_button1,
                                proof_container1,
                            ],
                            spacing=5,
                        ),
                        ft.Column(
                            col={"sm": 9, "md": 5},
                            controls=[
                                ft.Container(width=10, height=10),
                                ft.Image(sled_a1, width=30, height=90, fit=ft.ImageFit.CONTAIN),
                                ft.ElevatedButton(
                                    "Открыть 3D модель",
                                    on_click=lambda e: start_pygame_with_sled1(e),
                                    style=ft.ButtonStyle(color="#4E426D"),
                                    width=180
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,
                        ),
                    ],
                    spacing=20,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),

                ft.ResponsiveRow(
                    controls=[
                        ft.Column(
                            col={"sm": 12, "md": 7},
                            controls=[
                                ft.Text("Теорема 2", size=24, weight=ft.FontWeight.BOLD),
                                ft.Text(
                                    "Через две пересекающиеся прямые проходит плоскость, и притом только одна",
                                    size=20, weight=ft.FontWeight.W_500
                                ),
                                proof_button2,
                                proof_container2,
                            ],
                            spacing=5,
                        ),
                        ft.Column(
                            col={"sm": 9, "md": 5},
                            controls=[
                                ft.Container(width=10, height=10),
                                ft.Image(sled_a2, width=30, height=90, fit=ft.ImageFit.CONTAIN),
                                ft.ElevatedButton(
                                    "Открыть 3D модель",
                                    on_click=lambda e: start_pygame_with_axy2(e),
                                    style=ft.ButtonStyle(color="#4E426D"),
                                    width=180
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,
                        ),
                    ],
                    spacing=20,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),


            ],
            spacing=15,
            scroll=ft.ScrollMode.AUTO
        ),
        expand=True
    )
    page.update()


def axy(a1, a2, a3, details1, page, start_pygame_with_axy1, start_pygame_with_axy2, start_pygame_with_axy3, e):
    details1.content = ft.Container(
        content=ft.Column(
            [
                ft.Column([ft.Text("Теория стереометрии. Аксиомы стереометрии: Аксиомы",
                            size=12, weight=ft.FontWeight.BOLD),

                ft.Text("Аксиомы стереометрии", size=28, weight=ft.FontWeight.BOLD)], spacing=5),


                ft.ResponsiveRow(
                    controls=[
                        ft.Column(
                            col={"sm": 12, "md": 7},
                            controls=[
                                ft.Text("Аксиома 1", size=24, weight=ft.FontWeight.BOLD),
                                ft.Text(
                                    "Через любые три точки, не лежащие на одной прямой, можно "
                                    "провести плоскость и при том только одну.",
                                    size=20, weight=ft.FontWeight.W_500
                                ),
                                ft.Text(
                                    "Эта аксиома однозначно определяет (задаёт) плоскость с помощью "
                                    "любых трёх её точек, не лежащих на одной прямой. Поэтому плоскость "
                                    "можно обозначать и не лежащими на одной прямой тремя точками. На "
                                    "приведённом рисунке плоскость можно записать как плоскость (ABC).",
                                    size=18, weight=ft.FontWeight.W_400
                                )
                            ],
                            spacing=5,
                        ),
                        ft.Column(
                            col={"sm": 9, "md": 5},
                            controls=[
                                ft.Container(width=40, height=40),
                                ft.Image(a1, width=30, height=90, fit=ft.ImageFit.CONTAIN),
                                ft.ElevatedButton(
                                    "Открыть 3D модель",
                                    on_click=lambda e: start_pygame_with_axy1(e),
                                    style=ft.ButtonStyle(color="#4E426D"),
                                    width=180
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,
                        ),
                    ],
                    spacing=20,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),

                ft.ResponsiveRow(
                    controls=[
                        ft.Column(
                            col={"sm": 12, "md": 7},
                            controls=[
                                ft.Text("Аксиома 2", size=24, weight=ft.FontWeight.BOLD),
                                ft.Text(
                                    "Если две точки прямой лежат в плоскости, то все точки прямой "
                                    "лежат в этой плоскости.",
                                    size=20, weight=ft.FontWeight.W_500
                                ),
                                ft.Text(
                                    "Из аксиомы 2 следует, что прямая, не лежащая в плоскости, не может "
                                    "иметь с плоскостью более одной общей точки. Если прямая и плоскость "
                                    "имеют только одну общую точку, то говорят, что прямая пересекает "
                                    "плоскость.",
                                    size=18, weight=ft.FontWeight.W_400
                                )
                            ],
                            spacing=5,
                        ),
                        ft.Column(
                            col={"sm": 9, "md": 5},
                            controls=[
                                ft.Container(width=40, height=40),
                                ft.Image(a2, width=30, height=90, fit=ft.ImageFit.CONTAIN),
                                ft.ElevatedButton(
                                    "Открыть 3D модель",
                                    on_click=lambda e: start_pygame_with_axy2(e),
                                    style=ft.ButtonStyle(color="#4E426D"),
                                    width=180
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,
                        ),
                    ],
                    spacing=20,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),

                ft.ResponsiveRow(
                    controls=[
                        ft.Column(
                            col={"sm": 12, "md": 7},
                            controls=[
                                ft.Text("Аксиома 3", size=24, weight=ft.FontWeight.BOLD),
                                ft.Text(
                                    "Если две плоскости имеют общую точку, то они имеют общую "
                                    "прямую, на которой лежат все общие точки этих плоскостей.",
                                    size=20, weight=ft.FontWeight.W_500
                                ),
                                ft.Text(
                                    "Можно представить эту аксиому как пересечение двух листков "
                                    "бумаги. Мы никогда не сможем пересечь их так, чтобы они пересекались "
                                    "только в одной точке, т.к. любая плоскость бесконечно продолжается "
                                    "во все стороны. Таким образом, плоскости пересекаются по прямой a.",
                                    size=18, weight=ft.FontWeight.W_400
                                )
                            ],
                            spacing=5,
                        ),
                        ft.Column(
                            col={"sm": 9, "md": 5},
                            controls=[
                                ft.Container(width=40, height=40),
                                ft.Image(a3, width=70, height=140, fit=ft.ImageFit.CONTAIN),
                                ft.ElevatedButton(
                                    "Открыть 3D модель",
                                    on_click=lambda e: start_pygame_with_axy3(e),
                                    style=ft.ButtonStyle(color="#4E426D"),
                                    width=180
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,
                        ),
                    ],
                    spacing=20,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                )
            ],
            spacing=15,
            scroll=ft.ScrollMode.AUTO
        ),
        expand=True
    )
    page.update()