..  _software_process:

================
Software Process
================

----------------------
Continuous Integration
----------------------

HDMF is tested against Ubuntu, macOS and Windows operating systems.
The project has both unit and integration tests.

* CircleCI runs all HDMF tests on Ubuntu
* Azure Pipelines runs all HDMF tests on Windows and macOS

Each time a PR is published or updated, the project is built, packaged and tested on all support operating systems and python distributions. That way, as a contributor you know if you introduced regressions or coding style inconsistencies.

There are badges in the README_ file which shows the current condition of the dev branch.

.. _README: https://github.com/hdmf-dev/hdmf#readme


--------
Coverage
--------

Coverage is computed and reported using the coverage_ tool. There is a badge in the README_ file which
shows percentage coverage. A detailed report can be found on codecov_ which shows line by line which
lines are covered by the tests.

.. _coverage: https://coverage.readthedocs.io
.. _codecov: https://codecov.io/gh/hdmf-dev/hdmf/tree/dev/src/hdmf

..  _software_process_requirement_specifications:


--------------------------
Requirement Specifications
--------------------------

There are 2 kinds of requirements specification in HDMF.

Setup.py Dependencies
---------------------

The first one is the dependencies_ in the `setup.py` file which lists the abstract dependencies for
the HDMF project. Note that there should not be specific versions of packages in the `setup.py` file.

Requirements.txt Dependencies
-----------------------------

The second one is `requirements.txt` which contain a list of pinned (concrete) dependencies to reproduce
an entire development environment to work with HDMF.

In order to check the status of the required packages requires.io_ is used to create a badge on the project
README_. If all the required packages are up to date,
a green badge appears.

If some of the packages are outdated, see :ref:`update_requirements_files`.

.. _dependencies: https://github.com/hdmf-dev/hdmf/blob/dev/setup.py
.. _requires.io: https://requires.io/github/hdmf-dev/hdmf/requirements/?branch=dev


-------------------------
Versioning and Releasing
-------------------------

HDMF uses versioneer_ for versioning source and wheel distributions. Versioneer creates a semi-unique release
name for the wheels that are created. It requires a version control system (git in HDMF's case) to generate a release name.
After all the tests pass, CircleCI creates both wheels(*.whl) and source distribution(*.tgz) for Python 3
and uploads them back to GitHub as a release_. Versioneer makes it possible to get the source distribution from GitHub and create
wheels directly without having to use a version control system because it hardcodes versions in the source distribution.

.. _versioneer: https://github.com/warner/python-versioneer
.. _release: https://github.com/hdmf-dev/hdmf/releases
