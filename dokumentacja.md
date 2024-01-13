## DOKUMENTACJA APLIKACJI MEDRADAR ZREALIZOWANEJ W RAMACH ZAJĘĆ INŻYNIERII OPROGRAMOWANIA W SEMESTRZE ZIMOWYM ROKU AKADEMICKIEGO 2023/2024

## 1.	Charakterystyka oprogramowania

Nazwa skrócona: MEDRADAR

Nazwa pełna: MEDRADAR – INTERNETOWA REJESTRACJA PACJENTÓW

Krótki opis ze wskazaniem celów: 

Aplikacja internetowa została opracowana z myślą o obszarze zarządzania wybraną placówką medyczną, z zaimplementowanymi funkcjonalnościami umożliwiającymi efektywną obsługę procesów zapisów oraz rejestracji pacjentów, zarówno w kontekście świadczeń finansowanych ze środków Narodowego Funduszu Zdrowia, jak i w przypadku wizyt prywatnych. Jednym z głównych celów aplikacji jest wspieranie pacjentów poprzez ułatwienie procesu zapisów oraz przypominanie o zbliżających się wizytach. Implementacja tej aplikacji jest kluczowym krokiem w optymalizacji procesów administracyjnych i organizacyjnych w placówce medycznej, wspierając jednocześnie komunikację z pacjentami i poprawiając jakość świadczonych usług.

## 2.	Prawa autorskie

Autorzy:

Klaudia Biendarra,

Natalia Szymańska,

Mieczysław Kledzik.

Warunki licencyjne do oprogramowania:

Licencja Freeware na to oprogramowanie, nazwane XXX, umożliwia jego bezpłatne użytkowanie zarówno w celach osobistych, jak i komercyjnych. Użytkownik ma prawo do swobodnego rozpowszechniania oryginalnej wersji, lecz nie może modyfikować ani dekompilować kodu źródłowego. Brak oficjalnego wsparcia technicznego. Wszelkie zmiany w licencji będą dostępne online. Autor nie gwarantuje użyteczności czy niezawodności oprogramowania, a licencja automatycznie wygasa w przypadku naruszenia jej postanowień.

## 3.	Specyfikacja wymagań.

IDENTYFIKATOR	RQ-001

NAZWA	Rejestracja pacjentów

OPIS	Implementacja funkcji umożliwiającej skuteczną rejestrację pacjentów w systemie, poprzez rejestrację, a później logowanie się do swojego konta.

PRIORYTET	1 – wymagane

KATEGORIA	funkcjonalne


IDENTYFIKATOR	RQ-002

NAZWA	Dane osobowe

OPIS	Przekierowanie do strony home i obowiązek zarejestrowania podstawowych danych pacjenta wymaganych do zapisania wizyty, takich jak imię, nazwisko, data urodzenia itp.

PRIORYTET	1 – wymagane

KATEGORIA	funkcjonalne

IDENTYFIKATOR	RQ-003

NAZWA	Błędne wpisane danych przez pacjenta

OPIS	Dodanie monitu gdy pacjent zauważy błąd w swoich danych, aby skontaktował się z przychodnią – ręczne zmienianie danych pacjentów przez administratorów przychodni. 

PRIORYTET	1 – wymagane

KATEGORIA	funkcjonalne


IDENTYFIKATOR	RQ-004

NAZWA	Rejestracja Wizyt

OPIS	Dodanie funkcji umożliwiającej zapis pacjentów na wizyty. W tym celu system powinien przechowywać daty dostępności danego lekarza oraz umożliwiać wybór terminu przez pacjenta.

PRIORYTET	1 – wymagane

KATEGORIA	funkcjonalne


IDENTYFIKATOR	RQ-005

NAZWA	Weryfikacja Dostępności Terminów

OPIS	Implementacja mechanizmu weryfikacji dostępności terminów, aby uniknąć konfliktów z już zarejestrowanymi pacjentami.

PRIORYTET	1 – wymagane

KATEGORIA	funkcjonalne



IDENTYFIKATOR	RQ-006

NAZWA	Możliwość wyboru wizyty – prywatna / NFZ

OPIS	Implementacja mechanizmu pozwalającego na wybór pomiędzy wizytą komercyjną, a wizytą na NFZ.

PRIORYTET	1 – wymagane

KATEGORIA	funkcjonalne


IDENTYFIKATOR	RQ-007

NAZWA	Przypomnienia o Wizytach

OPIS	Dodanie funkcji wysyłania przypomnień o nadchodzących wizytach pacjentom, w celu zminimalizowania liczby nieobecności.

PRIORYTET	2 – przydatne

KATEGORIA	funkcjonalne


IDENTYFIKATOR	RQ-008

NAZWA	Historia Rejestracji Pacjentów

OPIS	Zapewnienie możliwości przeglądania historii rejestracji pacjentów w celu uzyskania kompleksowej widoczności danych.

PRIORYTET	2 – przydatne

KATEGORIA	funkcjonalne


IDENTYFIKATOR	RQ-009

NAZWA	Wydruk potwierdzenia wizyty

OPIS	Implementacja możliwości drukowania potwierdzeń rejestracji wizyt dla pacjentów.

PRIORYTET	3 – opcjonalne

KATEGORIA	funkcjonalne


IDENTYFIKATOR	RQ-010

NAZWA	Zabezpieczenia Danych Pacjentów

OPIS	Chronienie konta pacjenta hasłem – wprowadzonym przez użytkownika poprzez przechowywanie go w zaszyfrowanej bazie danych. Użycie chronionej bazy danych do przechowywania danych pacjentów.

PRIORYTET	1 – wymagane

KATEGORIA	pozafunkcjonalne


IDENTYFIKATOR	RQ-011

NAZWA	Automatyczne przekierowanie z HTTP na HTTPS

OPIS	Automatyczne przekierowania z HTTP na HTTPS zapewniają, że cała komunikacja odbywa się w bezpiecznym środowisku, zwiększając ogólny poziom bezpieczeństwa strony.

PRIORYTET	2 - przydatne

KATEGORIA	pozafunkcjonalne


## 4.	Architektura oprogramowania.

Architektura rozwoju – stos technologiczny:
•	Python
•	Django
•	Html
•	DB Browser for SQLite

Architektura uruchomieniowa – stos technologiczny:
•	System operacyjny Windows: 8, 10, 11.
•	Przeglądarka internetowa (Mozilla, Google Chrome, Opera, Microsoft Edge).

## 5.	Testy 

a)	Testy funkcjonalne: 

IDENTYFIKATOR	FUNC_TEST_001

NAZWA SCENARIUSZA	Test rejestracji pacjentów

SCENARIUSZ	Krok 1:Użytkownik wybiera opcję "Rejestracja".

Krok 2: Wypełnia formularz danych osobowych.

Krok 3: Wysyła formularz.

Krok 4: Sprawdzenie czy dane pacjenta zostały zarejestrowane poprawnie w systemie.

OCZEKIWANY REZULTAT	Dane pacjenta są zapisane w bazie danych, można je odnaleźć i potwierdzić poprawność.

WYNIK	POZYTYWNY


IDENTYFIKATOR	FUNC_TEST_002

NAZWA SCENARIUSZA	Test umawiania wizyt

SCENARIUSZ	Krok 1: Użytkownik loguje się na swoje konto.

Krok 2: Wybiera opcję umówienia wizyty.

Krok 3: Wybiera preferowaną datę i godzinę.

Krok 4: Potwierdza umówienie wizyty.

OCZEKIWANY REZULTAT	Wizyta zostaje zarejestrowana w kalendarzu pacjenta i w systemie przychodni.

WYNIK	W TRAKCIE BUDOWY


IDENTYFIKATOR	FUNC_TEST_003

NAZWA SCENARIUSZA	Pierwsze zalogowanie

SCENARIUSZ	Krok 1: Po rejestracji wyskakuje monit o konieczności podania swoich danych

Krok 2: Użytkownik musi wpisać swoje dane.

OCZEKIWANY REZULTAT	Monit wyświetla się tylko raz i tylko dla nowych użytkowników przychodni.

WYNIK	POZYTYWNY

IDENTYFIKATOR	FUNC_TEST_004

NAZWA SCENARIUSZA	Rejestracja danych pacjenta

SCENARIUSZ	Krok 1: Użytkownik wpisuje swoje dane.

Krok 2: Użytkownik wysyła swoje dane.

Krok 3: Dane użytkownika zostają zapisane w bazie.

OCZEKIWANY REZULTAT	Dane pacjenta znajdują się w bazie.

WYNIK	POZYTYWNY

IDENTYFIKATOR	FUNC_TEST_005

NAZWA SCENARIUSZA	Sprawdzenie dostępnych lekarzy

SCENARIUSZ	Krok 1: Użytkownik klika na Listę Lekarzy.

Krok 2: Po przejściu na podstrone wyświetla się lista dostępnych aktualnie lekarzy.

Krok 3: Listę można sortować po specjalizacji i sprawdzić w jakie dni i w jakich godzinach lekarz przyjmuje w przychodni. 

OCZEKIWANY REZULTAT	Wyświetlenie wszystkich lekarzy obecnie pracujących w przychodni oraz sortowanie ich po specjalizacji z poprawnymi godzinami przyjęcia. 

WYNIK	POZYTYWNY

IDENTYFIKATOR	FUNC_TEST_006

NAZWA SCENARIUSZA	Podstrona z wizytami pacjenta

SCENARIUSZ	Krok 1: Użytkownik klika na Lista Wizyt.

Krok 2: Po przejściu na podstronę wyświetlają się wizyty, które już się odbyły jak i te nadchodzące.

OCZEKIWANY REZULTAT	Wyświetlenie wszystkich historycznych wizyt, oraz nadchodzących dla danego pacjenta. 

WYNIK	POZYTYWNY


IDENTYFIKATOR	FUNC_TEST_007

NAZWA SCENARIUSZA	Kontakt z przychodnią

SCENARIUSZ	Krok 1: Użytkownik klika na Kontakt

Krok 2: Po przejściu na podstronę wyświetlają się możliwe metody kontaktu z przychodnią.

OCZEKIWANY REZULTAT	Wyświetlenie wszystkich możliwości kontaktu z przychodnią.

WYNIK	POZYTYWNY


b)	Testy wydajnościowe:

IDENTYFIKATOR	PERF_TEST_001

NAZWA SCENARIUSZA	Test czasu odpowiedzi

SCENARIUSZ	Pomiar czasu potrzebnego na rejestrowanie pacjentów, umawianie wizyt.

OCZEKIWANY REZULTAT	Akcje użytkownika są obsługiwane w rozsądnym czasie, zapewniając płynne doświadczenie użytkownika.

WYNIK	POZYTYWNY

IDENTYFIKATOR	PERF_TEST_002

NAZWA SCENARIUSZA	Ocena responsywności interfejsu na różnych urządzeniach.

SCENARIUSZ	Testowanie interfejsu użytkownika na różnych przeglądarkach internetowych.

OCZEKIWANY REZULTAT	Określenie, czy interfejs użytkownika jest responsywny, zapewniając w ten sposób płynne doświadczenie użytkownika.

WYNIK	POZYTYWNY
