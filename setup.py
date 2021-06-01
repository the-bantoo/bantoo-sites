# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in bantoo_sites/__init__.py
from bantoo_sites import __version__ as version

setup(
	name='bantoo_sites',
	version=version,
	description='Common customisations for bantoo sits',
	author='Bantoo Innovations',
	author_email='devs@thebantoo.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
