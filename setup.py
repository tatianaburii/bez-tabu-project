from setuptools import setup, find_packages

setup(
    name="bez_tabu",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "bez-tabu=bez_tabu.cli:main",  # якщо точка входу в cli.py
        ]
    },
    author="Andrii Tikhyi, Tetiana Burii, Vladyslav Sarbash, Oleksandr Konovaliuk",
    description="Personal assistant CLI for address book and notes",
)
