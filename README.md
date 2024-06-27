# menv

menv is a command-line tool for managing virtual environments and installing Python packages. It provides a simple interface to create, activate, deactivate, save, and install requirements for your projects.

## Installation

To install menv, you can use pip:

```
pip install menv
```

## Usage

menv provides the following commands:

- `menv init [args]`: Create a virtual environment. Additional arguments can be passed to the `virtualenv` command.
- `menv activate`: Activate the virtual environment.
- `menv deactivate`: Deactivate the virtual environment.
- `menv save`: Save the current requirements to a `menv.json` file.
- `menv start`: Install the saved requirements. Use the `--force` flag to ignore Python version mismatch.
- `menv run`: Run scripts of menv.json


Please note that menv currently only supports Windows operating system.

## Example

Here's an example of how to use menv:

1. Create a virtual environment:

```
menv init
```

2. Activate the virtual environment:

```
menv activate
```

3. Install required packages:

```
menv start
```

4. Save the current requirements:

```
menv save
```

5. Deactivate the virtual environment:

```
menv deactivate
```

6. Run scripts
```
menv run start
```
i
In menv.json
```
    "scripts": {
        "start": "python app.py"
    }
```

That's it! You can now use menv to manage your virtual environments and install Python packages.
