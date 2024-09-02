def obtener_nombres_sin_numeros(mensaje):
    while True:
        try:
            nombres = input(mensaje)
            
            # Validar que no contenga números
            # char.isdigit() : identifica si es un numero o no.
            # raise : lanza una excepcion.
            if any(char.isdigit() for char in nombres):
                raise ValueError("El nombre no debe contener números.")
            
            # Si la validación pasa, salir del bucle
            return nombres
        
        except ValueError as e:
            print("Error:", e)

def obtener_fechas_numerica(mensaje):
    while True:
        try:
            fechas = input(mensaje)
            
            # Validar que la entrada sea numérica
            if not fechas.isdigit():
                raise ValueError("Las fechas deben contener solo números.")
            
            return fechas
        
        except ValueError as e:
            print("Error:", e)

def obtener_rfc(apellido_paterno, apellido_materno, primer_nombre, año, mes, día):
    # Iniciales del RFC
    iniciales_apellido_paterno = apellido_paterno[:2].upper()
    iniciales_apellido_materno = apellido_materno[0].upper()
    iniciales_primer_nombre = primer_nombre[0].upper()
    
    # Año (últimos dos dígitos)
    año_corto = año[-2:]
    
    # Mes y día con dos dígitos
    mes_corto = mes.zfill(2)
    día_corto = día.zfill(2)
    
    # Crear RFC
    rfc = f"{iniciales_apellido_paterno}{iniciales_apellido_materno}{iniciales_primer_nombre}{año_corto}{mes_corto}{día_corto}"
    
    return rfc

# Solicitar datos al usuario
apellido_paterno = obtener_nombres_sin_numeros("Ingrese el apellido paterno: ")
apellido_materno = obtener_nombres_sin_numeros("Ingrese el apellido materno: ")
primer_nombre = obtener_nombres_sin_numeros("Ingrese el primer nombre: ")

# Solicitar año, mes y día
while True:
    try:
        año = obtener_fechas_numerica("Ingrese el año de nacimiento (completo, ejemplo: 1991): ")
        mes = obtener_fechas_numerica("Ingrese el mes de nacimiento (número, ejemplo: 4 o 12): ")
        día = obtener_fechas_numerica("Ingrese el día de nacimiento (número, ejemplo: 7 o 25): ")

        año = int(año)
        mes = int(mes)
        día = int(día)

        if not (1900 <= año <= 2024):
            raise ValueError("El año debe estar entre 1900 y 2024.")
        if not (1 <= mes <= 12):
            raise ValueError("El mes debe estar entre 1 y 12.")
        if not (1 <= día <= 31):
            raise ValueError("El día debe estar entre 1 y 31.")
        
        # Si todo es correcto, salir del bucle
        break

    except ValueError as e:
        print("Error en los datos ingresados:", e)

# Generar RFC
rfc = obtener_rfc(apellido_paterno, apellido_materno, primer_nombre, str(año), str(mes), str(día))
print("RFC generado:", rfc)