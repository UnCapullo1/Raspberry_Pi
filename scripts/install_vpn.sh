#!/bin/bash

GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}=== Instalador de VPN (WireGuard via PiVPN) ===${NC}"
echo "Este script lanzará el instalador oficial de PiVPN."
echo "IMPORTANTE: Durante la instalación, elige 'WireGuard' cuando te pregunte el protocolo."
echo "Después de instalar, usa el comando 'pivpn add' para crear un nuevo perfil para tu móvil/PC."
echo ""
read -p "Presiona Enter para continuar..."

curl -L https://install.pivpn.io | bash

echo -e "${GREEN}=== Instalación Finalizada ===${NC}"
echo "Para conectar un dispositivo:"
echo "1. Ejecuta: pivpn add"
echo "2. Ponle un nombre (ej: movil-juan)"
echo "3. Ejecuta: pivpn -qr"
echo "4. Escanea el código con la app WireGuard en tu móvil."
