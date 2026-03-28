import tkinter as tk
from tkinter import messagebox, ttk
from db import search_cves, update_cve_status, get_statistics
from api_import import import_cves_from_nvd

def run_gui():
    root = tk.Tk()
    root.title("🛡️ CVE-Datenbank")
    root.geometry("900x600")

    # --- Suchbereich ---
    frame_search = tk.Frame(root)
    frame_search.pack(pady=10)

    tk.Label(frame_search, text="🔍 Stichwort:").grid(row=0, column=0)
    keyword_entry = tk.Entry(frame_search)
    keyword_entry.grid(row=0, column=1)

    tk.Label(frame_search, text="🔒 Schweregrad:").grid(row=0, column=2)
    severity_entry = tk.Entry(frame_search)
    severity_entry.grid(row=0, column=3)

    def suche():
        keyword = keyword_entry.get()
        severity = severity_entry.get()
        results = search_cves(keyword, severity, None)
        update_tree(results)

    tk.Button(frame_search, text="Suchen", command=suche).grid(row=0, column=4, padx=10)

    # --- Tabelle ---
    tree = ttk.Treeview(root, columns=("ID", "Beschreibung", "Datum", "Schwere", "Status"), show="headings")
    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, width=150)
    tree.pack(fill="both", expand=True)

    def update_tree(data):
        tree.delete(*tree.get_children())
        for row in data:
            tree.insert("", "end", values=row)

    # --- Buttons ---
    frame_actions = tk.Frame(root)
    frame_actions.pack(pady=10)

    def importiere():
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
