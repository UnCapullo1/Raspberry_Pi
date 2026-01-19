#!/bin/bash

GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}=== Configuración de Carpeta Compartida (Samba) ===${NC}"

echo "Introduce la ruta absoluta de la carpeta a compartir (ejemplo: /srv/nas/disco1):"
read SHARE_PATH

if [ ! -d "$SHARE_PATH" ]; then
    echo "Error: La carpeta $SHARE_PATH no existe."
    exit 1
fi

echo "Introduce el nombre que se verá en la red (ejemplo: Peliculas):"
read SHARE_NAME

CONF_FILE="/etc/samba/smb.conf"

# Backup
sudo cp "$CONF_FILE" "$CONF_FILE.bak.$(date +%Y%m%d%H%M%S)"

# Añadir configuración bloque al final
echo -e "\n[$SHARE_NAME]" | sudo tee -a "$CONF_FILE"
echo "path = $SHARE_PATH" | sudo tee -a "$CONF_FILE"
echo "writeable = yes" | sudo tee -a "$CONF_FILE"
echo "create mask = 0775" | sudo tee -a "$CONF_FILE"
echo "directory mask = 0775" | sudo tee -a "$CONF_FILE"
echo "public = no" | sudo tee -a "$CONF_FILE"

echo -e "${GREEN}Configuración añadida. Reiniciando servicio Samba...${NC}"
sudo systemctl restart smbd

echo "Carpeta '$SHARE_NAME' compartida con éxito."
