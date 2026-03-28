[IDOR Vulnerability Testing - Praktische Checkliste](IDOR%20Vulnerability%20Testing%20-%20Praktische%20Checkliste%20272588ff46e680f4892dddcf3bc6d2ed.md)

Ihr Ziel ist es, die Anomalie zu finden.

1. Sortieren Sie im Angriffsfenster die Ergebnisse, indem Sie auf die Spaltenüberschrift **"Status "** klicken, um alle "200 OK"-Antworten zusammenzufassen.
2. Sehen Sie sich nun die Spalte **"Länge "** für alle "200 OK"-Antworten an. Sie werden feststellen, dass die meisten sichtbaren Produkte eine sehr ähnliche Antwortlänge haben.
3. **Finden Sie die "200 OK"-Antworten, deren "Länge" sich deutlich von allen anderen unterscheidet (kleiner ist).** Warum?
4. Klicken Sie auf eine dieser Zeilen in der Ergebnistabelle. Klicken Sie im unteren Bereich auf die Registerkarte **Antwort** > **Render**, um die Seite anzuzeigen und Ihren Verdacht zu bestätigen.

**Einreichung**

Um die Übung abzuschließen, machen Sie einen Screenshot des Fensters **Eindringlingsangriff**. Ihr Screenshot muss deutlich zeigen:

1. Die Liste der Payloads und ihre Antworten.
2. Die anomale Antwort (mit der unterschiedlichen Länge) wird hervorgehoben.
3. Die Registerkarte **Antwort > Rendern** mit den Details einer der kleineren Antworten.# Decoder Ring
- Be... sure... to... drink... your... Ovomaltine? Nein, das war's nicht.

**Ziel**

Ziel dieser Übung ist es, eine IDOR-Schwachstelle (Insecure Direct Object Reference) zu identifizieren und eine automatisierte Aufzählungstechnik zu verwenden, um ein verstecktes Produkt auf der Gin & Juice Shop-Website zu entdecken und darauf zuzugreifen.

**Hintergrund**

**Insecure Direct Object Reference (IDOR)** ist eine häufige Web-Schwachstelle, die auftritt, wenn eine Anwendung direkten Zugriff auf Objekte (wie Benutzerkonten, Dateien oder Datenbankeinträge) auf der Grundlage von Benutzereingaben ermöglicht. Zum Beispiel verweist eine URL wie `.../getProduct?id=123` direkt auf das Produkt `123`.

Wenn die Anwendung nicht ordnungsgemäß überprüft, ob der aktuelle Benutzer berechtigt ist, auf das angeforderte Objekt zuzugreifen, kann ein Angreifer die ID manipulieren, um auf Daten zuzugreifen, die er nicht sehen sollte, wie z. B. die Dokumente anderer Benutzer oder, in unserem Fall, versteckte Produkte.

Wenn wir die genaue ID eines versteckten Objekts nicht kennen, können wir eine **Aufzählung** durchführen: eine Technik, bei der wir schnell einen großen Bereich möglicher IDs testen, um herauszufinden, welche davon gültig sind. Wir werden Burp Intruder verwenden, um diesen Prozess zu automatisieren.

**Erforderliche Tools**

- Ein moderner Webbrowser (wie Firefox oder Chrome)
- Burp Suite Gemeinschaftsausgabe

### Anweisungen

### **Teil 1: Identifizieren Sie den Angriffsvektor**

1. Starten Sie die Burp Suite und konfigurieren Sie Ihren Browser so, dass er den Datenverkehr über den Proxy leitet.
2. Navigieren Sie zu dem Gin & Juice Shop unter `https://ginandjuice.shop`.
3. Klicken Sie auf ein beliebiges sichtbares Produkt, um zu dessen Detailseite zu gelangen.
4. Gehen Sie in Burp Suite auf die Registerkarte **Proxy** > **HTTP-Verlauf**. Suchen Sie die Anfrage für die Produktseite, die Sie gerade geladen haben. Sie wird wie folgt aussehen: GET /catalog/product?productId=1".
5. Beachten Sie, dass die Anwendung eine einfache Zahl im Parameter `productId` verwendet, um zu erkennen, welches Produkt angezeigt werden soll. Dies ist unser Ziel für den IDOR-Angriff.

**Teil 2: Aufzählung von IDs mit Burp Intruder**

Da wir nun ein Ziel haben, müssen wir die richtige ID für das versteckte Produkt finden. Wir werden diese Suche automatisieren.

1. Klicken Sie in Ihrem **HTTP-Verlauf** mit der rechten Maustaste auf die erfolgreiche Produktanfrage (z. B. `GET /catalog/product?productId=1`) und wählen Sie **"An Intruder senden "**.
2. Gehen Sie auf die Registerkarte **Intruder** > **Positionen**. Burp fügt automatisch Nutzlastmarkierungen (`§...§`) hinzu. Klicken Sie zunächst auf die Schaltfläche **"§ löschen "** auf der rechten Seite, um die Standardmarkierungen zu entfernen.
3. Markieren Sie im Anfrage-Editor vorsichtig **nur die Nummer** der `ProductId` (z.B. die `1` in `productId=1`). Klicken Sie auf die Schaltfläche **"Add §"**. Die Anfragezeile sollte nun wie folgt aussehen:
GET /Katalog/Produkt?productId=§1§ HTTP/2".
4. Wechseln Sie nun zur Registerkarte **Eindringlinge** > **Zahlungssätze**.
    - Stellen Sie unter **Zahlungssätze** sicher, dass der **Zahlungstyp** auf **"Zahlen "** eingestellt ist.
    - Konfigurieren Sie unter **Zahllastoptionen** den folgenden Bereich:
        - **Von:** `1`
        - **Bis:** `100`
        - Schrittweite:** `1`
5. Klicken Sie auf die Schaltfläche **"Angriff starten "** oben rechts. Ein neues Angriffsfenster wird geöffnet und beginnt, Anfragen zu senden.

### **Teil 3: Analysieren Sie die Ergebnisse und finden Sie das versteckte Produkt**

Das Angriffsfenster zeigt Ihnen das Ergebnis jeder Anfrage von ID 1 bis 100 an.