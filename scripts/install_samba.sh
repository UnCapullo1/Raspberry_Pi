#!/bin/bash

# Colores para output
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== Iniciando instalación de Servidor Samba ===${NC}"

# 1. Actualizar el sistema
echo "Actualizando lista de paquetes..."
sudo apt-get update
# Opcional: sudo apt-get upgrade -y (comentado para ahorrar tiempo, descomentar si se desea)

# 2. Instalar Samba y utilidades de sistema de archivos (NTFS)
echo -e "${GREEN}Instalando Samba y soporte NTFS (ntfs-3g)...${NC}"
sudo apt-get install -y samba samba-common-bin ntfs-3g

# 3. Crear directorio base si no existe
NAS_ROOT="/srv/nas"
if [ ! -d "$NAS_ROOT" ]; then
    echo "Creando directorio base en $NAS_ROOT..."
    sudo mkdir -p "$NAS_ROOT"
    sudo chown -R pi:pi "$NAS_ROOT" 2>/dev/null || sudo chown -R $USER:$USER "$NAS_ROOT"
    sudo chmod 755 "$NAS_ROOT"
fi

# 4. Configuración de usuario Samba
echo -e "${GREEN}Configuración de Usuario Samba${NC}"
echo "Se usará el usuario actual ($USER) para el acceso Samba."
echo "Por favor, introduce una contraseña para el acceso a la red (puede ser diferente a la del sistema):"
sudo smbpasswd -a $USER

echo -e "${GREEN}=== Instalación base completada ===${NC}"
echo "Siguiente paso: Ejecuta './scripts/mount_usb.sh' para configurar tus discos."
