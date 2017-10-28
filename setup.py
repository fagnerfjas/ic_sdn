from setuptools import setup, find_packages

setup(
	name='Fagner',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        ic=ic_sdn.ic:cli
        sdn=ic_sdn.sdn:cli
    ''',
)
