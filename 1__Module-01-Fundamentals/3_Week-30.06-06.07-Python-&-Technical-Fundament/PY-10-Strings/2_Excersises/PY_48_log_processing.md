# 🐍 Log Processing - Log-Einträge auswerten

**Kurs:** Cyber Security Analyst - Python Basics | **Datum:** 01.07.2025

---

## Aufgabe

**Ziel:** Zähle Aktionen eines bestimmten Users aus Log-Einträgen.

**Anforderungen:**
- Input: Username, Anzahl Zeilen, Log-Zeilen (`timestamp,username,action`)
- Verarbeitung: Filtere nach User, zähle Aktionen
- Output: Aktionen alphabetisch sortiert mit Anzahl

---

## Lösung

```python
# Eingaben
target_user = input("Enter target username: ")
n = int(input("Enter number of log lines: "))

# Aktionen zählen
action_counts = {}

for _ in range(n):
    line = input()
    timestamp, username, action = line.split(",")
    
    # Nur Ziel-User verarbeiten
    if username == target_user:
        if action in action_counts:
            action_counts[action] += 1
        else:
            action_counts[action] = 1

# Sortiert ausgeben
for action in sorted(action_counts.keys()):
    print(f"{action}: {action_counts[action]}")
```

**Alternative mit .get():**
```python
target_user = input("Enter target username: ")
n = int(input("Enter number of log lines: "))

action_counts = {}
for _ in range(n):
    parts = input().split(",")
    if parts[1] == target_user:
        action_counts[parts[2]] = action_counts.get(parts[2], 0) + 1

for action in sorted(action_counts):
    print(f"{action}: {action_counts[action]}")
```

---

## Tests

| Input | Output | ✓ |
|-------|--------|---|
| User: `bob`, 5 Zeilen mit bob: upload(2), logout(1) | `logout: 1` `upload: 2` | ✅ |
| User: `alice`, 6 Zeilen mit alice: read(2), write(1), delete(1) | `delete: 1` `read: 2` `write: 1` | ✅ |

---

## Notizen

- **`.split(",")`:** Trennt Log-Zeile an Kommas
- **`for _ in range(n)`:** `_` wenn Variable nicht gebraucht wird
- **`sorted(dict.keys())`:** Keys alphabetisch sortieren
- **Case-sensitive:** `"bob"` ≠ `"Bob"` (Groß-/Kleinschreibung beachten)
