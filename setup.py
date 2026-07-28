# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# get version from __version__ variable in silent_print/__init__.py
from silent_print import __version__ as version

setup(
	name='silent_print',
	version=version,
	description='Silent print using https://github.com/imTigger/webapp-hardware-bridge',
	author='Roque Vera',
	author_email='roquegv@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	# frappe is provided by the bench environment, not by pip. Declaring it here
	# made uv resolve frappe transitively, which fails because frappe's own
	# metadata carries `PyPika @ git+https://...` and uv rejects transitive URL
	# dependencies. requirements.txt is left in place but no longer read; it must
	# not simply be emptied, as ''.strip().split('\n') yields [''] — an invalid
	# requirement.
	install_requires=[]
)
