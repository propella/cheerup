# Author's notes

## instructions

```
git clone git@github.com:propella/cheerup.git
cd cheerup
pyenv local 3.9
python -m venv .venv --prompt cheerup
source .venv/bin/activate
make install

export OPENAI_API_KEY=(Your OpenAI API Key)
export LANG=ja_JP.UTF-8

cheerup -c ls

git commit xxx
git push xxx
git tag xxx
git push xxx
```

interesting commands

```
ls
git status
sl
rm -rf /*
export LANG=zh_CN.UTF-8
```

## todos

- Interrupt the response when the user press any key.
