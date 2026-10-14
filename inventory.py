#!/usr/bin/env python3

import json
import argparse
import subprocess

def main():

    wynik = subprocess.run(['docker', 'ps', '--format', "{{.Names}}"], capture_output=True, text=True)

    lista_kontenerow = [k for k in wynik.stdout.strip().split('\n') if k]

    dynamic_data = {
        "docker_nodes": {
            "hosts": lista_kontenerow
        }
    }

    dynamic_host_vars = {}
    for kontener in lista_kontenerow:
        dynamic_host_vars[kontener] = {"ansible_connection": "docker"}
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--host", type=str, help="Display variables for a specific host")

    args = parser.parse_args()

    if args.list:
        print(json.dumps(dynamic_data, indent=4))
    elif args.host:
        print(json.dumps(dynamic_host_vars.get(args.host, {}), indent=4))

if __name__ == '__main__':
    main()