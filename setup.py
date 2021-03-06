from setuptools import setup, find_packages

setup(
    name='data-sets',
    version='2.1.0',

    description='Flask based UI for displaying & segmenting a single database table',

    install_requires=[
        'mara-db>=4.0.0',
        'mara-page>=1.4.1',
        'arrow'
    ],

    dependency_links=[
    ],

    packages=find_packages(),

    author='Mara contributors',
    license='MIT',

    entry_points={},
)

