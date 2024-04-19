import flet as ft
from utils.login import validate_data


def login_view(page: ft.Page):
    page.controls.clear()

######  LOGIN  ######
    title = ft.Container(
        content=ft.Text(
            "LOGIN",
            size=24,
            color=ft.colors.BLUE,
            text_align="center",
            weight=ft.FontWeight.W_700,
        ),
        padding=ft.padding.only(bottom=20),
    )
        
######  USERNAME  ######
    username = ft.Container(
        content=ft.TextField(
                    label="Username",
                    dense=True,
                    border_radius=10,
                    focused_border_width=2,
                    color=ft.colors.BLACK,
                    border_color=ft.colors.BLUE,
                    label_style=ft.TextStyle(color=ft.colors.BLACK26),
                )
    )
    
######  PASSWORD  ######
    password = ft.Container(
        content=ft.TextField(
                    label="Password",
                    password=True,
                    can_reveal_password=True,
                    dense=True,
                    border_radius=10,
                    focused_border_width=2,
                    color=ft.colors.BLACK,
                    border_color=ft.colors.BLUE,
                    label_style=ft.TextStyle(color=ft.colors.BLACK26),
                )
    )

    error_message = ft.Text("", color=ft.colors.RED, visible=False, text_align="center")

########  BUTTON  ########
    login_btn = ft.Container(
        ft.ElevatedButton(
            content=ft.Text(
                "Login",
                size=20,
            ),
            height=47,
            width=316,
            on_click=lambda e: validate_data(page, username, password, error_message),
        ),
        margin=ft.margin.only(top=20),
    )
    
    layout = ft.Container(
        content=ft.ResponsiveRow(
            controls=[
                title,
                username,
                password,
                error_message,
                login_btn,
            ],
            spacing=0,
            width=300,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            
        ),
        bgcolor=ft.colors.GREY_300,
        expand=True,
        alignment=ft.alignment.center,
        padding=ft.padding.only(bottom=20),
    )

    page.add(layout)
    