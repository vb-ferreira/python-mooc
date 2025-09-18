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
    mo.md(r"""## **1.1 A program of multiple commands**""")
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


@app.cell(disabled=True)
def _():
    # My Solution
    _username = input('What is your name? ')
    print(_username)
    print(_username)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **2.1 More than one input**""")
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


@app.cell(disabled=True)
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


@app.cell(disabled=True)
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


@app.cell(disabled=True)
def _():
    # My Solution
    _name = input('Please type in a name: ')
    _year = input('Please type in a year: ')

    print(_name + " is a valiant knight, born in the year " + _year + ". One morning " + _name + " woke up to an awful racket: a dragon was approaching the village. Only " + _name + " could save the village's residents.")
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


@app.cell(disabled=True)
def _():
    # My Solution
    _name = input('What is your name? ')
    print('!' + _name + '!' + _name + '!')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **3 More about variables**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **3.1 Printing with f-strings**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Extra space

    Sua amiga está trabalhando em um aplicativo para quem procura emprego. Ela lhe envia este trecho de código:
    ```python
    name = "Tim Tester"
    age = 20
    skill1 = "python"
    level1 = "beginner"
    skill2 = "java"
    level2 = "veteran"
    skill3 = "programming"
    level3 = "semiprofessional"
    lower = 2000
    upper = 3000

    print("my name is ", name, " , I am ", age, "years old")
    print("my skills are")
    print("- ", skill1, " (", level1, ")")
    print("- ", skill2, " (", level2, ")")
    print("- ", skill3, " (", level3, " )")
    print("I am looking for a job with a salary of", lower, "-", upper, "euros per month")
    ```
    O programa deve imprimir exatamente o seguinte:
    ```none
    my name is Tim Tester, I am 20 years old

    my skills are
     - python (beginner)
     - java (veteran)
     - programming (semiprofessional)

    I am looking for a job with a salary of 2000-3000 euros per month
    ```
    O código funciona quase corretamente, mas não completamente. Este exercício possui testes muito rigorosos, que verificam a saída para cada bit de espaço em branco.

    Corrija o código para que a impressão pareça correta. Observe especialmente como a notação de vírgula no comando `print` insere automaticamente um espaço ao redor das diferentes partes separadas por vírgula.

    A maneira mais fácil de transformar o código para que ele atenda aos requisitos é usar **f-strings**.

    **Dica**: você pode imprimir uma linha vazia adicionando um comando `print` vazio ou adicionando o caractere de quebra de linha `\n` à sua string.
    ///
    """
    )
    return


@app.cell
def _():
    # My Solution
    name = "Tim Tester"
    age = 20
    skill1 = "python"
    level1 = "beginner"
    skill2 = "java"
    level2 = "veteran"
    skill3 = "programming"
    level3 = "semiprofessional"
    lower = 2000
    upper = 3000

    print(f"my name is {name}, I am {age} years old\n")
    print("my skills are")
    print(f" - {skill1} ({level1})")
    print(f" - {skill2} ({level2})")
    print(f" - {skill3} ({level3})\n")
    print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **3.2 Floating point numbers**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Arithmetics

    Este programa já contém duas variáveis ​​inteiras, `x` e `y`:
    ```python
    x = 27
    y = 15
    ```

    Por favor, complete o programa para que ele também imprima o seguinte:
    ```none
    27 + 15 = 42
    27 - 15 = 12
    27 * 15 = 405
    27 / 15 = 1.8
    ```
    ///
    """
    )
    return


@app.cell
def _():
    # My Solution
    x = 27
    y = 15

    print(f'{x} + {y} = {x + y}')
    print(f'{x} - {y} = {x - y}')
    print(f'{x} * {y} = {x * y}')
    print(f'{x} / {y} = {x / y}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Fix the code: Print a single line

    Cada comando `print` geralmente imprime uma linha própria, completa com uma mudança de linha no final. No entanto, se ele receber um argumento adicional `end = ""`, ele não imprimirá uma mudança de linha.

    Por exemplo:
    ```python
    print("Hi ", end="")
    print("there!")
    ```

    ```none
    # output
    Hi there!
    ```
    Por favor, corrija este programa para que todo o cálculo, incluindo o resultado, seja impresso em uma única linha. Não altere o número de comandos `print` utilizados.
    ```python
    print(5)
    print(" + ")
    print(8)
    print(" - ")
    print(4)
    print(" = ")
    print(5 + 8 - 4)
    ```
    ///
    """
    )
    return


@app.cell
def _():
    # My Solution
    print(5, end='')
    print(" + ", end='')
    print(8, end='')
    print(" - ", end='')
    print(4, end='')
    print(" = ", end='')
    print(5 + 8 - 4)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **4. Arithmetic operations**""")
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
