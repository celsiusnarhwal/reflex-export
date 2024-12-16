# Reflex Export Action

This GitHub Action exports a [Reflex](https://reflex.dev) project while caching its Node.js dependencies and
Next.js build artifacts.

## Usage

Reflex must be available on the system path or in your project's virtual environment before you run this action.
In the latter case, the virtual environment must be located in a `.venv` folder at the root of your Reflex project.

> [!WARNING]
> This means [Poetry](https://python-poetry.org) users must do one of the following prior to installing their project's dependencies:
> - set [`virtualenvs.in-project`](https://python-poetry.org/docs/configuration#virtualenvsin-project) to `true`
> - set [`virtualenvs.create`](https://python-poetry.org/docs/configuration#virtualenvscreate) to `false`

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