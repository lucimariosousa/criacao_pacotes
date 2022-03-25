from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="preco-e-palavras",
    version="0.0.1",
    author="lucimario_sousa",
    author_email="lucimario_custodio@hotmail.com",
    description="Operacoes simples com numeros e palavras",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="my_github_repository_project_link"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)