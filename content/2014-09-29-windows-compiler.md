Title: New Microsoft C++ compiler for Python 2.7 on Windows,
Tags: cookbook, minibook

Compiling C extensions for Python on Windows used to be complicated. One had to install the adequate (unsupported) versions of Microsoft Visual Studio and the Windows compilers. Furthemore, it was necessary to invoke some commands on the command-line interface before running Python or IPython. In the end, installing non-pure-Python packages, or building non-pure-Python distributions for Windows users was a pain.

Microsoft is now trying to simplify this task by releasing a compiler package specifically targetting Python 2.7. This means that it should be much easier to compile C extensions for Python 2.7 on Windows now.

<!-- PELICAN_END_SUMMARY -->

You will find an [unofficial announcement by Microsoft here](http://code.activestate.com/lists/python-dev/132763/), and the [compiler package here](http://www.microsoft.com/en-us/download/details.aspx?id=44266).

The instructions to compile C extensions on Windows that you'll find in the IPython minibook and cookbook should still be valid, but they're likely to be soon superseded by simpler instructions based on this new compiler package.
