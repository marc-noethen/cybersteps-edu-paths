[🔍 Burp Suite Labor - Mein Arbeitsblatt](%F0%9F%94%8D%20Burp%20Suite%20Labor%20-%20Mein%20Arbeitsblatt%20272588ff46e6805ab88acaaf298d25fa.md)

*Wenn es beim ersten Mal nicht klappt, versuche es noch einmal...*

**Ziel**

Verwenden Sie Burp Repeater, um eine HTTP-Anfrage manuell zu manipulieren und Informationen zu entdecken, die über die normale Benutzeroberfläche nicht zugänglich sind.

**Anleitung**

1. Navigieren Sie zu dem folgenden PortSwigger Web Security Academy Labor. Dieses Labor demonstriert eine häufige Schwachstelle in der Zugangskontrolle.
    - **Labor-Link:** [https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter](https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter)
2. Melden Sie sich im Labor mit den angegebenen Anmeldeinformationen für `wiener` an.
3. Klicken Sie auf "Mein Konto". Beachten Sie die Anfrage im HTTP-Verlauf von Burp nach Ihren Benutzerdaten. Senden Sie diese Anfrage an Repeater.
4. Ihre Aufgabe ist es, die Kontoseite für den Benutzer `Carlos` zu sehen. Ändern Sie in Repeater die Anfrage so ab, dass Sie die Benutzerdaten von Carlos statt Ihrer eigenen abfragen.
5. Finden Sie Carlos' API-Schlüssel auf seiner Kontoseite.

**Übermittlung**

Übermitteln Sie den API-Schlüssel für den Benutzer "carlos".