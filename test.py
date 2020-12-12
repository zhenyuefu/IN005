# -*- coding: utf-8 -*-
"""
Code modifiable.
"""

from automate import Automate
from state import State
from transition import Transition
from parser import *

automate = Automate.creationAutomate("exempleAutomate.txt")
new_auto = Automate.completeAutomate(automate, "abc")
new_auto.show("exempleAutomate")
