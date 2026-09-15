# terminal_game.py
import time

print("🏰 ¡Bienvenido a la Aventura del Castillo Encantado! 🏰")
print("Tu objetivo es escapar con vida. Cuidado con los peligros...\n")
time.sleep(1)

# Variables del juego
hp = 100
tiene_llave = False
juego_terminado = False

# Bucle principal: El juego continúa mientras tengas salud y no hayas terminado
while not juego_terminado and hp > 0:
    print("-" * 40)
    print(f"❤️  Salud actual: {hp} | 🗝️  Llave: {'Sí' if tiene_llave else 'No'}")
    print("Estás en el Gran Salón. Tienes tres caminos:")
    print("1. Ir a la izquierda (Cocina)")
    print("2. Ir a la derecha (Biblioteca)")
    print("3. Ir hacia adelante (Puerta Principal)")
    
    # Toma de decisión principal
    eleccion = input("\n¿Qué decides hacer? (Elige 1, 2 o 3): ")
    
    if eleccion == "1":
        # Flujo de control dentro de una habitación
        print("\nEntras a la cocina. Está muy oscura y escuchas un ruido extraño.")
        print("1. Abrir la alacena misteriosa.")
        print("2. Volver corriendo al Gran Salón.")
        
        eleccion_cocina = input("¿Qué haces? (1 o 2): ")
        
        if eleccion_cocina == "1":
            print("\n¡Oh no! Un goblin saltó de la alacena y te atacó.")
            hp -= 30
            print("Pierdes 30 puntos de salud. Logras escapar de vuelta al salón.")
        elif eleccion_cocina == "2":
            print("\nRegresas al Gran Salón a salvo.")
        else:
            print("\nTe pones nervioso y tropiezas, regresando al Gran Salón.")
            
    elif eleccion == "2":
        print("\nEntras a la biblioteca polvorienta. Ves un cofre brillante en una mesa.")
        print("1. Abrir el cofre.")
        print("2. Ignorar el cofre y volver al Gran Salón.")
        
        eleccion_biblio = input("¿Qué haces? (1 o 2): ")
        
        if eleccion_biblio == "1":
            if not tiene_llave:
                print("\n¡Encuentras la Llave Dorada! Esto podría abrir la puerta principal.")
                tiene_llave = True
            else:
                print("\nEl cofre está vacío. Ya tomaste la llave antes.")
        else:
            print("\nRegresas al Gran Salón sin tocar nada.")
            
    elif eleccion == "3":
        print("\nTe acercas a la enorme Puerta Principal. Tiene una cerradura pesada.")
        
        # Verificamos si el jugador cumplió la condición para ganar
        if tiene_llave:
            print("¡Usas la Llave Dorada y la puerta se abre crujiendo!")
            print("\n🎉 ¡Felicidades! Escapaste del Castillo Encantado y ganaste el juego. 🎉")
            juego_terminado = True
        else:
            print("La puerta está bloqueada. Necesitas encontrar una llave para abrirla.")
            print("Regresas al Gran Salón para seguir buscando.")
            
    else:
        # Manejo de errores si el usuario ingresa algo inválido
        print("\n❌ Por favor, elige una opción válida (1, 2 o 3).")

# Mensaje de derrota si el bucle termina por falta de hp
if hp <= 0:
    print("\n💀 Te has quedado sin puntos de salud. ¡Fin del juego!")