## 📊 Zusammenfassung nach dem 80/20-Prinzip

### **Internet vs. World Wide Web: Der Unterschied**

**Oft verwechselt, aber unterschiedlich**:

```
┌──────────────────────────────────────┐
│          INTERNET                    │  = Infrastruktur
│  (Globales Netzwerk von Computern)  │  = Die "Straßen"
│                                      │
│  ┌────────────────────────────────┐ │
│  │     WORLD WIDE WEB (WWW)       │ │  = Dienst auf dem Internet
│  │  (System von verlinkten        │ │  = Die "Adressen & Ziele"
│  │   Hypertext-Dokumenten)        │ │
│  └────────────────────────────────┘ │
│                                      │
│  Weitere Dienste: E-Mail, FTP, etc. │
└──────────────────────────────────────┘
```

**Internet** = Netzwerk-Infrastruktur (TCP/IP, Router, Kabel) **World Wide Web** = Hypertext-System (HTTP, HTML, Webseiten)

**Analogie**: Internet = Straßennetz | WWW = Adressen und Häuser auf diesen Straßen

### **Webseiten-Typen**

**Static Website (Statische Webseite)**:

```
HTML-Datei auf Server
    ↓
Jeder Besucher sieht gleichen Inhalt
    ↓
Keine Datenbank, keine User-Interaktion
```

**Beispiele**: Visitenkarten-Websites, Portfolios, Infoseiten

**Dynamic Website (Dynamische Webseite)**:

```
Server generiert Inhalt on-the-fly
    ↓
Inhalt basiert auf User/Datenbank/Zeit
    ↓
Interaktive Features
```

**Beispiele**: Facebook, Amazon, YouTube, Nachrichtenportale

**Heute**: Wir lernen die **Bausteine** (HTML/CSS), die für **beide** gelten!

### **Wie das Web funktioniert: Client-Server-Modell**

```
┌──────────────┐                      ┌──────────────┐
│   BROWSER    │                      │  WEB SERVER  │
│   (Client)   │                      │              │
└──────┬───────┘                      └──────┬───────┘
       │                                     │
       │  1. HTTP Request                   │
       │  "Gib mir index.html"              │
       │ ───────────────────────────────────>│
       │                                     │
       │                                     │  2. Server
       │                                     │     findet Datei
       │                                     │
       │  3. HTTP Response                  │
       │  [HTML, CSS, JS Dateien]           │
       │ <───────────────────────────────────│
       │                                     │
       │  4. Browser rendert Seite          │
       │     (zeigt Inhalt an)              │
       │                                     │
```

**Ablauf**:

1. **User** tippt URL (z.B. `http://www.example.com`)
2. **Browser** sendet **HTTP Request** an **Server**
3. **Server** antwortet mit **HTML/CSS/JS-Dateien**
4. **Browser** **rendert** (zeichnet) Webseite

**Wichtig**: Browser = Software auf **deinem** Gerät | Server = Computer **irgendwo** im Internet

### **HTML: Die Struktur (das "Was")

**HTML (HyperText Markup Language)** = **Auszeichnungssprache** für Webseiten-Struktur

**Kernkonzepte**:

#### **Tags (Markierungen)**

```html
<tagname>
```

- Umgeben von **Spitzklammern** `< >`
- Meist **paarweise**: `<p>` (öffnend) und `</p>` (schließend)
- Schließ-Tag hat **Schrägstrich** `/`

#### **Elemente**

```html
<p>Dies ist ein Absatz.</p>
 │              │          │
 │              │          └─ Closing Tag
 │              └──────────── Inhalt (Content)
 └─────────────────────────── Opening Tag

Zusammen = ELEMENT
```

**Void Elements** (ohne Schließ-Tag):

```html
<img src="bild.jpg" alt="Beschreibung">
<br>  <!-- Zeilenumbruch -->
<hr>  <!-- Horizontale Linie -->
```

#### **Attribute**

```html
<a href="https://google.com">Zu Google</a>
   │                │
   │                └─ Wert (Value)
   └──────────────────── Name

Format: name="value"
```

### **HTML-Grundstruktur: Das Skelett jeder Webseite**

```html
<!DOCTYPE html>                    <!-- Dokumenttyp: HTML5 -->
<html>                             <!-- Wurzelelement -->
<head>                             <!-- Meta-Bereich (unsichtbar) -->
    <meta charset="UTF-8">         <!-- Zeichenkodierung -->
    <meta name="viewport" 
          content="width=device-width, 
                   initial-scale=1.0">  <!-- Responsive Design -->
    <title>Meine Seite</title>     <!-- Titel (Browser-Tab) -->
</head>
<body>                             <!-- Sichtbarer Inhalt -->
    <h1>Überschrift</h1>           <!-- Heading -->
    <p>Ein Absatz Text.</p>        <!-- Paragraph -->
</body>
</html>
```

**Struktur-Übersicht**:

```
<!DOCTYPE html>     → Dokumenttyp-Deklaration
<html>              → Alles drin
  <head>            → Meta-Informationen
    <title>         → Seitentitel
  </head>
  <body>            → Sichtbarer Content
    <h1>, <p>, ...  → Inhaltselemente
  </body>
</html>
```

### **Wichtige HTML-Tags**

|Tag|Bedeutung|Beispiel|
|---|---|---|
|`<h1>` bis `<h6>`|Überschriften (1=größte)|`<h1>Hauptüberschrift</h1>`|
|`<p>`|Absatz (Paragraph)|`<p>Text hier.</p>`|
|`<a>`|Link (Anchor)|`<a href="url">Text</a>`|
|`<img>`|Bild (Image)|`<img src="bild.jpg" alt="Beschreibung">`|
|`<div>`|Container (Block-Level)|`<div>Gruppierter Inhalt</div>`|
|`<span>`|Container (Inline)|`<span>Inline-Text</span>`|
|`<ul>` / `<ol>`|Liste (unordered/ordered)|`<ul><li>Item</li></ul>`|
|`<li>`|Listenelement|`<li>Punkt 1</li>`|
|`<br>`|Zeilenumbruch|`Text<br>Neue Zeile`|
|`<hr>`|Horizontale Linie|`<hr>`|

**Wichtige Attribute**:

- `href`: Link-Ziel (`<a href="...">`)
- `src`: Quelle (`<img src="...">`)
- `alt`: Alternativtext (`<img alt="...">`)
- `class`: CSS-Klasse (`<div class="...">`)
- `id`: Eindeutige ID (`<div id="...">`)
- `style`: Inline-CSS (`<p style="...">`)

### **CSS: Das Styling (das "Wie")

**CSS (Cascading Style Sheets)** = **Stylesheet-Sprache** für Webseiten-Aussehen

**Separation of Concerns**:

```
HTML → Was IST der Inhalt?      (Struktur, Bedeutung)
CSS  → Wie SIEHT er aus?        (Farbe, Layout, Schrift)
```

**CSS kontrolliert**:

- 🎨 Farben
- ✍️ Schriftarten und -größen
- 📏 Abstände (Margin, Padding)
- 📐 Layout (Position, Größe)
- ✨ Animationen

#### **CSS-Syntax**

```css
selector {
  property: value;
  property: value;
}
```

**Beispiel**:

```css
p {
  color: navy;
  font-size: 16px;
}

│   │         │
│   │         └─ Wert (Value)
│   └─────────── Eigenschaft (Property)
└───────────────── Selektor (wählt Elemente)
```

**Erklärung**: Alle `<p>`-Elemente bekommen blaue Schrift und Schriftgröße 16 Pixel

#### **CSS-Selektoren**

**Element-Selektor** (wählt alle Elemente eines Typs):

```css
h1 {
  color: teal;
}
```

→ Alle `<h1>` werden türkis

**Class-Selektor** (wählt Elemente mit bestimmter Klasse):

```css
.highlight {
  background-color: yellow;
}
```

→ Alle Elemente mit `class="highlight"` bekommen gelben Hintergrund

HTML:

```html
<p class="highlight">Dieser Text ist hervorgehoben</p>
```

**ID-Selektor** (wählt Element mit bestimmter ID):

```css
#header {
  font-size: 24px;
}
```

→ Element mit `id="header"` bekommt Schriftgröße 24px

HTML:

```html
<div id="header">Header-Inhalt</div>
```

**Wichtig**:

- **Class** (`.`) = Mehrfach verwendbar
- **ID** (`#`) = Nur einmal pro Seite!

### **CSS einbinden: Drei Methoden**

#### **1. External CSS (Empfohlen!)** ✅

**HTML** (`index.html`):

```html
<head>
  <link rel="stylesheet" href="style.css">
</head>
```

**CSS** (`style.css`):

```css
body {
  background-color: lightyellow;
}
```

**Vorteile**:

- ✅ Wiederverwendbar auf mehreren Seiten
- ✅ Saubere Trennung
- ✅ Leicht wartbar

#### **2. Internal CSS** ⚠️

```html
<head>
  <style>
    body {
      background-color: lightyellow;
    }
    h1 {
      color: green;
    }
  </style>
</head>
```

**Verwendung**: Nur für einzelne Seiten oder seitenspezifische Styles

#### **3. Inline CSS** ❌ (Vermeiden!)

```html
<p style="color: red; font-weight: bold;">Roter Text</p>
```

**Nachteile**:

- ❌ Vermischt Struktur und Stil
- ❌ Schwer wartbar
- ❌ Nicht wiederverwendbar

**Nur in Ausnahmefällen!**

### **HTML & CSS zusammen: Praktisches Beispiel**

**HTML** (`index.html`):

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Meine erste Webseite</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Willkommen!</h1>
    <p class="intro">Dies ist meine erste Webseite.</p>
    <p>Ich lerne HTML und CSS.</p>
</body>
</html>
```

**CSS** (`style.css`):

```css
body {
    background-color: #f0f0f0;  /* Hellgrauer Hintergrund */
    font-family: Arial, sans-serif;
}

h1 {
    color: dodgerblue;          /* Blaue Überschrift */
    text-align: center;         /* Zentriert */
}

.intro {
    font-weight: bold;          /* Fettschrift */
    color: darkgreen;           /* Dunkelgrün */
}
```

**Ergebnis im Browser**:

- Seite mit hellgrauem Hintergrund
- Blaue, zentrierte Überschrift "Willkommen!"
- Erster Absatz fett und dunkelgrün
- Zweiter Absatz normal (Arial-Schrift)

### **Webseite erstellen: Schritt-für-Schritt (Windows 11)**

#### **Schritt 1: Ordner erstellen**

1. **Datei-Explorer** öffnen
2. Neuen Ordner erstellen: `meine_webseite`
3. In den Ordner wechseln

#### **Schritt 2: VS Code öffnen**

1. VS Code starten
2. **Datei** → **Ordner öffnen** → `meine_webseite` wählen

#### **Schritt 3: Dateien erstellen**

1. Neue Datei: `index.html`
2. Neue Datei: `style.css`

**Ordnerstruktur**:

```
meine_webseite/
├── index.html
└── style.css
```

#### **Schritt 4: HTML schreiben**

**`index.html`**:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Meine Seite</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Hallo Welt!</h1>
    <p>Ich lerne Webentwicklung.</p>
</body>
</html>
```

**Speichern**: `Strg + S`

#### **Schritt 5: CSS schreiben**

**`style.css`**:

```css
h1 {
    color: dodgerblue;
}

body {
    background-color: #f0f0f0;
}
```

**Speichern**: `Strg + S`

#### **Schritt 6: Im Browser öffnen**

1. Im Datei-Explorer: `index.html` finden
2. **Rechtsklick** → **Öffnen mit** → **Browser wählen** (Chrome, Edge, Firefox)
3. Seite wird angezeigt!

**Änderungen testen**:

1. CSS-Datei ändern (z.B. `color: red;`)
2. Speichern (`Strg + S`)
3. Browser **aktualisieren** (`F5` oder `Strg + R`)
4. Änderung sehen!

### **Browser Developer Tools nutzen**

**HTML-Quellcode ansehen**:

1. Beliebige Webseite öffnen
2. **Rechtsklick** → **Seitenquelltext anzeigen** / **Untersuchen**
3. HTML-Code wird angezeigt

**Developer Tools öffnen**:

- **Windows**: `F12` oder `Strg + Shift + I`
- **Rechtsklick** → **Element untersuchen**

**Was sieht man?**

- **Elements**: HTML-Struktur (interaktiv)
- **Styles**: CSS-Regeln für ausgewähltes Element
- **Console**: JavaScript-Konsole (später)
- **Network**: Netzwerk-Anfragen

**Nützlich für**:

- Verstehen, wie Seiten aufgebaut sind
- Eigene Seiten debuggen
- CSS live testen (temporär)

### **Wichtige CSS-Eigenschaften (Starter-Set)**

**Text-Styling**:

```css
color: blue;              /* Textfarbe */
font-size: 20px;          /* Schriftgröße */
font-family: Arial;       /* Schriftart */
font-weight: bold;        /* Fettschrift */
text-align: center;       /* Ausrichtung */
text-decoration: underline; /* Unterstreichung */
```

**Hintergrund**:

```css
background-color: yellow; /* Hintergrundfarbe */
```

**Abstände**:

```css
margin: 10px;             /* Außenabstand */
padding: 10px;            /* Innenabstand */
```

**Größe**:

```css
width: 200px;             /* Breite */
height: 100px;            /* Höhe */
```

**Rahmen**:

```css
border: 1px solid black;  /* Rahmen: Dicke, Stil, Farbe */
```

### **Farbangaben in CSS**

**Farbnamen** (einfach):

```css
color: red;
color: blue;
color: lightgreen;
```

**Hexadezimal** (präzise):

```css
color: #FF0000;  /* Rot */
color: #00FF00;  /* Grün */
color: #0000FF;  /* Blau */
color: #f0f0f0;  /* Hellgrau */
```

**RGB** (Red, Green, Blue):

```css
color: rgb(255, 0, 0);     /* Rot */
color: rgb(0, 255, 0);     /* Grün */
color: rgba(0, 0, 255, 0.5); /* Blau, 50% transparent */
```

### **Warum Trennung von HTML und CSS?**

**Problem ohne Trennung**:

```html
<!-- Alles durcheinander -->
<p style="color: red; font-size: 16px; margin: 10px;">
  Text mit direktem Styling
</p>
<p style="color: red; font-size: 16px; margin: 10px;">
  Nochmal das gleiche Styling wiederholt
</p>
```

**Nachteile**:

- ❌ Code-Wiederholung
- ❌ Schwer wartbar (Änderung = jedes Element einzeln)
- ❌ Unübersichtlich
- ❌ Vermischt Struktur und Stil

**Lösung mit Trennung**:

**HTML** (nur Struktur):

```html
<p class="highlight">Text 1</p>
<p class="highlight">Text 2</p>
```

**CSS** (nur Stil):

```css
.highlight {
  color: red;
  font-size: 16px;
  margin: 10px;
}
```

**Vorteile**:

- ✅ Wiederverwendbar (eine Regel, viele Elemente)
- ✅ Zentrale Änderung (eine Stelle = überall geändert)
- ✅ Übersichtlich
- ✅ Klare Trennung

### **Kernbotschaft**

**Web-Entwicklung** beginnt mit zwei Grundpfeilern:

**HTML** = **Struktur** und **Bedeutung** (das "Was")

- Tags, Elemente, Attribute
- Grundgerüst jeder Webseite
- `<html>`, `<head>`, `<body>`

**CSS** = **Aussehen** und **Darstellung** (das "Wie")

- Selektoren, Eigenschaften, Werte
- Steuert Farben, Schriften, Layout
- Getrennt von HTML (External CSS)

**Zusammenspiel**:

```
HTML strukturiert → CSS stylt → Browser rendert
```

**Client-Server-Modell**:

- **Browser** (Client) fragt an
- **Server** antwortet mit HTML/CSS
- **Browser** zeigt Seite an

**Best Practice**: **Separation of Concerns**

- HTML für Struktur
- CSS für Stil
- Sauber getrennt = wartbar + flexibel

**Nächste Schritte**: JavaScript (für Interaktivität) kommt später!

**Analogie finale**: HTML ist wie das **Skelett und Organe** eines Hauses (Struktur, Räume, Türen), CSS ist die **Farbe, Tapete und Dekoration** (wie es aussieht). Zusammen ergeben sie eine vollständige, ansehnliche Webseite! 🏠🎨💻

---

## Übersichtstabelle

|**Kategorie**|**Details**|
|---|---|
|**Verwendete Tools**|• **VS Code** (Visual Studio Code): Code-Editor (Windows & macOS) - [code.visualstudio.com](https://code.visualstudio.com/)<br>• **Web-Browser**: Chrome, Firefox, Safari, Edge (zum Anzeigen von Webseiten)<br>• **Browser Developer Tools**: Rechtsklick → "Untersuchen" / "Element untersuchen" (macOS & Windows: F12)<br>• **Finder/Datei-Explorer**: Dateiverwaltung (macOS: Finder; Windows: Explorer)<br>• **Notepad++/Sublime Text**: Alternative Code-Editoren (Windows)<br>• **TextEdit**: Einfacher Text-Editor (macOS; Windows: Notepad)<br>• **Live Server Extension**: VS Code-Erweiterung für lokalen Webserver<br>• **Emmet**: HTML/CSS-Schnelleingabe in VS Code (vorinstalliert)<br>• **Git/GitHub**: Versionskontrolle (optional, für Projekte)<br>• **Browser-Extensions**: Web Developer, ColorZilla, WhatFont<br>• **Validator**: W3C HTML/CSS Validator (online-Tools)|
|**Technische Fachbegriffe**|• **Internet**: Globales Netzwerk von Computern (Infrastruktur)<br>• **World Wide Web (WWW)**: Dienst auf dem Internet (Hypertext-System)<br>• **Web Page**: Einzelne Webseite (ein HTML-Dokument)<br>• **Website**: Sammlung zusammenhängender Webseiten<br>• **Static Website**: Statische Webseite (fester Inhalt)<br>• **Dynamic Website**: Dynamische Webseite (generierter Inhalt)<br>• **Web Browser**: Programm zum Anzeigen von Webseiten (Client)<br>• **Web Server**: Computer, der Webseiten bereitstellt (Server)<br>• **Client-Server Model**: Client-Server-Modell<br>• **HTTP** (HyperText Transfer Protocol): Übertragungsprotokoll<br>• **URL** (Uniform Resource Locator): Webadresse<br>• **Rendering**: Darstellung/Zeichnung der Webseite<br>• **HTML** (HyperText Markup Language): Struktursprache für Webseiten<br>• **Markup Language**: Auszeichnungssprache<br>• **Tag**: HTML-Markierung (z.B. `<p>`)<br>• **Element**: HTML-Element (Tag + Inhalt + Schließ-Tag)<br>• **Opening Tag**: Öffnendes Tag (z.B. `<h1>`)<br>• **Closing Tag**: Schließendes Tag (z.B. `</h1>`)<br>• **Attribute**: HTML-Attribut (zusätzliche Information)<br>• **Value**: Attributwert<br>• **Void Element**: Leeres Element ohne Schließ-Tag (z.B. `<img>`)<br>• **DOCTYPE**: Dokumenttyp-Deklaration<br>• **Root Element**: Wurzelelement (`<html>`)<br>• **Meta-Information**: Meta-Daten (nicht sichtbar)<br>• **Character Encoding**: Zeichenkodierung (UTF-8)<br>• **Viewport**: Darstellungsbereich (für Responsive Design)<br>• **CSS** (Cascading Style Sheets): Stylesheet-Sprache<br>• **Selector**: CSS-Selektor (wählt Elemente aus)<br>• **Declaration Block**: Deklarationsblock (in `{}`)<br>• **Property**: CSS-Eigenschaft (z.B. `color`)<br>• **Value**: CSS-Wert (z.B. `blue`)<br>• **External CSS**: Externe CSS-Datei (`.css`)<br>• **Internal CSS**: Interne CSS (im `<head>`)<br>• **Inline CSS**: Inline-CSS (im `style`-Attribut)<br>• **Specificity**: CSS-Spezifität (Vorrangregeln)<br>• **Separation of Concerns**: Trennung von Zuständigkeiten<br>• **Responsive Design**: Anpassungsfähiges Design (verschiedene Bildschirmgrößen)|
|**Wichtige Vokabeln**|• **Infrastruktur**: Grundlegende Struktur/Basis<br>• **Verlinkt**: Miteinander verbunden<br>• **Hypertext**: Text mit Links zu anderen Dokumenten<br>• **Dokument**: Einzelne Datei/Seite<br>• **Sammlung**: Gruppe zusammengehöriger Elemente<br>• **Gehostet**: Auf Server gespeichert/bereitgestellt<br>• **Fester Inhalt**: Unveränderlicher Content<br>• **Dynamisch generiert**: On-the-fly erstellt<br>• **Interaktion**: Benutzer-Eingaben/Aktionen<br>• **Bausteine**: Grundlegende Komponenten<br>• **Abrufen**: Holen/Fetchen<br>• **Anzeigen**: Darstellen/Rendern<br>• **Anfrage**: Request<br>• **Antwort**: Response<br>• **Verarbeiten**: Prozessieren<br>• **Interpretieren**: Verstehen/Auswerten<br>• **Auszeichnen**: Markieren (Markup)<br>• **Struktur**: Aufbau/Organisation<br>• **Paar**: Zusammengehörige Tags (öffnend + schließend)<br>• **Spitzklammern**: Angle Brackets `< >`<br>• **Schrägstrich**: Forward Slash `/`<br>• **Leer**: Ohne Inhalt (Void)<br>• **Name-Wert-Paar**: Attribut = "Wert"<br>• **Anker**: Link/Hyperlink<br>• **Meta-Information**: Informationen über die Seite<br>• **Sichtbar**: Im Browser angezeigt<br>• **Überschrift**: Heading<br>• **Absatz**: Paragraph<br>• **Einbetten**: Einfügen (Embed)<br>• **Alternativer Text**: Beschreibung für Screenreader/wenn Bild fehlt<br>• **Container**: Umhüllendes Element<br>• **Gruppieren**: Zusammenfassen<br>• **Inline**: Innerhalb einer Zeile<br>• **Block**: Eigener Absatz<br>• **Quellcode**: Source Code<br>• **Entwickler-Tools**: Developer Tools<br>• **Hierarchisch**: Baumstruktur<br>• **Darstellung**: Appearance/Präsentation<br>• **Aussehen**: Look/Style<br>• **Farben**: Colors<br>• **Schriftarten**: Fonts<br>• **Abstand**: Spacing<br>• **Layout**: Anordnung<br>• **Animation**: Bewegte Effekte<br>• **Trennung**: Separation<br>• **Bedeutung**: Semantik<br>• **Präsentation**: Visuelle Darstellung<br>• **Wartbar**: Maintainable<br>• **Flexibel**: Anpassbar<br>• **Kaskadierend**: Cascading (Vererbung)<br>• **Regel**: CSS-Rule<br>• **Deklaration**: Declaration<br>• **Semikolon**: Trennzeichen `;`<br>• **Klasse**: Class (`.my-class`)<br>• **ID**: Eindeutige Kennung (`#my-id`)<br>• **Verknüpfen**: Linken<br>• **Einbetten**: Embed<br>• **Aktualisieren**: Refresh (Seite neu laden)<br>• **Fundament**: Foundation/Grundlage|