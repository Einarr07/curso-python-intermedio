import random

def choose_options():
    options = ('piedra', 'papel', 'tijera')

    # Entrada del usuario
    user_option = input('\n👉 Elige: piedra, papel o tijera => ')
    user_option = user_option.lower()

    # Validación de la opción
    if user_option not in options:
        print('⚠️ Esa opción no es válida, intenta de nuevo.')
        return None, None

    # Opción aleatoria de la computadora
    computer_option = random.choice(options)

    print(f"\n🧑 Usuario eligió: {user_option}")
    print(f"💻 Computadora eligió: {computer_option}")

    return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print("🤝 ¡Empate!")
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print("🪨 Piedra aplasta tijera ✂️ → ¡Usuario gana esta ronda!")
            user_wins += 1
        else:
            print("📄 Papel envuelve piedra 🪨 → Computadora gana esta ronda!")
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print("📄 Papel envuelve piedra 🪨 → ¡Usuario gana esta ronda!")
            user_wins += 1
        else:
            print("✂️ Tijera corta papel 📄 → Computadora gana esta ronda!")
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print("✂️ Tijera corta papel 📄 → ¡Usuario gana esta ronda!")
            user_wins += 1
        else:
            print("🪨 Piedra aplasta tijera ✂️ → Computadora gana esta ronda!")
            computer_wins += 1

    return user_wins, computer_wins


def run_game():
    rounds = 1
    computer_wins = 0
    user_wins = 0

    print("🎮 Bienvenido a Piedra, Papel o Tijera 🎮\n")
    print("El primero en ganar 2 rondas es el campeón 🏆\n")

    while True:
        print("=" * 30)
        print(f"🕹️ RONDA {rounds}")
        print("=" * 30)
        print(f"Marcador: Usuario {user_wins} - {computer_wins} Computadora\n")

        rounds += 1

        user_option, computer_option = choose_options()
        if user_option is None:
            continue  # vuelve a pedir opción si no fue válida

        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

        # Condiciones de victoria
        if computer_wins == 2:
            print("\n💻 La COMPUTADORA es la ganadora 🏆")
            break

        if user_wins == 2:
            print("\n🧑 ¡El USUARIO es el ganador! 🏆")
            break


if __name__ == "__main__":
    run_game()
