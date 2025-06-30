#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Onderwerp: data science

(c) 2025 Hogeschool Utrecht,
Peter van den Berg (peter.vandenberg@hu.nl)

Gebruik onderstaande code bij dat les over data-analyse, en bij de bijbehorende inleveroefening.

"""


import csv
from collections import Counter
import matplotlib.pyplot as plt

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

frequencies = Counter(data['aantal_vrijwilligers'])
plt.bar(frequencies.keys(), frequencies.values())
plt.xlabel('Aantal vrijwilligers')
plt.ylabel('Frequentie')
plt.show()

plt.xlabel('Aantal uren')
plt.ylabel('Frequentie')
plt.hist(data['aantal_uren'])
plt.show()

plt.boxplot(data['percentage_buitenwerk'])
plt.show()

plt.scatter(data['aantal_vrijwilligers'], data['aantal_uren'])
plt.xlabel('Aantal vrijwilligers')
plt.ylabel('Aantal uren')
plt.show()

frequencies = Counter(data['succes'])
plt.bar(frequencies.keys(), frequencies.values())
plt.xlabel('Succes (0=False, 1=True)')
plt.ylabel('Frequentie')
plt.show()

successful = []
unsuccessful = []
for i in range(len(data['succes'])):
    if data['succes'][i]:
        successful.append(data['actief'][i])
    else:
        unsuccessful.append(data['actief'][i])
unsuccessful_freqs = Counter(unsuccessful)
successful_freqs = Counter(successful)

plt.bar(unsuccessful_freqs.keys(), unsuccessful_freqs.values(), width=0.5, label='Onsuccesvol')
plt.bar(successful_freqs.keys(), successful_freqs.values(), width=0.5, align='edge', label='Succesvol')
plt.xlabel('Actief (0=False, 1=True)')
plt.ylabel('Frequentie')
plt.legend()
plt.show()

data['succes_prediction'] = []
for i in range(len(data['succes'])):
    if data['actief'][i]:
        data['succes_prediction'].append(True)
    else:
        data['succes_prediction'].append(False)

correct = 0
for i in range(len(data['succes'])):
    if data['succes'][i] == data['succes_prediction'][i]:
        correct += 1
print(f"{correct} / 99 = {round(correct/99*100, 1)}%") 