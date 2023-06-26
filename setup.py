from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mro_information_system/__init__.py
from mro_information_system import __version__ as version

setup(
	name="mro_information_system",
	version=version,
	description="For apps tailored specifically to the IT team in MRO",
	author="Dan Navarro",
	author_email="danjeremynavarro@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
