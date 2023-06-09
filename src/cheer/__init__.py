import os
import sys
from pprint import pprint
import argparse
from typing import Optional
import openai


def get_response(cmd: str, locale: Optional[str] = None) -> str:
    """Get response from OpenAI API."""

    prompt = "You are an AI assistant adept at complimenting programmers. Please provide verbose compliments on the user's Unix command inputs."

    if locale:
        prompt += f" Use the language in the locale: {locale}."

    # print(prompt)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": prompt,
            },
            {"role": "user", "content": cmd},
        ],
    )
    # pprint(response)
    return response["choices"][0]["message"]["content"]


def interactive(lang: Optional[str] = None) -> None:
    """Interactive mode."""

    while True:
        try:
            cmd = input("$ ")
            message = get_response(cmd, lang)
            print(message)
        except (KeyboardInterrupt, EOFError):
            return


def oneshot(cmd: str, lang: Optional[str] = None) -> None:
    """One-shot mode."""

    message = get_response(cmd, lang)
    print(message)


def main() -> None:
    """Main function."""

    parser = argparse.ArgumentParser(prog="cheer", description="Cheer up programmers.")
    parser.add_argument(
        "-i", "--interactive", action="store_true", help="Interactive mode"
    )
    parser.add_argument("-c", "--command", help="Cheer up for the command")
    parser.add_argument(
        "-l",
        "--lang",
        default=os.environ.get("LANG"),
        help="Locale. Default is LANG environment variable.",
    )
    args = parser.parse_args()

    if args.interactive:
        interactive(args.lang)
    elif args.command:
        oneshot(args.command, args.lang)
    else:
        parser.print_help()

    sys.exit(0)
