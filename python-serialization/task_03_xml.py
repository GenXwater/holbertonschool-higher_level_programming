#!/usr/bin/env python3


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)

    tree = ET.ElementTree(root)
    try:
        tree.write(filename)
        return True
    except Exception as e:
        return False


def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result_dict = {}
        for child in root:
            result_dict[child.tag] = child.text

        return result_dict
    except FileNotFoundError:
        return None
    except ET.ParseError:
        return None
    except Exception as e:
        return None
