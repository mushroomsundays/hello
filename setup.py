from setuptools import setup, find_packages

#with open('requirements.txt') as f:
#    requirements = f.read().splitlines()

#with open('README.md', 'r') as f:
#    long_description = f.read()

setup(
    name='hello',
    version='0.1',
    description='Hello World project for creating a package.',
    license='MIT',
    long_description='Hello World project for creating a package.',
    author='John',
    author_email='fake@email.com',
    url='https://fakeurl.com',
    packages=find_packages(),
    install_requires=['numpy', 'wheel'],
    entry_points={
        'console_scripts': [
            'run_lifetime = src.main:main'
        ]
    }
)
