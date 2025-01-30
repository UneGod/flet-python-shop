import flet as ft
from front.buttons import SuccessBtn
import back.registerb as rg
import back.loginb as lg
import time
import random
import back.get_product as gp
import back.add_product as ap


def main(page: ft.Page):

    def buy_button_click(e, product_name):
                page.snack_bar = ft.SnackBar(ft.Text(f"Товар '{product_name}' добавлен в корзину!"))
                page.snack_bar.open = True
                page.update()

    def registerBox(e):
        page.remove(log)
        page.add(reg)
        page.add(ic)
        

    def back_to_log(e):
        page.clean()
        page.add(log)

    def go_to_profile(e):
        page.clean()


    def login(e):
        success = lg.loging(Login.value, Pass.value)
        if success[4]:
            page.remove(log)
            page.title = "Welcome!"
            numb = ''.join(random.choices('0123456789abcdef', k=6))

            def user_button_click(e):
                    page.clean()
                    img = success[5]
                    avatar = ft.CircleAvatar(
                        foreground_image_src=img,
                        radius=50,
                    )

                    username = ft.Text(
                        success[1],
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,
                    )

                    bio = ft.Text(
                        "Python разработчик | Люблю создавать красивые интерфейсы.",
                        size=16,
                        color=ft.colors.WHITE70,
                    )

                    actions = ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="Редактировать профиль",
                                icon=ft.icons.EDIT,
                                bgcolor=ft.colors.BLUE_700,
                                color=ft.colors.WHITE,
                            ),
                            ft.ElevatedButton(
                                text="Сообщение",
                                icon=ft.icons.MESSAGE,
                                bgcolor=ft.colors.GREEN_700,
                                color=ft.colors.WHITE,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10,
                    )

                    social_icons = ft.Row(
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.FACEBOOK,
                                icon_color=ft.colors.BLUE_500,
                                tooltip="Facebook",
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10,
                    )

                    profile_container = ft.Column(
                        controls=[
                            ft.Container(
                                content=avatar,
                                alignment=ft.alignment.center,
                                padding=10,
                            ),
                            ft.Container(
                                content=username,
                                alignment=ft.alignment.center,
                                padding=5,
                            ),
                            ft.Container(
                                content=bio,
                                alignment=ft.alignment.center,
                                padding=5,
                            ),
                            ft.Divider(color=ft.colors.WHITE24, height=20),
                            actions,
                            ft.Divider(color=ft.colors.WHITE24, height=20),
                            social_icons,
                        ],
                        spacing=10,
                    )

                    page.add(profile_container, ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=go_to_main_page))


            def add_product(e):
                ap.register_product(product_name_field.value, product_price_field.value, product_stock_quantity.value, product_image_field.value)
                page.update()

            def go_to_main_page(e):
                page.clean()
                products = gp.get_product()

                product_cards = []
                for product in products:
                    card = ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                [
                                    ft.Image(
                                    src=product["image"],
                                    width=150,
                                    height=150,
                                    fit=ft.ImageFit.CONTAIN,
                                ),
                                    ft.Text(product["name"], size=16, weight="bold"),
                                    ft.Text(f"Цена: {product['price']}", size=14),
                                    ft.Text(f'B наличии: {product['stock']}', size=14),
                                    ft.ElevatedButton(
                                        "Купить",
                                        on_click=lambda e, pn=product["name"]: buy_button_click(e, pn),
                                        color="white",
                                        bgcolor="#6200ea",
                                        width=120,
                                        height=40,
                                    ),
                                ],
                                spacing=8,
                                alignment="center",
                                horizontal_alignment="center",
                            ),
                            padding=10,
                            width=150,
                        ),
                        color="#2e2e2e",
                        elevation=5,
                    )
                    product_cards.append(card)

                    products_grid = ft.GridView(
                        product_cards,
                        runs_count=3,
                        spacing=15,
                        run_spacing=15,
                        expand=True,
                    )
                page.add(
                    ft.Row(
                        [user_button, add_product_button],
                        alignment="spaceBetween",
                    ),
                    ft.Column(
                        [ft.Text("Наши товары", size=24, weight="bold", text_align="center")],
                        alignment="center",
                    ),
                    products_grid,
                )


            def go_to_add(e):
                page.clean()
                page.add(add_product_page)
            
            product_name_field = ft.TextField(label="Название товара", autofocus=True)
            product_price_field = ft.TextField(label="Цена", keyboard_type="number")
            product_image_field = ft.TextField(label="Ссылка на изображение")
            product_stock_quantity = ft.TextField(label='Количество товара')
            
            add_product_page = ft.Column(
                        [
                            ft.Text("Добавить товар", size=24, weight="bold", text_align="center"),
                            product_name_field,
                            product_price_field,
                            product_image_field,
                            product_stock_quantity,
                            ft.ElevatedButton(
                                "Добавить товар",
                                on_click=add_product,
                                color="white",
                                bgcolor="#6200ea",
                            ),
                            ft.ElevatedButton(
                                "На главную",
                                on_click=go_to_main_page,
                                color="white",
                                bgcolor="#6200ea",
                            ),
                        ],
                        spacing=20,
                        alignment="center",
            )

            user_button = ft.IconButton(
                icon=ft.icons.PERSON,
                on_click=user_button_click,
                bgcolor="#6200ea",
                width=50,
                height=50,
                tooltip="Профиль",
            )

            products = gp.get_product()

            product_cards = []
            for product in products:
                card = ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.Image(
                                src=product["image"],
                                width=150,
                                height=150,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                                ft.Text(product["name"], size=16, weight="bold"),
                                ft.Text(f"Цена: {product['price']} рублей", size=14),
                                ft.Text(f'B наличии: {product['stock']}', size=14),
                                ft.ElevatedButton(
                                    "Купить",
                                    on_click=lambda e, pn=product["name"]: buy_button_click(e, pn),
                                    color="white",
                                    bgcolor="#6200ea",
                                    width=120,
                                    height=40,
                                ),
                            ],
                            spacing=8,
                            alignment="center",
                            horizontal_alignment="center",
                        ),
                        padding=10,
                        width=150,
                    ),
                    color="#2e2e2e",
                    elevation=5,
                )
                product_cards.append(card)

                products_grid = ft.GridView(
                    product_cards,
                    runs_count=3,
                    spacing=15,
                    run_spacing=15,
                    expand=True,
                )

            add_product_button = ft.ElevatedButton(
                "Добавить товар",
                icon=ft.icons.ADD,
                color="white",
                bgcolor="#6200ea",
                on_click=go_to_add
            )

            text_block = ft.Text(
                "Добро пожаловать!",
                size=24,
                weight="bold",
                text_align="center",
            )

            center_container = ft.Container(
                content=text_block,
                alignment=ft.alignment.center,
                expand=True,
            )

            a = ft.Row([user_button],alignment="end",)

            page.add(
                a,
                center_container,
            )
            

            time.sleep(2)

            if success[4] == "No":

                page.title = "Shop"
                page.remove(a, center_container)
                page.add(
                    ft.Row(
                        [user_button],
                        alignment="end",
                    ),
                    ft.Column(
                        [ft.Text("Наши товары", size=24, weight="bold", text_align="center")],
                        alignment="center",
                    ),
                    products_grid,
                )

            elif success[4] == "Yes":
                page.title = "Shop"
                page.remove(a, center_container)
                page.add(
                    ft.Row(
                        [user_button, add_product_button],
                        alignment="spaceBetween",
                    ),
                    ft.Column(
                        [ft.Text("Наши товары", size=24, weight="bold", text_align="center")],
                        alignment="center",
                    ),
                    products_grid,
                )
            return
        return

    def registers(e):
        reg_new = rg.register(Login.value, Email.value, Pass.value, "No", Photo.value)
        if reg_new == 0:
            a = ft.Text("Login is currently used")
            page.add(a)
            time.sleep(5)
            page.remove(a)
            return
        

    ic = ft.IconButton(icon=ft.Icons.ARROW_BACK, icon_color=ft.colors.AMBER, icon_size=32, on_click=back_to_log)
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.GREY_900
    page.theme_mode = "dark"

    Login = ft.TextField(
        width=300,
        height=50,
        label="Введите логин",
        label_style=ft.TextStyle(color=ft.colors.GREY_400, size=14),
        border_color=ft.colors.GREY_700,
        focused_border_color=ft.colors.BLUE_400,
        cursor_color=ft.colors.BLUE_400,
        text_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
        border_radius=8,
        filled=True,
        fill_color=ft.colors.GREY_800,
        content_padding=ft.padding.symmetric(horizontal=16, vertical=12),
        prefix_icon=ft.Icon(name=ft.Icons.PERSON, color=ft.colors.AMBER, size=32),
        prefix_style=ft.TextStyle(color=ft.colors.GREY_400),
    )

    Email = ft.TextField(
        width=300,
        height=50,
        label="Введите почту",
        label_style=ft.TextStyle(color=ft.colors.GREY_400, size=14),
        border_color=ft.colors.GREY_700,
        focused_border_color=ft.colors.BLUE_400,
        cursor_color=ft.colors.BLUE_400,
        text_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
        border_radius=8,
        filled=True,
        fill_color=ft.colors.GREY_800,
        content_padding=ft.padding.symmetric(horizontal=16, vertical=12),
        prefix_icon=ft.Icon(name=ft.Icons.EMAIL, color=ft.colors.AMBER, size=32),
        prefix_style=ft.TextStyle(color=ft.colors.GREY_400),
    )

    Pass = ft.TextField(
        width=300,
        height=50,
        label="Введите пароль",
        label_style=ft.TextStyle(color=ft.colors.GREY_400, size=14),
        border_color=ft.colors.GREY_700,
        focused_border_color=ft.colors.BLUE_400,
        cursor_color=ft.colors.BLUE_400,
        text_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
        border_radius=8,
        filled=True,
        fill_color=ft.colors.GREY_800,
        content_padding=ft.padding.symmetric(horizontal=16, vertical=12),
        prefix_icon=ft.Icon(name=ft.Icons.LOCK, color=ft.colors.AMBER, size=32),
        prefix_style=ft.TextStyle(color=ft.colors.GREY_400),
        password=True, 
        can_reveal_password=True
    )

    Photo = ft.TextField(
        width=300,
        height=50,
        label="Введите ссылку на изображение профиля",
        label_style=ft.TextStyle(color=ft.colors.GREY_400, size=14),
        border_color=ft.colors.GREY_700,
        focused_border_color=ft.colors.BLUE_400,
        cursor_color=ft.colors.BLUE_400,
        text_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
        border_radius=8,
        filled=True,
        fill_color=ft.colors.GREY_800,
        content_padding=ft.padding.symmetric(horizontal=16, vertical=12),
        prefix_icon=ft.Icon(name=ft.Icons.ADD_A_PHOTO, color=ft.colors.AMBER, size=32),
        prefix_style=ft.TextStyle(color=ft.colors.GREY_400),
    )

    log = ft.Row(
            [
                ft.Column(
                [
                    Login,
                    Pass,
                    SuccessBtn(text="Войти", on_click=login),
                    SuccessBtn("Зарегистрироваться", on_click=registerBox)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
    
    reg = ft.Row(
            [
                ft.Column(
                [
                    Login,
                    Email,
                    Pass,
                    Photo,
                    SuccessBtn(text="Зарегистрироваться", on_click=registers)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

    page.add(
        log
    )


ft.app(main)