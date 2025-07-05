#!/bin/bash
# Aktywacja wirtualnego środowiska
source venv/bin/activate
echo "Wirtualne środowisko aktywowane."
echo "Dostępne komendy:"
echo "  make html        - buduje dokumentację HTML"
echo "  make latexpdf    - buduje dokumentację PDF"
echo "  ./build.sh help  - pokazuje wszystkie opcje budowania"
