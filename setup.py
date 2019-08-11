from distutils.core import setup

setup(
  name = 'dataset-split',
  packages = ['dataset-split'],
  version = '0.1.1-beta',
  license='MIT',
  description = 'Simple script that splits a dataset into train/test/valid folders',
  author = 'Murilo Ferreira',
  author_email = 'fferreira.murilo@gmail.com',
  url = 'http://git.murilo.xyz', 
  download_url = 'https://github.com/muriloxyz/dataset-split/archive/v0.1.1-beta.tar.gz',
  keywords = ['ml', 'ds', 'machine-learning', 'data', 'data-science',  'dataset',
  			  'tool', 'utils'],  
  install_requires=[],
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
