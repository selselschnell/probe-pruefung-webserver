# Probe Prüfung

Dies ist eine Beispiel wie die nächste Informatik-Prüfung aussehen wird. Die
Prüfung ist Open-Book, was bedeutet Sie dürfen alle Ressourcen verwenden:
jupyter notebooks, dieses Projekt, das letzte Projekt, das Internet...

**Kommunikation mit anderen ist verboten!!!**

Arbeiten Sie mit Commits! Spätestens nach jeder Aufgabe sollten Sie einen
Commit erstellen (verwenden Sie `"Aufgabe x fertig."` als Commit-Nachricht.)

## Aufgabe 1 (Repository forken - 1 P.)

Forken Sie das Repository in Ihren eigenen Github-Account.

## Aufgabe 2 (Style anpassungen - 3 P.)

Ändern Sie die Datein `main.css` so ab, das möglichst genau dem folgenden Bild
entspricht. Verschwenden Sie keine Zeit mit Details.

![index.png](index.png)

## Aufagbe 3 (Webscraper schreiben - 4 P.)

1. Gehen Sie auf die Webseite
   'https://www.w3schools.com/cssref/css_selectors.asp' und untersuchen Sie die
   Tabelle. Welche HTML/CSS Elemente werden verwendet?
3. Wie heisst die CSS Klasse des mittleren Eintrags?
4. Öffnen Sie die Datei `scrape.py` und lesen Sie durch den Code.
5. Führen Sie die Datei `scrape.py` aus und vergleichen Sie den Inhalt der neu
   erzeugten Datei `selectors.json` mit der Tabelle auf der Webseite.
   Was fällt Ihnen auf?
6. Organisieren Sie Ihren Code in 3 Funktionen wie sie in `run.py` definiert
   sind.
   - `my_scraper()` führt den Webscraping Code aus und gibt `table_rows`
     zurück.
   - `my_filter()` führt Ihre filter-Funktion aus (ist für den Moment noch leer)
     und gibt `table_rows` zurück
   - `write_json()` schreibt das Resultat in eine json-Datei.
7. Löschen Sie die Datei `selectors.json` und führen Sie alle 3 Funktionen in
   `scrape.py` aus. Wenn alles geklappt hat, sollten Sie die Datei
   `selectors.json` wieder erhalten. Kopieren Sie die 3 Funktionen nach
   `run.py` und stellen Sie sicher das alle benötigten Module geladen sind.

## Aufgabe 4 (In die eigene Website einbauen - 4 P.)

1. Fügen Sie eine neue Datei `scraping.html` hinzu, die `base.html` erweitert.
1. Fügen Sie einen Link hinzu der den Webscraping Code in `run.py` aufruft. Sie
   können das verhalten testen indem Sie `selectors.json` löschen. Diese sollte
   nach anklicken des Links neu erscheinen.

## Aufgabe 5 (Resultate anzeigen - 4 P.)

1. Erstellen Sie eine neue Seite `results.html` die `base.html` erweitert.
   Diese Seite soll die Resultate von Ihrem Webscraping anzeigen.
1. Passen Sie die Ausgabe auf der Webseite nach Ihren wünschen an. Vielleicht
   möchten Sie alles in einer Tabelle darstellen, oder Sie möchten nur ein
   zufälliges Element mit der `choice`-Funktion darstellen.

## Aufagbe 6 (Pull Request - 1 P.)

Erstellen Sie einen Pull Request zu dem Repository das Sie geforkt haben
(upstream).

## Aufgabe 7 (Bonus 1: Erstellen Sie ein neues Design - 2 P.)

Erstellen Sie einen neuen Branch in dem Sie ein alternatives Design entwickeln.
Erstellen Sie einen weiteren Pull Request von diesem Branch.

## Aufgabe 8 (Bonus 2: Filtern - 3 P.)

Erstellen Sie einen neuen Branch und implementieren Sie eine filter-Funktion
die Elemente aus dem Webscraping filtert welche genau ein `;` enthalten.
Erstellen Sie einen neuen Pull Request wenn Sie fertig sind.
