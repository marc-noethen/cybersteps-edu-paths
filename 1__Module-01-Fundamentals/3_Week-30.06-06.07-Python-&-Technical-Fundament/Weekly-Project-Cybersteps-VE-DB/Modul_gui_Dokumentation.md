# 🐍 GUI-Modul (gui.py)

**Kurs:** Python & Datenbanken | **Datum:** [DD.MM.YYYY]

---

## Aufgabe

**Ziel:** Grafische Benutzeroberfläche für die CVE-Datenbank mit tkinter erstellen

**Anforderungen:**
- Funktion: `run_gui()` - Startet die Anwendung
- Features: Suche, Tabellenansicht, API-Import, Statistiken
- Bibliothek: tkinter (Standard-Python-GUI)

---

## Lösung

```python
import tkinter as tk
from tkinter import messagebox, ttk
from db import search_cves, update_cve_status, get_statistics
from api_import import import_cves_from_nvd

def run_gui():
    """Startet die grafische Benutzeroberfläche."""
    root = tk.Tk()
    root.title("🛡️ CVE-Datenbank")
    root.geometry("900x600")

    # === SUCHBEREICH ===
    frame_search = tk.Frame(root)
    frame_search.pack(pady=10)

    tk.Label(frame_search, text="🔍 Stichwort:").grid(row=0, column=0)
    keyword_entry = tk.Entry(frame_search)
    keyword_entry.grid(row=0, column=1)

    tk.Label(frame_search, text="🔑 Schweregrad:").grid(row=0, column=2)
    severity_entry = tk.Entry(frame_search)
    severity_entry.grid(row=0, column=3)

    def suche():
        """Führt die Suche aus und aktualisiert die Tabelle."""
        keyword = keyword_entry.get()
        severity = severity_entry.get()
        results = search_cves(keyword, severity, None)
        update_tree(results)

    tk.Button(frame_search, text="Suchen", command=suche).grid(row=0, column=4, padx=10)

    # === TABELLE (Treeview) ===
    tree = ttk.Treeview(
        root, 
        columns=("ID", "Beschreibung", "Datum", "Schwere", "Status"), 
        show="headings"
    )
    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, width=150)
    tree.pack(fill="both", expand=True)

    def update_tree(data):
        """Aktualisiert die Tabellenansicht mit neuen Daten."""
        tree.delete(*tree.get_children())
        for row in data:
            tree.insert("", "end", values=row)

    # === AKTIONS-BUTTONS ===
    frame_actions = tk.Frame(root)
    frame_actions.pack(pady=10)

    def importiere():
        """Öffnet Popup für API-Import."""
        def do_import():
            keyword = entry_keyword.get()
            try:
                count = int(entry_count.get())
                import_cves_from_nvd(keyword, count)
                messagebox.showinfo("Import", "Import abgeschlossen.")
            except Exception as e:
                messagebox.showerror("Fehler", str(e))

        popup = tk.Toplevel()
        popup.title("CVE Importieren")
        tk.Label(popup, text="Suchbegriff:").pack()
        entry_keyword = tk.Entry(popup)
        entry_keyword.pack()
        tk.Label(popup, text="Anzahl:").pack()
        entry_count = tk.Entry(popup)
        entry_count.pack()
        tk.Button(popup, text="Start", command=do_import).pack(pady=5)

    def statistik():
        """Zeigt Statistik-Dialog."""
        s = get_statistics()
        message = (
            f"Gesamt: {s['total']}\n"
            f"Kritisch: {s['critical']}\n"
            f"Hoch: {s['high']}\n"
            f"Mittel: {s['medium']}\n"
            f"Niedrig: {s['low']}"
        )
        messagebox.showinfo("Statistik", message)

    tk.Button(frame_actions, text="📥 API-Import", command=importiere).pack(side="left", padx=10)
    tk.Button(frame_actions, text="📊 Statistik", command=statistik).pack(side="left", padx=10)

    root.mainloop()
```

---

## GUI-Aufbau

```
┌─────────────────────────────────────────────────────────┐
│  🛡️ CVE-Datenbank                               [_][□][X] │
├─────────────────────────────────────────────────────────┤
│  🔍 Stichwort: [________]  🔑 Schweregrad: [____] [Suchen] │
├─────────────────────────────────────────────────────────┤
│  ID          │ Beschreibung │ Datum      │ Schwere │Status│
│──────────────│──────────────│────────────│─────────│──────│
│  CVE-2024-...│ A buffer...  │ 2024-01-15 │ HIGH    │ New  │
│  CVE-2024-...│ Remote code..│ 2024-01-10 │ CRITICAL│ New  │
│  ...         │ ...          │ ...        │ ...     │ ...  │
├─────────────────────────────────────────────────────────┤
│           [📥 API-Import]    [📊 Statistik]              │
└─────────────────────────────────────────────────────────┘
```

---

## Komponenten

| Komponente | Widget | Funktion |
|------------|--------|----------|
| Suchfeld Stichwort | `tk.Entry` | Keyword-Filter |
| Suchfeld Schweregrad | `tk.Entry` | Severity-Filter |
| Suchen-Button | `tk.Button` | Führt Suche aus |
| Ergebnis-Tabelle | `ttk.Treeview` | Zeigt CVEs an |
| API-Import | `tk.Button` | Öffnet Import-Dialog |
| Statistik | `tk.Button` | Zeigt Statistik-Popup |

---

## Tests

| Aktion | Erwartet | Ergebnis | ✓ |
|--------|----------|----------|---|
| Programm starten | Fenster öffnet sich | 900x600 Fenster | ✅ |
| Suche ohne Filter | Alle CVEs angezeigt | Tabelle gefüllt | ✅ |
| Suche mit Keyword | Gefilterte Ergebnisse | Passende CVEs | ✅ |
| API-Import klicken | Popup erscheint | Dialog öffnet | ✅ |
| Statistik klicken | Statistik-Popup | Zahlen angezeigt | ✅ |

---

## Notizen

- **Konzept:** Event-driven GUI mit Callbacks (`command=`)
- **Tipp:** `ttk.Treeview` für tabellarische Daten
- **Layout:** `pack()` für einfaches Layout, `grid()` für Formulare
- **Alternative:** PyQt5 oder PySide6 für modernere UIs
- **Verbesserung:** Scrollbar für lange Listen hinzufügen
