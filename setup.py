from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='valipy',
    packages=find_packages(),
    version='0.1.2',
    description='A chainable, fluent Python library for validating data',
    long_description=long_description,  # Include the content of README.md here
    long_description_content_type='text/markdown',  # Specify the content type
    author='Joaquin Jose Von Chong',
    license='MIT',
    author_email = 'jjvonchong@outlook.com',      # Type in your E-Mail
    url = 'https://github.com/pimepan/valipy',   # Provide either the link to your github or to your website
    keywords = ['validation', 'data', 'schema', 'schema validation'],   # Keywords that define your package best
    readme='README.md',
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)