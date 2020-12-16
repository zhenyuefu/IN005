# -*- coding: utf-8 -*-
from transition import *
from state import *
import os
import copy
from sp import *
from parser import *
from itertools import product
from automateBase import AutomateBase


class Automate(AutomateBase):
    def succElem(self, state, lettre):
        """State x str -> list[State]
        rend la liste des états accessibles à partir d'un état
        state par l'étiquette lettre
        """
        successeurs = []
        # t: Transitions
        for t in self.getListTransitionsFrom(state):
            if t.etiquette == lettre and t.stateDest not in successeurs:
                successeurs.append(t.stateDest)
        return successeurs

    def succ(self, listStates, lettre):
        """list[State] x str -> list[State]
        rend la liste des états accessibles à partir de la liste d'états
        listStates par l'étiquette lettre
        """
        successeurs = []
        for state in listStates:
            for t in self.getListTransitionsFrom(state):
                if t.etiquette == lettre and t.stateDest not in successeurs:
                    successeurs.append(t.stateDest)
        return successeurs

    """ Définition d'une fonction déterminant si un mot est accepté par un automate.
    Exemple :
            a=Automate.creationAutomate("monAutomate.txt")
            if Automate.accepte(a,"abc"):
                print "L'automate accepte le mot abc"
            else:
                print "L'automate n'accepte pas le mot abc"
    """

    @staticmethod
    def accepte(auto, mot):
        """Automate x str -> bool
        rend True si auto accepte mot, False sinon
        """
        list_states = auto.getListInitialStates()
        for ch in mot:
            list_states = auto.succ(list_states, ch)
        list_fin = auto.getListFinalStates()
        for state in list_states:
            if state in list_fin:
                return True
        return False

    @staticmethod
    def estComplet(auto, alphabet):
        """Automate x str -> bool
        rend True si auto est complet pour alphabet, False sinon
        """
        for state in auto.listStates:
            list_t = auto.getListTransitionsFrom(state)
            list_etiquette = []
            for t in list_t:
                if t.etiquette not in list_etiquette:
                    list_etiquette.append(t.etiquette)
            for ch in alphabet:
                if ch not in list_etiquette:
                    return False
        # while True:
        #     list_next = []
        #     for state in list_states:
        #         list_t = auto.getListTransitionsFrom(state)
        #         list_etiquette = []
        #         for t in list_t:
        #             list_etiquette.append(t.etiquette)
        #         for ch in alphabet:
        #             if ch not in list_etiquette:
        #                 return False
        #             list_next += auto.succ(list_states, ch)
        #     if list_next:
        #         break
        #     list_states = list_next
        return True

    @staticmethod
    def estDeterministe(auto):
        """Automate  -> bool
        rend True si auto est déterministe, False sinon
        """
        list_int = auto.getListInitialStates()
        if len(list_int) > 1:
            return False
        for state in auto.listStates:
            list_t = auto.getListTransitionsFrom(state)
            list_etiquette = []
            for t in list_t:
                if t.etiquette in list_etiquette:
                    return False
                list_etiquette.append(t.etiquette)
        return True

    @staticmethod
    def completeAutomate(auto, alphabet):
        """Automate x str -> Automate
        rend l'automate complété d'auto, par rapport à alphabet
        """
        if Automate.estComplet(auto, alphabet):
            return auto
        auto_new = copy.deepcopy(auto)
        pur = State(-1, False, False)
        auto_new.addState(pur)
        for state in auto.listStates:
            list_t = auto.getListTransitionsFrom(state)
            list_etiquette = list(set(t.etiquette for t in list_t))
            for ch in alphabet:
                if ch not in list_etiquette:
                    auto_new.addTransition(Transition(state, ch, pur))
        return auto_new

    @staticmethod
    def determinisation(auto):
        """Automate  -> Automate
        rend l'automate déterminisé d'auto
        """
        list_init = auto.getListInitialStates()
        list_etiquette = auto.getAlphabetFromTransitions()
        list_states_DFA_from_NFA = [list_init]
        list_states_DFA = [State(0, True, False, label=str(list_init))]
        for state in list_init:
            if state in auto.getListFinalStates():
                list_states_DFA = [State(0, True, True, label=str(list_init))]
                break
        list_states = list_init
        list_transitions = []
        i = 0
        list_next = []
        while True:
            for ch in list_etiquette:
                list_temp = auto.succ(list_states, ch)
                if list_temp not in list_states_DFA_from_NFA:
                    add = False
                    for state in list_temp:
                        if state.fin:
                            i += 1
                            list_states_DFA.append(
                                State(i, False, True, label=str(list_temp))
                            )
                            add = True
                            break
                    if not add:
                        i += 1
                        list_states_DFA.append(
                            State(i, False, False, label=str(list_temp))
                        )
                    list_transitions.append(
                        Transition(
                            list_states_DFA[
                                list_states_DFA_from_NFA.index(list_states)
                            ],
                            ch,
                            list_states_DFA[i],
                        )
                    )
                    list_states_DFA_from_NFA.append(list_temp)
                    list_next.append(list_temp)
                else:
                    list_transitions.append(
                        Transition(
                            list_states_DFA[
                                list_states_DFA_from_NFA.index(list_states)
                            ],
                            ch,
                            list_states_DFA[list_states_DFA_from_NFA.index(list_temp)],
                        )
                    )
            if list_next == []:
                break
            list_states = list_next[0]
            del list_next[0]
        new_auto = Automate(list_transitions)
        return new_auto

    @staticmethod
    def complementaire(auto, alphabet):
        """Automate -> Automate
        rend  l'automate acceptant pour langage le complémentaire du langage de a
        """

    @staticmethod
    def intersection(auto0, auto1):
        """Automate x Automate -> Automate
        rend l'automate acceptant pour langage l'intersection des langages des deux automates
        """
        return

    @staticmethod
    def union(auto0, auto1):
        """Automate x Automate -> Automate
        rend l'automate acceptant pour langage l'union des langages des deux automates
        """
        return

    @staticmethod
    def concatenation(auto1, auto2):
        """Automate x Automate -> Automate
        rend l'automate acceptant pour langage la concaténation des langages des deux automates
        """
        return

    @staticmethod
    def etoile(auto):
        """Automate  -> Automate
        rend l'automate acceptant pour langage l'étoile du langage de a
        """
        return
