# Pipfile

[Pipfile docs](https://github.com/pypa/pipfile)

"Pipfile and its sister Pipfile.lock are a replacement for the existing standard pip's requirements.txt file."

> **NOTE: Still In Development**
> Pipfile will replace requirements.txt at some point in the future, natively in `pip` itself

Pipfile will be a much more powerful (and saner) way of managing Python packages and dependencies.

* Very similar approach to NPM's and `package.json`

## Requirements.txt
The current solution for PIP covers the most common use-cases of keeping track of dependency requirements

```
###### Requirements without Version Specifiers ######
nose
nose-cov
beautifulsoup4

###### Requirements with Version Specifiers ######
#   See https://www.python.org/dev/peps/pep-0440/#version-specifiers
docopt == 0.6.1             # Version Matching. Must be version 0.6.1
keyring >= 4.1.1            # Minimum version 4.1.1
coverage != 3.5             # Version Exclusion. Anything except version 3.5
Mopidy-Dirble ~= 1.1        # Compatible release. Same as >= 1.1, == 1.*

###### Refer to other requirements files ######
-r other-requirements.txt

###### A particular file ######
./downloads/numpy-1.9.2-cp34-none-win32.whl
http://wxpython.org/Phoenix/snapshot-builds/wxPython_Phoenix-3.0.3.dev1820+49a8884-cp34-none-win_amd64.whl
```

**Issues:**

* The workflow is too easy to not target your exact dependency requirements
    -  get different versions from dev -> test -> prod
* No way to install a package **and** save it to the requirements file
    - `pip install requests && pip freeze > requirements.txt`
* Freezing
    - When you `freeze` your environment, you get **everything**
        + It becomes impossible to determine which packages you are actually targeting and which are only dependencies
    - If you customized your requirements file, a new `freeze` will override/remove those customizations

## Pipfile
* Uses [TOML](https://github.com/toml-lang/toml) (Tom's Obvious, Minimal Language) sytax
    - An .INI like syntax
    - Provides much more functionality than normal text file
    - More feature-filled specification than JSON, so can add a lot more functionality

* Allows dev and prod dependencies to live in the same file
    - Previously, you would have a `requirements` directory with diff files for `prod`, `test`, etc.

* Allows you to 'require' installation on a certain platform, or specific python version

* Makes use of a 'lock' file, which:
    - Allows you to keep dependencies out of your requirements, so it's clear what your application needs
    - Pins the exact installed version of every package and their dependencies so there is no guess-work when installing in different environments
