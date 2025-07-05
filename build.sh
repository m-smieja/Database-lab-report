#!/bin/bash
# Skrypt do budowania dokumentacji

# Aktywacja wirtualnego środowiska
source venv/bin/activate

case "$1" in
    html)
        echo "Buduję dokumentację HTML..."
        make html
        echo "Gotowe! Otwórz _build/html/index.html"
        ;;
    pdf)
        echo "Buduję dokumentację PDF przez LaTeX..."
        make latex
        cd _build/latex
        make
        cd ../..
        echo "Gotowe! PDF znajduje się w _build/latex/database_report.pdf"
        ;;
    latexpdf)
        echo "Buduję dokumentację PDF (automatycznie)..."
        make latexpdf
        echo "Gotowe! PDF znajduje się w _build/latex/database_report.pdf"
        ;;
    clean)
        echo "Czyszczę pliki build..."
        make clean
        rm -rf _build/
        ;;
    serve)
        echo "Uruchamiam serwer z auto-reload..."
        sphinx-autobuild . _build/html
        ;;
    update)
        echo "Aktualizuję wszystkie submoduły..."
        git submodule update --remote --merge
        ;;
    *)
        echo "Użycie: $0 {html|pdf|latexpdf|clean|serve|update}"
        exit 1
        ;;
esac
