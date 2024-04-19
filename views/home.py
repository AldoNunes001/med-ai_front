import flet as ft


def home_view(page: ft.Page):
    # page.window_always_on_top = True
    page.controls.clear()
    
    def open_close_side_bar(e):
        side_bar.width = 45 if side_bar.width == 200 else 200
        side_bar.update()
    
    side_bar = ft.Container(
        content=ft.Column(
            controls=[
                ft.IconButton(
                    icon=ft.icons.MENU_OPEN,
                    icon_color=ft.colors.WHITE,
                    icon_size=24,
                    on_click=open_close_side_bar,
                ),
                ft.Text("sidebar"),
            ],
        ),
        bgcolor=ft.colors.PINK,
        width=200,
        padding=ft.padding.only(top=10, left=0),
        visible=True,
        animate=ft.animation.Animation(100, ft.AnimationCurve.EASE),
    )
    
    layout = ft.Container(
        content=ft.Row(
            controls=[
                side_bar,
                ft.Container(
                    bgcolor=ft.colors.AMBER,
                    expand=True,
                )
            ],
            spacing=0,
        ),
        bgcolor=ft.colors.WHITE,
        expand=True,
    )

    page.add(layout)
