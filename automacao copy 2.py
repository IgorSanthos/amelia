from pywinauto import application

# Conecte-se ao aplicativo
app = application.Application().connect(title_re=".*Selecione a pasta.*")

# Acesse a janel
dialog = app.window(title_re=".*Selecione a pasta.*")

# Obtenha o endereço da pasta selecionada
path_element = dialog.child_window(title="FolderPath", control_type="Edit")
folder_path = path_element.get_value()

print("Caminho da pasta selecionada:", folder_path)
