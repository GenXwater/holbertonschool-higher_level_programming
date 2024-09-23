#!/usr/bin/python3
"""
Only sub class of
"""


def inherits_from(obj, a_class):
    """
    Vérifie si l'objet ivent de la classe a_classe, et que l'objet
    n'est pas directement de la classe a_class, mais d'une classe qui
    en hérite
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
