# -*- coding: utf-8 -*-
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


install_requires = \
["pandas==1.3.5"
]

setup_kwargs = {
    'name': 'combine_csv',
    'version': '0.0.5',
    'description': 'A program to combine csv',
    'py_modules': ['combine_csv'],
    'entry_points':{
        'console_scripts':
        ['combine_csv=combine_csv:main']
    },
    'long_description': long_description,
    'author': 'Rachel Nguyen',
    'author_email': 'baongoc21099@ku.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}

setup(**setup_kwargs)
