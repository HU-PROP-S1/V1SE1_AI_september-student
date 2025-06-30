#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt


"""
Oriëntatie op AI

Opdracht: Data science

(c) 2025 Hogeschool Utrecht,
Peter van den Berg (peter.vandenberg@hu.nl)

Opdracht:
Werk onderstaande functies uit. Elke functie krijgt een niet-lege en
ongesorteerde lijst *lst* met gehele getallen (int) als argument.
Voeg commentaar toe om je code toe te lichten.

Je kunt je functies testen met het gegeven raamwerk door het bestand
uit te voeren (of met behulp van `pytest`, als je weet hoe dat werkt).
Lever je werk in op Canvas als alle tests slagen.

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""

# TODO: Vul hier je naam, klas en studentnummer in.
naam = ""
klas = ""
studentnummer = -1


"""
1. Implementatie mean
    Implementeer onderstaande functie om het gemiddelde van een lijst getallen te berekenen.

"""
def mean(lst):
    """
    Bepaal het gemiddelde van een lijst getallen.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        float: Het gemiddelde van de gegeven getallen.
    """
    return


"""
2. Implementatie q1
    Implementeer onderstaande functie om het eerste kwartiel van een lijst getallen te berekenen.
    
"""
def q1(lst):
    """
    Bepaal het eerste kwartiel Q1 van een lijst getallen.

    Hint: maak gebruik van `median()`

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        float: Het eerste kwartiel Q1 van de gegeven getallen.
    """
    return


"""
3. Implementatie q3
    Implementeer onderstaande functie om het derde kwartiel van een lijst getallen te berekenen.
    
"""
def q3(lst):
    """
    Bepaal het derde kwartiel Q3 van een lijst getallen.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        float: Het derde kwartiel Q3 van de gegeven getallen.
    """
    return


"""
4. Implementatie var
    Implementeer onderstaande functie om de variantie van een lijst getallen te berekenen.
    
"""
def var(lst):
    """
    Bepaal de variantie van een lijst getallen.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        float: De variantie van de gegeven getallen.
    """
    return


"""
5. Implementatie std
    Implementeer onderstaande functie om de standaarddeviatie van een lijst getallen te berekenen.
    
"""
def std(lst):
    """
    Bepaal de standaardafwijking van een lijst getallen.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        float: De standaardafwijking van de gegeven getallen.
    """
    return


"""
6. Implementatie cor
    Implementeer onderstaande functie om Pearsons correlatiecoëfficient r tussen twee lijsten van getallen te berekenen.
    
"""
def cor(x, y):
    """
    Bereken de Pearsons correlatiecoëfficient r tussen twee lijsten van getallen.

    Args:
        x (list): De eerste lijst met gehele getallen.
        y (list): De tweede lijst met gehele getallen.

    Returns:
        float: Pearsons correlatiecoëfficient r.
    """

    return



""", 
7. Implementatie freq
    Implementeer onderstaande functie om de frequenties van een lijst getallen te berekenen.
    
"""
def freq(lst):
    """
    Bepaal de frequenties van alle getallen in een lijst.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        dict: Een dictionary met als 'key' de waardes die voorkomen in de lijst
            en als 'value' het aantal voorkomens (de frequentie) van die waarde.

    Examples:
        >> freq([0, 0, 4, 7, 7])
        {0: 2, 4: 1, 7: 2}

        >> freq([1, 1, 2, 3, 2, 1])
        {1: 3, 2: 2, 3: 1}
    """
    freqs = dict()
    return freqs

"""
8. Implementatie plot_grades
    Implementeer onderstaande functie om het gemiddelde eindcijfer t.o.v. de gemiddelde aanwezigheid te plotten in een spreidingsdiagram.
    - Toon een x- en een y-label
    - Toon een grafiektitel (dit heb je nog nooit hoeven doen en zul je zelf moeten uitzoeken) 
"""
def plot_grades(presence, grade):
    """
    Plot het gemiddelde eindcijfer t.o.v. de gemiddelde aanwezigheid te plotten in een spreidingsdiagram. 

    Args:
        presence (list): Een lijst met gehele getallen.
        grade (list): Een lijst met kommagetallen.
    """
    plt.show()


"""
(Optioneel)
9. Implementatie modes
    Implementeer onderstaande functie om de modi van een lijst getallen te berekenen.
    
"""
def modes(lst):
    """
    Bepaal alle modi van een lijst getallen.

    Hint: maak gebruik van `freq()`.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        list: Een gesorteerde lijst van de modi van de gegeven getallen.

    Examples:
        >> modes([0, 0, 4, 7, 7])
        [0, 7]

        >> modes([1, 1, 2, 3, 2, 1])
        [1]
    """
    modi = []



"""
# XXX>
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import os
import sys

def __my_assert_args(function, args, expected_output, check_type=True):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.
    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(',)', ')')
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output)} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"
    if type(expected_output) is float:
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    else:
        assert output == expected_output, msg


def test_id():
    assert naam != "", "Je moet je naam nog invullen!"
    assert studentnummer != -1, "Je moet je studentnummer nog invullen!"
    assert klas != "", "Je moet je klas nog invullen!"


def test_mean():
    testcases = [
        (([4, 2, 5, 8, 6],), 5.0),
        (([1, 3, 2, 4, 6, 2, 4, 2],), 3.0)
    ]

    for case in testcases:
        __my_assert_args(mean, case[0], case[1])


def test_mean_simulated():
    import random
    import statistics

    for lst_size in range(1, 11):
        lst_test = [random.choice(range(5)) for _ in range(lst_size)]
        __my_assert_args(mean, (lst_test,), statistics.mean(lst_test), False)


def test_q1():
    testcases = [
        (([4, 2, 5, 8, 6],), 3.0),
        (([1, 3, 4, 6, 4, 2],), 2.0),
        (([1, 3, 5, 6, 1, 4, 2],), 1.0),
        (([5, 7, 4, 4, 6, 2, 8],), 4.0),
        (([0, 5, 5, 6, 7, 7, 12],), 5.0),
        (([1, 4, 3, 5, 6, 2, 4, 1],), 1.5),
        (([3, 5, 7, 8, 9, 11, 15, 16, 20, 21],), 7.0),
        (([1, 2, 5, 6, 7, 9, 12, 15, 18, 19, 27],), 5.0),
        (([0, 1, 2, 2, 2, 2, 3, 5, 5],), 1.5),

    ]

    for case in testcases:
        __my_assert_args(q1, case[0], case[1])


def test_q3():
    testcases = [
        (([4, 2, 5, 8, 6],), 7.0),
        (([1, 3, 4, 6, 4, 2],), 4.0),
        (([1, 3, 5, 6, 2, 4, 1],), 5.0),
        (([5, 7, 4, 4, 6, 2, 8],), 7.0),
        (([0, 5, 5, 6, 7, 7, 12],), 7.0),
        (([1, 4, 3, 5, 6, 2, 4, 1],), 4.5),
        (([3, 5, 7, 8, 9, 11, 15, 16, 20, 21],), 16.0),
        (([1, 2, 5, 6, 7, 9, 12, 15, 18, 19, 27],), 18.0),
        (([0, 1, 2, 2, 2, 2, 3, 5, 5],), 4.0),

    ]

    for case in testcases:
        __my_assert_args(q3, case[0], case[1])


def test_var():
    testcases = [
        (([4, 2, 5, 8, 6],), 4.0),
        (([1, 3, 2, 4, 6, 2, 4, 2],), 2.25)
    ]

    for case in testcases:
        __my_assert_args(var, case[0], case[1])


def test_var_simulated():
    import random
    import statistics

    for lst_size in range(1, 11):
        lst_test = [random.choice(range(5)) for _ in range(lst_size)]
        __my_assert_args(var, (lst_test,), statistics.pvariance(lst_test), False)


def test_std():
    testcases = [
        (([4, 2, 5, 8, 6],), 2.0),
        (([1, 3, 2, 4, 6, 2, 4, 2],), 1.5)
    ]

    for case in testcases:
        __my_assert_args(std, case[0], case[1])


def test_cor():
    testcases = [
        (([1, 2, 3, 4], [1, 2, 3, 4]), 1.0),
        (([1, 2, 3, 4], [-1, -2, -3, -4]), -1.0),
        (([1, 2, 3, 4], [0, 0, 0, 0]), 0.0),
        (([1, 2, 3, 4], [4, 7, 8, 15]), 0.9429903335828895),
        (([29, 36, 41, 45, 48, 50, 56, 61, 67, 67, 67, 71, 75, 79, 83, 88], [4.1, 4.3, 4.0, 5.2, 4.8, 4.9, 5.9, 5.2, 4.9, 5.7, 6.2, 6.1, 4.4, 6.1, 6.8, 6.9]), 0.7872043771861374),
    ]

    for case in testcases:
        __my_assert_args(cor, case[0], case[1])


def test_std_simulated():
    import random
    import statistics

    for lst_size in range(1, 11):
        lst_test = [random.choice(range(5)) for _ in range(lst_size)]
        __my_assert_args(std, (lst_test,), statistics.pstdev(lst_test), False)


def test_freq():
    testcases = [
        (([4, 2, 5, 8, 6],), {2: 1, 4: 1, 5: 1, 6: 1, 8: 1}),
        (([1, 3, 4, 6, 4, 2],), {1: 1, 2: 1, 3: 1, 4: 2, 6: 1}),
        (([1, 3, 5, 6, 2, 4, 1],), {1: 2, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}),
        (([1, 4, 3, 5, 6, 2, 4, 1],), {1: 2, 2: 1, 3: 1, 4: 2, 5: 1, 6: 1})
    ]

    for case in testcases:
        __my_assert_args(freq, case[0], case[1])


def test_modes():
    testcases = [
        (([4, 2, 5, 8, 6],), [2, 4, 5, 6, 8]),
        (([1, 3, 4, 6, 4, 2],), [4]),
        (([1, 3, 4, 6, 2, 4, 2],), [2, 4]),
        (([1, 3, 2, 4, 6, 2, 4, 2],), [2])
    ]

    for case in testcases:
        __my_assert_args(modes, case[0], case[1])

def test_modes_simulated():
    if sys.version_info[0] >= 3 and sys.version_info[1] >= 8:
        import random
        import statistics
        for lst_size in range(1, 11):
            lst_test = [random.choice(range(5)) for _ in range(lst_size)]
            __my_assert_args(modes, (lst_test,), sorted(statistics.multimode(lst_test)))

def __main():
    """ Test alle functies. """
    # Noodzakelijk voor gekleurde tekst binnen een Windows terminal
    os.system("")

    try:
        print("\x1b[32m")   # Groene tekstkleur
        test_id()

        test_mean()
        test_mean_simulated()
        print("Je functie mean(lst) werkt goed!")

        test_q1()
        print("Je functie q1(lst) werkt goed!")

        test_q3()
        print("Je functie q3(lst) werkt goed!")

        test_var()
        test_var_simulated()
        print("Je functie var(lst) werkt goed!")

        test_std()
        test_std_simulated()
        print("Je functie std(lst) werkt goed!")

        test_cor()
        print("Je functie cor(x, y) werkt goed!")

        test_freq()
        print("Je functie freq(lst) werkt goed!")

        plot_grades([29, 36, 41, 45, 48, 50, 56, 61, 67, 67, 67, 71, 75, 79, 83, 88], [4.1, 4.3, 4.0, 5.2, 4.8, 4.9, 5.9, 5.2, 4.9, 5.7, 6.2, 6.1, 4.4, 6.1, 6.8, 6.9])
        print("Je functie plot_grades faalt niet!")

        test_modes()
        test_modes_simulated()
        print("Je functie modes(lst) werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("\x1b[38;5;208m")
        print("Echter, test dit testframework niet of je de juiste plot bij vraag 8 hebt gemaakt.\x1b[0m")
        print("Controleer dus nog even of je plot correct is en lever dan pas je werk in op Canvas...")

    except AssertionError as ae:
        print("\x1b[31m")   # Rode tekstkleur
        if not ae:
            print("Je code veroorzaakt onderstaande AssertionError:")
            raise ae
        else:
            print(ae)

    print("\x1b[0m")    # Reset tekstkleur


if __name__ == '__main__':
    __main()
