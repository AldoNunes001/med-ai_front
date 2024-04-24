import requests


def get_patient_data(page, menu_sidebar, tf_search_cpf, tf_patient_name, tf_patient_cpf, error_msg_search, patient_info):
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
