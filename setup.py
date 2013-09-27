from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import os
import sys

import escrapper

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.rst')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='escrapper',
    version=escrapper.__version__,
    url='http://github.com/esparta/websvn/',
    license='Apache Software License',
    author=escrapper.__author__,
    tests_require=['pytest'],
    install_requires=['beautifulsoup4>=4.3.1',
                    'requests>=1.2.3'
                    ],
    cmdclass={'test': PyTest},
    author_email='esparta@gmail.com',
    description='Scrapping tool, can process WebSVN portal ',
    long_description=long_description,
    packages=['WebSVN'],
    include_package_data=True,
    platforms='any',
    test_suite='websvn.test_app',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 1 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    extras_require={
        'testing': ['pytest'],
    }
)