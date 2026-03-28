# 🖥️ The Giving Tree - XML zu Python Dictionary

**Kurs:** Cyber Security Analyst - Technical Foundation Basics | **Datum:** 02.07.2025

---

## Aufgabe

**Ziel:** Parse XML mit `xml.etree.ElementTree` und konvertiere es in ein verschachteltes Python Dictionary.

---

## Lösung

### Python Script

```python
import xml.etree.ElementTree as ET

xml_data = """
<album title="Abbey Road" artist="The Beatles">
  <track number="1" duration="4:20">
    <title>Come Together</title>
    <genre>Rock</genre>
  </track>
  <track number="2" duration="3:29">
    <title>Something</title>
    <genre>Rock</genre>
  </track>
  <track number="7" duration="3:05" rating="5_stars">
    <title>Here Comes the Sun</title>
    <genre>Folk Rock</genre>
  </track>
</album>
"""

# XML parsen
root = ET.fromstring(xml_data)

# Dictionary aufbauen
album_dict = {
    "title": root.attrib["title"],
    "artist": root.attrib["artist"],
    "tracks": []
}

# Tracks durchlaufen
for track in root.findall("track"):
    track_dict = {
        "number": track.attrib["number"],
        "duration": track.attrib["duration"],
        "title": track.find("title").text,
        "genre": track.find("genre").text
    }
    # Optionales rating hinzufügen
    if "rating" in track.attrib:
        track_dict["rating"] = track.attrib["rating"]
    
    album_dict["tracks"].append(track_dict)

print(album_dict)
```

### Ausgabe

```python
{
    'title': 'Abbey Road',
    'artist': 'The Beatles',
    'tracks': [
        {'number': '1', 'duration': '4:20', 'title': 'Come Together', 'genre': 'Rock'},
        {'number': '2', 'duration': '3:29', 'title': 'Something', 'genre': 'Rock'},
        {'number': '7', 'duration': '3:05', 'title': 'Here Comes the Sun', 'genre': 'Folk Rock', 'rating': '5_stars'}
    ]
}
```

---

## Notizen

- **`ET.fromstring()`:** Parst XML-String direkt
- **`.attrib`:** Dictionary aller Attribute eines Elements
- **`.find("tag")`:** Findet erstes Kind-Element mit diesem Tag
- **`.findall("tag")`:** Findet alle Kind-Elemente mit diesem Tag
- **`.text`:** Text-Inhalt des Elements
