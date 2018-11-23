from setuptools import setup, find_packages

with open('requirements.txt') as f:
    reqs = f.read()

setup(
    name='drqa',
    version='0.1.0',
    description='The Enrichment Project by Elie Azeraf for IBM',
    license=license,
    python_requires='>=3.5',
    packages=find_packages(),
    install_requires=reqs.strip().split('\n'),
)
