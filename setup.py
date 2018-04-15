from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'tunet',
    version = '2.0.1',
    description = 'Tsinghua University Network (tunet) login and logout tools',
    long_description = long_description,
    url = 'https://github.com/Yibo-Li/pytunet',
    author = 'Yibo Li',
    author_email = 'gansuliyibo@126.com',
    keywords = 'tunet login logout',
    packages = ['tunet'],
    install_requires = ['requests'],
    license = 'MIT'
)
