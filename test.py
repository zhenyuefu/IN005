# -*- coding: utf-8 -*-
"""
Code modifiable.
"""

from automate import Automate
from state import State
from transition import Transition
from parser import *

automate = Automate.creationAutomate("exempleAutomate.txt")
automate = Automate.determinisation(automate)
automate.show("exempleAutomate")