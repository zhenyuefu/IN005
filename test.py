# -*- coding: utf-8 -*-
"""
Code modifiable.
"""

from automate import Automate
from state import State
from transition import Transition
from parser import *

automate = Automate.creationAutomate("exempleAutomate.txt")
automate2 = Automate.determinisation(automate)
automate2.show("exempleAutomate")