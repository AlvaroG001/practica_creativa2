
FROM python:3.7.7-slim



WORKDIR /usr/src/app

COPY docker2.py ./


# Actualizar el índice de paquetes
RUN apt-get update

# Instalar build-essential
RUN apt-get install -y build-essential

# Instalar gcc
RUN apt-get install -y gcc

# Instalar git
RUN apt-get install -y git

RUN pip install --upgrade pip





EXPOSE 9080:9080

ENTRYPOINT python3 docker2.py 
