import flet as ft
import back.get_product as gp

def pdd():
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
    return products_grid