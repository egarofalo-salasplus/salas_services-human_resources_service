# Dockerfile para desplegar una aplicación Django en Azure App Service

# Usa una imagen oficial de Python 3.12 basada en Debian Bullseye
FROM python:3.12-slim-bullseye

# Configura variables de entorno para evitar prompts interactivos
ENV ACCEPT_EULA=Y DEBIAN_FRONTEND=noninteractive

# Instala las dependencias necesarias
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    unixodbc \
    unixodbc-dev \
    gnupg \
    apt-transport-https \
    ca-certificates \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Agrega la clave y el repositorio de Microsoft para Debian 11 (Bullseye)
RUN curl -sSL https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl -sSL https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Instala el controlador ODBC 17 para SQL Server
RUN apt-get update && apt-get install -y \
    msodbcsql17 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de dependencias
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Copiar el script de inicio y darle permisos de ejecución
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Exponer el puerto que utilizará Django
EXPOSE 8000

# Establecer el script de inicio como el entrypoint del contenedor
ENTRYPOINT ["/entrypoint.sh"]