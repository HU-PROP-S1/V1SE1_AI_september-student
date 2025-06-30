#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Oefening: statistiek

(c) 2025 Hogeschool Utrecht,
Peter van den Berg (peter.vandenberg@hu.nl)

Je kunt je functies testen met het gegeven raamwerk door het bestand
uit te voeren (of met behulp van `pytest`, als je weet hoe dat werkt).
Lever je werk in op Canvas als alle tests slagen.

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""

def remove_dominated(m):
    """
    Filtert matrix door gedomineerde strategieën te elimineren. 
    LET OP: de functie dient alleen STRIKT gedomineerde strategieën te elimineren. 
    Dit is wanneer de ene actie altijd hogere utility geeft dan de ander.

    Args:
        m list[list[tuple[int, int]]]: De matrix van tuples van int

    Returns:
        list[list[tuple[int, int]]]: De gefilterde matrix
    """



"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import os


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


def test_remove_dominated():
    testcases = [
        (([[(1, 1), (3, 3)],[(2, 2), (3, 0)]],), [[(1, 1), (3, 3)], [(2, 2), (3, 0)]]),
        (([[(0, 3), (1, 1)],[(2, 2), (3, 2)]],), [[(2, 2), (3, 2)]]),
        (([[(0, 3), (1, 0)],[(0, 2), (3, 0)]],), [[(0, 3)], [(0, 2)]]),
        (([[(3, 0), (1, 1)],[(2, 2), (0, 3)]],), [[(1, 1)]]),
        (([[(0, 3), (1, 1)],[(2, 2), (3, 0)]],), [[(2, 2)]]),
        (([[(1, 1), (0, 3)],[(3, 0), (3, 3)]],), [[(3, 3)]]),
        (([[(4, 4), (1, 1)],[(2, 2), (5, 0)]],), [[(4, 4)]])
    ]

    for case in testcases:
        __my_assert_args(remove_dominated, case[0], case[1])

def __main():
    """ Test alle functies. """
    # Noodzakelijk voor gekleurde tekst binnen een Windows terminal
    os.system("")

    try:
        print("\x1b[32m")   # Groene tekstkleur

        test_remove_dominated()
        print("Je functie remove_dominated(m) werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")

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
