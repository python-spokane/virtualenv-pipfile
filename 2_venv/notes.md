# Virtual Environments

"A virtual environment is a Python environment such that the Python interpreter, libraries and scripts installed into it are isolated from those installed in other virtual environments, and (by default) any libraries installed in a “system” Python, i.e., one which is installed as part of your operating system."

When we create a new virtual environment, it creates an isolated environment with it’s own local interepreter linked to it’s own libraries/scripts paths. (i.e. it's own copy of Python and any installed libraries from PIP, etc).

When we use this local interpreter, it loads the libraries from the local environment, or if it can’t find one locally, tries to locate that library in the parent/system environment.

---

## venv / pyvenv

[venv docs](https://docs.python.org/3/library/venv.html)

Built-in support for creating virtual environments without the need for additional libs/packages (part of stdlib).

Additionally, includes a set of built-in functionality and APIs to enable extending venvs programatically.

> **Note: only available in >= Python 3.3

#### Initialization:
**Python 3.3 - 3.5**

* posix:  
`pyvenv /path/to/new/virtual/environment`
* windows:  
`c:\Temp>c:\Python34\python c:\Python34\Tools\Scripts\pyvenv.py myenv`
* windows (if proper pathing setup):  
`c:\Temp>c:\Python34\python -m venv myenv`

**Python 3.6 and higher**

"Note The `pyvenv` script has been deprecated as of Python 3.6 in favor of using python3 -m venv to help prevent any potential confusion as to which Python interpreter a virtual environment will be based on."

* posix:  
`python3 -m venv /path/to/new/virtual/environment`
* windows:  
`c:\>c:\Python35\python -m venv c:\path\to\myenv`
* windows (if proper pathing setup):  
`c:\>python -m venv myenv c:\path\to\myenv`

#### Activation:

* posix:  
`source <venv_path>/bin/activate`
* windows:  
`C:\> <venv_path>/Scripts/activate`

#### Deactivation:

`deactivate`

---

## virtualenv

[virtualenv docs](https://github.com/pypa/virtualenv)

* [Released in 2007](http://www.ianbicking.org/blog/2007/10/workingenv-is-dead-long-live-virtualenv.html) by Ian Bicking
* Supports Python 2.7 to 3.6 (so far)

#### Installation:

`pip install virtualenv`

#### Initialization:

`virtualenv /path/to/new/virtual/environment`

#### Activation:

* posix:  
`source <venv_path>/bin/activate`
* windows:  
`C:\> <venv_path>/Scripts/activate`

#### Deactivation:

`deactivate`

#### Configuration:

* `-p PYTHON_EXE, --python=PYTHON_EXE`  
The Python interpreter to use, e.g., –python=python2.5 will use the python2.5 interpreter to create the new environment. The default is the interpreter that virtualenv was installed with (like /usr/bin/python)
* `--system-site-packages`  
Give the virtual environment access to the global site-packages.
* `--no-setuptools` `--no-pip` `--no-wheel`  
skip installation of these tools. Useful if not needed, or testing specific customisations / alternate channels
* `--extra-search-dir=DIR`
Directory to look for setuptools/pip distributions in. This option can be specified multiple times.

### Companion libs:
**[Pew](https://github.com/berdario/pew) - Python Env Wrapper**
**[Virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)**

### Virtualenvwrapper:

1. **Organizes all of your virtual environments in one place**. 
Specify a **single** directory to store all of your venv directories and files **by default**, instead of having them at the root of the project, or having to specify the full path when creatinv a new venv.  
`~/.virtualenvs`

2. **Wrappers for managing your virtual environments (create, delete, copy)**
    - `mkvirtualenv <my_venv>` - create a new venv
    - `rmvirtualenv <my_venv>` - removes the venv and all related files
    - `lsvirtualenv` - lists all venvs
    - `cpvirtualenv <old_venv> <new_venv>` - copies an existing venv
    - `allvirtualenv` - run a command for all venvs
        + `allvirtualenv pip install -U requests`

3. **Use a single command to switch between environments**
Calling the `activate` script in each venv's directory (`source <venv_path>/bin/activate`) is tedious.  
Provide a single `workon` command that can be invoked anywhere.  
`workon project1`
`workon project2`

4. **Tab completion for commands that take a virtual environment as argument**
5. **User-configurable hooks for all operations**
    - `premkvirtualenv`
    - `postmkvirtualenv`
