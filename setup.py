#!/usr/bin/env python

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()


setup(
    name='django-Rest-phonenumber-confirmation',
    version='0.2',
    packages=find_packages(),
    description='Phone number confirmation',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Thomas Adel',
    author_email='thomas.adel31@gmail.com',
    url='https://github.com/thomas545/django-Rest-phonenumber-confirmation',
    keywords='django-phonenumber-confirmation phonenumber confirmations twilio django-twilio',
    zip_safe=False,
    license='MIT',
    install_requires=[
        'Django>=3.0',
        'djangorestframework>=3.11.0',
        'django-phonenumber-field>=4.0.0',
        'phonenumbers>=8.12.1',
        'twilio>=6.0.0',
    ],
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
    ],
)