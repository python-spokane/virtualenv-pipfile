# pyenv - Simple Python Version Management

[pyenv docs](https://github.com/pyenv/pyenv)

"pyenv lets you easily switch between multiple versions of Python. It's simple, unobtrusive, and follows the UNIX tradition of single-purpose tools that do one thing well."

Pyenv is simple tool that lets you keep multiple versions of Python installed on your OS and swap them as-needed. This is beneficial since it allows you to keep your system's python version in-tact.

Like a python version of: nvm, rbenv, etc
It uses a path-shiming approach to managing multiple pythons / environments. No new files or packages are installed, your path iss imply updated to point to existing installations.

Features:
* Change the global Python version on a per-user basis
* Use per-project Python versions via config files
* Provides overrides for active Python version via environment variables

When you execute a shim, pyenv determines which Python version to use by reading it from the following sources, in this order:

1. The PYENV_VERSION environment variable (if specified). You can use the pyenv shell command to set this environment variable in your current shell session.
2. The application-specific .python-version file in the current directory (if present). You can modify the current directory's .python-version file with the pyenv local command.
3. The first .python-version file found (if any) by searching each parent directory, until reaching the root of your filesystem.
4. The global $(pyenv root)/version file. You can modify this file using the pyenv global command. If the global version file is not present, pyenv assumes you want to use the "system" Python. (In other words, whatever version would run if pyenv weren't in your PATH.)
