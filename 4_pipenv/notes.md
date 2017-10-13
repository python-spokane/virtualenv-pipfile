# Pipenv
_Sacred Marriage of Pipfile, Pip, & Virtualenv_

[Pipenv src](https://github.com/kennethreitz/pipenv)
[Pipenv docs](https://pipenv.readthedocs.io/en/latest/)

"Pipenv harnesses Pipfile, Pip, and Virtualenv together in unison to create a single, high-quality tool that is optimized for workflow efficiency and best practices. Windows is a first–class citizen, in our world."

Pipenv is a wrapper around both Virtualenv and Pip, providing a unified way to handle both your environment and requirements under a single cli.

It abstracts away the implementation of your venv and removes the need for you to install and configure 3rd (4th?) party libraries and scripts, like virtualenvwrapper. This isn't to say that these libraries are not used - pipenv uses [Pew](https://github.com/berdario/pew) for managing venvs behind the scenes - just that as the end user, you no longer need to focus on this aspect. 

Since dependent libraries are tied so closely to the management of venvs, it makes sense to have one tool handle both jobs - though the main purpose for wrapping Pip is simply a means to offer support for [Pipfiles](https://github.com/pypa/pipfile).

### Features

* Pip and virtualenv work together, not as separate tools
* Pipfile support
* Hashes for dependency management - providing consistent installs
* Security checks and wranings
* Visualisation of dependency graphs
* Automatic loading of environment files (`.env`)
* Automatic Python version installation  
>This requires `pyenv` installed

--- 

### Installation

`pip install pipenv`

---

### Venv usage

Almost any command of Pipenv will create a new venv if one does not already exist.

**Initialization:**

* Create a new, empty venv
    - `pipenv --two` - Python2.x
    - `pipenv --three` - Python3.x
    - `pipenv --python <version>` - Pythonx.x

> **Note:** If you have `pyenv` installed and do not have the targed Python version, pipenv will automatically install that version of Python for you.

* `pipenv install --<two>|<three>|<python>`
Create a venv and install all packages

* `pipenv --rm`
Remove the venv

**Retrieve venv information:**

* `pipenv --where`
Output the location of the project

* `pipenv --venv`
Output the location of the venv

* `pipenv --py`
Output the location of the current Python interpreter

**Running Code:**

* `pipenv run <command>` (`pipenv run python manage.py shell`)
Runs the provided command under the venv, even if you are not within the context of an 'activated' venv

* `pipenv shell`
Spawns a shell within the activated virtualenv

---

### Pip usage

**Installing Packages:**

* `pipenv install`  
install all dependencies from the Pipfile

* `pipenv install <package>`  
install a specific package

* `pipenv install <package>==<version>`  
install specific package at a specific version

* Additional options:
    - `--dev`
    Install both develop and default packages from Pipfile.lock.
    - `--system`
    Use the system `pip` command rather than the one from your virtualenv
    - `--ignore-pipfile`
    Ignore the Pipfile and install from the Pipfile.lock
    - `--skip-lock`
    Ignore the Pipfile.lock and install from the Pipfile. In addition, do not write out a Pipfile.lock reflecting changes to the Pipfile

**Package Management:**

* `pipenv graph`
Output a full dependency tree of all packages

* `pipenv check`
Check that all installed packages meet requirements and have hashes that match the lock file
