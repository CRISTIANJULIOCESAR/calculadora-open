import sumar
import resta
import multiplicacion
import dividir
import suma_avanzada

def menu():
    print("Bienvenido a la calculadora")
    print("1. Sumar 2 números")
    print("2. Restar 2 números")
    print("3. Multiplicar 2 números")
    print("4. Dividir 2 números")
    print("5. Suma avanzada (N números)")
    print("6. Salir")

    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                print(f"Resultado: {sumar.sumar(a, b)}")
            elif opcion == 2:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                print(f"Resultado: {resta.restar(a, b)}")
            elif opcion == 3:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                print(f"Resultado: {multiplicacion.multiplicar(a, b)}")
            elif opcion == 4:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                print(f"Resultado: {dividir.dividir(a, b)}")
            elif opcion == 5:
                numeros = input("Ingrese los números separados por comas: ")
                numeros = list(map(float, numeros.split(',')))
                print(f"Resultado: {suma_avanzada.suma_avanzada(numeros)}")
            elif opcion == 6:
                print("¡Adiós!")
                break
            else:
                print("Opción no válida, intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    menu()
