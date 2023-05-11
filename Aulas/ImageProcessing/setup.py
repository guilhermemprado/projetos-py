from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing-test",
    version="0.0.1",
    author="Guilherme Mattos Arruda de Paula Prado",
    author_email="guimattos1983@gmail.com",
    description="Test version - Image processing. This project belongs to Karina Tiemi Kato, Tech Lead, Machine Learning Engineer, Data Scientist Specialist at Take. This package is a demo for simulation of upload on the Test Pypi website, and it's from class of the Bootcamp developer full stack Python. E-mail:karinatkato@gmail.com.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guilhermemprado/projetos-py/tree/master/Aulas/ImageProcessing",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
