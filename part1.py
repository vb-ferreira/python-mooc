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


@app.cell
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Times five

    Escreva um programa que peça um número ao usuário. O programa então imprime o número multiplicado por cinco.

    O programa deve funcionar da seguinte forma:
    ```none
    Please type in a number: 3
    3 times 5 is 15
    ```
    ///
    """
    )
    return


@app.cell(disabled=True)
def _():
    # My Solution
    _n = int(input('Please type a number: '))
    print(f'{_n} times 5 is {_n * 5}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Name and age

    Escreva um programa que pergunte ao usuário seu nome e ano de nascimento. O programa então imprime a seguinte mensagem:
    ```none
    What is your name? Frances Fictitious
    Which year were you born? 1990
    Hi Frances Fictitious, you will be 31 years old at the end of the year 2021
    ```
    ///
    """
    )
    return


@app.cell(disabled=True)
def _():
    _name = input('What is your name? ')
    _age = int(input('Which year were you born? '))
    print(f'Hi {_name}, you will be {2021 - _age} years old at the end of the year 2021')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Seconds in a day

    Escreva um programa que solicite ao usuário um número de dias. O programa então imprime o número de segundos correspondente à quantidade de dias fornecida.

    O programa deve funcionar da seguinte forma:
    ```none
    How many days? 1
    Seconds in that many days: 86400
    ```
    ///
    """
    )
    return


@app.cell(disabled=True)
def _():
    # My Solution
    _days = int(input('How many days? '))
    print(f'Seconds in that many thays: {_days * 24 * 60 * 60}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Fix the code: Product

    Este programa solicita ao usuário três números. O programa então imprime o produto, ou seja, os números multiplicados entre si. No entanto, há algo errado com o programa — ele não funciona direito, como você pode ver ao executá-lo. Por favor, corrija.

    Um exemplo da execução esperada do programa:
    ```none
    Please type in the first number: 2
    Please type in the second number: 3
    Please type in the third number: 5
    The product is 30
    ```
    ///
    """
    )
    return


@app.cell(disabled=True)
def _():
    # My Solution
    _number1 = int(input("Please type in the first number: "))
    _number2 = int(input("Please type in the second number: "))
    _number3 = int(input("Please type in the third number: "))

    _product = _number1 * _number2 * _number3

    print("The product is", _product)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Sum and product

    Escreva um programa que peça ao usuário dois números. O programa então imprimirá a soma e o produto dos dois números.

    O programa deve funcionar da seguinte forma:
    ```none
    Number 1: 3
    Number 2: 7
    The sum of the numbers: 10
    The product of the numbers: 21
    ```
    ///
    """
    )
    return


@app.cell(disabled=True)
def _():
    # My Solution
    _n1 = int(input('Number 1: '))
    _n2 = int(input('Number 2: '))

    print(f'The sum of the numbers: {_n1 + _n2}')
    print(f'The product of the numbers: {_n1 * _n2}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Sum and mean

    Escreva um programa que peça ao usuário quatro números. O programa então imprime a soma e a média dos números.

    O programa deve funcionar da seguinte forma:
    ```none
    Number 1: 2
    Number 2: 1
    Number 3: 6
    Number 4: 7
    The sum of the numbers is 16 and the mean is 4.0
    ```
    ///
    """
    )
    return


@app.cell(disabled=True)
def _():
    # My Solution
    _n1 = int(input('Number 1: '))
    _n2 = int(input('Number 2: '))
    _n3 = int(input('Number 3: '))
    _n4 = int(input('Number 4: '))

    _soma = _n1 + _n2 + _n3 + _n4

    print(f'The sum of the numbers is {_soma} and the mean is {_soma / 4}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Food expenditure
    Escreva um programa que estime o gasto típico de um usuário com alimentação.

    O programa pergunta ao usuário quantas vezes por semana ele come no refeitório estudantil. Em seguida, pergunta o preço de um almoço típico de estudante e o valor gasto com compras de supermercado durante a semana.

    Com base nessas informações, o programa calcula o gasto típico de um usuário com alimentação, tanto semanal quanto diária.

    O programa deve funcionar da seguinte forma:
    ```none
    How many times a week do you eat at the student cafeteria? 4
    The price of a typical student lunch? 2.5
    How much money do you spend on groceries in a week? 28.5

    Average food expenditure:
    Daily: 5.5 euros
    Weekly: 38.5 euros
    ```
    ///
    """
    )
    return


@app.cell(disabled=True)
def _():
    # My Solution
    _weeks = int(input('How many times a week do you eat at the student cafeteria? '))
    _price = float(input('The price of a typical student lunch? '))
    _money = float(input('How much money do you spend on groceries in a week? '))

    _weekly = (_weeks * _price) + _money
    _daily = _weekly / 7

    print('Average food expenditure:')
    print(f'Daily: {_daily} euros')
    print(f'Weekly: {_weekly} euros')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Students in groups ⚓

    Escreva um programa que solicite o número de alunos em um curso e o tamanho desejado do grupo. O programa então imprimirá o número de grupos formados a partir dos alunos do curso. Se a divisão não for par, um dos grupos pode ter menos membros do que o especificado.

    Se você não conseguir fazer seu código funcionar como esperado, não há problema algum em prosseguir e retornar a este exercício mais tarde. O tópico da próxima seção são instruções condicionais. Este exercício também pode ser resolvido usando uma construção condicional.
    ```none
    How many students on the course? 8
    Desired group size? 4
    Number of groups formed: 2
    ```

    ```none
    How many students on the course? 11
    Desired group size? 3
    Number of groups formed: 4
    ```
    **Dica**: o operador de divisão inteira `//` pode ser útil aqui.
    ///
    """
    )
    return


@app.cell(disabled=True)
def _():
    # My Solution
    _n = int(input('How many students on the course? '))
    _s = int(input('Desired group size? '))

    _r = (_n//_s) + bool(_n - (_s * (_n//_s)))

    print(f'Number of groups formed: {_r}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// details | **Model Solution**
        type: info

    ```python
    students = int(input("How many students on the course? "))
    group_size = int(input("Desired group size? "))

    groups = (students + group_size - 1) // group_size

    print("Number of groups formed:", groups)
    ```
    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **5. Conditional statements**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Orwell

    Escreva um programa que peça ao usuário um número inteiro. O programa deve imprimir "Orwell" se o número for exatamente 1984, caso contrário, não fará nada.
    ```none
    Please type in a number: 2020
    Please type in a number: 1984
    Orwell
    ```
    ///
    """
    )
    return


@app.cell(disabled=True)
def _():
    # My Solution
    _n = int(input('Please type in a number: '))

    if _n == 1984:
        print('Orwell')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Absolute value

    Escreva um programa que peça ao usuário um número inteiro. Se o número for menor que zero, o programa deve imprimir o número multiplicado por -1. Caso contrário, o programa imprime o número como ele está. Veja os exemplos de comportamento esperado abaixo.
    ```none
    Please type in a number: -7
    The absolute value of this number is 7

    Please type in a number: 1
    The absolute value of this number is 1
    ```
    ///
    """
    )
    return


@app.cell(disabled=True)
def _():
    # My Solution
    _n = int(input('Please type in a number: '))

    if _n < 0:
        _n *= -1

    print('The absolute value of this number is', _n)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Soup or no soup

    Escreva um programa que peça o nome do usuário. Se o nome for qualquer coisa diferente de "Jerry", o programa solicitará o número de porções e exibirá o custo total. O preço de uma porção individual é 5,90.

    Dois exemplos da execução do programa:
    ```none
    Please tell me your name: Kramer
    How many portions of soup? 2
    The total cost is 11.8
    Next please!

    Please tell me your name: Jerry
    Next please!
    ```
    ///
    """
    )
    return


@app.cell(disabled=True)
def _():
    # My Solution
    _name = input('Please tell me your name: ')

    if _name != 'Jerry':
        _portions = int(input('How many portions of soup? '))
        print(f'The total cost is {_portions * 5.9}')

    print('Next please!')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Order of magnitude

    Escreva um programa que peça ao usuário um número inteiro. O programa deve então imprimir a magnitude do número, conforme os exemplos a seguir.
    ```none
    Please type in a number: 950
    This number is smaller than 1000
    Thank you!

    Please type in a number: 59
    This number is smaller than 1000
    This number is smaller than 100
    Thank you!

    Please type in a number: 2
    This number is smaller than 1000
    This number is smaller than 100
    This number is smaller than 10
    Thank you!

    Please type in a number: 1123
    Thank you!
    ```
    ///
    """
    )
    return


@app.cell(disabled=True)
def _():
    # My Solution
    _n = int(input('Please type in a number: '))

    if _n < 1000:
        print('This number is smaller than 1000')

    if _n < 100:
        print('This number is smaller than 100')

    if _n < 10:
        print('This number is smaller than 10')

    print('Thank you!')

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Calculator

    Escreva um programa que peça ao usuário dois números e uma operação. Se a operação for adição, multiplicação ou subtração, o programa deve calcular e imprimir o resultado da operação com os números fornecidos. Se o usuário digitar qualquer outra coisa, o programa não deve imprimir nada.

    Alguns exemplos de comportamento esperado:
    ```none
    Number 1: 10
    Number 2: 17
    Operation: add

    10 + 17 = 27
    ```
    ///
    """
    )
    return


@app.cell(disabled=True)
def _():
    # My Solution
    _n1 = int(input('Number 1: '))
    _n2 = int(input('Number 2: '))

    _operation = input('Operation: ')

    if _operation == 'add':
        print(f'{_n1} + {_n2} = {_n1 + _n2}')
    if _operation == 'subtract':
        print(f'{_n1} - {_n2} = {_n1 - _n2}')
    if _operation == 'multiply':
        print(f'{_n1} * {_n2} = {_n1 * _n2}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Termperatures

    Escreva um programa que peça ao usuário a temperatura em graus Fahrenheit e, em seguida, imprima a mesma em graus Celsius. Se a temperatura convertida cair abaixo de zero grau Celsius, o programa também deverá imprimir "Brr! It's cold in here!".

    A fórmula para converter graus Fahrenheit para graus Celsius pode ser facilmente encontrada em qualquer mecanismo de busca de sua escolha.

    Dois exemplos de comportamento esperado:
    ```none
    Please type in a temperature (F): 101
    101 degrees Fahrenheit equals 38.333333333333336 degrees Celsius

    Please type in a temperature (F): 21
    21 degrees Fahrenheit equals -6.111111111111111 degrees Celsius
    Brr! It's cold in here!
    ```
    ///
    """
    )
    return


@app.cell(disabled=True)
def _():
    # My Solution
    _tf = int(input('Please type in a temperature (F): '))

    _tc = (5 / 9) * (_tf - 32)

    print(f'{_tf} degrees Fahrenheit equals {_tc} degrees Celsius')

    if _tc < 0: 
        print("Brr! It's cold in here!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Daily wages

    Escreva um programa que solicite o salário por hora, as horas trabalhadas e o dia da semana. O programa deve então imprimir os salários diários, que são iguais ao salário por hora multiplicado pelas horas trabalhadas, exceto aos domingos, quando o salário por hora é dobrado.
    ```none
    Hourly wage: 8.5
    Hours worked: 3
    Day of the week: Monday
    Daily wages: 25.5 euros

    Hourly wage: 12.5
    Hours worked: 10
    Day of the week: Sunday
    Daily wages: 250.0 euros
    ```
    ///
    """
    )
    return


@app.cell(disabled=True)
def _():
    # My Solution
    _s = float(input('Hourly wage: '))
    _h = float(input('Hours worked: '))
    _d = input('Day oh the week: ')

    if _d == 'Sunday':
        print(f'Daily wages: {_s * _h * 2} euros')
    else:
        print(f'Daily wages: {_s * _h} euros')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | What to wear tomorrow

    Escreva um programa que peça a previsão do tempo para amanhã e, em seguida, sugira roupas adequadas ao clima.

    A sugestão deve mudar se a temperatura (medida em graus Celsius) estiver acima de 20, 10 ou 5 graus, e também se houver chuva no radar.

    Alguns exemplos de comportamento esperado:
    ```none
    What is the weather forecast for tomorrow?
    Temperature: 21
    Will it rain (yes/no): no
    Wear jeans and a T-shirt

    What is the weather forecast for tomorrow?
    Temperature: 11
    Will it rain (yes/no): no
    Wear jeans and a T-shirt
    I recommend a jumper as well

    What is the weather forecast for tomorrow?
    Temperature: 7
    Will it rain (yes/no): no
    Wear jeans and a T-shirt
    I recommend a jumper as well
    Take a jacket with you

    What is the weather forecast for tomorrow?
    Temperature: 3
    Will it rain (yes/no): yes
    Wear jeans and a T-shirt
    I recommend a jumper as well
    Take a jacket with you
    Make it a warm coat, actually
    I think gloves are in order
    Don't forget your umbrella!
    ```

    ///
    """
    )
    return


@app.cell(disabled=True)
def _():
    # My Solution
    print('What is the weather forecast for tomorrow?')
    _t = int(input('Temperature: '))
    _r = input('Will it rain (yes/no): ')

    print("Wear jeans and a T-shirt")

    if _t <= 20:
        print("I recommend a jumper as well")

    if _t <= 10:
        print("Take a jacket with you")

    if _t <= 5:
        print("Make it a warm coat, actually")
        print("I think gloves are in order")


    if _r == 'yes':
        print("Don't forget your umbrella!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Solving a quadratic equation

    Escreva um programa para resolver uma equação quadrática da forma ax² + bx + c. O programa solicita os valores a, b e c. Ele deve então usar a fórmula quadrática para resolver a equação. A fórmula quadrática expressa com a função sqrt do Python é a seguinte:
    ```none
    x = (-b ± sqrt(b² - 4ac))/(2a).
    ```
    Você pode assumir que a equação sempre terá duas raízes reais, então a fórmula acima sempre funcionará.

    Um exemplo de comportamento esperado:
    ```none
    Value of a: 1
    Value of b: 2
    Value of c: -8

    The roots are 2.0 and -4.0
    ```
    ///
    """
    )
    return


@app.cell
def _():
    # My Solution
    from math import sqrt

    _a = int(input('Value of a: '))
    _b = int(input('Value of b: '))
    _c = int(input('Value of c: '))

    _r1 = (-_b + sqrt(_b**2 - 4*_a*_c))/ (2 * _a)
    _r2 = (-_b - sqrt(_b**2 - 4*_a*_c))/ (2 * _a)

    print(f'The roots are {_r1} and {_r2}')
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
