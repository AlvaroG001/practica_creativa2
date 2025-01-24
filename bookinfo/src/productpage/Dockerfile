FROM python:3.9-slim

WORKDIR /usr/src/app

# Copia el proyecto completo al contenedor
COPY practica_creativa2 /usr/src/app/practica_creativa2

# Instala las dependencias desde requirements.txt
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libffi-dev \
    libssl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install --upgrade pip
RUN pip3 install -r /usr/src/app/practica_creativa2/bookinfo/src/productpage/requirements.txt

# Expone el puerto 9080
EXPOSE 9080

# Comando para ejecutar la aplicación
CMD ["python3", "/usr/src/app/practica_creativa2/bookinfo/src/productpage/productpage.py", "9080"]
