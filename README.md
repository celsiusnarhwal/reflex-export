# Reflex Export Action

This GitHub Action exports a [Reflex](https://reflex.dev) project while caching its Node.js dependencies.

## Usage

Reflex must be availble on your system path or in your project's virtual environment before you run this action.
In the latter case, your virtual environment must be located at either a `.venv` folder in the action's working directory
or the value of the `UV_PROJECT_ENVIRONMENT` environment variable if it is set 
(the action uses [uv](https://docs.astral.sh/uv) internally).

> [!WARNING]
> [Poetry](https://python-poetry.org) users must either: 
> - set [`virtualenvs.in-project`](https://python-poetry.org/docs/configuration#virtualenvsin-project) to `true`
> - set [`virtualenvs.create`](https://python-poetry.org/docs/configuration#virtualenvscreate) to `false`
> - export the output of `poetry env info --path` to the `UV_PROJECT_ENVIRONMENT` environment variable
>
> or the action will fail.


```yaml
- name: Checkout Repository
  uses: actions/checkout@v4
  
  # Install Reflex and other dependencies using the tool of your choice, then...

- name: Export Project
  uses: celsiusnarhwal/reflex-export@main
```

The action takes an optional `args` input which may be used to provide additional arguments to `reflex export`, e.g.:

```yaml
- name: Export Project
  uses: celsiusnarhwal/reflex-export@main
  with:
    args: --frontend-only --loglevel debug
```