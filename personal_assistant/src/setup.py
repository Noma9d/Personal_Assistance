from setuptools import setup, find_namespace_packages, find_packages

import json
import os

setup(
    name='Willy',
    version='v1.0.11',
    description='Personal Assistant Willy',
    url='https://github.com/Kagev/GOIT_PersonalAssistance',
    author='PyCrafters',
    author_email='PyCrafters@goit.com',
    license='GNU',
    packages=find_namespace_packages(),
    classifiers=["Programming Language :: Python :: 3",
                "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
                "Operating System :: OS Independent",
                ],
    entry_points={
        'console_scripts':
            ['willy = project_willy.main:main']
                  }
)
