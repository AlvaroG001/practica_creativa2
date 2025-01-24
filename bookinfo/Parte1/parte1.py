import os
import subprocess

def install_dependencies():
    print("Actualizando los paquetes y asegurando que pip esté instalado...")
    os.system("sudo apt-get update -y")
    os.system("sudo apt-get install -y python3-pip")

    print("Instalando las dependencias desde requirements.txt...")
    os.system("pip3 install -r /home/lunadavid3012/requirements.txt")

def modify_templates(group_number):
    print("Modificando los títulos de las plantillas con el número de grupo...")
    templates_path = "/home/lunadavid3012/practica_creativa2/bookinfo/src/productpage/templates"
    files_to_modify = ["index.html", "productpage.html"]

    for file_name in files_to_modify:
        full_path = os.path.join(templates_path, file_name)
        with open(full_path, "r") as fin:
            content = fin.read()

        updated_content = content.replace(
            "{% block title %}Simple Bookstore App{% endblock %}",
            f"{{% block title %}}Simple Bookstore App {group_number}{{% endblock %}}"
        )

        with open(full_path, "w") as fout:
            fout.write(updated_content)

    print("Modificaciones completadas.")

def start_application(port):
    print(f"Arrancando la aplicación en el puerto {port}...")
    app_path = "/home/lunadavid3012/practica_creativa2/bookinfo/src/productpage"
    os.chdir(app_path)
    subprocess.Popen(["python3", "productpage_monolith.py", str(port)])

def main():
    # Configuración inicial
    group_number = os.getenv("GROUP_NUMBER", "Default_Group")
    port = 9080  # Cambiar por el puerto deseado

    # Paso 1: Clonar el repositorio
    print("Clonando el repositorio...")
    os.system("git clone https://github.com/carlossalval99/practica_creativa2.git /home/lunadavid3012/practica_creativa2")

    # Paso 2: Instalar dependencias
    install_dependencies()

    # Paso 3: Modificar las plantillas
    modify_templates(group_number)

    # Paso 4: Iniciar la aplicación
    start_application(port)

    print("La aplicación debería estar disponible ahora en la IP pública de la máquina virtual.")

if __name__ == "__main__":
    main()
