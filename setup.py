from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path: str)->List[str]:
    '''
    Returns a list of requirements
    '''
    requirements = []
    with open(file_path) as f:
        req = f.readlines()
        req = [r.replace('\n', "") for r in req]

        if HYPHEN_E_DOT in req:
            req.remove(HYPHEN_E_DOT)
    return req

setup(
    name = "mlops001",
    version = 0.001,
    author = "Sandeep Kumar",
    author_email= "sandeepkumar998855@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)
