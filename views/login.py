import flet as ft
import requests
from utils.login import make_login, validate_data


# def make_login(username, password):
#     user = requests.post("http://127.0.0.1:8000/api/teste",
#                          json={"username": username, "password": password}).json()

#     if user["is_authenticated"] is False:
#         print("Usuário não autenticado")
#     else:
#         print("Usuário autenticado")
        
#     return user


def login_view(page: ft.Page):
    page.controls.clear()
    # GREEN = ft.colors.GREEN_500
    # page.theme = ft.Theme(
        
    # def validate_data(e):
    #     # nome_textfield = nome.controls[1]
    #     print("teste")
    #     # username_textfield = username.content.controls[0]
    #     username_textfield = username.content
    #     password_textfield = password.content
        
    #     username_value = username_textfield.value
    #     password_value = password_textfield.value
        
    #     flag = False
    #     if not username_value:
    #         # page.show_dialog("Por favor, digite seu nome.")
    #         username_textfield.error_text = "Por favor, digite o username."
    #         username_textfield.update()
    #         # print("Por favor, digite seu nome.")
    #         flag = True
    #     else:
    #         username_textfield.error_text = ""
    #         username_textfield.update()
        
    #     if not password_value:
    #         password_textfield.error_text = "Por favor, digite o password."
    #         password_textfield.update()
    #         # page.show_dialog("Por favor, escolha um gênero.")
    #         flag = True
    #     else:
    #         password_textfield.error_text = ""
    #         password_textfield.update()

    #     if flag:
    #         return
        
    #     user = make_login(username_value, password_value)
        
        # page.go("/sobre") 

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
        
    # def refresh(e):
    #     # border_color=ft.colors.BLUE,
    #     username.content.error_text = ""
    #     page.update()
    ######  USERNAME  ######
    username = ft.Container(
        content=ft.TextField(
                    # value="Username",
                    label="Username",
                    # height=44,
                    dense=True,
                    # label="Email",
                    # hint_text="Digite seu nome...",
                    # filled=True,
                    # bgcolor=GREEN,
                    border_radius=10,
                    # border_color=GREEN,
                    # focused_border_color=ft.colors.YELLOW,
                    focused_border_width=2,
                    color=ft.colors.BLACK,
                    border_color=ft.colors.BLUE,
                    label_style=ft.TextStyle(color=ft.colors.BLACK26),
                    # focused_color=ft.colors.BLUE,
                    # hint_text="hint_text",
                    # selection_color=ft.colors.PINK,
                    # bgcolor=ft.colors.GREY_200,
                    # key="nome",
                    # focused_color=ft.colors.BLACK,
                    # hint_style=ft.TextStyle(color=ft.colors.GREY_500),
                    # on_focus=refresh,
                    # keyboard_type=ft.KeyboardType.EMAIL,
                )
    )
    
            
        
    ######  PASSWORD  ######
    password = ft.Container(
        content=ft.TextField(
                    # value="Password",
                    label="Password",
                    # height=44,
                    password=True,
                    can_reveal_password=True,
                    # keyboard_type=ft.KeyboardType.PASSWORD,
                    dense=True,
                    # label="Email",
                    # hint_text="Digite seu nome...",
                    # filled=True,
                    # bgcolor=GREEN,
                    border_radius=10,
                    # border_color=GREEN,
                    # focused_border_color=ft.colors.YELLOW,
                    focused_border_width=2,
                    color=ft.colors.BLACK,
                    border_color=ft.colors.BLUE,
                    label_style=ft.TextStyle(color=ft.colors.BLACK26),
                    # key="nome",
                    # focused_color=ft.colors.BLACK,
                    # hint_style=ft.TextStyle(color=ft.colors.GREY_500),
                    # keyboard_type=ft.KeyboardType.EMAIL,
                )
    )

    error_message = ft.Text("", color=ft.colors.RED, visible=False, text_align="center")

########  VALIDATE DATA  ########
    login_btn = ft.Container(
        ft.ElevatedButton(
            # text="Login",
            content=ft.Text(
                "Login",
                size=20,
            ),
            # bgcolor=GREEN,
            # color=ft.colors.WHITE,
            height=47,
            width=316,
            # style=ft.ButtonStyle(
            #     shape=ft.RoundedRectangleBorder(radius=10),
            # ),
            # on_click=lambda _: page.go("/sobre")
            on_click=lambda e: validate_data(page, username, password, error_message),
            # on_click=teste,
        ),
        margin=ft.margin.only(top=20),
        # height=47,
        # width=316,
        # margin=ft.margin.only(top=245),
        # padding=30,
        # border_radius=10,
        # bgcolor=GREEN,
        # alignment=ft.alignment.center,
        # on_hover=hover_button,
        # on_click=teste,
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
            # expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            
        ),
        bgcolor=ft.colors.GREY_300,
        expand=True,
        alignment=ft.alignment.center,
        padding=ft.padding.only(bottom=20),
    )

    page.add(layout)
    # return layout
    