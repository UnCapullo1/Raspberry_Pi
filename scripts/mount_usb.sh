#!/bin/bash

GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${GREEN}=== Asistente de Montaje de Discos USB ===${NC}"

# Verificar si hay discos conectados (excluyendo la tarjeta SD mmcblk)
echo "Detectando discos..."
lsblk -o NAME,MODEL,SIZE,TYPE,FSTYPE | grep -v "mmcblk"

echo -e "${BLUE}Nota: sda, sdb, etc. son tus discos USB.${NC}"
echo "Por favor, introduce el nombre de la partición que quieres montar (ejemplo: sda1):"
read PARTITION

if [ ! -b "/dev/$PARTITION" ]; then
    echo "Error: La partición /dev/$PARTITION no existe."
    exit 1
fi

# Obtener UUID
UUID=$(blkid -o value -s UUID /dev/$PARTITION)
TYPE=$(blkid -o value -s TYPE /dev/$PARTITION)

if [ -z "$UUID" ]; then
    echo "Error: No se pudo obtener el UUID de $PARTITION."
    exit 1
fi

echo "Partición detectada: $PARTITION (Tipo: $TYPE, UUID: $UUID)"

# Preguntar punto de montaje
echo "Introduce el nombre para la carpeta de montaje (ejemplo: disco1):"
read MOUNT_NAME
MOUNT_POINT="/srv/nas/$MOUNT_NAME"

# Crear directorio
if [ ! -d "$MOUNT_POINT" ]; then
    echo "Creando directorio $MOUNT_POINT..."
    sudo mkdir -p "$MOUNT_POINT"
    # Permisos iniciales temporales para montar
    sudo chmod 777 "$MOUNT_POINT"
fi

# Hacer backup de fstab
sudo cp /etc/fstab /etc/fstab.bak.$(date +%Y%m%d%H%M%S)

# Añadir a fstab
echo -e "${GREEN}Configurando montaje automático...${NC}"

# Opciones de montaje según tipo de sistema de archivos
if [ "$TYPE" == "ntfs" ]; then
    FSTAB_ENTRY="UUID=$UUID $MOUNT_POINT ntfs-3g defaults,auto,users,rw,nofail,umask=000 0 0"
elif [ "$TYPE" == "ext4" ]; then
    FSTAB_ENTRY="UUID=$UUID $MOUNT_POINT ext4 defaults,auto,users,rw,nofail 0 0"
elif [ "$TYPE" == "vfat" ] || [ "$TYPE" == "exfat" ]; then
    FSTAB_ENTRY="UUID=$UUID $MOUNT_POINT $TYPE defaults,auto,users,rw,nofail,umask=000 0 0"
else
    FSTAB_ENTRY="UUID=$UUID $MOUNT_POINT auto defaults,auto,users,rw,nofail 0 0"
fi

# Verificar si ya existe en fstab
if grep -q "$UUID" /etc/fstab; then
    echo "Aviso: Este disco ya parece estar en /etc/fstab. No se añadirá duplicado."
else
    echo "$FSTAB_ENTRY" | sudo tee -a /etc/fstab
    echo "Entrada añadida a /etc/fstab."
fi

# Probar montaje
echo "Montando discos..."
sudo mount -a

if mount | grep -q "$MOUNT_POINT"; then
    echo -e "${GREEN}¡Éxito! El disco está montado en $MOUNT_POINT${NC}"
else
    echo "Advertencia: No se pudo verificar el montaje inmediato. Reinicia para comprobar."
fi
