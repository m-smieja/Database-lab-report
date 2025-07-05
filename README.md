# Database Report

Kompleksowa dokumentacja systemu bazy danych CRM.

## Struktura projektu

```
Database_report/
├── index.rst              # Główny plik dokumentacji
├── conf.py                # Konfiguracja Sphinx
├── Makefile               # Makefile dla Sphinx
├── requirements.txt       # Zależności Python
├── .readthedocs.yml       # Konfiguracja Read the Docs
├── chapter_1/             # Rozdział 1: Wstęp
│   └── index.rst
├── chapter_2/             # Rozdział 2: Analiza szczegółowa
│   ├── 2.1/              # Submoduł: Wydajność, Skalowanie i Replikacja
│   ├── 2.2/              # Submoduł: Sprzęt dla bazy danych
│   ├── 2.3/              # Submoduł: Konfiguracja baz danych
│   ├── 2.4/              # Submoduł: Bezpieczeństwo
│   └── 2.5/              # Submoduł: Kopie zapasowe
├── chapter_3/             # Rozdział 3: Projekt bazy danych
│   └── index.rst
├── chapter_4/             # Rozdział 4: Analiza i optymalizacja
│   └── index.rst
├── chapter_5/             # Rozdział 5: Opis repozytoriów
│   └── index.rst
└── task_modules/          # Submoduł: Moduły zadań
```

## Wymagania

- Python 3.10+
- LaTeX (texlive-full)
- Git

## Instalacja

1. Klonuj repozytorium z submodułami:
```bash
git clone --recurse-submodules git@github.com:m-smieja/Database_report.git
cd Database_report
```

2. Utwórz środowisko wirtualne:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Budowanie dokumentacji

### HTML
```bash
./build.sh html
# lub
make html
```

### PDF (przez LaTeX)
```bash
./build.sh pdf
# lub
make latexpdf
```

### Serwer z auto-reload
```bash
./build.sh serve
```

## Praca z submodułami

### Aktualizacja wszystkich submodułów
```bash
./build.sh update
# lub
git submodule update --remote --merge
```

### Praca z konkretnym submodułem
```bash
cd chapter_2/2.1
git pull origin main
# wprowadź zmiany
git add .
git commit -m "Opis zmian"
git push origin main
cd ../..
git add chapter_2/2.1
git commit -m "Update submodule 2.1"
```

## Autorzy submodułów

- **2.1** - Broksonn (Wydajność, Skalowanie i Replikacja)
- **2.2** - oszczeda (Sprzęt dla bazy danych)
- **2.3** - Chaiolites (Konfiguracja baz danych)
- **2.4** - BlazejUl (Bezpieczeństwo)
- **2.5** - m-smieja (Kopie zapasowe i odzyskiwanie danych)

## Autor dokumentacji

Miłosz Śmieja

## Licencja

MIT License
