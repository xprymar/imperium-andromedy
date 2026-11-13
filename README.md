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
