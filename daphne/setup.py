from setuptools import setup, find_packages

setup(
    name='daphne',
    version='1.0.0',
    author='Arkonova Daria',
    author_email='your.email@example.com',
    description='A powerful data processing library for small and large-scale data.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Arkonova/daphne',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'datasets',
        'tensorflow-datasets',
        'scikit-learn',
        'py7zr',
        'h5py'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
