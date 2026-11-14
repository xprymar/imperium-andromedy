# Imperium Andromedy — oficjalna witryna projektu (Etap II)

**Wersja:** 1.5 (13 listopada 2026 r.)\
**Stan:** strona opublikowana pod https://imperiumandromedy.pl, domena i HTTPS aktywne.  
**Opłacone zakupy projektu (12.11.2026):** 123,66 zł; środki niezaangażowane 176,34 zł. Domena 20,53 zł, MEDA z dostawą 47,99 zł, Kingston DataTraveler Exodia M 64 GB z dostawą 36,88 zł oraz zakupy Action 18,26 zł (kartki samoprzylepne 3,15 zł, koszulki do segregatora 100 szt. 8,32 zł, segregator 6,79 zł). Pendrive opłacono przy zamówieniu 11.11.2026 (potwierdzenie Cesarza z 12.11); odbiór obu urządzeń potwierdzono 13.11.2026.  
**Język:** polski.

## Zawartość

- `index.html` — witryna główna, flaga, władze, misja, bilans, etapy rozwoju;
- `konstytucja.html` — pełny tekst zatwierdzonej Konstytucji;
- `finanse.html` — pełny tekst planu budżetowego Fazy I;
- `archiwum.html` — publiczny rejestr aktów i poprawiona odezwa Jakuba I;
- `dokumenty/` — pliki DOCX, rejestr XLSX i kopia historyczna archiwum ZIP;
- `assets/` — grafika flagi, herbu, style i skrypt mobilnej nawigacji.

Witryna jest responsywna i działa także lokalnie, bez serwera i bez połączenia internetowego. Nie ma formularzy gromadzących dane osobowe, pikseli reklamowych, narzędzi analitycznych ani ciasteczek śledzących.

## Jak uruchomić lokalnie

Otwórz `index.html` dwukrotnym kliknięciem. Możesz też uruchomić lokalny serwer z katalogu strony:

```bash
python -m http.server 8000
```

Następnie otwórz `http://localhost:8000/`.

## Publikacja w GitHub Pages

1. Na koncie GitHub utwórz nowe **publiczne repozytorium** dla projektu, np. `imperium-andromedy` (albo wykorzystaj istniejące repozytorium przeznaczone do tego projektu).
2. Prześlij do głównego katalogu repozytorium pliki z tej paczki (tak, by `index.html` leżał w katalogu głównym).
3. Otwórz **Settings → Pages**, wybierz **Deploy from a branch**, gałąź `main`, folder `/ (root)`, następnie **Save**.
4. Po opublikowaniu witryna będzie dostępna pod adresem `https://NAZWA_UŻYTKOWNIKA.github.io/imperium-andromedy/` (zależnie od nazwy repozytorium).
5. Opcjonalnie kup domenę `.pl` i ustaw ją w **Settings → Pages → Custom domain** oraz u rejestratora domeny. **Nie rób tego, zanim nie zdecydujesz o wydatku i nie sprawdzisz dostępności domeny**.

### Aktualny bilans i archiwum

Bieżące pliki tekstowe: `dane/ewidencja_wydatkow.csv`, `dane/budzet_aktualny.csv` oraz `dokumenty/Bilans_Skarbu_2026-11-12.md`. Bilans z 11.11.2026 zachowano jako historyczny. Pliki DOCX i XLSX z 11.11.2026 są **historycznymi migawkami** i nie uwzględniają późniejszych zakupów Action; bieżąca ewidencja jest w CSV i w [rejestrze Excel z 13.11.2026](dokumenty/Centralny_Rejestr_Imperium_Andromedy_2026-11-13.xlsx). Aneks nr 4 w formacie Word jest dostępny na stronie Skarbu i w Archiwum.

### Ważne

- Nie przesyłaj do publicznego repozytorium wewnętrznego rejestru obywateli lub prywatnej księgowości bez sprawdzenia danych.
- Po potwierdzeniu nowej płatności uzgodnij ewidencję wydatków, bilans i datę danych na stronie.
- Roszczenie do M31 ma charakter deklaracji projektu, bez skutku prawnego jako uznana suwerenność.
- Plik `CNAME` wskazuje opłaconą domenę imperiumandromedy.pl.

## Infrastruktura cyfrowa w budżecie Fazy I

W przyjętym planie Fazy I przydzielono **60 zł** na infrastrukturę cyfrową: domena `.pl` (limit 20,53 zł), pamięć USB (30,99 zł) i techniczne koszty/dostawę (8,48 zł). Domenę opłacono: 20,53 zł. Pendrive Kingston 64 GB zamówiono za 36,88 zł z dostawą (26,49 zł + 10,39 zł). Razem zakupy IT 57,41 zł, pozostaje 2,59 zł. Płatność za pendrive została dokonana 11.11.2026 przy składaniu zamówienia (potwierdzona przez Cesarza 12.11.2026). Hosting GitHub Pages jest bezpłatny.


## Aktualizacja Skarbu 11.11.2026

Cesarz zatwierdził przesunięcie 20 zł z rezerwy do badań. Obecne limity: rezerwa 160 zł, infrastruktura cyfrowa 60 zł, dokumentacja 30 zł, badania 50 zł. Trzy zakupy: IA-FIN/001/2026 20,53 zł, IA-FIN/002/2026 47,99 zł oraz IA-FIN/003/2026 36,88 zł. Wydruk dokumentów własną drukarką: 0 zł; materiały Action planowane na 12.11.2026. W `finanse.html` znajduje się aktualny stan; plan finansowy Word zawiera aneks nr 2, a aktualny bilans po zakupie pendrive’a jest w osobnym aneksie nr 3. W katalogu `dokumenty/` opublikowano także aktualny plan MEDA, centralny rejestr Excel i historyczną kopię ZIP sprzed korekty odezwy. Linki do pobrania znajdują się w `archiwum.html`.

## Zabezpieczenia witryny

Polityka CSP w dokumentach HTML dopuszcza skrypty, arkusze stylów i obrazy z domeny witryny. Polityka no-referrer ogranicza przekazywanie adresu odwiedzanej strony do innych serwisów. Przekierowanie HTTP na HTTPS obsługuje GitHub Pages.


## Aktualizacja Skarbu 12.11.2026

Cesarz przekazał informację o zakupie w sklepie Action: kartki samoprzylepne **3,15 zł**, koszulki do segregatora (100 szt.) **8,32 zł** i segregator **6,79 zł**. Łącznie **18,26 zł** ujęte w dziale dokumentacja, identyfikatory **IA-FIN/004–006/2026**. W dziale dokumentacja pozostało **11,74 zł** z limitu 30,00 zł. Łączne wydatki Fazy I wzrosły do **123,66 zł**, a niezaangażowane środki wynoszą **176,34 zł**. Pendrive opłacono w dniu zamówienia 11.11.2026; wszystkie zakupy Fazy I na 12.11.2026 zostały opłacone, łącznie 123,66 zł. Odbiór płytki MEDA oraz pendrive'a potwierdzono 13.11.2026. Wykonanie kopii archiwum wymaga osobnego potwierdzenia.

## Status Archiwum Imperialnego — 12.11.2026

Cesarz zgłosił ukończenie fizycznego Archiwum Imperialnego (Tom I). Zapis oparty jest na deklaracji założyciela, bez niezależnej weryfikacji zawartości segregatora. Nie potwierdzono jeszcze wykonania kopii zapasowej na zamówionym pendrivie. Zakończenie Fazy I nadal wymaga zamknięcia bilansu finansowego; nie ogłoszono jej formalnie zakończonej.

## Sprawozdanie końcowe finansów Fazy I — 12.11.2026

Sporządzono [IA-FIN-RAP/001/2026](dokumenty/Sprawozdanie_Finansowe_Fazy_I_2026-11-12.md) i przedłożono Cesarzowi do zatwierdzenia. Rozliczenie kasowo-budżetowe: zatwierdzony limit **300,00 zł**, wszystkie sześć opłaconych pozycji **123,66 zł**, niewykorzystane środki **176,34 zł**, w tym rezerwa **160,00 zł**. Wszelkie limity działów zostały zachowane. Pendrive został odebrany **13.11.2026**. Wykonanie kopii cyfrowej archiwum wciąż oczekuje na potwierdzenie. Sporządzenie sprawozdania nie oznacza zatwierdzenia przez Cesarza, formalnego zamknięcia Fazy I ani rozpoczęcia Fazy II. Bilans jest dostępny [na stronie](bilans-koncowy-fazy-i.html) oraz [w wersji Word do druku](dokumenty/IA-FIN-RAP-001-2026_Bilans_Koncowy_Fazy_I.docx). Status płatności uzgodniono z bieżącym rejestrem Excel i aneksem nr 4.

## Odbiór urządzenia MEDA — 13.11.2026

Cesarz potwierdził fizyczny odbiór i rozpakowanie Raspberry Pi Pico 2 WH, zakupionego za 47,99 zł z dostawą (IA-FIN/002/2026). Status sprzętu: **odebrane; czeka na konfigurację i testy MEDA 0.1**. Nie wpisujemy jeszcze wyniku eksperymentu, ponieważ nie został wykonany lub potwierdzony. Zakup był rozliczony wcześniej i odbiór nie zmienia salda Skarbu: 123,66 zł wydatków; 176,34 zł wolnego limitu. Nie potwierdzono odbioru pendrive'a.

## Dostawa pendrive'a i kompletność zakupów — 13.11.2026

**Protokół odbioru:** [IA-ARC-OD/001/2026](dokumenty/Protokol_Odbioru_Wyposazenia_2026-11-13.md) — dokumentuje odbiór dwóch urządzeń bez utożsamiania go z zakończeniem testów i archiwizacji.



Cesarz potwierdził odbiór pamięci USB Kingston DataTraveler Exodia M 64 GB. W tym samym dniu potwierdził również odbiór i rozpakowanie Raspberry Pi Pico 2 WH. Tym samym wszystkie zakupione elementy Fazy I zostały dostarczone albo udostępnione (domena, wyposażenie Action, płytka i pamięć USB). Status wykonania kopii zapasowej archiwum cyfrowego: **do potwierdzenia**. Odbiór nie powoduje ponownego naliczenia kosztów; pozostaje 123,66 zł wydatków i 176,34 zł niewykorzystanych środków. Bilans końcowy datowany na 12.11.2026 jest historycznym stanem na dzień bilansowy i nie należy go zmieniać wstecz.


## Formalne zamknięcie Fazy I — 13.11.2026

**DEKRET IA-DEC/004/2026 — ZATWIERDZONY.** Cesarz Jakub I decyzją z **13 listopada 2026 r.** zatwierdził bilans końcowy [IA-FIN-RAP/001/2026](dokumenty/Sprawozdanie_Finansowe_Fazy_I_2026-11-12.md) ze stanem na 12.11.2026 i **formalnie zakończył Fazę I — Organizacja ziemskiej administracji i dokumentacji**. Tekst aktu: [Dekret Imperialny nr 004/2026](dokumenty/Dekret_Imperialny_004_2026.md) i [wersja na stronie](dekret-004-2026.html). Budżet 300,00 zł, wydatki opłacone 123,66 zł, pozostało 176,34 zł (w tym nienaruszona rezerwa 160,00 zł). Zakupy w całości odebrane 13.11.2026 lub wcześniej; nadal **nie potwierdzono kopii archiwum na pendrivie ani testu MEDA 0.1**. Wcześniejsze informacje o niezatwierdzonym raporcie i otwartej Fazie I w rozdziałach datowanych 12.11.2026 są historycznym zapisem stanu sprzed dekretu. **Faza II nie została otwarta, nie przydzielono nowego budżetu ani nie zatwierdzono nowych zakupów.**


## Inauguracja Fazy II i przygotowanie MEDA 0.1 — 13.11.2026

**Faza II została zatwierdzona i uruchomiona** na podstawie wyraźnej decyzji Cesarza Jakuba I. [Dekret IA-DEC/005/2026](dokumenty/Dekret_Imperialny_005_2026.md) zatwierdza [plan IA–PLAN/II–001/2026](dokumenty/Plan_Strategiczny_Fazy_II_2026-11-13.md), harmonogram 90 dni (13.11.2026–10.02.2027), limit 60,00 zł i wyodrębnienie poza budżetem II rezerwy 116,34 zł. **Wydatki Fazy II na start: 0,00 zł.** Alokacje: 35,00 zł MEDA; 5,00 zł infrastruktura i bezpieczeństwo; 10,00 zł dokumentacja; 10,00 zł bufor. Żadne zakupy nie zostały automatycznie zatwierdzone. Historyczny bilans Fazy I pozostaje bez zmian.

Projekt MEDA prowadzony przez Departament Badań Kosmicznych. [MEDA 0.1](meda-0-1.html): przygotowano [kod MicroPython](programy/meda/meda_0_1_hello.py) i [dziennik IA–MEDA–OBS/001](dokumenty/IA-MEDA-OBS-001-2026_Dziennik_uruchomienia.md), ale **nie potwierdzono uruchomienia ani 10 błysków LED**. Firmware dla Pico 2 WH: stabilna wersja z oficjalnego https://micropython.org/download/RPI_PICO2_W/; środowisko Thonny: https://thonny.org/.


## MEDA 0.1 — ukończenie pierwszego testu (13.11.2026)

Cesarz Jakub I po wykonaniu instrukcji zgłosił: „Wszystko zadziałało”. Na tej podstawie odnotowano **pomyślne ukończenie MEDA 0.1**, tj. uruchomienie MicroPythona oraz 10 kontrolowanych błysków wbudowanej LED na Raspberry Pi Pico 2 WH. Wpis w [dzienniku IA–MEDA–OBS/001/2026](dokumenty/IA-MEDA-OBS-001-2026_Dziennik_uruchomienia.md) ma charakter meldunku wykonawcy. Szczegóły firmware i dokładna godzina nie zostały przekazane. [Strona MEDA 0.1](meda-0-1.html) ma status zakończony; **MEDA 1.0 (Morse) pozostaje do wykonania**. Brak wydatków Fazy II; kopia archiwum na pendrivie wciąż niepotwierdzona.


## MEDA 1.0 — nadajnik Morse'a: przygotowanie 13.11.2026

Kontynuując wykonany test MEDA 0.1, Departament Badań Kosmicznych przygotował [program MicroPython](programy/meda/meda_1_0_morse.py), [instrukcję na stronie](meda-1-0.html) i [dziennik IA–MEDA–OBS/002/2026](dokumenty/IA-MEDA-OBS-002-2026_Dziennik_Morse.md). Wiadomość: `IMPERIUM ANDROMEDY JAKUB I ZIEMIA 10 11 2026`. Sterowanie: START, TEMPO 5–25 WPM, STATUS, STOP; Ctrl+C w trakcie emisji. Sukces wymaga trzech fizycznie zaobserwowanych i potwierdzonych emisji; **aktualny status 0/3, testy NIEPOTWIERDZONE**. Dalsze wydatki: 0,00 zł. To lokalny test komunikacji optycznej, nie emisja do M31.


## MEDA 1.0 — zakończenie testów (13.11.2026)

Po przeprowadzeniu instrukcji [MEDA 1.0](meda-1-0.html) operator przekazał meldunek „Przebiegło pomyślnie”. W kontekście polecenia wykonania trzech emisji odnotowano **3/3 sesje jako pomyślne według zbiorczego meldunku operatora**. Szczegóły w [dzienniku IA–MEDA–OBS/002/2026](dokumenty/IA-MEDA-OBS-002-2026_Dziennik_Morse.md). Nie uzyskano danych o dokładnych godzinach ani tempie; nie przeprowadzono niezależnego odbioru sygnału. MEDA 0.1 i 1.0 zakończone; MEDA 1.5, ewentualny panel lokalny Wi-Fi, pozostaje następnym opcjonalnym krokiem. Budżet Fazy II nie zmienił się: 60,00 zł limitu, 0,00 zł wydatków; kopia cyfrowa archiwum na pendrivie nadal niepotwierdzona.


## MEDA 1.5 — przygotowanie panelu Wi-Fi (13.11.2026)

Po ukończeniu MEDA 1.0 utworzono [program panelu Wi-Fi](programy/meda/meda_1_5_panel_wifi.py), [wzór pliku danych sieciowych](programy/meda/wifi_local_PRZYKLAD.py), [dziennik IA–MEDA–OBS/003/2026](dokumenty/IA-MEDA-OBS-003-2026_Dziennik_WiFi.md) i [instrukcję na stronie](meda-1-5.html). Wersja testowa łączy się z prywatną siecią Wi-Fi 2,4 GHz i udostępnia lokalne polecenia LED ON, LED OFF, MORSE (`MEDA ANDROMEDA`), STOP. Rzeczywiste hasło Wi-Fi wolno umieścić wyłącznie lokalnie w pliku `wifi_local.py` na płytce; nie publikować tego pliku. Panel HTTP nie posiada logowania/HTTPS i nie jest przeznaczony do publicznego Internetu. **Status testu: niepotwierdzony, 0/4.** Wydatki Fazy II wciąż 0,00 zł.


## Diagnostyka MEDA 1.5 — bezpośredni punkt Wi-Fi Pico, 14.11.2026

Telefon Android zgłaszał ERR_TOO_MANY_RETRIES przy próbie dostępu do serwera Pico na 192.168.18.110, podczas gdy komputer Ethernet otwierał stronę. Wszystkie urządzenia należały do 192.168.18.0/24. Zidentyfikowano router ARRIS TG6441B; izolacja AP pozostaje hipotezą, nie potwierdzonym stanem konfiguracji. Przygotowano [diagnostyczny serwer HTTP w trybie AP](programy/meda/meda_1_5_pico_ap_test.py) i [protokół testu](dokumenty/IA-MEDA-OBS-004-2026_Test_Pico_AP.md). Wymaga prywatnego pliku `meda_ap_config.py` na Pico, z indywidualnym hasłem; nie publikować danych dostępowych. **Status: tylko przygotowano, wynik niepotwierdzony.** Bez nowych kosztów i bez zmian w zatwierdzonym programie MEDA 1.5.
