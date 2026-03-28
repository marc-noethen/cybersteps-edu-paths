_X-Ray vision: ON_

**Ziel**

Entwickeln Sie Fähigkeiten im Umgang mit Standard-Browser-Tools, um `uber.com` auf technische Hinweise, strukturelle Informationen und versehentlich offengelegte Daten zu untersuchen.

**Anweisungen**

**HINWEIS:** Interagieren Sie mit `https://www.uber.com` nur als normaler Benutzer. Sie können das Chrome-Add-on verwenden: [https://www.wappalyzer.com/](https://www.wappalyzer.com/) Beobachten Sie die Daten, die Ihr Browser empfängt.

1. **`robots.txt` Hinweise:** Untersuchen Sie die `robots.txt` von `uber.com`. Welche zwei Arten von Pfaden fordert Uber von den Crawlern zu vermeiden? Was könnte dies über diese Bereiche aussagen?
    
    `Disallow: /app/ = Code Secrets Disallow: /api/ = User, Company informations`
    
2. **Code & Network Traces:** Untersuchen Sie den Quellcode der Homepage von "[Uber.com](http://uber.com/)" und die Netzwerkanfragen (Browser Developer Tools oder Wappalyzer):
    
    - Identifizieren Sie die wichtigsten JavaScript-Bibliotheken/Frameworks für das Frontend. Wie?
        
        JavaScript Bibliotheken `Hammer.js2.0.7, web-vitals, core-js`
        
    - Identifizieren Sie integrierte Dienste von Drittanbietern. Was waren die Anhaltspunkte?
        
        - Cloudfare, Google
        - **Externe Domains im Network-Tab**
        - **Script-Tags von Drittanbietern im Quellcode**
        - **Cookies/LocalStorage von fremden Domains**
        - **Eingebettete Widgets / iFrames / APIs**
3. Benutzen Sie ein passives Tool, um herauszufinden, welche Servertechnologien für `uber.com` vorgeschlagen werden? Sie können verwenden: [https://builtwith.com/](https://builtwith.com/)
    
    1. `nginx`
    2. `google cloud`
    3. `Cloudflare`
    4. `UltraDnS`
    5. `NSone`

**Einreichung**

Reichen Sie ein Dokument ein, das Folgendes enthält:

- Ihre Analyse von `uber.com/robots.txt`.
- Ihre Ergebnisse zu Frontend-Bibliotheken/Frameworks und Diensten von Drittanbietern, mit Methoden zur Identifizierung.
- Servertechnologien, die durch ein Tool und seine passive Methodik identifiziert wurden.