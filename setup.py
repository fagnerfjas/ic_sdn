from setuptools import setup, find_packages

setup(
	name='Fagner',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    #py_moduloes=['yourscript'],
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        yourscript=pacote.scripts.script:cli
        outro=pacote.utils:cli
    ''',
)
