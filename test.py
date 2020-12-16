# -*- coding: utf-8 -*-
"""
Code modifiable.
"""

from automate import Automate
from state import State
from transition import Transition
from parser import *

list_states = [State(0, True, False), State(1, False, False)]
automate = Automate.creationAutomate("exempleAutomate.txt")
automate.show("example")
acc = Automate.creationAutomate("Fichiers de test/testAcc.txt")
acc.show("Accept")
compl = Automate.creationAutomate("Fichiers de test/testCompl.txt")
compl.show("complet")
automate2 = Automate.determinisation(automate)
automate2.show("det")

print(automate.succ(list_states, "a"))
print(Automate.estComplet(compl, "ab"))