import requests
import flet as ft


def list_patients(page, list_patients_info, patient_info, error_msg_search):
    token = page.client_storage.get("access_token")
    headers = {"Authorization": f"Bearer {token}"}
    url = f"http://127.0.0.1:8000/api/patients/"
    
    try:
        patients = requests.get(url, headers=headers).json()
        # print(patients)
        # list_patients_info.content.append = ft.Row()
        list_patients_info.content.controls.clear()
        for patient in patients:
            # print(patient)
            list_patients_info.content.controls.append(ft.Row(
                controls=[ft.Text(value=f'CPF: {patient["cpf"]} | NOME: {patient["name"]}', color="black")])
            )
            # print(list_patients_info.content.controls)
        
        # print(list_patients_info.content.controls[0].controls[0])
        # print(list_patients_info.content.controls[1].value)
        # print(list_patients_info.content.controls[2].value)
        # print(list_patients_info.content.controls[3].value)
        list_patients_info.visible = True
        patient_info.visible = False
        error_msg_search.value = ""
        page.update()
        
    except:
        # menu_sidebar.content.controls[2].controls[1].value = "     Erro ao pegar pacientes"
        # page.update()
        print("Erro ao pegar pacientes")


def get_patient_data(page, menu_sidebar, tf_search_cpf, tf_patient_name, tf_patient_cpf, error_msg_search, patient_info, list_patients_info):
    # cpf = menu_sidebar.content.controls[1].controls[1].value
    cpf = tf_search_cpf.value

    # temp = page.get_control("layout")
    # print(temp)

    token = page.client_storage.get("access_token")
    # print(token)
    headers = {"Authorization": f"Bearer {token}"}
    # print(headers)
    url = f"http://127.0.0.1:8000/api/patients/{cpf}"
    
    # print(patient_data)

    # page.controls[0].content.controls[1].content.controls[2].content.controls[1].value = patient_data["name"]
    try:
        patient_data = requests.get(url, headers=headers).json()
        # page.controls[0].content.controls[1].content.controls[2].content.controls[0].controls[1].value = patient_data["name"]
        # page.controls[0].content.controls[1].content.controls[2].content.controls[0].controls[3].value = patient_data["cpf"]
        # menu_sidebar.content.controls[2].controls[1].visible = False
        tf_patient_name.value = patient_data["name"]
        tf_patient_cpf.value = patient_data["cpf"]
        error_msg_search.value = ""
        patient_info.visible = True
        list_patients_info.visible = False
        page.update()
    except:
        # print("Problema em pegar paciente")
        # menu_sidebar.content.controls[2].controls[1].visible = True
        menu_sidebar.content.controls[2].controls[1].value = "     Paciente não encontrado"
        error_msg_search.value = "     Paciente não encontrado"
        patient_info.visible = False
        page.update()
    # page.controls[0].content.controls[1].content.controls[2].content.controls[3].value = patient_data["cpf"]
    # return user


def add_patient(page, tf_patient_name, tf_patient_cpf, error_msg_search, patient_info, list_patients_info):

    tf_patient_name.value = ""
    tf_patient_cpf.value = ""
    error_msg_search.value = ""
    patient_info.visible = True
    list_patients_info.visible = False
    page.update()
    

def save_patient(page, patient_name, patient_cpf):

    username = page.client_storage.get("username")
    token = page.client_storage.get("access_token")
    headers = {"Authorization": f"Bearer {token}"}
    url = f"http://127.0.0.1:8000/api/patients/"
    
    patient = requests.post(url, headers=headers,
                            json={"name": patient_name, "cpf": patient_cpf, "username": username}).json()
    
    return patient


def close_dlg(page, dlg):
    dlg.open = False
    page.update()
        

def validate_data_patient(page, tf_patient_name, tf_patient_cpf):
    
    name_error = ""
    cpf_error = ""
    
    if not tf_patient_name.value:
        name_error = "Por favor, digite o nome do paciente."
    
    if not tf_patient_cpf.value:
        cpf_error = "Por favor, digite o CPF do paciente."
    
    tf_patient_name.error_text = name_error
    tf_patient_cpf.error_text = cpf_error
    
    tf_patient_name.update()
    tf_patient_cpf.update()

    if name_error or cpf_error:
        return

    patient = save_patient(page, tf_patient_name.value, tf_patient_cpf.value)

    if patient is not None:
        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Paciente salvo com sucesso."),
            actions=[
                ft.TextButton("Ok", on_click=lambda e: close_dlg(page, dlg))
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER,
        )
        page.dialog = dlg
        dlg.open = True
        page.update()
        # print("Paciente salvo com sucesso.")
    else:
        dlg = ft.AlertDialog(
            title=ft.Text("Paciente salvo com sucesso."), on_dismiss=lambda e: print("Dialog dismissed!")
        )
        page.dialog = dlg
        dlg.open = True
        page.update()
        # print("Problema ao salvar paciente.")
        # page.update()