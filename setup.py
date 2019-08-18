from distutils.core import setup

setup(
  name = 'dataset-split',
  packages = ['dataset_split'],
  scripts = ['dataset_split/dataset-split'],
  version = '0.17-beta',
  license='MIT',
  description = 'Simple script that splits a dataset into train/test/valid folders',
  long_description = 'Check Github repository for more informations',
  author = 'Murilo Ferreira',
  author_email = 'fferreira.murilo@gmail.com',
  url = 'http://github.com/muriloxyz/dataset-split', 
  download_url = 'https://github.com/muriloxyz/dataset-split/archive/v0.17-beta.tar.gz',
  keywords = ['ml', 'ds', 'machine-learning', 'data', 'data-science',  'dataset', 'tool', 'utils'],  
  install_requires = [],
  python_requires = '>=3.5',
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
