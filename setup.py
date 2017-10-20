from setuptools import setup

setup(
	name='yourscript',
    version='0.1',
    py_moduloes=['yourscript'],
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        yourscript=yourscript:cli
    ''',
)
