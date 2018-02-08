from setuptools import setup, find_packages
from subprocess import Popen, PIPE


def tag():
    process = Popen (["git", "describe", "--abbrev=0", "--tags"], stdout=PIPE)
    tag=process.communicate()[0].strip()
    tag=bytes.decode(tag)
    return tag

def readme():
    readme_short = """
    PyRXNLP - NLP and Text Mining tools for building intelligent data-driven applications.
    

    ### Features:
     - Topics extraction
     - Text clustering
     - Opinosis opinion summarization


    """
    return readme_short


setup(
    name="pyrxnlp",
    version=tag(),
    packages=find_packages(),
    description='Natural language processing tools',
    long_description=readme(),
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing :: Linguistic'
    ],
    author='RxNLP',
    author_email='kavita.ganesan@rxnlp.com',
    license='LICENSE',
    url='https://github.com/RxNLP/pyrxnlp',
    download_url='https://github.com/RxNLP/pyrxnlp/archive/{0}.tar.gz'.format(tag()),
    keywords=['Sentence Clustering', 'Topics Extraction',
              'Opinosis Summarization', 'Text Similarity'],
    install_requires=[
        'requests==2.9.1'
    ],
    include_package_data=True,
    entry_points={

    }
)
