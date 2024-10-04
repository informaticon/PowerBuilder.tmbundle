#!/usr/bin/env nix-shell
#!nix-shell -i python -p python3Packages.pyyaml python3Packages.jinja2

import jinja2
import plistlib
import yaml
import json


def recurseStringifyKeys(val):

    if isinstance(val, dict):
        for key in [*val.keys()]:
            recurseStringifyKeys(val[key])

            if not isinstance(key, str):
                val[str(key)] = val[key]
                del val[key]

    if isinstance(val, list):
        for sub_val in val:
            recurseStringifyKeys(sub_val)


template = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates')
).get_template('PowerBuilder.tmLanguage.yaml.j2')

yml = template.render()
tm = yaml.safe_load(yml)

with open('Syntaxes/PowerBuilder.tmLanguage.yaml', 'w') as yml_file:
    yml_file.write(yml)


recurseStringifyKeys(tm)

with open('Syntaxes/PowerBuilder.tmLanguage', 'w') as plist_file:
    plist_file.write(plistlib.dumps(tm).decode())

with open('Syntaxes/PowerBuilder.tmLanguage.json', 'w') as json_file:
    json_file.write(json.dumps(tm))
