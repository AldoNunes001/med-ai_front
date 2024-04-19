import flet as ft
from views.login import login_view


def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Med-AI"

    page.update()

    login_view(page)


if __name__ == "__main__":
    ft.app(target=main)