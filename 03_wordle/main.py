import wordle

if __name__ == '__main__':
    while True:
        with open("cheat.txt", "w") as f:
            f.write(wordle.CHOSEN_WORD)
        guess = wordle.GuessWord(
            w_str=input(">")
        )
        if guess.is_valid():
            guess.apply_guesses()
            guess.jump_turn()
            print(wordle.GuessWord.counter)

