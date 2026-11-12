# Imperium Andromedy — oficjalna witryna projektu (Etap II)

**Wersja:** 1.4 (12 listopada 2026 r.)\
**Stan:** strona opublikowana pod https://imperiumandromedy.pl, domena i HTTPS aktywne.  
**Zakupy i zobowiązania projektu (12.11.2026):** 123,66 zł; środki niezaangażowane 176,34 zł. Domena 20,53 zł, MEDA z dostawą 47,99 zł, Kingston DataTraveler Exodia M 64 GB z dostawą 36,88 zł oraz zakupy Action 18,26 zł (kartki samoprzylepne 3,15 zł, koszulki do segregatora 100 szt. 8,32 zł, segregator 6,79 zł). Pendrive zamówiono, płatność do potwierdzenia; dostaw obu urządzeń nie potwierdzono.  
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

Bieżące pliki tekstowe: `dane/ewidencja_wydatkow.csv`, `dane/budzet_aktualny.csv` oraz `dokumenty/Bilans_Skarbu_2026-11-12.md`. Bilans z 11.11.2026 zachowano jako historyczny. Pliki DOCX i XLSX z 11.11.2026 są **historycznymi migawkami** i nie uwzględniają późniejszych zakupów Action; bieżąca ewidencja jest w CSV i w rejestrze Excel z 12.11.2026. Aneks nr 4 w formacie Word jest dostępny na stronie Skarbu i w Archiwum.

### Ważne

- Nie przesyłaj do publicznego repozytorium wewnętrznego rejestru obywateli lub prywatnej księgowości bez sprawdzenia danych.
- Po potwierdzeniu nowej płatności uzgodnij ewidencję wydatków, bilans i datę danych na stronie.
- Roszczenie do M31 ma charakter deklaracji projektu, bez skutku prawnego jako uznana suwerenność.
- Plik `CNAME` wskazuje opłaconą domenę imperiumandromedy.pl.

## Infrastruktura cyfrowa w budżecie Fazy I

W przyjętym planie Fazy I przydzielono **60 zł** na infrastrukturę cyfrową: domena `.pl` (limit 20,53 zł), pamięć USB (30,99 zł) i techniczne koszty/dostawę (8,48 zł). Domenę opłacono: 20,53 zł. Pendrive Kingston 64 GB zamówiono za 36,88 zł z dostawą (26,49 zł + 10,39 zł). Razem zakupy IT 57,41 zł, pozostaje 2,59 zł. Płatność pendrive’a wymaga potwierdzenia. Hosting GitHub Pages jest bezpłatny.


## Aktualizacja Skarbu 11.11.2026

Cesarz zatwierdził przesunięcie 20 zł z rezerwy do badań. Obecne limity: rezerwa 160 zł, infrastruktura cyfrowa 60 zł, dokumentacja 30 zł, badania 50 zł. Trzy zakupy: IA-FIN/001/2026 20,53 zł, IA-FIN/002/2026 47,99 zł oraz IA-FIN/003/2026 36,88 zł. Wydruk dokumentów własną drukarką: 0 zł; materiały Action planowane na 12.11.2026. W `finanse.html` znajduje się aktualny stan; plan finansowy Word zawiera aneks nr 2, a aktualny bilans po zakupie pendrive’a jest w osobnym aneksie nr 3. W katalogu `dokumenty/` opublikowano także aktualny plan MEDA, centralny rejestr Excel i historyczną kopię ZIP sprzed korekty odezwy. Linki do pobrania znajdują się w `archiwum.html`.

## Zabezpieczenia witryny

Polityka CSP w dokumentach HTML dopuszcza skrypty, arkusze stylów i obrazy z domeny witryny. Polityka no-referrer ogranicza przekazywanie adresu odwiedzanej strony do innych serwisów. Przekierowanie HTTP na HTTPS obsługuje GitHub Pages.


## Aktualizacja Skarbu 12.11.2026

Cesarz przekazał informację o zakupie w sklepie Action: kartki samoprzylepne **3,15 zł**, koszulki do segregatora (100 szt.) **8,32 zł** i segregator **6,79 zł**. Łącznie **18,26 zł** ujęte w dziale dokumentacja, identyfikatory **IA-FIN/004–006/2026**. W dziale dokumentacja pozostało **11,74 zł** z limitu 30,00 zł. Łączny koszt zakupów i zobowiązań Fazy I wzrósł do **123,66 zł**, a niezaangażowane środki wynoszą **176,34 zł**. Dotychczasowe zobowiązanie za pendrive pozostaje ujęte w koszcie zakupów, ale płatność nadal wymaga potwierdzenia.
