import marimo

__generated_with = "0.15.5"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **1. Getting Started**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Vamos começar a programar nos familiarizando com o comando `print`, que imprime texto. Nesse contexto, imprimir significa essencialmente que o programa exibirá algum texto na tela.

    O programa a seguir imprimirá "Olá!" na tela:
    """
    )
    return


@app.cell
def _():
    print('Olá!')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""O programa não funcionará a menos que o código seja escrito **exatamente** como está acima. Por exemplo, tentar executar o comando `print` sem as aspas, como mostrado a seguir lançará um **erro de sintaxe**.""")
    return


app._unparsable_cell(
    r"""
    print(Olá!)
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Em resumo, se você quiser imprimir um **texto**, ele deve estar todo **entre aspas**, caso contrário o Python não o interpretará corretamente.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Emoticon

    Escreva um programa que imprima um emoticon: `:-)`
    ///
    """
    )
    return


@app.cell
def _():
    # My Solution
    print(':-)')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **1.2 A program of multiple commands**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Vários comandos escritos em sucessão serão executados **em ordem**, do primeiro ao último.""")
    return


@app.cell
def _():
    print("Welcome to Introduction to Programming!")
    print("First we will practice using the print command.")
    print("This program prints three lines of text on the screen.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Fix the code: Seven Brothers

    "Seitsemän veljestä" é um dos primeiros romances já escritos em finlandês. É a história de sete irmãos órfãos aprendendo a se virar no mundo.

    Este programa deveria imprimir os nomes dos irmãos em ordem alfabética, mas ainda não está funcionando direito. Por favor, corrijam o programa para que os nomes sejam impressos na ordem correta.
    ```python

    print("Simeoni")
    print("Juhani")
    print("Eero")
    print("Lauri")
    print("Aapo")
    print("Tuomas")
    print("Timo")
    ```
    ///
    """
    )
    return


@app.cell
def _():
    # My Solution
    print("Aapo")
    print("Eero")
    print("Juhani")
    print("Lauri")
    print("Simeoni")
    print("Timo")
    print("Tuomas")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Row, Row, Row Your Boat

    Por favor, escreva um programa que imprima as seguintes linhas exatamente como estão escritas a seguir:

    ```none
    Row, row, row your boat,
    Gently down the stream.
    Merrily, merrily, merrily, merrily,
    Life is but a dream.
    ```
    ///
    """
    )
    return


@app.cell
def _():
    # My Solution
    print('Row, row, row your boat,')
    print('Gently down the stream.')
    print('Merrily, merrily, merrily, merrily,')
    print('Life is but a dream.')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **1.2 Arithmetic operations**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Você também pode inserir operações aritméticas dentro de um comando `print`. Executá-lo imprimirá o **resultado** da operação.""")
    return


@app.cell
def _():
    print(2 + 5)
    print(3 * 3)
    print(2 + 2 * 10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Observe a ausência de aspas nas operações aritméticas acima. As aspas são usadas para indicar **strings**. No contexto da programação, strings são **sequências de caracteres**. Elas podem consistir em letras, números e quaisquer outros tipos de caracteres, como pontuação. As strings geralmente são impressas exatamente como são escritas. Portanto, os dois comandos a seguir produzem dois resultados bastante diferentes:""")
    return


@app.cell
def _():
    print(2 + 2 * 10)
    print("2 + 2 * 10")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **1.3 Commenting**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Qualquer linha que comece com o símbolo `#` é um comentário. Isso significa que qualquer texto nessa linha após o símbolo `#` não afetará de forma alguma o funcionamento do programa. O Python simplesmente o ignorará.

    Comentários são usados para explicar como um programa funciona, tanto para o próprio programador quanto para outras pessoas que leem o código. Neste programa, um comentário explica o cálculo realizado no código:
    """
    )
    return


@app.cell
def _():
    print("Hours in a year:")
    # there are 365 days in a year and 24 hours in each day
    print(365*24)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Minutes in a year

    Escreva um programa que imprima o número de minutos em um ano. Use código Python para realizar o cálculo, como no exemplo anterior.
    ///
    """
    )
    return


@app.cell
def _():
    # My Solution
    print('Minutos no ano:')
    print(365*24*60)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Print some code

    Até agora, você provavelmente usou aspas duplas `"` para imprimir strings. Além das aspas duplas, o Python também aceita aspas simples `'`.

    Isso é útil se você quiser imprimir as aspas em si. Por favor, escreva um programa que imprima o seguinte:
    ```none
    print("Hello there!")
    ```
    ///
    """
    )
    return


@app.cell
def _():
    # My Solution
    print('print("Hello there!")')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **2. Information from the user**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    O termo "input" refere-se a qualquer informação que um usuário fornece ao programa. O comando Python `input` lê uma linha de entrada digitada pelo usuário. Ele também pode ser usado para exibir uma mensagem ao usuário, solicitando uma entrada específica.

    O programa a seguir lê o nome do usuário com o comando `input`. Em seguida, ele o imprime com o comando `print`:
    """
    )
    return


@app.cell
def _():
    _name = input("What is your name? ")
    print("Hi there, " + _name)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Name twice

    Escreva um programa que peça o nome do usuário e o exiba duas vezes, em duas linhas consecutivas.

    Um exemplo de como o programa deve funcionar:
    ```none
    What is your name? Paul
    Paul
    Paul
    ```
    ///
    """
    )
    return


@app.cell
def _():
    # My Solution
    _username = input('What is your name? ')
    print(_username)
    print(_username)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **2.1 Referencing a variable**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **2.2 More than one input**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Se a mesma variável for usada para armazenar mais de uma entrada, cada novo valor **substituirá** o anterior. Isso significa que, se a mesma variável for usada para armazenar duas entradas em sucessão, não há como acessar o primeiro valor de entrada após ele ter sido substituído pelo segundo.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Name and address

    Escreva um programa que solicite o nome e o endereço do usuário. O programa também deve imprimir as informações fornecidas, da seguinte forma:
    ```none
    Given name: Steve
    Family name: Sanders
    Street address: 91 Station Road
    City and postal code: London EC05 6AW
    Steve Sanders
    91 Station Road
    London EC05 6AW
    ```

    ///
    """
    )
    return


@app.cell
def _():
    # My Solution
    _gname = input('Given name: ')
    _fname = input('Family name: ')
    _street = input('Street address: ')
    _city = input('City and postal code: ')

    print(_gname + ' ' + _fname)
    print(_street)
    print(_city)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Fix the code: Utterances
    Aqui está um programa que deve solicitar três declarações e imprimi-las, assim:
    ```none
    The 1st part: hickory
    The 2nd part: dickory
    The 3rd part: dock
    hickory-dickory-dock!
    ```

    No entanto, há algo errado com o código abaixo. Por favor, corrija.
    ///
    """
    )
    return


@app.cell
def _():
    # My Solution
    part1 = input("The 1st part: ")
    part2 = input("The 2st part: ")
    part3 = input("The 3st part: ")
    print(part1 + '-' + part2 + '-' + part3 + '!')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Story

    Escreva um programa que imprima a seguinte história. O usuário informa um nome e um ano, que devem ser inseridos no texto.
    ```none
    Please type in a name: Mary
    Please type in a year: 1572

    Mary is a valiant knight, born in the year 1572. One morning Mary woke up to an awful racket: 
    a dragon was approaching the village. Only Mary could save the village's residents.
    ```
    ///
    """
    )
    return


@app.cell
def _():
    # My Solution
    _name = input('Please type in a name: ')
    _year = input('Please type in a year: ')

    print(_name + " is a valiant knight, born in the year " + _year + ". One morning " + _name + " woke up to an awful racket: a dragon was approaching the village. Only " + _name + " could save the village's residents.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Uma única variável pode ser referenciada muitas vezes em um programa.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Name and exclamation marks

    Escreva um programa que peça o nome do usuário e o imprima duas vezes em uma única linha, de modo que haja um ponto de exclamação no início da linha, outro entre os dois nomes e um terceiro no final da linha.

    O programa deve funcionar da seguinte forma:
    ```none
    What is your name? Paul
    !Paul!Paul!
    ```
    ///
    """
    )
    return


@app.cell
def _():
    # My Solution
    _name = input('What is your name? ')
    print('!' + _name + '!' + _name + '!')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **3 More about variables**""")
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **Dependencies**""")
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
