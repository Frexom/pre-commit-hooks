# pytest-pre-commit
A pre-commit hook to replace newly added CRLF with LF (or the opposite).


## pre-commit

To know more about pre-commit, see [here](https://pre-commit.com/).


## Pre-commit config
After installing pre-commit, you can add the following line in your .pre-commit-config.yaml to add the CRLF-to-LF hook to your repo :

```yaml
repos:
-   repo: https://github.com/Frexom/crlf-to-lf
    rev: 0.0.1
    hooks:
    -   id: crlf-to-lf
```

If you want to replace LF by CRLF, you need to add the `--keep-crlf` argument :

```yaml
repos:
-   repo: https://github.com/Frexom/crlf-to-lf
    rev: 0.0.1
    hooks:
    -   id: crlf-to-lf
        args: [ --keep-crlf ]
```
