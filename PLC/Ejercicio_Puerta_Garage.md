# Ejercicio de Programación LOGO!: Puerta de Garaje Automática

## 1. Enunciado del Problema

Se desea automatizar el control de una puerta de garaje enrollable utilizando un PLC Siemens LOGO!. El sistema debe cumplir con las siguientes especificaciones:

*   **Apertura**: Al pulsar el botón de `Abrir` (S1), la puerta debe subir hasta alcanzar el final de carrera de apertura (FCA).
*   **Cierre**: Al pulsar el botón de `Cerrar` (S2), la puerta debe bajar hasta alcanzar el final de carrera de cierre (FCC).
*   **Seguridad (Fotocélula)**: Si durante el cierre se detecta un objeto atravesando la puerta (Fotocélula activa), la puerta debe detenerse inmediatamente y volver a abrirse por completo.
*   **Luz de Aviso**: Una luz intermitente debe activarse 5 segundos antes de que la puerta empiece a moverse y mantenerse activa durante todo el movimiento (apertura o cierre).
*   **Parada de Emergencia**: Un pulsador de seta (NC) debe detener cualquier movimiento inmediatamente.

## 2. Tabla de Variables (Entradas y Salidas)

| Símbolo | Dirección | Tipo | Descripción |
| :--- | :--- | :--- | :--- |
| **S1** | I1 | NO | Pulsador de Marcha (Abrir) |
| **S2** | I2 | NO | Pulsador de Marcha (Cerrar) |
| **FCA** | I3 | NC | Final de Carrera (Puerta Abierta) |
| **FCC** | I4 | NC | Final de Carrera (Puerta Cerrada) |
| **PE** | I5 | NC | Pulsador de Emergencia (Seta) |
| **FC** | I6 | NC | Fotocélula de seguridad (Barrera) |
| **KM1** | Q1 | - | Contactor Motor Subir (Abrir) |
| **KM2** | Q2 | - | Contactor Motor Bajar (Cerrar) |
| **H1** | Q3 | - | Luz de Aviso (Intermitente) |

*Nota: Los finales de carrera se suelen cablear normalmente cerrados (NC) por seguridad, pero en la lógica se pueden negar o tratar según conveniencia.*

## 3. Lógica de Solución Propuesta

### A. Control de Motores (Enclavamientos)
Para evitar cortocircuitos, **NUNCA** deben activarse Q1 y Q2 al mismo tiempo. Se debe usar un enclavamiento eléctrico y lógico.

#### Lógica de Apertura (Q1):
*   **SET** (Activar): Pulsador S1 + (NO está pulsado S2) + (NO está activo KM2)
*   **RESET** (Desactivar): Final de carrera FCA + Pulsador de Emergencia + (Fallo térmico si hubiera)

#### Lógica de Cierre (Q2):
*   **SET**: Pulsador S2 + (NO está pulsado S1) + (NO está activo KM1)
*   **RESET**: Final de carrera FCC + Fotocélula (I6) + Pulsador de Emergencia

### B. Gestión de la Fotocélula
Si la fotocélula (I6) detecta algo mientras Q2 (bajar) está activo:
1.  Resetea Q2 (detiene bajada).
2.  Activa Q1 (inicia subida) hasta FCA.

### C. Luz de Aviso (Q3) con Preaviso
Para el preaviso de 5 segundos:
1.  Al pulsar S1 o S2, se activa un **Temporizador con Retardo a la Conexión** que da paso a los motores después de 5s.
2.  La luz Q3 se activa inmediatamente al pulsar S1 o S2.
3.  Q3 se apaga cuando los motores se detienen (al llegar a los finales de carrera).
4.  Para la intermitencia, se usa un bloque **Generador de Impulsos Asíncrono**.

## 4. Estructura del Programa (LAD / KOP)

```text
Segmento 1: Abrir Puerta
   I1 (S1)      I2 (S2)     Q2 (Cerrar)   FCA (I3)   PE (I5)      Q1 (Abrir)
---| |-----------|/|-----------|/|---------| |--------| |----------( S ) 
   (Nota: FCA y PE son NC físicos, en programa se evalúan como '1' si están OK)

Segmento 2: Cerrar Puerta
   I2 (S2)      I1 (S1)     Q1 (Abrir)    FC (I6)    FCC (I4)     Q2 (Cerrar)
---| |-----------|/|-----------|/|---------|/|--------| |----------( S ) 

Segmento 3: Seguridad Fotocélula (Re-apertura)
   I6 (FC)      Q2 (Bajando)                                      Q1 (Abrir)
---| |-----------| |------------------------------------------------( S )
                                                                  Q2 (Cerrar)
                                                                    ( R )

... (Lógica de temporizadores para el preaviso omitida por simplicidad en este esquema texto, se recomienda usar bloques TON)
```

## 5. Bloques Funcionales Útiles en LOGO! Soft Comfort

*   **RS (Relé Autoenclavador)**: Ideal para memorizar el estado de "Abriendo" o "Cerrando".
*   **Retardo a la conexión (TON)**: Para el preaviso de la luz.
*   **Generador de impulsos**: Para hacer parpadear la luz Q3.
*   **Puertas AND/OR/NOT**: Para la lógica combinacional de condiciones.
