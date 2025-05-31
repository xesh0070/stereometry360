import flet as ft

a1 = "assets/a1.svg"
a2 = "assets/a2.svg"
a3 = "assets/a3_ok.svg"
sled_a1 = "assets/sled_a1.svg"
sled_a2 = "assets/sled_a2.svg"
parallel_line1 = "assets/parallel_line1.svg"
parallel_line_lemma = "assets/parallel_line_lemma.svg"
parallel_line3 = "assets/parallel_line3.svg"
parallel_line_plane1 ="assets/parallel_line_plane1.svg"
parallel_line_plane2 ="assets/parallel_line_plane2.svg"
parallel_line_plane3 ="assets/parallel_line_plane3.svg"

def lines_arrangement(e, page, details1):
    # Создаем контейнеры для доказательств, которые будут скрыты/показаны
    proof_container1 = ft.Column([], spacing=5)
    proof_container2 = ft.Column([], spacing=5)
    proof_container3 = ft.Column([], spacing=5)

    # Доказательства
    doc_1 = ft.Column(
        controls=[
            ft.Text("Дано: Прямые a и b в пространстве.", size=18, weight=ft.FontWeight.BOLD),
            ft.Text("Доказать:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text("1) Прямые могут быть параллельны, пересекаться или скрещиваться.", size=18),
            ft.Text("Доказательство:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text(
                "1. Если прямые лежат в одной плоскости, то возможны два случая:\n"
                "   - Прямые пересекаются (имеют одну общую точку)\n"
                "   - Прямые параллельны (не имеют общих точек)\n\n"
                "2. Если прямые не лежат в одной плоскости, то они называются скрещивающимися. "
                "Скрещивающиеся прямые не имеют общих точек и не параллельны.",
                size=18),
        ],
        spacing=5,
        tight=True,
    )

    doc_2 = ft.Column(
        controls=[
            ft.Text("Дано: Прямые a и b скрещиваются.", size=18, weight=ft.FontWeight.BOLD),
            ft.Text("Доказать:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text("1) Через одну из скрещивающихся прямых можно провести плоскость, параллельную другой прямой.", size=18),
            ft.Text("2) Такая плоскость единственна.", size=18),
            ft.Text("Доказательство:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text(
                "1. Пусть даны скрещивающиеся прямые a и b. Возьмем произвольную точку M на прямой a.\n"
                "2. Через точку M проведем прямую b', параллельную прямой b.\n"
                "3. Прямые a и b' определяют плоскость α. По построению b ∥ b' и b' ⊂ α ⇒ b ∥ α.\n"
                "4. Единственность следует из того, что через прямую a и точку M проходит единственная плоскость, "
                "а через точку M можно провести единственную прямую, параллельную b.",
                size=18),
        ],
        spacing=5,
        tight=True,
    )

    doc_3 = ft.Column(
        controls=[
            ft.Text("Дано: Прямые a ∥ b, c ∥ b.", size=18, weight=ft.FontWeight.BOLD),
            ft.Text("Доказать: a ∥ c.", size=18, weight=ft.FontWeight.BOLD),
            ft.Text("Доказательство:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text(
                "1. Если все три прямые лежат в одной плоскости, то утверждение следует из планиметрии.\n"
                "2. Если прямые не лежат в одной плоскости:\n"
                "   - Через прямую a и произвольную точку M на прямой b проведем плоскость α.\n"
                "   - Через прямую c и точку M проведем плоскость β.\n"
                "   - Так как b ∥ a и b ∥ c, то b ∥ α и b ∥ β.\n"
                "   - Плоскости α и β содержат точку M и параллельны прямой b ⇒ они совпадают.\n"
                "   - Таким образом, прямые a и c лежат в одной плоскости и параллельны прямой b ⇒ a ∥ c.",
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
                ft.Column([ft.Text("Теория стереометрии. Взаимное расположение прямых в пространстве",
                                   size=12, weight=ft.FontWeight.BOLD),
                           ft.Text("Взаимное расположение прямых в пространстве", size=28, weight=ft.FontWeight.BOLD)],
                          spacing=5),

                ft.ResponsiveRow(
                    controls=[
                        ft.Column(
                            col={"sm": 12, "md": 7},
                            controls=[
                                ft.Text("Основные случаи взаимного расположения", size=24, weight=ft.FontWeight.BOLD),
                                ft.Text(
                                    "В пространстве две прямые могут:\n"
                                    "1. Лежать в одной плоскости и пересекаться\n"
                                    "2. Лежать в одной плоскости и быть параллельными\n"
                                    "3. Не лежать в одной плоскости (скрещиваться)",
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
                                ft.Text("Плоскость, параллельная скрещивающейся прямой", size=24, weight=ft.FontWeight.BOLD),
                                ft.Text(
                                    "Через каждую из двух скрещивающихся прямых проходит плоскость, параллельная другой прямой, и притом только одна.",
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
                                ft.Text("Транзитивность параллельности прямых", size=24, weight=ft.FontWeight.BOLD),
                                ft.Text(
                                    "Если две прямые параллельны третьей прямой, то они параллельны между собой.",
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
                                ft.Image(sled_a2, width=30, height=90, fit=ft.ImageFit.CONTAIN),
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
            ],
            spacing=15,
            scroll=ft.ScrollMode.AUTO
        ),
        expand=True
    )
    page.update()

def parallel_line_plane(e, page, details1):
        # Создаем контейнеры для доказательств, которые будут скрыты/показаны
        proof_container1 = ft.Column([], spacing=5)
        proof_container2 = ft.Column([], spacing=5)
        proof_container3 = ft.Column([], spacing=5)

        # Доказательства
        doc_1 = ft.Column(
            controls=[
                ft.Text("Дано: Прямая a ∥ плоскости α, M ∈ α.", size=18, weight=ft.FontWeight.BOLD),
                ft.Text("Доказать:", size=18, weight=ft.FontWeight.BOLD),
                ft.Text("1) Существует прямая b ∥ a, M ∈ b, b ⊂ α.", size=18),
                ft.Text("2) Прямая b единственна.", size=18),

                ft.Text("Доказательство 1:", size=18, weight=ft.FontWeight.BOLD),
                ft.Text(
                    "Через прямую a и точку M можно провести плоскость β. Так как a ∥ α, то a не пересекает α. "
                    "Плоскости α и β пересекаются по прямой b, проходящей через M. Прямые a и b лежат в одной плоскости β "
                    "и не пересекаются (так как a ∥ α и b ⊂ α), значит a ∥ b. Существование доказано.",
                    size=18),

                ft.Text("Доказательство 2:", size=18, weight=ft.FontWeight.BOLD),
                ft.Text(
                    "Предположим, существует другая прямая c ⊂ α, M ∈ c, c ∥ a. Тогда a ∥ c и a ∥ b ⇒ c ∥ b. "
                    "Но c и b лежат в одной плоскости α и проходят через одну точку M ⇒ c = b. Единственность доказана.",
                    size=18),
            ],
            spacing=5,
            tight=True,
        )

        doc_2 = ft.Column(
            controls=[
                ft.Text("Дано: a ∥ α, β ⊃ a, β ∩ α = b", size=18, weight=ft.FontWeight.BOLD),
                ft.Text("Доказать: a ∥ b", size=18, weight=ft.FontWeight.BOLD),

                ft.Text("Доказательство:", size=18, weight=ft.FontWeight.BOLD),
                ft.Text(
                    "1) Прямые a и b лежат в одной плоскости β (по условию).\n"
                    "2) Прямая a не пересекает плоскость α (так как a ∥ α).\n"
                    "3) Прямая b лежит в плоскости α ⇒ a и b не пересекаются.\n"
                    "4) Из 1) и 3) следует, что a ∥ b.",
                    size=18),
            ],
            spacing=5,
            tight=True,
        )

        doc_3 = ft.Column(
            controls=[
                ft.Text("Дано: a ∥ α, a ∥ b, b ⊂ α", size=18, weight=ft.FontWeight.BOLD),
                ft.Text("Доказать: b ∥ α", size=18, weight=ft.FontWeight.BOLD),

                ft.Text("Доказательство:", size=18, weight=ft.FontWeight.BOLD),
                ft.Text(
                    "1) Так как a ∥ b, то существует плоскость β, содержащая a и b.\n"
                    "2) Так как a ∥ α, то a не пересекает α.\n"
                    "3) Прямая b ⊂ α и b ⊂ β ⇒ β ∩ α = b.\n"
                    "4) Любая другая прямая c ⊂ α, параллельная a, должна совпадать с b (по теореме о единственности).\n"
                    "5) Следовательно, b ∥ α.",
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
                        ft.Text("Теория стереометрии. Параллельность прямой и плоскости",
                                size=12, weight=ft.FontWeight.BOLD),
                        ft.Text("Параллельность прямой и плоскости", size=28, weight=ft.FontWeight.BOLD)
                    ], spacing=5),

                    ft.ResponsiveRow(
                        controls=[
                            ft.Column(
                                col={"sm": 12, "md": 7},
                                controls=[
                                    ft.Text("Определение", size=24, weight=ft.FontWeight.BOLD),
                                    ft.Text(
                                        "Прямая и плоскость называются параллельными, если они не имеют общих точек.",
                                        size=20, weight=ft.FontWeight.W_500
                                    ),
                                    ft.Text(
                                        "a ∩ α = ∅ ⇒ a ∥ α",
                                        size=18, weight=ft.FontWeight.W_400
                                    ),
                                ],
                                spacing=5,
                            ),
                            ft.Column(
                                col={"sm": 9, "md": 5},
                                controls=[
                                    ft.Container(width=10, height=10),
                                    ft.Image(parallel_line_plane1, width=70, height=120, fit=ft.ImageFit.CONTAIN),
                                    ft.ElevatedButton(
                                        "Открыть 3D модель",
                                        # on_click=lambda e: start_pygame_with_parallel_line_plane1(e),
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
                                    ft.Text("Признак параллельности прямой и плоскости", size=24,
                                            weight=ft.FontWeight.BOLD),
                                    ft.Text(
                                        "Если прямая параллельна некоторой прямой, лежащей в плоскости, то она параллельна самой плоскости.",
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
                                    ft.Image(parallel_line_plane2, width=70, height=120, fit=ft.ImageFit.CONTAIN),
                                    ft.ElevatedButton(
                                        "Открыть 3D модель",
                                        # on_click=lambda e: start_pygame_with_parallel_line_plane3(e),
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
                                    ft.Text("Теорема о пересечении плоскостей", size=24, weight=ft.FontWeight.BOLD),
                                    ft.Text(
                                        "Если две плоскости пересекаются и одна из них содержит прямую, параллельную другой плоскости, то линия пересечения плоскостей параллельна этой прямой.",
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
                                    ft.Image(parallel_line_plane3, width=70, height=140, fit=ft.ImageFit.CONTAIN),
                                    ft.ElevatedButton(
                                        "Открыть 3D модель",
                                        # on_click=lambda e: start_pygame_with_parallel_line_plane4(e),
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
def parallel_line(e, page, details1):
            # Создаем контейнеры для пруфоф, которые будут скрыты/показаны
            proof_container1 = ft.Column([], spacing=5)
            proof_container2 = ft.Column([], spacing=5)
            proof_container3 = ft.Column([], spacing=5)

            # Доказательства
            doc_1 = ft.Column(
                controls=[
                    ft.Text("Дано: Прямая a, M ∉ a.", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("Доказать:", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("1) Существует прямая b ∥ a, M ∈ b.", size=18),

                    ft.Text("2) Прямая b единственна.", size=18),

                    ft.Text("Доказательство 1:", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text(
                        "Через прямую а и точку M, не лежащую на ней, можно провести единственную плоскость α. В плоскости α  можно провести единственную прямую b, параллельную а, проходящую через точку M (из аксиомы планиметрии о параллельных прямых). Существование такой прямой доказано.",
                        size=18),
                    ft.Text("Доказательство 2:", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text(
                        "Докажем единственность такой прямой. Предположим, что существует другая прямая с, проходящая через точку M и параллельная прямой а. Пусть параллельные прямые а и с лежат в плоскости β. Тогда плоскость β проходит через точку M и прямую а. Но через точку M и прямую а проходит единственная плоскость (в силу аксиомы 2). Значит, плоскости β и α совпадают. Из аксиомы параллельных прямых, следует, что прямые b и с совпадают, так как в плоскости существует единственная прямая, проходящая через данную точку и параллельная заданной прямой. Единственность доказана.",
                        size=18),
                ],
                spacing=5,
                tight=True,
            )

            doc_2 = ft.Column(
                controls=[
                    ft.Text("Дано: b ∥ a, a ∩ α = M", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("Доказать: b ∩ α = N", size=18, weight=ft.FontWeight.BOLD),


                    ft.Text("Доказательство:", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text(
                        "Существует некоторая плоскость β, в которой лежат параллельные прямые а и b. Точка М принадлежит и плоскости α, и прямой а, которая лежит в плоскости β. Значит, М – общая точка плоскостей α и β. А по третьей аксиоме, существует прямая MN, по которой пересекаются эти две плоскости.\n " 
                        "Прямая MN пересекается с прямой b.(так как в противном случае, получается, что прямые MN и b параллельные, то есть a = MN, что невозможно, так как прямая а пересекается с плоскостью α в точке М по условию). То есть точка N – это точка пересечения прямой b и плоскости α. b ∩ α = N\n"
                        "Докажем, что N - это единственная общая точка прямой b и плоскости α. Допустим, что есть другая точка, но тогда прямая bпринадлежит плоскости α (по второй аксиоме). То есть MN = b, что невозможно, так как прямые а и b параллельны, а прямая а должна пересекаться с прямой MN. Лемма доказана.",
                        size=18),

                ],
                spacing=5,
                tight=True,
            )

            doc_3 = ft.Column(
                controls=[
                    ft.Text("Дано: b ∥ a, a ∩ α = M", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("Доказать: b ∩ α = N", size=18, weight=ft.FontWeight.BOLD),

                    ft.Text("Доказательство:", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text(
                        "Существует некоторая плоскость β, в которой лежат параллельные прямые а и b. Точка М принадлежит и плоскости α, и прямой а, которая лежит в плоскости β. Значит, М – общая точка плоскостей α и β. А по третьей аксиоме, существует прямая MN, по которой пересекаются эти две плоскости.\n "
                        "Прямая MN пересекается с прямой b.(так как в противном случае, получается, что прямые MN и b параллельные, то есть a = MN, что невозможно, так как прямая а пересекается с плоскостью α в точке М по условию). То есть точка N – это точка пересечения прямой b и плоскости α. b ∩ α = N\n"
                        "Докажем, что N - это единственная общая точка прямой b и плоскости α. Допустим, что есть другая точка, но тогда прямая bпринадлежит плоскости α (по второй аксиоме). То есть MN = b, что невозможно, так как прямые а и b параллельны, а прямая а должна пересекаться с прямой MN. Лемма доказана.",
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

            def toggle_proof3(e):
                if proof_container3.controls:
                    proof_container3.controls.clear()
                    e.control.text = "Показать доказательство"
                else:
                    proof_container3.controls.append(doc_3)
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

            proof_button3 = ft.TextButton(
                "Показать доказательство",
                on_click=toggle_proof3,
                style=ft.ButtonStyle(color="#4E426D")
            )

            details1.content = ft.Container(
                content=ft.Column(
                    [
                        ft.Column([ft.Text("Теория стереометрии. Аксиомы стереометрии: Параллельные прямые в пространстве",
                                           size=12, weight=ft.FontWeight.BOLD),
                                   ft.Text("Параллельные прямые в пространстве", size=28, weight=ft.FontWeight.BOLD)],
                                  spacing=5),

                        ft.ResponsiveRow(
                            controls=[
                                ft.Column(
                                    col={"sm": 12, "md": 7},
                                    controls=[
                                        ft.Text("Определение", size=24, weight=ft.FontWeight.BOLD),
                                        ft.Text(
                                            "Две прямые в пространстве называются параллельными, если они лежат в одной плоскости и не пересекаются.",
                                            size=20, weight=ft.FontWeight.W_500
                                        ),
                                        ft.Text(
                                            "Прямые  и  лежат в плоскости и не пересекаются ⇒ прямые a и b параллельны (a ∥ b).",
                                            size=18, weight=ft.FontWeight.W_400
                                        ),
                                    ],
                                    spacing=5,
                                ),
                                ft.Column(
                                    col={"sm": 9, "md": 5},
                                    controls=[
                                        ft.Container(width=10, height=10),
                                        ft.Image(parallel_line1, width=30, height=90, fit=ft.ImageFit.CONTAIN),
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
                                        ft.Text("Теорема о параллельных прямых", size=24, weight=ft.FontWeight.BOLD),
                                        ft.Text(
                                            "Через любую точку пространства, не лежащую на данной прямой, проходит прямая, параллельная данной, и притом только одна.",
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
                                        ft.Text("Лемма о двух параллельных прямых", size=24, weight=ft.FontWeight.BOLD),
                                        ft.Text(
                                            "Если одна из двух параллельных прямых пересекает некоторую плоскость, то и вторая прямая пересекает эту плоскость.",
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
                                        ft.Image(parallel_line_lemma, width=80, height=160, fit=ft.ImageFit.CONTAIN),
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
                                        ft.Text("Теорема о трёх прямых в пространстве", size=24, weight=ft.FontWeight.BOLD),
                                        ft.Text(
                                            "Если две прямые параллельны третьей прямой, то они параллельны между собой.",
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
                                        ft.Image(parallel_line3, width=30, height=90, fit=ft.ImageFit.CONTAIN),
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

                    ],
                    spacing=15,
                    scroll=ft.ScrollMode.AUTO
                ),
                expand=True
            )
            page.update()


def parallel_planes(e, page, details1):
    # Создаем контейнеры для доказательств
    proof_container1 = ft.Column([], spacing=5)
    proof_container2 = ft.Column([], spacing=5)
    proof_container3 = ft.Column([], spacing=5)

    # Доказательства
    doc_1 = ft.Column(
        controls=[
            ft.Text("Дано: α ∥ β, γ ∩ α = a, γ ∩ β = b", size=18, weight=ft.FontWeight.BOLD),
            ft.Text("Доказать: a ∥ b", size=18, weight=ft.FontWeight.BOLD),

            ft.Text("Доказательство:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text(
                "1) Плоскости α и β параллельны ⇒ не имеют общих точек.\n"
                "2) Прямые a и b лежат в одной плоскости γ.\n"
                "3) Если бы a и b пересекались, то их точка пересечения принадлежала бы и α, и β, что невозможно.\n"
                "4) Следовательно, a ∥ b.",
                size=18),
        ],
        spacing=5,
        tight=True,
    )

    doc_2 = ft.Column(
        controls=[
            ft.Text("Дано: a ∩ b = O, a ⊂ α, b ⊂ α, a' ∥ a, b' ∥ b, a' ⊂ β, b' ⊂ β",
                    size=18, weight=ft.FontWeight.BOLD),
            ft.Text("Доказать: α ∥ β", size=18, weight=ft.FontWeight.BOLD),

            ft.Text("Доказательство:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text(
                "1) Если бы α ∩ β = c, то c ∥ a и c ∥ b (по теореме о параллельных прямых).\n"
                "2) Но a и b пересекаются в точке O ⇒ через O можно провести только одну прямую, параллельную c.\n"
                "3) Получаем противоречие ⇒ плоскости не пересекаются ⇒ α ∥ β.",
                size=18),
        ],
        spacing=5,
        tight=True,
    )

    doc_3 = ft.Column(
        controls=[
            ft.Text("Дано: α ∥ β, γ ∥ δ, γ ∩ α = a, δ ∩ β = b", size=18, weight=ft.FontWeight.BOLD),
            ft.Text("Доказать: a ∥ b", size=18, weight=ft.FontWeight.BOLD),

            ft.Text("Доказательство:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text(
                "1) По свойству параллельных плоскостей: γ ∥ δ ⇒ линии пересечения с параллельными плоскостями параллельны.\n"
                "2) Аналогично для α ∥ β ⇒ a ∥ b.",
                size=18),
        ],
        spacing=5,
        tight=True,
    )

    # Функции для показа/скрытия доказательств
    def toggle_proof1(e):
        proof_container1.controls.clear() if proof_container1.controls else proof_container1.controls.append(doc_1)
        e.control.text = "Скрыть доказательство" if proof_container1.controls else "Показать доказательство"
        page.update()

    def toggle_proof2(e):
        proof_container2.controls.clear() if proof_container2.controls else proof_container2.controls.append(doc_2)
        e.control.text = "Скрыть доказательство" if proof_container2.controls else "Показать доказательство"
        page.update()

    def toggle_proof3(e):
        proof_container3.controls.clear() if proof_container3.controls else proof_container3.controls.append(doc_3)
        e.control.text = "Скрыть доказательство" if proof_container3.controls else "Показать доказательство"
        page.update()

    # Кнопки доказательств
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
                    ft.Text("Теория стереометрии. Параллельность плоскостей",
                            size=12, weight=ft.FontWeight.BOLD),
                    ft.Text("Параллельные плоскости", size=28, weight=ft.FontWeight.BOLD)
                ], spacing=5),

                ft.ResponsiveRow(
                    controls=[
                        ft.Column(
                            col={"sm": 12, "md": 7},
                            controls=[
                                ft.Text("Определение", size=24, weight=ft.FontWeight.BOLD),
                                ft.Text(
                                    "Две плоскости называются параллельными, если они не пересекаются.",
                                    size=20, weight=ft.FontWeight.W_500
                                ),
                                ft.Text(
                                    "α ∩ β = ∅ ⇒ α ∥ β",
                                    size=18, weight=ft.FontWeight.W_400
                                ),
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
                                ft.Text("Теорема о линии пересечения", size=24, weight=ft.FontWeight.BOLD),
                                ft.Text(
                                    "Если две параллельные плоскости пересечены третьей плоскостью, то линии пересечения параллельны.",
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
                                ft.Image(sled_a2, width=30, height=90, fit=ft.ImageFit.CONTAIN),
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
                                ft.Text("Признак параллельности плоскостей", size=24, weight=ft.FontWeight.BOLD),
                                ft.Text(
                                    "Если две пересекающиеся прямые одной плоскости соответственно параллельны двум прямым другой плоскости, то эти плоскости параллельны.",
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
                                ft.Text("Свойство параллельных плоскостей", size=24, weight=ft.FontWeight.BOLD),
                                ft.Text(
                                    "Отрезки параллельных прямых, заключенные между параллельными плоскостями, равны.",
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
                                ft.Image(sled_a2, width=30, height=90, fit=ft.ImageFit.CONTAIN),
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
            ],
            spacing=15,
            scroll=ft.ScrollMode.AUTO
        ),
        expand=True
    )
    page.update()
def polyhedrons(e, page, details1):
    # Создаем контейнеры для доказательств
    proof_container1 = ft.Column([], spacing=5)
    proof_container2 = ft.Column([], spacing=5)
    proof_container3 = ft.Column([], spacing=5)
    proof_container4 = ft.Column([], spacing=5)

    # Доказательства и теоремы
    doc_1 = ft.Column(
        controls=[
            ft.Text("Определение тетраэдра:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text(
                "Тетраэдр - это многогранник с четырьмя треугольными гранями, "
                "шестью рёбрами и четырьмя вершинами. Является частным случаем пирамиды.",
                size=18),
            ft.Text("Свойства:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text(
                "1) Любая грань может быть принята за основание\n"
                "2) Имеет 4 грани, 6 рёбер, 4 вершины\n"
                "3) Плоскость, проходящая через середины двух скрещивающихся рёбер, делит тетраэдр на две равные части",
                size=18),
        ],
        spacing=5,
        tight=True,
    )

    doc_2 = ft.Column(
        controls=[
            ft.Text("Определение параллелепипеда:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text(
                "Параллелепипед - это призма, основанием которой служит параллелограмм. "
                "Имеет 6 граней (все параллелограммы), 12 рёбер, 8 вершин.",
                size=18),
            ft.Text("Виды:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text(
                "1) Прямой - боковые рёбра перпендикулярны основаниям\n"
                "2) Прямоугольный - все грани прямоугольники\n"
                "3) Наклонный - боковые рёбра не перпендикулярны основаниям",
                size=18),
        ],
        spacing=5,
        tight=True,
    )

    doc_3 = ft.Column(
        controls=[
            ft.Text("Теорема о диагоналях параллелепипеда:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text(
                "Диагонали параллелепипеда пересекаются в одной точке и делятся этой точкой пополам.",
                size=18, weight=ft.FontWeight.W_500),
            ft.Text("Доказательство:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text(
                "1) Рассмотрим три диагональные плоскости параллелепипеда\n"
                "2) Каждая из них - параллелограмм по свойству параллелепипеда\n"
                "3) Диагонали параллелограмма точкой пересечения делятся пополам\n"
                "4) Следовательно, все четыре диагонали проходят через одну точку - центр симметрии",
                size=18),
        ],
        spacing=5,
        tight=True,
    )

    doc_4 = ft.Column(
        controls=[
            ft.Text("Теорема о прямоугольном параллелепипеде:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text(
                "Квадрат длины диагонали прямоугольного параллелепипеда равен сумме квадратов трёх его измерений.",
                size=18, weight=ft.FontWeight.W_500),
            ft.Text("Доказательство:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text(
                "1) Пусть измерения равны a, b, c\n"
                "2) Диагональ основания d₁ = √(a² + b²)\n"
                "3) Искомая диагональ d = √(d₁² + c²) = √(a² + b² + c²)\n"
                "4) Что и требовалось доказать",
                size=18),
        ],
        spacing=5,
        tight=True,
    )

    # Функции для показа/скрытия доказательств
    def toggle_proof1(e):
        proof_container1.controls.clear() if proof_container1.controls else proof_container1.controls.append(doc_1)
        e.control.text = "Скрыть теорию" if proof_container1.controls else "Показать теорию"
        page.update()

    def toggle_proof2(e):
        proof_container2.controls.clear() if proof_container2.controls else proof_container2.controls.append(doc_2)
        e.control.text = "Скрыть теорию" if proof_container2.controls else "Показать теорию"
        page.update()

    def toggle_proof3(e):
        proof_container3.controls.clear() if proof_container3.controls else proof_container3.controls.append(doc_3)
        e.control.text = "Скрыть доказательство" if proof_container3.controls else "Показать доказательство"
        page.update()

    def toggle_proof4(e):
        proof_container4.controls.clear() if proof_container4.controls else proof_container4.controls.append(doc_4)
        e.control.text = "Скрыть доказательство" if proof_container4.controls else "Показать доказательство"
        page.update()

    # Кнопки
    proof_button1 = ft.TextButton(
        "Показать теорию",
        on_click=toggle_proof1,
        style=ft.ButtonStyle(color="#4E426D")
    )

    proof_button2 = ft.TextButton(
        "Показать теорию",
        on_click=toggle_proof2,
        style=ft.ButtonStyle(color="#4E426D")
    )

    proof_button3 = ft.TextButton(
        "Показать доказательство",
        on_click=toggle_proof3,
        style=ft.ButtonStyle(color="#4E426D")
    )

    proof_button4 = ft.TextButton(
        "Показать доказательство",
        on_click=toggle_proof4,
        style=ft.ButtonStyle(color="#4E426D")
    )

    details1.content = ft.Container(
        content=ft.Column(
            [
                ft.Column([
                    ft.Text("Стереометрия. Многогранники", size=12, weight=ft.FontWeight.BOLD),
                    ft.Text("Тетраэдр и параллелепипед", size=28, weight=ft.FontWeight.BOLD)
                ], spacing=5),

                # Секция тетраэдра
                ft.ResponsiveRow(
                    controls=[
                        ft.Column(
                            col={"sm": 12, "md": 7},
                            controls=[
                                ft.Text("Тетраэдр", size=24, weight=ft.FontWeight.BOLD),
                                ft.Text(
                                    "Основной объект стереометрии, простейший многогранник с треугольными гранями.",
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
                                ft.Image("assets/tetrahedron.png", width=30, height=90, fit=ft.ImageFit.CONTAIN),
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

                # Секция параллелепипеда
                ft.ResponsiveRow(
                    controls=[
                        ft.Column(
                            col={"sm": 12, "md": 7},
                            controls=[
                                ft.Text("Параллелепипед", size=24, weight=ft.FontWeight.BOLD),
                                ft.Text(
                                    "Важнейший многогранник, основанный на параллелограммах. Широко применяется в архитектуре и технике.",
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
                                ft.Image("assets/parallelepiped.png", width=30, height=90, fit=ft.ImageFit.CONTAIN),
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

                # Теоремы
                ft.ResponsiveRow(
                    controls=[
                        ft.Column(
                            col={"sm": 12, "md": 12},
                            controls=[
                                ft.Text("Основные теоремы", size=24, weight=ft.FontWeight.BOLD),
                            ],
                            spacing=5,
                        ),
                    ],
                    spacing=20,
                ),

                ft.Column(
                    controls=[
                        ft.Column(
                            col={"sm": 12, "md": 6},
                            controls=[
                                ft.Text("Свойство диагоналей параллелепипеда", size=22, weight=ft.FontWeight.BOLD),
                                proof_button3,
                                proof_container3,
                            ],
                            spacing=5,
                        ),
                        ft.Column(
                            col={"sm": 12, "md": 6},
                            controls=[
                                ft.Text("Теорема о диагонали прямоугольного параллелепипеда", size=22, weight=ft.FontWeight.BOLD),
                                proof_button4,
                                proof_container4,
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

def perpendicular_line_plane(e, page, details1):
    # Создаем контейнеры для доказательств
    proof_container1 = ft.Column([], spacing=5)
    proof_container2 = ft.Column([], spacing=5)
    proof_container3 = ft.Column([], spacing=5)

    # Доказательства
    doc_1 = ft.Column(
        controls=[
            ft.Text("Определение:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text("Прямая называется перпендикулярной плоскости, если она перпендикулярна всем прямым в этой плоскости.", size=18),
            ft.Text("Доказательство признака перпендикулярности:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text(
                "Если прямая перпендикулярна двум пересекающимся прямым, лежащим в плоскости, то она перпендикулярна этой плоскости.\n\n"
                "Дано: прямая a ⊥ b, a ⊥ c, где b и c ⊂ α, b ∩ c = O\n"
                "Доказать: a ⊥ α\n\n"
                "1. Возьмем произвольную прямую m ⊂ α, проходящую через O\n"
                "2. Проведем через O прямую n ∥ a ⇒ a ⊥ α ⇔ n ⊥ α\n"
                "3. Так как n ∥ a и a ⊥ b, a ⊥ c ⇒ n ⊥ b и n ⊥ c\n"
                "4. По теореме о трех перпендикулярах n ⊥ m\n"
                "5. Так как m - произвольная ⇒ n ⊥ α ⇒ a ⊥ α",
                size=18),
        ],
        spacing=5,
    )

    doc_2 = ft.Column(
        controls=[
            ft.Text("Теорема о единственности:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text(
                "Через любую точку пространства проходит единственная прямая, перпендикулярная данной плоскости.\n\n"
                "Доказательство:\n"
                "1. Существование: построим две пересекающиеся прямые в плоскости и проведем перпендикуляр к ним\n"
                "2. Единственность: предположим, есть две перпендикулярные прямые ⇒ они параллельны (противоречие)",
                size=18),
        ],
        spacing=5,
    )

    doc_3 = ft.Column(
        controls=[
            ft.Text("Теорема о плоскости перпендикуляров:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text(
                "Все прямые, перпендикулярные данной прямой в данной точке, лежат в одной плоскости.\n\n"
                "Доказательство:\n"
                "1. Пусть a ⊥ b и a ⊥ c в точке O\n"
                "2. Любая другая прямая d ⊥ a может быть выражена как линейная комбинация b и c\n"
                "3. Следовательно, все такие прямые лежат в плоскости, определяемой b и c",
                size=18),
        ],
        spacing=5,
    )

    # Функции переключения доказательств
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

    # Кнопки доказательств
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
                    ft.Text("Теория стереометрии. Перпендикулярность прямой и плоскости",
                           size=12, weight=ft.FontWeight.BOLD),
                    ft.Text("Перпендикулярность прямой и плоскости",
                           size=28, weight=ft.FontWeight.BOLD)
                ], spacing=5),

                ft.ResponsiveRow(
                    controls=[
                        ft.Column(
                            col={"sm": 12, "md": 7},
                            controls=[
                                ft.Text("Признак перпендикулярности", size=24, weight=ft.FontWeight.BOLD),
                                ft.Text(
                                    "Если прямая перпендикулярна двум пересекающимся прямым, лежащим в плоскости, "
                                    "то она перпендикулярна этой плоскости.",
                                    size=20, weight=ft.FontWeight.W_500),
                                proof_button1,
                                proof_container1,
                            ],
                            spacing=5,
                        ),
                        ft.Column(
                            col={"sm": 9, "md": 5},
                            controls=[
                                ft.Container(width=10, height=10),
                                ft.Image(a1, width=30, height=90, fit=ft.ImageFit.CONTAIN),
                                ft.ElevatedButton(
                                    "Открыть 3D модель",
                                    # on_click=lambda e: start_pygame_with_perp1(e),
                                    style=ft.ButtonStyle(color="#4E426D"),
                                    width=180
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,
                        ),
                    ],
                    spacing=20,
                ),

                ft.ResponsiveRow(
                    controls=[
                        ft.Column(
                            col={"sm": 12, "md": 7},
                            controls=[
                                ft.Text("Единственность перпендикуляра", size=24, weight=ft.FontWeight.BOLD),
                                ft.Text(
                                    "Через любую точку пространства проходит единственная прямая, "
                                    "перпендикулярная данной плоскости.",
                                    size=20, weight=ft.FontWeight.W_500),
                                proof_button2,
                                proof_container2,
                            ],
                            spacing=5,
                        ),
                        ft.Column(
                            col={"sm": 9, "md": 5},
                            controls=[
                                ft.Container(width=10, height=10),
                                ft.Image(a2, width=30, height=90, fit=ft.ImageFit.CONTAIN),
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
                ),

                ft.ResponsiveRow(
                    controls=[
                        ft.Column(
                            col={"sm": 12, "md": 7},
                            controls=[
                                ft.Text("Плоскость перпендикуляров", size=24, weight=ft.FontWeight.BOLD),
                                ft.Text(
                                    "Все прямые, перпендикулярные данной прямой в данной точке, "
                                    "лежат в одной плоскости.",
                                    size=20, weight=ft.FontWeight.W_500),
                                proof_button3,
                                proof_container3,
                            ],
                            spacing=5,
                        ),
                        ft.Column(
                            col={"sm": 9, "md": 5},
                            controls=[
                                ft.Container(width=10, height=10),
                                ft.Image(a2, width=30, height=90, fit=ft.ImageFit.CONTAIN),
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
                ),
            ],
            spacing=15,
            scroll=ft.ScrollMode.AUTO
        ),
        expand=True
    )
    page.update()
