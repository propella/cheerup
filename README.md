# cheerup - Cheer on your command-line expertise!

`cheerup` is a tool designed to elevate your programming experience by complimenting your Unix command-line inputs. Created with the goal to foster learning, motivation, and a sense of achievement among programmers, it's like your own personal assistant that helps you see the magic in every command you run.

Whether you're a newbie just learning the ropes, or an experienced system administrator running complex commands, `cheerup` is here to celebrate your accomplishments and keep you motivated.

## Instructions

```shell
pip install -e .
export OPENAI_API_KEY=<your openai API key>
cheerup -i
$ echo "Hello, World!"
```

The last 10 conversations are saved into `${TMPDIR}cheerup_history.json`.
