import subprocess

# Lista das bibliotecas a serem desinstaladas
libs_to_uninstall = ["webdriver_manager", "webdrivermanager", "webdriver_manager.chrome"]

# Desinstalando as bibliotecas
for lib in libs_to_uninstall:
    subprocess.run(["pip", "uninstall", "-y", lib])

# Instalando a versão correta do webdriver_manager
subprocess.run(["pip", "install", "webdriver_manager"])

print("webdriver_manager instalado com sucesso!")
