# Password Puzzler

_A hashed hint to a hidden word._

**Goal**

Understand how easily very short passwords can be "cracked" if their hash is known, by writing a Python script to brute-force the password space.

**Instructions**

You are given the following SHA-256 hash:`d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1`

This is the SHA-256 hash of a very short password consisting _only of lowercase English letters_. Your mission is to find this password.

You will need to write a Python script to do this, using the hashlib module. Consider trying lengths from 1 up to a small maximum (e.g., 3, 4, or 5 letters).

After you succeed, lookup online a “sha256 decrypter tool” and verify your answer.

**Question:** Why is the term “sha256 decrypt” not accurate?

**Submission**

Submit:

1. Your complete Python script (`.py` file).
2. The password that matches the given SHA-256 hash.
3. Your answer to the question


---
---

# Passwort-Rätsel

_Ein Hash-Hinweis auf ein verstecktes Wort._

**Ziel**

Verstehen Sie, wie leicht sehr kurze Passwörter „geknackt” werden können, wenn ihr Hash bekannt ist, indem Sie ein Python-Skript schreiben, das den Passwortraum mit Brute-Force-Methoden durchsucht.

**Anleitung**

Sie erhalten den folgenden SHA-256-Hash: `d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1`.

Dies ist der SHA-256-Hash eines sehr kurzen Passworts, das _nur aus englischen Kleinbuchstaben_ besteht. Ihre Aufgabe ist es, dieses Passwort zu finden.

Dazu müssen Sie ein Python-Skript schreiben, das das Modul „hashlib“ verwendet. Probieren Sie Längen von 1 bis zu einer kleinen maximalen Länge aus (z. B. 3, 4 oder 5 Buchstaben).

Wenn Sie erfolgreich waren, suchen Sie online nach einem „sha256-Entschlüsselungstool“ und überprüfen Sie Ihre Antwort.

**Frage:** Warum ist der Begriff „sha256 decrypt” nicht korrekt?

**Einreichung**

Reichen Sie Folgendes ein:

1. Ihr vollständiges Python-Skript (`.py`-Datei).
2. Das Passwort, das mit dem angegebenen SHA-256-Hash übereinstimmt.
3. Ihre Antwort auf die Frage.


---

Answer: 
****Warum ist „SHA256 decrypt" nicht korrekt?**

SHA-256 ist eine **Hash-Funktion**, keine Verschlüsselung.

- **Verschlüsselung** ist umkehrbar — mit dem richtigen Schlüssel kann man die Originaldaten wiederherstellen.
- **Hashing** ist eine **Einwegfunktion** — es gibt keinen Schlüssel und keine mathematische Möglichkeit, vom Hash zurück zum Original zu rechnen.

Was Online-Tools tun, ist kein "Entschlüsseln", sondern ein **Nachschlagen in vorberechneten Datenbanken** (Rainbow Tables). Sie haben Millionen von Wörtern vorher gehasht und suchen nur nach Übereinstimmungen.

**Korrekte Begriffe:** "Hash lookup", "Hash cracking", "Reverse lookup"