from setuptools import setup, find_packages

setup(
    name = 'unsupervised_functions',
    version = '0.1.0',
    packages = find_packages(exclude=['tests*']),
    long_description = open('README.md').read(),
    install_requires = ['numpy', 'pandas', 'seaborn', 'cufflinks', 'sklearn', 'scikit-surprise'],
    extras_require={
        'interactive': ['streamlit'],
    },
    url = 'https://github.com/CaitMc/unsupervised-predict-streamlit-template',
    author = 'Team_ES2_Data_Flex',
    author_email = ['caitlinmclaren13@gmail.com','lebusotsilo6@gmail.com','nom.mraqisa@gmail.com','patrickmasilo26@gmail.com','peakanyok@gmail.com','noluthandojesie@gmail.com']
)
