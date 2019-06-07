from setuptools import find_packages
from setuptools import setup


setup(
    name='pivotal-pre-commit',
    description='Some out-of-the-box hooks for pre-commit.',
    url='https://github.com/pivotal-energy-solutions/pre-commit-hooks',
    version='0.0.2',

    author='Steven K',
    author_email='steven@pointcircle.com',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages('.', exclude=('tests*')),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'copyright_checker = pre_commit_hooks.copyright_checker:main',
        ],
    },
)