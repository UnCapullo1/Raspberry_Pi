import os
import subprocess
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_script(script_name):
    script_path = os.path.join(os.path.dirname(__file__), script_name)
    if os.path.exists(script_path):
        try:
            # Ejecutamos el script usando el mismo intérprete de python actual
            subprocess.run([sys.executable, script_path], check=True)
        except subprocess.CalledProcessError:
            print(f"\n[!] Error al ejecutar {script_name}")
        except Exception as e:
            print(f"\n[!] Ocurrió un error inesperado: {e}")
    else:
        print(f"\n[!] Error: El archivo {script_name} no se encuentra en la carpeta.")
    
    input("\nPresione Enter para volver al menú principal...")

def main_menu():
    scripts = {
        "1": ("Cálculo de Bobina", "calculo_bobina.py"),
        "2": ("Cálculo de Cilindro", "calculo_cilindro.py"),
        "3": ("Cálculo de Doblado", "calculo_doblado.py"),
        "4": ("Cálculo de Embutición", "calculo_embuticion.py"),
        "5": ("Corte y Punzonado", "calculo_fuerzas_corte.py"),
        "6": ("Longitud Desarrollada", "calculo_longitud_desarrollada.py"),
        "7": ("Gestión de Costes", "ejercicio_costes.py"),
    }

    while True:
        clear_screen()
        print("========================================")
        print("   CALCULADORA MAESTRA DE FABRICACIÓN   ")
        print("========================================")
        print("Seleccione una opción de cálculo:")
        
        for key, (name, _) in scripts.items():
            print(f"  {key}. {name}")
        
        print("  0. Salir")
        print("----------------------------------------")
        
        opcion = input(">> Opción: ")
        
        if opcion == "0":
            print("\n¡Hasta luego!")
            break
        elif opcion in scripts:
            name, filename = scripts[opcion]
            print(f"\nIniciando: {name}...\n")
            run_script(filename)
        else:
            print("\n[!] Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main_menu()
