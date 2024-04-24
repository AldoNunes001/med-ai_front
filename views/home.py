import flet as ft
from utils.animations import open_close_sidebar
from utils.patient import get_patient_data, list_patients

# BLUE = "#B6CCFE"


def home_view(page: ft.Page):
    # page.window_always_on_top = True
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

    page.controls.clear()
    
    # def open_close_side_bar(e):
    #     side_bar.width = 60 if side_bar.width == 300 else 300
    #     side_bar.content.controls[0].icon = ft.icons.MENU_OPEN if side_bar.width == 300 else ft.icons.MENU

    #     if side_bar.width == 60:
    #         side_bar.content.controls[1].visible = False
    #     else:
    #         side_bar.content.controls[1].visible = True
            
    #     side_bar.update()

    patient_info = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                       ft.Text("Nome: ", size=20, color=ft.colors.BLUE, weight=ft.FontWeight.W_600), 
                       tf_patient_name := ft.TextField(
                           bgcolor=ft.colors.WHITE,
                           border_radius=50,
                           border_color=ft.colors.WHITE,
                           focused_border_color=ft.colors.BLUE,
                           height=40,
                           width=500,
                           text_size=16,
                           color=ft.colors.BLACK,
                           text_vertical_align=ft.VerticalAlignment.START,
                        #    col=8,
                       ),
                       ft.Text("            CPF: ", size=20, color=ft.colors.BLUE, weight=ft.FontWeight.W_600), 
                       tf_patient_cpf := ft.TextField(
                           bgcolor=ft.colors.WHITE,
                           border_radius=50,
                           border_color=ft.colors.WHITE,
                           focused_border_color=ft.colors.BLUE,
                           height=40,
                           width=200,
                           text_size=16,
                           color=ft.colors.BLACK,
                           text_vertical_align=ft.VerticalAlignment.START,
                        #    col=3
                       ),
                    #    ft.Text("            Sexo: ", size=20, color=ft.colors.BLUE, weight=ft.FontWeight.W_600), 
                    #    ft.TextField(
                    #        bgcolor=ft.colors.WHITE,
                    #        border_radius=50,
                    #        border_color=ft.colors.WHITE,
                    #        focused_border_color=ft.colors.BLUE,
                    #        height=40,
                    #        width=70,
                    #        text_size=16,
                    #        color=ft.colors.BLACK,
                    #        text_vertical_align=ft.VerticalAlignment.START,
                    #     #    col=3
                    #    ),
                    ],
                    wrap=True,
                )
            ],
        ),
        margin=40,
        visible=False,
    )

    
    list_patients_info = ft.Container(
        content=ft.Column(),
    )
    
    
    
    menu_sidebar = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(name=ft.icons.SEARCH, color=ft.colors.GREY_600, size=24),
                        ft.Text("    Digite o CPF do paciente"),
                    ],
                    spacing=20,
                    # vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        # ft.Icon(name=ft.icons.SEARCH, color=ft.colors.WHITE, size=24),
                        tf_search_cpf := ft.TextField(
                            keyboard_type=ft.KeyboardType.NUMBER,
                            bgcolor=ft.colors.WHITE54,
                            # border=ft.InputBorder.NONE,
                            border_color=ft.colors.GREY_600,
                            border_radius=50,
                            height=55,
                            focused_border_width=1,
                            focused_border_color=ft.colors.BLUE,
                            width=250,
                            text_size=14,
                            text_vertical_align=ft.VerticalAlignment.START,
                            text_align=ft.TextAlign.CENTER,
                            input_filter=ft.NumbersOnlyInputFilter(),
                            max_length=11,
                            icon=ft.icons.SEARCH,
                            ),
                    ],
                    spacing=20,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    # alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        ft.Icon(name=ft.icons.SEARCH, color=ft.colors.GREY_600, size=24),
                        # ft.Text("    Digite o CPF do paciente"),
                        # ft.Text("     Paciente não encontrado", color=ft.colors.RED, visible=False, text_align="center")
                        error_msg_search := ft.Text("", color=ft.colors.RED, text_align="center")
                    ],
                    spacing=20,
                    # vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Container(
                    ft.Row(
                        controls=[
                            # ft.Icon(name=ft.icons.SEARCH, color=ft.colors.GREY_600, size=6),
                            ft.ElevatedButton(
                                text="Buscar",
                                on_click=lambda e: get_patient_data(
                                    page,
                                    menu_sidebar=menu_sidebar,
                                    tf_search_cpf=tf_search_cpf,
                                    tf_patient_name=tf_patient_name,
                                    tf_patient_cpf=tf_patient_cpf,
                                    error_msg_search=error_msg_search,
                                    patient_info=patient_info,
                                    list_patients_info=list_patients_info,
                                    ),
                                ),
                        ],
                        spacing=20,
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=ft.padding.only(left=24),
                    margin=ft.margin.only(top=10),
                ),
                ft.Container(
                    ft.Row(
                        controls=[
                            # ft.Icon(name=ft.icons.ALL_OUT_ROUNDED, color=ft.colors.GREY_300, size=24),
                            # ft.Text("   "),
                            ft.ElevatedButton(
                                # text="Listar Pacientes",
                                content=ft.Text("Listar Pacientes", color=ft.colors.BLUE, size=16, weight=ft.FontWeight.W_600),
                                on_click=lambda e: list_patients(
                                    page,
                                    list_patients_info=list_patients_info,
                                    patient_info=patient_info,
                                    ),
                                style=ft.ButtonStyle(
                                    bgcolor=ft.colors.GREY_300,
                                    
                                    ),
                                ),
                        ],
                        spacing=20,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    margin=ft.margin.only(top=45, left=10),
                    # bgcolor=ft.colors.PINK,
                ),
            ],
            spacing=0,
        ),
        padding=10,
        margin=ft.margin.only(top=50),
    )
    
    sidebar = ft.Container(
        content=ft.Column(
            controls=[
                ft.IconButton(
                    icon=ft.icons.MENU_OPEN,
                    icon_color=ft.colors.WHITE,
                    icon_size=24,
                    # on_click=open_close_side_bar,
                    on_click=lambda e: open_close_sidebar(page, sidebar),
                ),
                menu_sidebar,
            ],
        ),
        bgcolor=ft.colors.GREY_600,
        # bgcolor=BLUE,
        width=300,
        # padding=ft.padding.only(top=10, left=0),
        padding=10,
        visible=True,
        animate=ft.animation.Animation(100, ft.AnimationCurve.EASE),
    )
    
    
    principal = ft.Container(
        ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(name=ft.icons.LOCAL_HOSPITAL_ROUNDED, color=ft.colors.BLUE, size=40),
                        ft.Text("Med-AI", color=ft.colors.BLUE, size=40, weight=ft.FontWeight.W_900),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    # spacing=0,
                ),
                ft.Divider(color=ft.colors.BLUE, thickness=0.5, height=2),
                patient_info,
                list_patients_info,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=ft.colors.GREY_300,
        expand=True,
        alignment=ft.alignment.center,
        padding=ft.padding.only(top=20, left=20, bottom=20, right=30),
    )
    
    layout = ft.Container(
        content=ft.Row(
            controls=[
                sidebar,
                principal,
            ],
            spacing=0,
        ),
        bgcolor=ft.colors.WHITE,
        expand=True,
    )

    page.add(layout)


if __name__ == "__main__":
    ft.app(target=home_view)
