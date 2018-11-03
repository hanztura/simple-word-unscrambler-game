# Machine Problem 1 - Simple Word Unscrambler Game

    > For the machine problem, your goal is to create a single-player Word Unscrambler
    Game, where the player (the user), will gain points by unscrambling a set
    of letters to get certain words.

## How to play the game?

    > Just run `main.py`

## Documentation

    * Engine - engine.py
        > Contains all the logic of the game, primarily includes: seeding of words from a dictionary file, picking words from dictionary, searching of anagrams of a given word from a given dictionary, combining words into a string, checking of words if it exists in a given dictinoary, and computing the players score based on a given scoring matrix.

    * Interface - interface.py
        > Contains all the interface of the game. Main module call's the `go()` method as the entry point of the game.
        > Each of the game's mode has it's own function.

    * Main - main.py
        > The file to run to play the game. It calls the interface.py's go method.

    * Configuration - config.py
        > This module contains the system variables. Like dictionary file name, number of retries allowed, and other configs.

## References

    * https://stackoverflow.com/questions/287871/print-in-terminal-with-colors
        > for the idea of printing with colors

    * https://stackoverflow.com/questions/44778/how-would-you-make-a-comma-separated-string-from-a-list-of-strings
        > in transforming array of numbers into string

## Clone repo from github

    > assuming we are saving the repo in directory Downloads

    ```bash
    cd Downloads
    git clone https://github.com/hanztura/simple-word-unscrambler-game
    ```

## Update repo using git

    > assuming we saved the repo in directory Downloads

    ```bash
    cd Downloads/simple-word-unscrambler-game
    git pull
    ```
