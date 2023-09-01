# pre-commit-hooks
This repo contains the multiple pre-commit hooks I created.

## pre-commit

To know more about pre-commit, see [here](https://pre-commit.com/).


## Pre-commit config
After installing pre-commit, you can add the following line in your .pre-commit-config.yaml to add a hook to your repo :

```yaml
repos:
-   repo: https://github.com/Frexom/pre-commit-hooks
    rev: 0.0.1
    hooks:
    -   id: crlf-to-lf
```

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
