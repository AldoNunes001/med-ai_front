import flet as ft
from views.login import login_view


def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # page.window_width = 1600
    # page.window_height = 1000
    page.window_center()
    # page.window_min_height = 1200
    # page.window_min_width = 1800
    # page.window_full_screen = True
    page.title = "Med-AI"

    page.update()

    login_view(page)


if __name__ == "__main__":
    ft.app(target=main)