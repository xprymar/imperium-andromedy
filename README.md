# Imperium Andromedy — oficjalna witryna projektu (Etap II)

**Wersja:** 1.3 (11 listopada 2026 r.)\
**Stan:** strona opublikowana pod https://imperiumandromedy.pl, domena i HTTPS aktywne.  
**Wydatki projektu (11.11.2026):** 68,52 zł; pozostało 231,48 zł. Koszt domeny 20,53 zł, zakup MEDA z dostawą 47,99 zł. Dostawy sprzętu jeszcze nie potwierdzono.  
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

### Ważne

- Nie przesyłaj do publicznego repozytorium wewnętrznego rejestru obywateli lub prywatnej księgowości bez sprawdzenia danych.
- Po potwierdzeniu nowej płatności uzgodnij ewidencję wydatków, bilans i datę danych na stronie.
- Roszczenie do M31 ma charakter deklaracji projektu, bez skutku prawnego jako uznana suwerenność.
- Plik `CNAME` wskazuje opłaconą domenę imperiumandromedy.pl.

## Infrastruktura cyfrowa w budżecie Fazy I

W przyjętym planie Fazy I przydzielono **60 zł** na infrastrukturę cyfrową: domena `.pl` (limit 20,53 zł), pamięć USB (30,99 zł) i techniczne koszty/dostawę (8,48 zł). Domenę opłacono: 20,53 zł; pozostałe 39,47 zł w dziale IT pozostaje niewydane. Hosting GitHub Pages jest bezpłatny.


## Aktualizacja Skarbu 11.11.2026

Cesarz zatwierdził przesunięcie 20 zł z rezerwy do badań. Obecne limity: rezerwa 160 zł, infrastruktura cyfrowa 60 zł, dokumentacja 30 zł, badania 50 zł. Dwa wydatki: IA-FIN/001/2026 20,53 zł oraz IA-FIN/002/2026 47,99 zł. W `finanse.html` znajduje się aktualny stan; plan finansowy Word zawiera aneks nr 2. W katalogu `dokumenty/` opublikowano także aktualny plan MEDA, centralny rejestr Excel i historyczną kopię ZIP sprzed korekty odezwy. Linki do pobrania znajdują się w `archiwum.html`.

## Zabezpieczenia witryny

Polityka CSP w dokumentach HTML dopuszcza skrypty, arkusze stylów i obrazy z domeny witryny. Polityka no-referrer ogranicza przekazywanie adresu odwiedzanej strony do innych serwisów. Przekierowanie HTTP na HTTPS obsługuje GitHub Pages.
