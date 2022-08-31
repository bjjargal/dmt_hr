from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in dmt_hr/__init__.py
from dmt_hr import __version__ as version

setup(
	name="dmt_hr",
	version=version,
	description="hr",
	author="bjjargal@gmail.com",
	author_email="bjjargal@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
