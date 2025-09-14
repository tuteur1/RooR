# setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='Eurocybersecurite-AI-Cybersecurity',
    version='0.2.2',
    description='AI-powered cybersecurity application by Eurocybersecurite',
    long_description=long_description,
    long_description_content_type="text/markdown",

    # ✅ Infos auteur
    author='Eurocybersecurite',
    author_email='mohamed.abdessemed@eurocybersecurite.fr',

    # ✅ Page du projet (homepage principale)
    url='https://github.com/Eurocybersecurite/Eurocybersecurite-AI-Cybersecurity',

    # ✅ Tu peux aussi ajouter plusieurs liens utiles
    project_urls={
        "Documentation": "https://github.com/Eurocybersecurite/Eurocybersecurite-AI-Cybersecurity/wiki",
        "Source": "https://github.com/Eurocybersecurite/Eurocybersecurite-AI-Cybersecurity",
        "Issues": "https://github.com/Eurocybersecurite/Eurocybersecurite-AI-Cybersecurity/issues",
    },

    license='MIT',
    packages=find_packages(where='RooR'),
    include_package_data=True,
    install_requires=[
        "flask",
        "transformers",
        "torch",
        "scikit-learn"
    ],
    entry_points={
        'console_scripts': [
            'cybersecurity=main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='cybersecurity, audit, remediation, flask, python',
    python_requires='>=3.11',
)
