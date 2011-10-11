from os import path
from setuptools import setup

INSTALL_REQUIRES = []
#TODO: get the version number from git instead
VERSION = "0.1"

# add configobj to the import if not there
try:
    import configobj
except ImportError:
    INSTALL_REQUIRES.append('configobj')

try:
    import argparse
except ImportError:
    INSTALL_REQUIRES.append('argparse')

setup(
    name='pycallgraph',
    version=VERSION,
    description='Python Call Graph uses GraphViz to generate call graphs ' \
        'from one execution of your Python code.',
    author='Gerald Kaszuba',
    author_email='pycallgraph@slowchop.com',
    url='http://pycallgraph.slowchop.com/',
    py_modules=['pycallgraph'],
    scripts=['scripts/pycallgraph'],
    install_requires=INSTALL_REQUIRES,
    #TODO: check if this is correct
    setup_requires=INSTALL_REQUIRES,
    long_description = \
'''Python Call Graph uses GraphViz to generate call graphs from one execution
of your Python code. It's very easy to use and can point out possible problems
with your code execution.''',
    download_url =
    'http://pycallgraph.slowchop.com/files/download/pycallgraph-%s.tar.gz' % \
        VERSION,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Debuggers',
        ],
)
