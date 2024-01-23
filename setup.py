from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in pg_management/__init__.py
from pg_management import __version__ as version

setup(
	name="pg_management",
	version=version,
	description="PG",
	author="Ajay",
	author_email="ajayjogdand374@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
