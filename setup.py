from setuptools import setup, find_packages
setup( 
    #Basic Package data
    name = "RSReader",
    version="0.1",

    #Package structure
    packages=find_packages('src'),
    package_dir={'':'src'},

    #install the rsreader executable
    entry_points= {
        'console_scripts': [
            'rsreader = rsreader.app:main'
            ]
    },
    install_requires = [
        'docutils == 0.4',
        ],
)
