def hello(name, lang):
    greetings = {"English": "Hello", "Spanish": "Hola", "German": "Hallo"}
    msg = f"{greetings[lang]} {name}!"
    print(msg)


if __name__ == "__main__":

    import argparse

    parses = argparse.ArgumentParser(description="Provide a personal greetings!.")

    parses.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person to greet",
    )

    parses.add_argument(
        "-l",
        "--lang",
        metavar="language",
        required=True,
        choices=["English", "Spanish", "German"],
        help="The language of the greeting.",
    )

    arg = parses.parse_args()

    hello(arg.name, arg.lang)
