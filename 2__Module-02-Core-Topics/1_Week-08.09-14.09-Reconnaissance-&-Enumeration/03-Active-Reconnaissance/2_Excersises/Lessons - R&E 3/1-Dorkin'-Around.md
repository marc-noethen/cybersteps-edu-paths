_Just a couple of dorks away from gold_

## **Ziel**

Verfeinern Sie Ihre Google-Dorking-Fähigkeiten, um spezifische öffentliche Informationen über ein großes Unternehmen zu finden und den strategischen Wert verschiedener Dork-Konstruktionen zu verstehen.

## **Anweisungen**

**Wichtiger ethischer Auftrag:** Diese Übungen führen Sie durch die passive Erkundung des realen Unternehmens Uber, wobei Sie NUR öffentlich zugängliche Informationen und rein passive Techniken verwenden. Sie **dürfen** KEINE Tools oder Techniken verwenden, die aktiv die Systeme, Netzwerke oder Anwendungen von Uber scannen, untersuchen, testen oder mit ihnen interagieren, es sei denn, Sie surfen im Internet oder nutzen öffentliche Suchdienste von Drittanbietern, die bestehende öffentliche Datenbanken abfragen. Halten Sie sich an öffentlich zugängliche Informationen und respektieren Sie alle Nutzungsbedingungen. Ihre Recherche dient dem Verständnis öffentlicher Daten, nicht dem Auffinden von Schwachstellen oder nicht öffentlichen Informationen.

Sie recherchieren mit Google über Uber. Konstruieren Sie Google Dorks und führen Sie sie für Folgendes aus:

1. **Offizielle Dokumente:** Finden Sie PDF-Dokumente, die auf `uber.com` gehostet werden. Notiere ein öffentliches Dokument deiner Wahl. Auf welche Art von Informationen zielt dieser Dork ab?
    
    1. [https://s23.q4cdn.com/407969754/files/doc_events/2024/Feb/14/uber-investor-update.pdf](https://s23.q4cdn.com/407969754/files/doc_events/2024/Feb/14/uber-investor-update.pdf)
    2. `enthält wertvolle Informationen über die finanzielle und operative Entwicklung von Uber`
    3. `site:uber.com filetype:pdf`
2. **Engineering Insights:** Finde Artikel auf `uber.com`, die "Sicherheit" in ihrem "Engineering"-Kontext diskutieren. Nennen Sie einen Titel. Welche Einblicke kann dies bieten?
    
    1. `Building Uber’s Multi-Cloud Secrets Management Platform to Enhance Security`
    2. `site:uber.com engineering sicherheit`
    3. `Der Artikel bietet wertvolle Einblicke in die Sicherheitspraktiken von Uber, insbesondere im Bereich der Geheimnisverwaltung über mehrere Cloud-Umgebungen hinweg. Die beschriebenen Strategien und Technologien können als Best Practices für Unternehmen dienen, die ihre Sicherheitsarchitektur verbessern möchten.`
        - `Ein CLI-Tool als Pre-Commit-Hook in Git blockiert Commits, die Geheimnisse enthalten.`
        - `Echtzeit-Scanning von Codeänderungen, Pull Requests, Slack-Nachrichten und Build-Logs.`
        - `Geplante Scans von Repositories, Dateisystemen und Container-Images.`
        - `Automatisierte Erstellung von Tickets bei Entdeckung eines Geheimnisses, um eine schnelle Behebung zu gewährleisten`
3. **Öffentliche Tech Talks:** Finden Sie Präsentationen (z. B. PPT, PDF auf Websites wie SlideShare) über die Technologie oder Projekte von Uber. Nennen Sie eine. Warum sind solche Präsentationen nützlich?
    
    1. `uber SlideShare presentation`
    2. [https://www.slideshare.net/slideshow/uber-presentation-138879481/138879481](https://www.slideshare.net/slideshow/uber-presentation-138879481/138879481)
    
    - **`Strategische Einblicke:** Sie bieten einen klaren Überblick über die Marktposition und die strategischen Ziele von Uber.`
    - **`SWOT-Analyse:** Hilft dabei, die internen Stärken und Schwächen sowie externe Chancen und Bedrohungen zu verstehen.`
    - **`Zukunftsperspektiven:** Gibt Empfehlungen für zukünftige Entwicklungen und Anpassungen in der Unternehmensstrategie.`
    - **`Wettbewerbsanalyse:** Vergleicht Uber mit anderen Marktteilnehmern und identifiziert potenzielle Bedrohungen und Chancen.`
4. **API Chatter:** Entdecken Sie Diskussionen über die API von Uber in Entwickler-Communities (z. B. Stack Overflow, GitHub). Welche technischen Details könnten sich daraus ergeben?
    
    1. [https://stackoverflow.com/questions/49857101/uber-api-for-real-time-tracking?utm_source=chatgpt.com](https://stackoverflow.com/questions/49857101/uber-api-for-real-time-tracking?utm_source=chatgpt.com)
    
    - **`Ride Request - Map API**: Ermöglicht das Abrufen des aktuellen Standorts eines Fahrzeugs während einer Fahrt.`
    - **`Ride Request - Current API**: Bietet Informationen über die aktuelle Fahrt des Nutzers.`
    - **`Ride Request - Details API**: Gibt detaillierte Informationen zu einer bestimmten Fahrt, einschließlich Wegpunkten und Zeitstempeln.`
5. **Hypothetisches Leck:** Wenn ein Trottel ein `uber.com`Dokument mit dem Titel `internal_strategy_notes_DO_NOT_DISTRIBUTE.docx` enthüllen würde, warum wäre dies von Bedeutung?
    
    1. `Damit würde das unternehmen, unternehmens geheimnisse weitergeben die das geschäft massiv schaden könnten da nun konkurrenz unternehmen die möglichkeit haben diese Dokumente für sich zu nutzen`

## **Einreichung**

Reichen Sie ein Dokument ein, das Folgendes enthält:

- Ihre Antwort für jede der 5 Anweisungen, einschließlich der verwendeten Google Dorks und Ihrer Analyse/Erläuterungen.