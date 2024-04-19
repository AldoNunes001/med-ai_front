import requests
from views.home import home_view


def make_login(username, password):
    user = requests.post("http://127.0.0.1:8000/api/teste",
                         json={"username": username, "password": password}).json()

    return user


def validate_data(page, username, password, error_message):
    # nome_textfield = nome.controls[1]
    print("teste")
    # username_textfield = username.content.controls[0]
    username_textfield = username.content
    password_textfield = password.content
    
    username_value = username_textfield.value
    password_value = password_textfield.value
    
    username_error = ""
    password_error = ""
    
    if not username_textfield.value:
        username_error = "Por favor, digite o username."
    
    if not password_textfield.value:
        password_error = "Por favor, digite o password."
    
    username_textfield.error_text = username_error
    password_textfield.error_text = password_error
    
    username_textfield.update()
    password_textfield.update()

    if username_error or password_error:
        return

    print(username_value, password_value)
    user = make_login(username_value, password_value)

    if user.get("is_authenticated"):
        print("Usuário autenticado")
        home_view(page)  # Chamar a home_view diretamente se autenticado
    else:
        error_message.value = "Usuário ou senha inválidos."
        error_message.visible = True
        page.update()
        print("Falha na autenticação do usuário")

        
        
        
