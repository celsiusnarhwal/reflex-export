# Reflex Export Action

[![Tests](https://github.com/celsiusnarhwal/reflex-export/actions/workflows/test.yml/badge.svg)](https://github.com/celsiusnarhwal/reflex-export/actions/workflows/test.yml)

This GitHub Action exports a [Reflex](https://reflex.dev) project while caching its Node.js dependencies and
Next.js build artifacts.

This action does not currently support Windows runners.

## Usage

Reflex must be available on the system path or in your project's virtual environment before you run this action.
If a `poetry.lock` file is found at the root of your Reflex project, the action will use [Poetry](https://python-poetry.org) to determine where
the virtual environment is located; otherwise, it will look for a `.venv` directory at your project's root.

```yaml
- name: Checkout Repository
  uses: actions/checkout@v4

  # Install Reflex and other dependencies using the tool of your choice, then...

- name: Export Project
  uses: celsiusnarhwal/reflex-export@v1
```

### Inputs

| **Name**       | **Description**                                                                                                                           |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| `args`         | Optional arguments to `reflex export`.                                                                                                    |
| `project-root` | A relative or absolute path to the root of your Reflex project. Required if your project is not located in the current working directory. |