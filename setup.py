# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import re

import versioneer

with open('README.rst', 'r') as fp:
    readme = fp.read()

pkgs = find_packages('src', exclude=['data'])
print('found these packages:', pkgs)

schema_dir = 'common/hdmf-common-schema/common'

reqs_re = re.compile("[<=>]+")
with open('requirements.txt', 'r') as fp:
    reqs = [reqs_re.split(x.strip())[0] for x in fp.readlines()]

print(reqs)

setup_args = {
    'name': 'hdmf',
    'version': versioneer.get_version(),
    'cmdclass': versioneer.get_cmdclass(),
    'description': 'A package for standardizing hierarchical object data',
    'long_description': readme,
    'long_description_content_type': 'text/x-rst; charset=UTF-8',
    'author': 'Andrew Tritt',
    'author_email': 'ajtritt@lbl.gov',
    'url': 'https://github.com/hdmf-dev/hdmf',
    'license': "BSD",
    'install_requires': reqs,
    'packages': pkgs,
    'package_dir': {'': 'src'},
    'package_data': {'hdmf': ["%s/*.yaml" % schema_dir, "%s/*.json" % schema_dir]},
    'classifiers': [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: Unix",
        "Topic :: Scientific/Engineering :: Medical Science Apps."
    ],
    'keywords': 'python '
                'HDF '
                'HDF5 '
                'cross-platform '
                'open-data '
                'data-format '
                'open-source '
                'open-science '
                'reproducible-research ',
    'zip_safe': False
}

if __name__ == '__main__':
    setup(**setup_args)
