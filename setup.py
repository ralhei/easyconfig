#!/usr/bin/env python

from distutils.core import setup

setup(name='easyconfig',
      version='0.1',
      description='EasyConfig extension to ConfigParser',
      author='Raph Heinkel',
      author_email='rh@ralph-heinkel.com',
      url='http:///',
      packages=['easyconfig'],
      tests_require=['pytest'],
      platforms=['unix', 'linux', 'win32'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Libraries',
          ],
      )
