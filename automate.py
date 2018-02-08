import argparse
import os
import sys
from subprocess import Popen, PIPE


def print_help():
    print("""
        ====What needs to happen========
        1. make sure all changes pushed to master
        2. generate a git tag
        3. remove dist/* to remove old distribution
        4. run python setup.py sdist , generates new distribution
        5. twine upload dist/*
        """)


# create description of task
parser = argparse.ArgumentParser(description='Distribute PyRXNLP')


parser.add_argument(
        '-i',
        '--info',
        action='store_true',
        help="info",
        required=False)
parser.add_argument(
        '-v',
        '--version',
        type=str,
        help="provide a version number that doesn't collide",
        required=False)


args = parser.parse_args()
version=args.version
info=args.info

if info:
    print_help()

elif version is not None:

    # 1. make sure all changes pushed to master
    # 2. generate a git tag
    # 3. remove dist/*
    # 4. run setup.py python setup.py sdist
    # 5. twine upload dist/*

    os.system ("git tag {0}".format(version))
    os.system ("git push origin {0}".format(version))
    os.system ("rm dist/*")
    os.system ("python setup.py sdist")
    os.system ("twine upload dist/*")

else:
    parser.print_help()