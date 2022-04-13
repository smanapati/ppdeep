from setuptools import setup
import ppdeep

with open('README.md') as f:
	long_description = f.read()

setup(
	name='ppdeep',
	version=ppdeep.__version__,
	author='Shobha Manapati',
	author_email='smanapati@neiu.com',
	description='Pure-Python library for computing fuzzy hashes (ssdeep)',
	long_description=long_description,
	url='https://github.com/smanapati/ppdeep',
	py_modules=['ppdeep'],
	classifiers=[
		'Programming Language :: Python :: 3',
		'Operating System :: OS Independent',
	],
)
