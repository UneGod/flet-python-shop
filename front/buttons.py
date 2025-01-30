import flet as ft


class SuccessBtn(ft.ElevatedButton):
    def __init__(self, text, on_click):
        super().__init__()
        self.bgcolor = ft.Colors.GREEN_800
        self.color = ft.Colors.WHITE
        self.text = text
        self.width = 200
        self.height = 40
        self.on_click = on_click