from setuptools import setup, find_packages

setup(
    name='Daphne',
    version='0.1.0b1',  # Измените версию на более подходящую для вашей стадии разработки
    packages=find_packages(),
    install_requires=[
        'matplotlib>=3.9.2',
        'numpy>=2.1.0',
        'pandas>=2.2.2',
        'psutil>=6.0.0',
        'pytest>=8.3.2',
        'scikit_learn>=1.5.1',
        'seaborn>=0.13.2',
    ],
    test_requires=[
        'pytest>=8.3.2',
    ],
    description='Daphne: A powerful library for processing data and preparing it for training neural network models.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Arkonova/Daphne',
    author='Arkonova Daria',
    author_email='daria.arkonova@gmail.com',
    license='Apache License 2.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
)
