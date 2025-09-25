import marimo

__generated_with = "0.15.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **1. Programming terminology**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Fix the syntax

    O programa a seguir contém vários erros de sintaxe. Corrija o programa para que a sintaxe fique em ordem e o programa funcione conforme especificado nos exemplos abaixo.
    ```python
    number = input("Please type in a number: ")
      if number>100
        print("The number was greater than one hundred")
        number - 100
        print("Now its value has decreased by one hundred)
         print("Its value is now"+ number)
     print(number + " must be my lucky number!")
     print("Have a nice day!)
    ```

    ```none
    Please type in a number: 13
    13 must be my lucky number!
    Have a nice day!

    Please type in a number: 101
    The number was greater than one hundred
    Now its value has decreased by one hundred
    Its value is now 1
    1 must be my lucky number!
    Have a nice day!
    ```
    ///
    """
    )
    return


@app.cell(disabled=True)
def _():
    # My Solution
    number = int(input("Please type in a number: "))
    if number > 100:
      print("The number was greater than one hundred")
      number = number - 100
      print("Now its value has decreased by one hundred")
      print("Its value is now " + str(number))
    print(str(number) + " must be my lucky number!")
    print("Have a nice day!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Number of characters

    A função `len` pode ser usada para descobrir o comprimento de uma string, entre outras coisas. A função retorna o número de caracteres em uma string.

    Alguns exemplos de como isso funciona:
    ```python
    word = "abcd"
    print(len(word))

    print(len("hi there"))

    word2 = "howdydoody"
    length = len(word2)
    print(length)

    empty_string = ""
    length = len(empty_string)
    print(length)
    ```
    ```none
    4
    8
    10
    0
    ```
    Escreva um programa que peça ao usuário uma palavra e, em seguida, imprima o número de caracteres, caso mais de um tenha sido digitado.

    Exemplos de comportamento esperado:
    ```none
    Please type in a word: hey
    There are 3 letters in the word hey
    Thank you!

    Please type in a word: b
    Thank you!
    ```
    ///
    """
    )
    return


@app.cell(disabled=True)
def _():
    # My Solution
    _word = input('Please type in a word: ')
    if len(_word) > 1:
        print(f'There are {len(_word)} letters in the word {_word}')
    print('Thank you!')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Typecasting

    Ao programar em Python, frequentemente precisamos alterar o tipo de dado de um valor. Por exemplo, um número de ponto flutuante pode ser convertido em um inteiro com a função `int`:
    ```python
    temperature = float(input("Please type in a temperature: "))
    print("The temperature is", temperature)
    print("...and rounded down it is", int(temperature))
    ```
    ```output
    Please type in a temperature: 5.15
    The temperature is 5.15
    ...and rounded down it is 5
    ```
    Observe que a função sempre arredonda para baixo, e não de acordo com as regras de arredondamento da matemática. Este é um exemplo de uma _floor function_.

    Escreva um programa que solicite ao usuário um número de ponto flutuante e, em seguida, imprima a parte inteira e a parte decimal separadamente. Use a função `int` do Python.

    Você pode assumir que o número fornecido pelo usuário é sempre maior que zero.

    Um exemplo de comportamento esperado:
    ```none
    Please type in a number: 1.34
    Integer part: 1
    Decimal part: 0.34
    ```
    ///
    """
    )
    return


@app.cell(disabled=True)
def _():
    # My Solution
    _n = float(input('Please type in a number: '))
    _integer = int(_n)
    _decimal = _n - _integer

    print('Integer part: ', _integer)
    print('Decimal part: ', _decimal)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **2. More conditionals**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r""" """)
    return


if __name__ == "__main__":
    app.run()
