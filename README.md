# pre-commit-hooks
This repo contains the multiple pre-commit hooks I created.

## What is pre-commit?

To know more about pre-commit, see [here](https://pre-commit.com/).


## Adding one of my hooks
After installing pre-commit, you can add the following line in your .pre-commit-config.yaml to add a hook to your repo :

```yaml
repos:
-   repo: https://github.com/Frexom/pre-commit-hooks
    rev: 0.0.1
    hooks:
    -   id: hook-id
```

## The hooks in this repo

### CRLF-to-LF

This hooks replaces CRLF Windows end-of-line characters by LF Linux end-of-lines. This help with keeping your repo consistent, not having enormous diffs due to the change of end-of-line characters, and having functional bash scripts (which don't work with CRLFs).
If you want to instead replace LFs by CRLFs, you need to add the `--keep-crlf` argument :

```yaml
repos:
-   repo: https://github.com/Frexom/pre-commit-hooks
    rev: 0.0.1
    hooks:
    -   id: crlf-to-lf
        args: [ --keep-crlf ]
```

You may also need to ignore some files, to do so, you can use the `--ignore` argument to ignore files with a given extensions the following way :
```yaml
-   repo: https://github.com/Frexom/pre-commit-hooks
    rev: 0.0.2
    hooks :
    -   id : crlf-to-lf
        args: ["--ignore", "db", "ttf", "--" ]
```
**Do not** forget the `--` command separator when specifying the `--ignore` args, or all you files will be treated as extensions.

### Pytest-check

This hook runs pytest before every commit, in order to be sure that all tests pass when editing the code. **/!\\ Warning /!\\** It is advised not to use this pre-commit hook if your tests do not run in a couple seconds.

If you do have both slow tests and fast tests, you can tell Pytest-check to only run the fast tests. For this, you need to specify the `--run-only` argument.

```yaml
repos:
-   repo: https://github.com/Frexom/pre-commit-hooks
    rev: 0.0.1
    hooks:
    -   id: pytest-check
        args: [ "--run-only", "tests/file1.py", "tests/file2.py" ]
```
By doing so, only the files `file1.py` and `file2.py` will be ran during the pre-commit hook execution.
