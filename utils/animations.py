import flet as ft


def open_close_sidebar(page, sidebar):
    sidebar.width = 60 if sidebar.width == 300 else 300
    sidebar.content.controls[0].icon = ft.icons.MENU_OPEN if sidebar.width == 300 else ft.icons.MENU

    # if sidebar.width == 60:
    #     sidebar.content.controls[1].visible = False
    # else:
    #     sidebar.content.controls[1].visible = True
        
    sidebar.update()