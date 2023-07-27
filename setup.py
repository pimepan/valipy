from setuptools import find_packages, setup
setup(
    name='valipy',
    packages=find_packages(),
    version='0.1.0',
    description='A chainable, fluent Python library for validating data',
    author='Joaquin Jose Von Chong',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)