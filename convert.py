#!/usr/bin/env nix-shell
#!nix-shell -i python -p python311Packages.pyyaml

import plistlib
import yaml


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


tm = None

with open('Syntaxes/PowerBuilder.tmLanguage.yaml', 'rb') as yml:
    tm = yaml.safe_load(yml)

recurseStringifyKeys(tm)

with open('Syntaxes/PowerBuilder.tmLanguage', 'w') as plist:
    plist.write(plistlib.dumps(tm).decode())
