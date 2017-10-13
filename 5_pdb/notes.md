# PDB - Python Debugger

[PDB docs](https://docs.python.org/3.6/library/pdb.html)

"The module pdb defines an interactive source code debugger for Python programs. It supports setting (conditional) breakpoints and single stepping at the source line level, inspection of stack frames, source code listing, and evaluation of arbitrary Python code in the context of any stack frame. It also supports post-mortem debugging and can be called under program control."

### Usage

1. Basic - `python 1_basic.py`
The most common use of the PDB is to import and call it in-line at the location of interest.
2. API - `python 2_basic.py`
The PDB class can be provided the script to run and execute it within the context of a running application.
1. As a script - `python -m pdb test.py`
When invoked as a script, pdb will automatically enter post-mortem debugging if the program being debugged exits abnormally. After post-mortem debugging (or after normal exit of the program), pdb will restart the program. Automatic restarting preserves pdb’s state (such as breakpoints) and in most cases is more useful than quitting the debugger upon program’s exit.


### Commands

**Information**

* `h(elp)`
Print all available commands
* `w(here)`
Output the current line / stack of execution
* `d(own)`
Move down the stack to newer frames
* `u(p)`
Move up the stack to older frames
* `l(ist) <first> <last>`
Show the source code around the current line
* `a(rgs)`
Print the argument list of the current function.
* `p / pp <expression>`
Print (or pretty print) the information from the expression

**Dynamic breakpoint handling**

* `b(reak) <line_number>`
Set a breakpoint in the current file
* `tbreak <line_number>`
Set a breakpoint in the current file, but only hit once
* `cl(ear) <args>`
Clear breakpoints for a given file/lineno or a set of breakpoint numbers
* `disable <breakpoint_num>`
Disable the given breakpoint
* `enable <breakpoint_num>`
Enable (re-enable) the given breakpoint

**Execution Flow**

* `next`
Execute the current line and stop
* `step`
Execute the current line and stop at next possible spot - could be in a function call
* `unt(il) <line_number>`
Continue execution until the line with a number greater than or equal to the provided one is reached
* `r(eturn)`
Continue execution until the current function returns
* `c(ont(inue))`
Continue execution, only stop when a breakpoint is encountered
