from setuptools import setup, find_packages

setup(
    version="0.0.2",
    # ...
    packages=find_packages(
        where='src',
        include=['main']
    ),
    package_dir={"": "src"},
    # ...
    install_requires=[
        'virtualenv',
    ],
    entry_points={
        'console_scripts': [
            'menv = main:main'
        ],
    },
    author="JMMMMMMMMMM",
    description="virtualenv manager",
    name="menv",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url='https://github.com/JuanMolina2001/menv',
    python_requires='>=3.6',
    platforms=['win32'],
)
