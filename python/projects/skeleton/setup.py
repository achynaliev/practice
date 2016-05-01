try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'Atai Chynaliev',
	'url': 'empty',
	'download_ulr': 'empty',
	'author_email': 'chynaliev.ae@gmail.com',
	'version': '0.1',
	'install requires': ['nose'],
	'packages': ['EX47'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)
