# Treinamento-Controle-2022
Repositório utilizado para o treinamento do Controle e Estratégia 2022

# Instalação

Primeiramente, para a instalação correta do nosso repositório, é necessário realizar a instalação do [FIRASim](https://github.com/IEEEVSS/FIRASim) e do [VSSReferee](https://github.com/VSSSLeague/VSSReferee), se atentando a todos os seus requisitos.

Você pode conferir o passo-a-passo da instalação [aqui](SETUP.md)

Após a instalação das dependências acima, clone esse repositório no diretório em que vocês instalaram o FIRASim e o VSSReferee por meio de:

```sh
git clone https://github.com/Red-Dragons-UFSCar/Treinamento-Controle-2022
```

Por seguinte, ao clonar esse repositório, instale nossas dependências do python utilizando:

```sh
pip3 install -r requirements.txt
```

Para gerar os arquivos de comunicação entre o código em Python e o simulador em C++, execute no repositório local os seguintes comandos:

```sh
mkdir build
cd build
qmake ..
make
```
