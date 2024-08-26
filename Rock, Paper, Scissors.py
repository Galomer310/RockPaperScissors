from week4.Day1.ExerciseXP.RockPaperScissors.Game import Game

def get_user_menu_choice():
    while True:
        user_menu_choice = input('''
        For a new game press 'n', for score press 's', and to quit press 'q'
        ''').lower()

        if user_menu_choice in ['n', 's', 'q']:
            return user_menu_choice
        else:
            print("Invalid choice! Please try again.")

def print_results(results):
    print("\nGame Results:")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("Thanks for playing!")

def main():
    results = {'win': 0, 'loss': 0, 'draw': 0}
    while True:
        choice = get_user_menu_choice()
        if choice == 'n':
            game = Game()
            result = game.play()
            results[result] += 1

        elif choice == 's':
            print_results(results)

        elif choice == 'q':
            print_results(results)
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
