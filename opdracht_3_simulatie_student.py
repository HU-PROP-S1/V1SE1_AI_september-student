#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Oriëntatie op AI

Opdracht: simulatie

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

debuginfo = True

"""
1. Implementatie is_always_defect
    Implementeer onderstaande functie om te achterhalen of de tegenstander 'Always defect' is.

"""
def is_always_defect(my_history, opponent_history):
    """
    Checkt of je tegenstander 'Always defect' is.

    Args:
        my_history (list[bool]): Een lijst met jouw gespeelde acties in het verleden.
        opponent_history (list[bool]): Een lijst de door jouw tegenstander gespeelde acties in het verleden.

    Returns:
        bool: True als je tegenstander 'Always defect' is, anders False.
    """
    return

"""
2. Implementatie play_against_always_defect
    Implementeer onderstaande functie om de beste actie te spelen tegen 'Always defect'.

"""
def play_against_always_defect(my_history, opponent_history):
    """
    Geeft de actie terug die gespeeld zal worden tegen 'Always defect' door jouw agent, 
    gegeven jouw en jouw tegenstanders' acties in het verleden.

    Args:
        my_history (list[bool]): Een lijst met jouw gespeelde acties in het verleden.
        opponent_history (list[bool]): Een lijst de door jouw tegenstander gespeelde acties in het verleden.

    Returns:
        bool: Jouw actie; samenwerken (True) of zelfzuchtig zijn (False).
    """
    return

"""
3. Implementatie is_alternate
    Implementeer onderstaande functie om te achterhalen of de tegenstander 'Alternate' is.

"""
def is_alternate(my_history, opponent_history):
    """
    Checkt of je tegenstander 'Alternate' is.

    Args:
        my_history (list[bool]): Een lijst met jouw gespeelde acties in het verleden.
        opponent_history (list[bool]): Een lijst de door jouw tegenstander gespeelde acties in het verleden.

    Returns:
        bool: True als je tegenstander 'Alternate' is, anders False.
    """
    return

"""
4. Implementatie play_against_alternate
    Implementeer onderstaande functie om de beste actie te spelen tegen 'Alternate'.

"""
def play_against_alternate(my_history, opponent_history):
    """
    Geeft de actie terug die gespeeld zal worden tegen 'Alternate' door jouw agent, 
    gegeven jouw en jouw tegenstanders' acties in het verleden.

    Args:
        my_history (list[bool]): Een lijst met jouw gespeelde acties in het verleden.
        opponent_history (list[bool]): Een lijst de door jouw tegenstander gespeelde acties in het verleden.

    Returns:
        bool: Jouw actie; samenwerken (True) of zelfzuchtig zijn (False).
    """
    return

"""
5. Implementatie is_tit_for_tat
    Implementeer onderstaande functie om te achterhalen of de tegenstander 'Tit for tat' is.

"""
def is_tit_for_tat(my_history, opponent_history):
    """
    Checkt of je tegenstander 'Tit for tat' is.

    Args:
        my_history (list[bool]): Een lijst met jouw gespeelde acties in het verleden.
        opponent_history (list[bool]): Een lijst de door jouw tegenstander gespeelde acties in het verleden.

    Returns:
        bool: True als je tegenstander 'Tit for tat' is, anders False.
    """
    return

"""
6. Implementatie play_against_tit_for_tat
    Implementeer onderstaande functie om de beste actie te spelen tegen 'Tit for tat'.

"""
def play_against_tit_for_tat(my_history, opponent_history):
    """
    Geeft de actie terug die gespeeld zal worden tegen 'Tit for tat' door jouw agent, 
    gegeven jouw en jouw tegenstanders' acties in het verleden.

    Args:
        my_history (list[bool]): Een lijst met jouw gespeelde acties in het verleden.
        opponent_history (list[bool]): Een lijst de door jouw tegenstander gespeelde acties in het verleden.

    Returns:
        bool: Jouw actie; samenwerken (True) of zelfzuchtig zijn (False).
    """
    return

"""
7. Implementatie play_against_unknown
    Implementeer onderstaande functie om de beste actie te spelen tegen een (nog) onbekende tegenstander.

"""
def play_against_unknown(my_history, opponent_history):
    """
    Geeft de actie terug die gespeeld zal worden tegen een onbekende tegenstander door jouw agent, 
    gegeven jouw en jouw tegenstanders' acties in het verleden.

    Args:
        my_history (list[bool]): Een lijst met jouw gespeelde acties in het verleden.
        opponent_history (list[bool]): Een lijst de door jouw tegenstander gespeelde acties in het verleden.

    Returns:
        bool: Jouw actie; samenwerken (True) of zelfzuchtig zijn (False).
    """
    return

"""
8. Optioneel: Implementatie is_final_round
    Implementeer onderstaande functie om te achterhalen of je in de laatste ronde zit.

    Args:
        my_history (list[bool]): Een lijst met jouw gespeelde acties in het verleden.
        opponent_history (list[bool]): Een lijst de door jouw tegenstander gespeelde acties in het verleden.

    Returns:
        bool: True als je in de laatste ronde zit, anders False.

"""
def is_final_round(my_history, opponent_history):
    return

"""
9. Optioneel: Implementatie play_final_round
    Implementeer onderstaande functie om de beste actie te spelen in de laatste ronde.

    Args:
        my_history (list[bool]): Een lijst met jouw gespeelde acties in het verleden.
        opponent_history (list[bool]): Een lijst de door jouw tegenstander gespeelde acties in het verleden.

    Returns:
        bool: Jouw actie; samenwerken (True) of zelfzuchtig zijn (False).

"""
def play_final_round(my_history, opponent_history):
    return


def strategy(my_history, opponent_history):
    """
    Geeft de actie terug die gespeeld zal worden door jouw agent, 
    gegeven jouw en jouw tegenstanders' acties in het verleden.

    Args:
        my_history (list[bool]): Een lijst met jouw gespeelde acties in het verleden.
        opponent_history (list[bool]): Een lijst de door jouw tegenstander gespeelde acties in het verleden.

    Returns:
        bool: Jouw actie; samenwerken (True) of zelfzuchtig zijn (False).
    """
    # 10. Optioneel: uncomment deze code en implementeer is_final_round en play_final_round
    # if is_final_round(my_history, opponent_history):
    #     return play_final_round(my_history, opponent_history)
    
    if is_always_defect(my_history, opponent_history):
        return play_against_always_defect(my_history, opponent_history)
    elif is_alternate(my_history, opponent_history):
        return play_against_alternate(my_history, opponent_history)
    elif is_tit_for_tat(my_history, opponent_history):
        return play_against_tit_for_tat(my_history, opponent_history)
    else:
        return play_against_unknown(my_history, opponent_history)

def always_defect(my_history, opponent_history):
    return False

def alternate(my_history, opponent_history):
    return len(opponent_history) % 2 == 0

def tit_for_tat(my_history, opponent_history):
    if not opponent_history:
        return True
    return opponent_history[-1]

strategies = {
    "Always defect": always_defect,
    "Alternate": alternate,
    "Tit for Tat": tit_for_tat,
    "Jouw strategie": strategy
}

def play_game(strategy1, strategy2, rounds):
    history = []
    errors = []
    for _ in range(rounds):
        try:
            history1 = [h[0] for h in history]
            history2 = [h[1] for h in history]
            action1 = strategy1(history1, history2)
            action2 = strategy2(history2, history1)
            if not isinstance(action1, bool) or not isinstance(action2, bool):
                raise ValueError("Jouw strategie moet een boolean teruggeven.")
            history.append((action1, action2))
        except Exception as e:
            errors.append(str(e))
    return calculate_scores(history), errors

def calculate_scores(history):
    payoff_matrix = (
        ((1, 1), (3, 0)),
        ((0, 3), (2, 2))
    )
    score1, score2 = 0, 0
    for action1, action2 in history:
        s1, s2 = payoff_matrix[int(action1)][int(action2)]
        score1 += s1
        score2 += s2
        if debuginfo:
            print(f"({action1}, {action2}) -> ({s1}, {s2})")
    return score1, score2

def run_tournament(strategies, rounds):
    results = {}
    total_scores = {name: 0 for name in strategies}

    for name1, strat1 in strategies.items():
        for name2, strat2 in strategies.items():
            if name1 < name2:
                if debuginfo:
                    print(f"{name1} vs {name2}")
                (score1, score2), errors = play_game(strat1, strat2, rounds)
                results[(name1, name2)] = (score1, score2)
                total_scores[name1] += score1
                total_scores[name2] += score2
                
                if debuginfo:
                    print(f"Eindscore {name1} vs {name2}: {score1} - {score2}")
                if errors:
                    print(f"Errors in spel: {name1} vs {name2}: {errors[0]}")

    return results, total_scores

if __name__ == "__main__":
    rounds = 20
    results, total_scores = run_tournament(strategies, rounds)

    positions = sorted(total_scores.items(), key=lambda x: x[1], reverse=True)
    print("\nEindscores:")
    for strategy, score in positions:
        print("{}: {}".format(strategy, score))
        
    if positions[0][0] == "Jouw strategie" or positions[1][0] == "Jouw strategie":
        print("\x1b[32m")
        print("Jouw strategie heeft gewonnen!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")
    else:
        print("\x1b[31m")   # Rode tekstkleur
        print(f"Jouw strategie heeft niet gewonnen")
    
    print("\x1b[0m")
