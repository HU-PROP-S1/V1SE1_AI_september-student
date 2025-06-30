#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

"""
Oriëntatie op AI

Oefening: predict_success

(c) 2025 Hogeschool Utrecht,
Peter van den Berg (peter.vandenberg@hu.nl)


Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""


def predict_success(data):
    """
    Voorspelt het succes van de vrijwilligersproject uit de dataset in de variabele data.
    - Het succes wordt voorspeld met een beslisboom.
    - Het resultaat van de voorspelling (True of False) wordt in de kolom 'succes_prediction' geplaatst.

    Args:
        data (dict[list]): de dataset met vrijwilligersprojecten
    """
    data['succes_prediction'] = []

"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import csv

def test_predict_with_tree():
    with open('vrijwilligers.csv') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        data = {}

        for header in headers:
            data[header] = []
        
        for row in reader:
            row[''] = int(row[''])
            row['jaar'] = int(row['jaar'])
            row['aantal_vrijwilligers'] = int(row['aantal_vrijwilligers'])
            row['aantal_uren'] = int(row['aantal_uren'])
            row['percentage_buitenwerk'] = float(row['percentage_buitenwerk'])
            row['actief'] = row['actief'] == 'True'
            row['succes'] = row['succes'] == 'True'
            for header in headers:
                data[header].append(row[header])

    predict_success(data)
        
    correct = 0
    for i in range(len(data['succes'])):
        assert len(data['succes_prediction']) > i, f"De kolom 'succes_prediction' is niet volledig gevuld."
        if data['succes'][i] == data['succes_prediction'][i]:
            correct += 1
    assert correct > 83, f"De prestatie van de beslisboom is niet hoger dan 83.8%, namelijk: {round((correct / 99) * 100, 1)}%."

if __name__ == '__main__':
    try:
        print("\x1b[32m")

        test_predict_with_tree()
        print("Je functie predict_success() doorstaat de tests!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")

    except AssertionError as ae:
        print("\x1b[31m")   # Rode tekstkleur
        if not ae:
            print("Je code veroorzaakt onderstaande AssertionError:")
            raise ae
        else:
            print(ae)
        print("\x1b[0m")    # Reset tekstkleur