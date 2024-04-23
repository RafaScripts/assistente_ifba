# Assistente Virtual Chaves

O Assistente Virtual Chaves é um projeto escrito em Python que implementa um assistente virtual capaz de reconhecer comandos de voz e executar ações como abrir programas, fechar aplicativos e suspender o sistema.

## Estrutura do Projeto

O projeto está estruturado da seguinte forma:

- O arquivo principal do assistente virtual está localizado em `src/main.py`.
- As funções para execução de programas externos estão implementadas em `src/executate.py`.
- Os testes unitários estão localizados em `unit_tests/__tests__.py`.

## Como Usar

1. Clone este repositório em sua máquina:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

2. Certifique-se de ter o Python instalado em sua máquina. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

3. Navegue até o diretório do projeto:

```bash
cd nome-do-repositorio
```

4. Antes de executar o código, é importante ajustar todos os caminhos absolutos no código para corresponderem aos da sua máquina. Você pode encontrar esses caminhos nos arquivos `main.py` e `executate.py` no diretório `src`.

5. Além disso, se você estiver usando um sistema operacional diferente de macOS, pode ser necessário ajustar os nomes dos programas a serem executados. Certifique-se de alterar esses nomes nos arquivos mencionados acima, de acordo com o sistema operacional que você está utilizando. Se estiver usando Linux, ative a flag `isMac` para `False`.

6. Execute o arquivo principal do assistente virtual:

```bash
python src/main.py
```

7. Se desejar executar os testes unitários, você pode fazê-lo da seguinte maneira:

```bash
python -m unittest unit_tests/__tests__.py
```

## Observações

- Este projeto não foi ajustado para ser executado em sistemas Windows. Se você estiver usando Windows, pode ser necessário realizar ajustes adicionais para que o código funcione corretamente.

https://youtu.be/80ooTQf6gwc

video apresentando o codigo

---

Este `README.md` fornece uma visão geral do projeto e orienta o usuário sobre como configurar e executar o código em sua própria máquina. Certifique-se de adaptar as instruções conforme necessário e incluir quaisquer detalhes adicionais que você ache relevantes para os usuários do seu projeto.