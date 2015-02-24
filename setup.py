__author__ = 'avathar'
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Translate ardrone-autonomy JS scripts to tum-simulator commands',
    'author': 'avathar',
    'url': 'https://github.com/avatharBot/PyTum',
    'author_email': 'ricardo.iva91@gmail.com',
    'version': '0.1',
    'name': 'PyTum'
}

setup(**config)