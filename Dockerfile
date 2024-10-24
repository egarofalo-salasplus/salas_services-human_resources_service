# Dockerfile para desplegar una aplicación Django en Azure App Service

# Utilizar una imagen base de Python (versión 3.12.5)
FROM python:3.12.5-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Instalar dependencias del sistema necesarias para pyodbc y ODBC
RUN apt-get update && apt-get install -y \
    gcc \
    unixodbc \
    unixodbc-dev \
    curl \
    gnupg \
    apt-transport-https \
    wget \
    && wget https://packages.microsoft.com/keys/microsoft.asc -O microsoft.asc \
    && apt-key add microsoft.asc \
    && wget https://packages.microsoft.com/config/debian/10/prod.list -O /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && rm -rf /var/lib/apt/lists/*

# Copiar el archivo de dependencias
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Copiar el script de inicio y darle permisos de ejecución
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Establecer las variables de entorno necesarias para Django
ENV DJANGO_SETTINGS_MODULE=human_resources_service.settings
ENV PYTHONUNBUFFERED=1
ENV DB_NAME="PersonasDB"
ENV DB_USER="ad"
ENV DB_HOST="salas-dw.database.windows.net"

# Exponer el puerto que utilizará Django
EXPOSE 8000

# Establecer el script de inicio como el entrypoint del contenedor
ENTRYPOINT ["/entrypoint.sh"]