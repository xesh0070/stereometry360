import flet as ft

cube2_2 = "assets/cube0_2.jpg"
prism_3 = "assets/3prism.jpg"
prism_4 = "assets/4_prism.jpg"
piramid_40 = "assets/4piramid.jpg"

def volumes(e, page, details1):
    # Создаем контейнеры для доказательств
    proof_container1 = ft.Column([], spacing=5)
    proof_container2 = ft.Column([], spacing=5)
    proof_container3 = ft.Column([], spacing=5)

    # Доказательства и формулы
    doc_1 = ft.Column(
        controls=[
            ft.Text("Формула объема прямоугольного параллелепипеда:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text("V = a * b * c", size=18),
            ft.Text("где a, b, c - длины ребер, выходящих из одной вершины", size=16),

            ft.Text("Доказательство:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text(
                "Прямоугольный параллелепипед можно разбить на abc единичных кубов. "
                "Каждый единичный куб имеет объем 1, поэтому общий объем равен произведению длин ребер.",
                size=18),
        ],
        spacing=5,
        tight=True,
    )

    doc_2 = ft.Column(
        controls=[
            ft.Text("Формула объема призмы:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text("V = S_осн * h", size=18),
            ft.Text("где S_осн - площадь основания, h - высота призмы", size=16),

            ft.Text("Доказательство:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text(
                "1) Для треугольной призмы: можно достроить до параллелепипеда, объем которого равен S_осн * h, "
                "а исходная призма будет составлять его половину.\n"
                "2) Для n-угольной призмы: можно разбить на (n-2) треугольных призм, объем каждой из которых равен "
                "S_треуг * h, а сумма площадей треугольников равна площади основания.",
                size=18),
        ],
        spacing=5,
        tight=True,
    )

    doc_3 = ft.Column(
        controls=[
            ft.Text("Формула объема пирамиды:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text("V = (1/3) * S_осн * h", size=18),
            ft.Text("где S_осн - площадь основания, h - высота пирамиды", size=16),

            ft.Text("Доказательство:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text(
                "1) Для треугольной пирамиды: можно разбить на три пирамиды с равными объемами, "
                "каждая из которых имеет общее основание с исходной пирамидой и высоту h.\n"
                "2) Для n-угольной пирамиды: можно разбить на (n-2) треугольных пирамид, "
                "объем каждой равен (1/3)*S_треуг*h, а сумма площадей треугольников равна площади основания.",
                size=18),
        ],
        spacing=5,
        tight=True,
    )

    # Функции для показа/скрытия доказательств
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

    def toggle_proof3(e):
        if proof_container3.controls:
            proof_container3.controls.clear()
            e.control.text = "Показать доказательство"
        else:
            proof_container3.controls.append(doc_3)
            e.control.text = "Скрыть доказательство"
        page.update()

    # Кнопки для показа доказательств
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

    proof_button3 = ft.TextButton(
        "Показать доказательство",
        on_click=toggle_proof3,
        style=ft.ButtonStyle(color="#4E426D")
    )

    details1.content = ft.Container(
        content=ft.Column(
            [
                ft.Column([
                    ft.Text("Теория стереометрии. Объемы геометрических тел",
                            size=12, weight=ft.FontWeight.BOLD),
                    ft.Text("Объемы геометрических фигур",
                            size=28, weight=ft.FontWeight.BOLD)
                ], spacing=5),

                ft.ResponsiveRow(
                    controls=[
                        ft.Column(
                            col={"sm": 12, "md": 7},
                            controls=[
                                ft.Text("Объем прямоугольного параллелепипеда",
                                        size=24, weight=ft.FontWeight.BOLD),
                                ft.Text(
                                    "Объем прямоугольного параллелепипеда равен произведению длин трех его ребер, "
                                    "выходящих из одной вершины.",
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
                                ft.Image(cube2_2,
                                         width=150, height=150, fit=ft.ImageFit.CONTAIN),
                                ft.ElevatedButton(
                                    "Открыть 3D модель",
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
                                ft.Text("Объем призмы",
                                        size=24, weight=ft.FontWeight.BOLD),
                                ft.Text(
                                    "Объем призмы равен произведению площади основания на высоту.",
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
                                ft.Image(prism_3,
                                         width=150, height=150, fit=ft.ImageFit.CONTAIN),
                                ft.ElevatedButton(
                                    "Открыть 3D модель",
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
                                ft.Text("Объем пирамиды",
                                        size=24, weight=ft.FontWeight.BOLD),
                                ft.Text(
                                    "Объем пирамиды равен одной трети произведения площади основания на высоту.",
                                    size=20, weight=ft.FontWeight.W_500
                                ),
                                proof_button3,
                                proof_container3,
                            ],
                            spacing=5,
                        ),
                        ft.Column(
                            col={"sm": 9, "md": 5},
                            controls=[
                                ft.Container(width=10, height=10),
                                ft.Image( piramid_40,
                                         width=30, height=90, fit=ft.ImageFit.CONTAIN),
                                ft.ElevatedButton(
                                    "Открыть 3D модель",
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
                            col={"sm": 12},
                            controls=[
                                ft.Text("Дополнительные формулы объемов",
                                        size=24, weight=ft.FontWeight.BOLD),
                                ft.Text(
                                    "• Объем цилиндра: V = πr²h\n"
                                    "• Объем конуса: V = (1/3)πr²h\n"
                                    "• Объем шара: V = (4/3)πr³\n"
                                    "• Объем усеченной пирамиды: V = (1/3)h(S₁ + S₂ + √(S₁S₂))",
                                    size=20, weight=ft.FontWeight.W_500
                                ),
                            ],
                            spacing=5,
                        ),
                    ],
                    spacing=20,
                ),
            ],
            spacing=15,
            scroll=ft.ScrollMode.AUTO
        ),
        expand=True
    )
    page.update()