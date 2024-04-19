import flet as ft
from views.home import home_view
from views.login import login_view
import requests


def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    user = requests.post("http://127.0.0.1:8000/api/teste",
                         json={"username": "", "password": ""}).json()
    
    if user["is_authenticated"] is False:
        # page.add(login_view)
        login_view(page)
    else:
        # page.add(home_view)
        home_view(page)

    page.update()

    def teste():
        print("teste")


if __name__ == "__main__":
    ft.app(target=main)