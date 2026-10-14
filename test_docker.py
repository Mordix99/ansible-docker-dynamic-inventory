import subprocess

wynik = subprocess.run(['docker', 'ps', '--format', "{{.Names}}"], capture_output=True, text=True)

lista_kontenerow = wynik.stdout.strip().split('\n')



print(lista_kontenerow)