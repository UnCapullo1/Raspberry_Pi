# Raspberry Pi NAS (Samba + WireGuard VPN)

Este proyecto contiene scripts y documentación para transformar tu Raspberry Pi en un **NAS (Network Attached Storage)** completo y seguro, accesible tanto desde tu red local como desde fuera de casa.

## 🚀 Características
- **Compartir Archivos (Samba)**: Accede a tus archivos desde Windows, macOS, Linux, Android y iOS.
- **Acceso Remoto (WireGuard)**: Conéctate a tu NAS desde cualquier lugar del mundo de forma segura.
- **Montaje Automático**: Scripts para detectar y montar tus discos duros USB automáticamente.

## 📋 Requisitos de Hardware
- **Raspberry Pi**: Modelo 4 o 5 recomendado (por los puertos USB 3.0 y velocidad Ethernet Gigabit). La Pi 3B+ también funciona pero será más lenta.
- **Tarjeta MicroSD**: Mínimo 16GB, Clase 10.
- **Almacenamiento**: Disco duro USB o SSD (recomendado para velocidad).
- **Fuente de Alimentación**: Oficial de Raspberry Pi para evitar problemas de energía con los discos.

## 🛠️ Instalación Rápida

1. **Clona este repositorio** en tu Raspberry Pi:
   ```bash
   git clone https://github.com/TU_USUARIO/Raspberry_Pi.git
   cd Raspberry_Pi
   ```
   *(Nota: Si la carpeta tiene otro nombre, entra en ella)*

2. **Dale permisos de ejecución a los scripts**:
   ```bash
   chmod +x scripts/*.sh
   ```

3. **Ejecuta los scripts en orden**:

   **Paso 1: Instalación Base (Samba)**
   Prepara el sistema e instala el servidor de archivos.
   ```bash
   ./scripts/install_samba.sh
   ```

   **Paso 2: Montar Discos USB**
   Conecta tu disco duro USB y ejecuta:
   ```bash
   ./scripts/mount_usb.sh
   ```

   **Paso 3: Configurar Carpetas Compartidas**
   Crea la carpeta compartida visible en la red.
   ```bash
   ./scripts/configure_share.sh
   ```

   **Paso 4: Acceso Remoto (VPN)**
   Instala WireGuard para acceder desde fuera.
   ```bash
   ./scripts/install_vpn.sh
   ```

## 📱 Cómo conectarse

### Desde Casa (Red Local)
- **Windows**: Abre el Explorador de Archivos y escribe `\\raspberrypi.local` en la barra de direcciones.
- **Mac**: Finder > Ir > Conectarse al servidor > `smb://raspberrypi.local`.
- **Móvil**: Usa una app como "Gestor de Archivos" o "VLC".

### Desde Fuera de Casa
1. Instala la app **WireGuard** en tu móvil u ordenador.
2. Usa el código QR generado por el script de VPN para importar la configuración.
3. Activa el interruptor en la app WireGuard.
4. Accede a tus archivos igual que si estuvieras en casa.
