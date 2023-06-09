import os
import sys
from pprint import pprint
import argparse
from typing import Optional
import openai


def chat(cmd: str, locale: Optional[str] = None) -> str:
    """Print response from OpenAI API."""

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
        stream=True,
    )
    # pprint(response)
    answer = ""
    for chunk in response:
        # pprint(chunk)
        content = chunk["choices"][0]["delta"].get("content", "")
        print(content, end="", flush=True)

        answer += content
    print()
    return answer


def interactive(lang: Optional[str] = None) -> None:
    """Interactive mode."""

    while True:
        try:
            cmd = input("$ ")
            chat(cmd, lang)
        except (KeyboardInterrupt, EOFError):
            return


def main() -> None:
    """Main function."""

    parser = argparse.ArgumentParser(
        prog="cheerup", description="Cheer on your command-line expertise!"
    )
    parser.add_argument(
        "-i", "--interactive", action="store_true", help="Interactive mode"
    )
    parser.add_argument("-c", "--command", help="Compliment the command")
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
        chat(args.command, args.lang)
    else:
        parser.print_help()

    sys.exit(0)
