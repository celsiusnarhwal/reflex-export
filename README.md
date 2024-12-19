# Reflex Export Action

[![Tests](https://github.com/celsiusnarhwal/reflex-export/actions/workflows/test.yml/badge.svg)](https://github.com/celsiusnarhwal/reflex-export/actions/workflows/test.yml)

This GitHub Action exports a [Reflex](https://reflex.dev) project while caching its Node.js dependencies and
Next.js build artifacts.

This action does not currently support Windows runners.

## Usage

> [!IMPORTANT]
> Reflex must be available on the system path or in your project's virtual environment before you run this action.
> In the latter case, the virtual environment must be located in a `.venv` directory that is in either your project's
> root or one of its parent directories.
> 
> If your preferred package manager has a default behavior of storing virtual environments somewhere else 
> (e.g., [Poetry](https://python-poetry.org/docs/configuration/#virtualenvsin-project), [pipenv](https://pipenv.pypa.io/en/latest/virtualenv.html#custom-virtual-environment-location)), you will
> need to configure it to either use the in-project `.venv` directory or install packages into the system environment. If that isn't 
> possible, you can use the [`interpreter` input](#inputs) to provide a path to the virtual environment's Python interpreter.

```yaml
- name: Checkout Repository
  uses: actions/checkout@v4

  # Install Reflex and other dependencies using the tool of your choice, then...

- name: Export Project
  uses: celsiusnarhwal/reflex-export@v1
```


### Inputs

| **Name**       | **Description**                                                                                                                                                                      |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `args`         | Optional arguments to `reflex export`.                                                                                                                                               |
| `project-root` | A relative or absolute path to the root of your Reflex project. Required if your project is not located in the current working directory. Defaults to the current working directory. |
| `interpreter`   | A path to the Python interpreter the action should use. May be absolute or relative to `project-root`.                                                                               |