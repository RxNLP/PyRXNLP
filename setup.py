from setuptools import setup, find_packages
from subprocess import Popen, PIPE
import io,os,sys

def tag():
    return os.getenv("version")


def read_text_lines(fname):
    with io.open(fname) as fd:
        lines=fd.readlines()
        return ''.join(lines)



setup(
    name="pyrxnlp",
    version=tag(),
    packages=find_packages(),
    description='Natural language processing tools',
    long_description=open("README.rst").read(),
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing :: Linguistic'
    ],
    author='RxNLP',
    author_email='kavita.ganesan@rxnlp.com',
    license='LGPL',
    url='https://github.com/RxNLP/pyrxnlp',
    download_url='https://github.com/RxNLP/pyrxnlp/archive/{0}.tar.gz'.format(tag()),
    keywords=['Sentence Clustering', 'Topics Extraction',
              'Opinosis Summarization', 'Text Similarity'],
    install_requires=[
        'requests==2.20.0'
    ],
    include_package_data=True,
    entry_points={

    }
)
