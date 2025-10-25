from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    """This function will return the list of requirements"""

    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            #Read lines from the file
            lines=file.readlines()
            #process each line
            for line in lines:
                requirement=line.strip()
                # ignore the empty lines and -e.
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("The requirements.txt file was not found.")

    return requirement_lst

print(get_requirements())

setup(
    name='network_security_project',
    version='0.0.1',
    author='Sumit Kumar Gupta',
    author_email='sumit.gupta.14486@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)
