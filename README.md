# DarkHats

Este pacote contém os arquivos do jogo e o script de inicialização. Siga as instruções abaixo para começar a jogar.

---

## Como Jogar

### Requisitos

* **Sistema Operacional:** Este jogo foi desenvolvido para Windows 7/10/11 ou Linux Mint/Ubuntu/Fedora/Arch
* **Processador:** Mínimo: Intel Celeron N3060 / AMD E1-2100 **(Linux é recomendado para melhor desempenho)** | Recomendado: Pentium 4
* **Memória RAM:** Mínimo: 64 MB | Recomendado: 128 / 256 MB
* **Placa de Vídeo:** Mínimo: Intel HD Graphics / AMD Radeon R2 | Recomendado: Qualquer GPU dedicada com suporte a OpenGL 2.0+
* **Armazenamento:** Mínimo: 100 MB livres | Recomendado: 300 MB livres

### Guia de Inicialização

*Windows*

1. **Abra a Pasta do Jogo**

   Navegue até o diretório onde você extraiu os arquivos do jogo. Você deverá encontrar dois itens principais:

   * Uma pasta chamada `game`
   * Um arquivo chamado `Game.bat`

2. **Execute o Arquivo**

   * Dê **dois cliques** em `Game.bat`
   * *Observação:* Uma janela preta de comando pode aparecer por alguns instantes. **Não a feche imediatamente.** Se ela fechar sozinha muito rápido, ocorreu algum erro.

3. **Jogue**

   * Assim que a janela terminar de baixar todas as dependências necessárias, o jogo será iniciado automaticamente.

4. **Executando Novamente**

   * Depois que todos os requisitos forem instalados, eles não serão baixados novamente.

*Linux / macOS*

1. **Abra a Pasta do Jogo**

   Navegue até o diretório onde você extraiu os arquivos do jogo. Você deverá encontrar:

   * Uma pasta chamada `game`

2. **Verificando o Diretório do Jogo**

   Ao abrir a pasta `Game`, você deverá ver:

   * 7 pastas chamadas `__pycache__`, `Attacks`, `Backup`, `Classes`, `Items`, `Main` e `Sounds`
   * 4 arquivos, incluindo um chamado `requirements.txt`

   Se esses itens estiverem presentes, você está na pasta correta.

   Clique na barra de endereço do gerenciador de arquivos e copie o caminho da pasta. Ele deve ser semelhante a:

   * `/home/hydro/Workspace/DarkHats-1/Game` (exemplo)

3. **Instalando as Dependências**

   Após copiar o caminho da pasta, abra o Terminal e execute:

```bash
$ sudo dnf install python3-pip
$ cd Workspace/DarkHats-1/Game
$ python3 -m pip install -r requirements.txt
```

4. **Executando o Jogo**

   Depois que as dependências forem instaladas, execute:

```bash
$ cd Main
$ python3 Menu.py
```

5. **Jogue**

   * Após executar o comando, o jogo deverá iniciar normalmente.

*É bem mais fácil jogar no windows...*

---

## Solução de Problemas

### "A janela do jogo abre e aparece 'No module named pygame'"

Isso geralmente significa que o script não conseguiu localizar o módulo `pygame`.

* **Verifique:** Certifique-se de estar usando a versão mais recente e de que todos os arquivos estejam corretamente dentro da pasta do jogo.
* **Verifique:** Certifique-se de não ter alterado o nome da pasta principal (como `DarkHats` ou `Game`).

### "Acesso Negado" ou "Erro de Permissão"

Se aparecer algum erro relacionado a permissões:

1. Clique com o botão direito em `Game.bat`
2. Selecione **Executar como administrador**

---

## Notas do Desenvolvedor

* **Estrutura de Pastas:** O inicializador espera que a pasta `Game` esteja localizada no diretório principal. Mover arquivos ou alterar a estrutura pode causar erros.
* **Antivírus:** Alguns softwares de segurança podem sinalizar arquivos `.bat` ou executáveis incluídos no jogo. Caso isso aconteça, adicione a pasta do jogo às exceções do antivírus.

---

**Divirta-se!**

---

# Área do Desenvolvedor

## Guia de Modificações (Mods)

> **Importante:** Sempre faça backup dos arquivos originais antes de modificá-los.

---

### Como Criar Mods

1. Dentro da pasta principal do jogo existem diretórios como `Main`, `Classes`, `Items`, entre outros. Eles contêm todos os arquivos responsáveis pelo funcionamento do jogo (**arquivos .py**).

2. Para modificar algo, basta alterar atributos como nome, dano ou ataques. Exemplo:

```python
class ExampleClass:
    def __init__(self):
        self.raceName = "Nome de Exemplo"
        self.Integrity = 85
        # etc...

        self.Attacks = {
            "Ataque de Exemplo": 40,
            # etc...
        }

        self.active_cooldowns = {
            "Ataque de Exemplo": 1
        }
```

* **Observação:** Nunca altere o nome da classe (`class ExampleClass`) sem também modificá-lo ou adicioná-lo ao arquivo `Menu`.
* O mesmo vale para os `SpecialAttacks`.

3. Divirta-se criando mods! O jogo foi feito para ser simples de modificar.

*Caso tenha algum problema ou dúvida, fique a vontade para me chamar pelo Discord!*

**Discord:** `marley21511`
