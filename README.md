# Ansible Dynamic Inventory for Docker

Prosty, dynamiczny inwentarz dla Ansible napisany w Pythonie. Skrypt automatycznie wykrywa działające kontenery Dockera i pozwala na zarządzanie nimi bezpośrednio przez demona Dockera (z pominięciem SSH).

## Jak używać:
1. Upewnij się, że masz uruchomione kontenery testowe, np.: 
   `docker run -d alpine sleep 3600`
2. Sprawdź, czy skrypt poprawnie generuje strukturę JSON: 
   `./inventory.py --list`
3. Przetestuj łączność za pomocą Ansible: 
   `ansible all -i inventory.py -m ping`# ansible-docker-dynamic-inventory
