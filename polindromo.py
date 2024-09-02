def identificar_p(palindromo):
    # Convertir todo el texto a minúsculas y eliminar espacios y caracteres especiales
    # ''.join(...) : crea una cadena ara unir elementos.
    # polindromo.lower() : convierte todas las letras en minusculas.
    # i.isalnum() : Filtra todos los caracteres alfanumericos.
    palindromo_puro = ''.join(i for i in palindromo.lower() if i.isalnum())
    
    # Condicional boolean if/ else
    # invierte el texto
    if palindromo_puro == palindromo_puro[::-1]:
        return "Palíndromo"
    else:
        return "No es un palíndromo"

palindromo = input("Introduce una palabra o frase: ")
resultado = identificar_p(palindromo)
print(resultado)
