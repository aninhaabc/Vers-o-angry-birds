from setuptools import setup, find_packages
import os

# Lendo o conteúdo do README.md para usar como descrição longa
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Função para coletar arquivos de uma pasta específica
def package_files(directory):
    paths = []
    for (path, _ , filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join(path,filename))
    return paths

imagens_file = package_files('imagens')
fonte_file = package_files('fonte')

setup(
    name="Versao-angry-birds",  # Substitua pelo nome do seu pacote   
    version="0.1.0",
    author="Ana Beatriz da Cunha",
    author_email="anabc1@al.insper.edu.br",
    description="Jogo para analisar a fisica e a algebra linear por trás de uma versão de angry birds",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aninhaabc/Versao-angry-birds",  # URL do repositório do seu projeto (se houver)
    packages=find_packages(),  # Encontra automaticamente todos os pacotes no diretório
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
    entry_points={
        'console_scripts': [
            'ana_patinho_vs_gatinho=jogo.tela_jogo:main',
        ],
    },
    install_requires=[  # Instala as dependências especificadas no requirements.txt
        line.strip() for line in open("requirements.txt").readlines()
    ],

    include_package_data=True,
    package_data={
        '': imagens_file + fonte_file
    }
)