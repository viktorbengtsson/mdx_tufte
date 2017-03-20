#! /usr/bin/env python
from setuptools import setup

setup(
    name='mdx_tufte',
    version='1.0.0',
    author='Viktor Bengtsson',
    author_email='mail@viktorbengtsson.com',
    description='Python-Markdown extension generating output compatible with tufte.css',
    url='https://github.com/viktorbengtsson/mdx_tufte',
    py_modules=['mdx_tufte'],
    install_requires=['Markdown>=2.6.8',],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)