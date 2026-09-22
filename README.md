# Netmiko – Automatizacija konfiguracije mrežnih uređaja

Python projekt za automatizaciju konfiguracije, dohvaćanje rezultata i izradu sigurnosnih kopija mrežnih uređaja pomoću biblioteke **Netmiko**.

---

## 📁 Struktura projekta

```text
Netmiko/
├── konfiguracija_uredaja/
│   ├── netmiko_konfiguracija_uredaja.py
│   ├── usmjernici.txt
│   ├── usmjernik1.txt
│   ├── usmjernik2.txt
│   └── usmjernik3.txt
│
├── rezultati_uredaja/
│   ├── netmiko_rezultati_uredaja.py
│   ├── usmjernici.txt
│   ├── Usmjernik1_rezultati.txt
│   ├── Usmjernik2_rezultati.txt
│   └── Usmjernik3_rezultati.txt
│
├── sigurnosna_kopija_uredaja/
│   ├── netmiko_sigurnosna_kopija_uredaja.py
│   ├── usmjernici.txt
│   ├── Usmjernik1_2026-9-11_sigurnosna_kopija.txt
│   ├── Usmjernik2_2026-9-11_sigurnosna_kopija.txt
│   └── Usmjernik3_2026-9-11_sigurnosna_kopija.txt
│
└── .venv/

📂 Opis direktorija

🔧 konfiguracija_uredaja

Ovaj direktorij sadrži Python skriptu i konfiguracijske datoteke za konfiguriranje mrežnih uređaja.

netmiko_konfiguracija_uredaja.py – glavna skripta za povezivanje s uređajima i slanje konfiguracijskih naredbi.
usmjernici.txt – popis IP adresa mrežnih uređaja.
usmjernik1.txt – konfiguracijske naredbe za prvi usmjernik.
usmjernik2.txt – konfiguracijske naredbe za drugi usmjernik.
usmjernik3.txt – konfiguracijske naredbe za treći usmjernik.

📊 rezultati_uredaja

Ovaj direktorij sadrži skriptu za dohvaćanje rezultata i izlaza s mrežnih uređaja.

netmiko_rezultati_uredaja.py – Python skripta za dohvaćanje podataka s mrežnih uređaja.
usmjernici.txt – popis IP adresa mrežnih uređaja.
Usmjernik1_rezultati.txt – rezultati dobiveni s prvog usmjernika.
Usmjernik2_rezultati.txt – rezultati dobiveni s drugog usmjernika.
Usmjernik3_rezultati.txt – rezultati dobiveni s trećeg usmjernika.

💾 sigurnosna_kopija_uredaja

Ovaj direktorij koristi se za izradu i spremanje sigurnosnih kopija konfiguracija mrežnih uređaja.

netmiko_sigurnosna_kopija_uredaja.py – Python skripta za izradu sigurnosnih kopija konfiguracija.
usmjernici.txt – popis IP adresa mrežnih uređaja.
Usmjernik1_2026-9-11_sigurnosna_kopija.txt – sigurnosna kopija konfiguracije prvog usmjernika.
Usmjernik2_2026-9-11_sigurnosna_kopija.txt – sigurnosna kopija konfiguracije drugog usmjernika.
Usmjernik3_2026-9-11_sigurnosna_kopija.txt – sigurnosna kopija konfiguracije trećeg usmjernika.

⚙️ Zahtjevi

Za pokretanje projekta potrebno je imati:

Python 3.x
Netmiko
SSH pristup mrežnim uređajima
Instalacija Netmiko biblioteke
pip install netmiko

🚀 Korištenje

Projekt se sastoji od tri osnovna dijela:

Konfiguracija mrežnih uređaja
Dohvaćanje rezultata s uređaja
Izrada sigurnosnih kopija konfiguracija

1. Konfiguracija uređaja

Pokrenite:

python konfiguracija_uredaja/netmiko_konfiguracija_uredaja.py

Skripta se povezuje s uređajima i primjenjuje konfiguracijske naredbe definirane u odgovarajućim .txt datotekama.

2. Dohvaćanje rezultata

Pokrenite:

python rezultati_uredaja/netmiko_rezultati_uredaja.py

Rezultati komunikacije s uređajima spremaju se u direktorij:

rezultati_uredaja/
3. Izrada sigurnosne kopije

Pokrenite:

python sigurnosna_kopija_uredaja/netmiko_sigurnosna_kopija_uredaja.py

Konfiguracije uređaja spremaju se kao sigurnosne kopije u direktorij:

sigurnosna_kopija_uredaja/

Datoteke sigurnosnih kopija uključuju datum izrade, što omogućuje lakše praćenje različitih verzija konfiguracija.

🔧 Konfiguracija

Prije pokretanja skripti potrebno je definirati podatke za povezivanje s mrežnim uređajima.

Potrebni podaci mogu uključivati:

IP adresu uređaja
Korisničko ime
Lozinku
Tip uređaja (device_type)
SSH postavke
Konfiguracijske naredbe

Važno: Nemojte spremati stvarne lozinke, privatne ključeve ili druge osjetljive podatke u GitHub repozitorij.

🎯 Cilj projekta

Cilj projekta je demonstrirati primjenu Python programskog jezika i biblioteke Netmiko za automatizaciju administracije mrežnih uređaja.

Projekt omogućuje:

🔧 automatiziranu konfiguraciju uređaja
📊 dohvaćanje rezultata s uređaja
💾 izradu sigurnosnih kopija konfiguracija
🔐 povezivanje s uređajima putem SSH-a
🤖 automatizaciju ponavljajućih mrežnih zadataka
