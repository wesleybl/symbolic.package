================
symbolic.package
================

This repository demonstrates the Pylance error when we have a symbolic link in python.analysis.extraPaths

See:

https://github.com/microsoft/pylance-release/issues/131


See that `python.analysis.extraPaths` points to the `lib` folder


`lib/my` is a symbolic link to `.lib/my`


Use:

    git clone https://github.com/wesleybl/symbolic.package
    cd symbolic.package
    code .


Open the `src/symbolic/package/__init__.py` file and type:

    import my

The autocomplete will not work, because `lib/my` is a symbolic link.

If we type:

    import real

The autocomplete will work, because `lib/real` is a real folder.
