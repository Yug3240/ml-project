from setuptools import find_packages,setup
from typing import List

hypen_e_dot='-e .'

def get_req(file_path:str)->list[str]:
    "this func written list of req"
    req=[]
    with open(file_path) as file_obj:
        req=file_obj.readlines()
        req=[r.replace('\n','') for r in req]
        if hypen_e_dot in req:
            req.remove(hypen_e_dot)
    return req


setup(
name='ml_project',
version='0.0.1',
author='yug',
author_email='yugantcmore@gmail.com',
packages=find_packages(),
install_requires=get_req('requirement.txt')
)