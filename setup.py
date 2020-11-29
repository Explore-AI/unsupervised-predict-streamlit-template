from setuptools import setup, find_packages

setup(
    name = 'unsupervised_functions',
    version = '0.1',
    packages = find_packages(exclude=['tests*']),
    license = 'MIT',
    description = 'Movie Recommender helper functions',
    long_description = open('README.md').read(),
    install_requires = ['numpy', 'pandas', 'seaborn', 'cufflinks', 'sklearn', 'scikit-surprise'],
    url = 'https://github.com/RobertoPRocha/unsupervised-predict-streamlit-template',
    author = 'Roberto Rocha',


)
