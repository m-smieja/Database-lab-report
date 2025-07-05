Analiza szczegółowa systemu
===========================

Ten rozdział zawiera pięć niezależnych projektów zarządzanych jako osobne repozytoria, 
każdy skupiający się na kluczowym aspekcie systemu bazy danych.

.. toctree::
   :maxdepth: 2
   :caption: Moduły:
   
   2.1/index
   2.2/index
   2.3/index
   2.4/index
   2.5/index

Wprowadzenie
------------

W tym rozdziale przedstawiamy pięć kluczowych komponentów systemu bazy danych:

1. **Wydajność, Skalowanie i Replikacja** - optymalizacja dla dużych wolumenów danych
2. **Sprzęt dla bazy danych** - dobór i konfiguracja infrastruktury
3. **Konfiguracja baz danych** - najlepsze praktyki konfiguracyjne
4. **Bezpieczeństwo** - zabezpieczenia i kontrola dostępu
5. **Kopie zapasowe i odzyskiwanie danych** - strategie backup i disaster recovery

Każdy moduł jest zarządzany w osobnym repozytorium Git, co umożliwia niezależny rozwój 
i specjalizację zespołów.

Struktura modułów
-----------------

.. list-table:: Przegląd modułów analitycznych
   :header-rows: 1
   :widths: 10 35 30 25

   * - Nr
     - Nazwa modułu
     - Zespół odpowiedzialny
     - Status
   * - 2.1
     - Wydajność, Skalowanie i Replikacja
     - Broksonn
     - W trakcie rozwoju
   * - 2.2
     - Sprzęt dla bazy danych
     - oszczeda
     - W trakcie rozwoju
   * - 2.3
     - Konfiguracja baz danych
     - Chaiolites
     - W trakcie rozwoju
   * - 2.4
     - Bezpieczeństwo
     - BlazejUl
     - W trakcie rozwoju
   * - 2.5
     - Kopie zapasowe i odzyskiwanie danych
     - m-smieja
     - W trakcie rozwoju

Współpraca między modułami
--------------------------

Moduły są ze sobą powiązane i tworzą spójną całość:

* **Wydajność** wpływa na decyzje dotyczące **sprzętu**
* **Konfiguracja** musi uwzględniać wymagania **bezpieczeństwa**
* **Kopie zapasowe** zależą od **skali** i **wydajności** systemu

Instrukcja pracy z submodułami
-------------------------------

Aktualizacja wszystkich modułów::

    git submodule update --remote --merge

Praca z konkretnym modułem::

    cd chapter_2/2.1
    git checkout main
    # wprowadź zmiany
    git add .
    git commit -m "Opis zmian"
    git push origin main
