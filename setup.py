from setuptools import setup

setup(
    name='shodanAPI-JSON',
    version='1.0.0',
    description='API result for Shodan in Json format',
    author='Ethan Lacerenza',
    scripts=[''],
    install_requires=[
        'shodan',
        'json'
        'os'
    ],
)