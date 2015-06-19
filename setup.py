"""Setup for googledrive XBlock."""

import os
from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='googledrive-xblock',
    version='0.1',
    description='googledrive XBlock',   # TODO: write a better description.
    packages=[
        'googledrive',
    ],
    install_requires=[
        'XBlock',
        'Jinja2',
    ],
    entry_points={
        'xblock.v1': [
            'googledrive = googledrive:GoogleDriveXBlock',
        ]
    },
    package_data=package_data("googledrive", ["static", "public"]),
)
