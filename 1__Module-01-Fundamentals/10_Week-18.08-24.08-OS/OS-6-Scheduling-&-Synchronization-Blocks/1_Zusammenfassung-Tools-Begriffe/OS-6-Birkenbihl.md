Welcome to your preparation for our session on Scheduling and Synchronization in Operating Systems. Willkommen zu deiner Vorbereitung auf unsere Sitzung über Scheduling und Synchronisation in Betriebssystemen.

In our last lesson, we explored processes and threads, the fundamental units of execution. In unserer letzten Lektion haben wir Prozesse und Threads untersucht, die grundlegenden Ausführungseinheiten.

Now, we'll delve into how an operating system juggles these tasks, deciding which process or thread gets to use the CPU and when, and how it ensures they can work together harmoniously without tripping over each other. Jetzt werden wir uns damit befassen, wie ein Betriebssystem diese Aufgaben jongliert, entscheidet, welcher Prozess oder Thread die CPU nutzen darf und wann, und wie es sicherstellt, dass sie harmonisch zusammenarbeiten können, ohne sich gegenseitig zu behindern.

These are crucial concepts for understanding how operating systems efficiently manage resources and prevent chaos in our digital world. Dies sind entscheidende Konzepte, um zu verstehen, wie Betriebssysteme Ressourcen effizient verwalten und Chaos in unserer digitalen Welt verhindern.

CPU Scheduling: Who Gets the CPU Next? CPU-Scheduling: Wer bekommt als Nächstes die CPU?

Imagine a very popular food truck, your computer, with only one chef, the CPU, and many hungry customers, processes and threads, all wanting their orders, tasks, processed. Stell dir einen sehr beliebten Food Truck vor, deinen Computer, mit nur einem Koch, der CPU, und vielen hungrigen Kunden, Prozessen und Threads, die alle ihre Bestellungen, Aufgaben, verarbeitet haben möchten.

The chef can only work on one order at a time. Der Koch kann nur an einer Bestellung gleichzeitig arbeiten.

Someone needs to decide which customer gets served next, and for how long the chef works on their order before possibly switching to another. Jemand muss entscheiden, welcher Kunde als Nächstes bedient wird und wie lange der Koch an dessen Bestellung arbeitet, bevor er möglicherweise zu einer anderen wechselt.

This is essentially what CPU scheduling is all about. Darum geht es im Wesentlichen beim CPU-Scheduling.

The operating system, OS, acts as the manager of this food truck, deciding which process or thread gets the CPU's attention. Das Betriebssystem, OS, fungiert als Manager dieses Food Trucks und entscheidet, welcher Prozess oder Thread die Aufmerksamkeit der CPU erhält.

This is vital because, on a modern computer, there are often dozens, if not hundreds, of active processes and threads, all vying for CPU time, from your web browser and music player to background system tasks. Dies ist von entscheidender Bedeutung, denn auf einem modernen Computer gibt es oft Dutzende, wenn nicht Hunderte von aktiven Prozessen und Threads, die alle um CPU-Zeit konkurrieren, von deinem Webbrowser und Musikplayer bis hin zu Systemhintergrundaufgaben.

Without scheduling, some tasks might never get to run, or your system could become sluggish and unresponsive. Ohne Scheduling könnten einige Aufgaben möglicherweise nie ausgeführt werden, oder dein System könnte träge und nicht reagierend werden.

Why Does the OS Bother Scheduling? Warum macht sich das OS die Mühe mit dem Scheduling?

Operating systems schedule tasks to achieve several important goals. Betriebssysteme planen Aufgaben, um mehrere wichtige Ziele zu erreichen.

Keeping the CPU Busy: An idle CPU is a wasted resource. Die CPU beschäftigt halten: Eine untätige CPU ist eine verschwendete Ressource.

The OS tries to ensure the CPU is always doing useful work. Das OS versucht sicherzustellen, dass die CPU immer nützliche Arbeit verrichtet.

Responsiveness: When you click a button or type something, you want a quick reaction. Reaktionsfähigkeit: Wenn du auf einen Button klickst oder etwas tippst, möchtest du eine schnelle Reaktion.

The OS tries to make interactive programs feel responsive. Das OS versucht, interaktive Programme reaktionsfähig wirken zu lassen.

Fairness: The OS attempts to give each process a fair chance to run, preventing any single power-hungry application from hogging all the CPU time. Fairness: Das OS versucht, jedem Prozess eine faire Chance zu geben, zu laufen, und verhindert, dass eine einzelne ressourcenhungrige Anwendung die gesamte CPU-Zeit blockiert.

Efficiency: Completing as many tasks as possible in a given amount of time. Effizienz: So viele Aufgaben wie möglich in einer bestimmten Zeitspanne erledigen.

Achieving all these goals perfectly at the same time can be tricky, so operating systems use smart strategies to find a good balance. Alle diese Ziele gleichzeitig perfekt zu erreichen, kann schwierig sein, daher nutzen Betriebssysteme intelligente Strategien, um ein gutes Gleichgewicht zu finden.

How Does the OS Manage Running Tasks? Wie verwaltet das OS laufende Aufgaben?

Taking Turns, Preemption: Most modern operating systems use preemptive scheduling. Abwechseln, Präemption: Die meisten modernen Betriebssysteme verwenden präemptives Scheduling.

This means the OS can interrupt a running task after a short period, a time slice, to give another task a turn on the CPU. Das bedeutet, dass das OS eine laufende Aufgabe nach einer kurzen Zeitspanne, einer Zeitscheibe, unterbrechen kann, um einer anderen Aufgabe einen Durchgang auf der CPU zu geben.

This is like the food truck manager telling the chef to pause one order to quickly handle a small, urgent one, ensuring everyone gets served eventually and the system feels responsive. Das ist wie wenn der Food-Truck-Manager dem Koch sagt, er solle eine Bestellung pausieren, um schnell eine kleine, dringende zu bearbeiten, damit am Ende jeder bedient wird und das System reaktionsfähig wirkt.

Older or simpler systems might use non-preemptive scheduling, where a task runs until it's completely finished or voluntarily gives up the CPU, which can sometimes lead to one task making everyone else wait too long. Ältere oder einfachere Systeme könnten nicht-präemptives Scheduling verwenden, bei dem eine Aufgabe läuft, bis sie vollständig beendet ist oder freiwillig die CPU abgibt, was manchmal dazu führen kann, dass eine Aufgabe alle anderen zu lange warten lässt.

Keeping Track, Context Switching: When the OS switches from one task to another, it needs to save the current progress of the outgoing task, its context, like all the ingredients and steps for an order, and then load the saved progress of the incoming task. Den Überblick behalten, Kontextwechsel: Wenn das OS von einer Aufgabe zur anderen wechselt, muss es den aktuellen Fortschritt der ausgehenden Aufgabe speichern, ihren Kontext, wie alle Zutaten und Schritte für eine Bestellung, und dann den gespeicherten Fortschritt der eingehenden Aufgabe laden.

This process is called a context switch. Dieser Prozess wird Kontextwechsel genannt.

It happens very fast, but it's a bit of overhead for the OS. Es geschieht sehr schnell, aber es bedeutet etwas Mehraufwand für das OS.

Think about it. Denk darüber nach.

Imagine you're juggling multiple homework assignments: math, history, and programming. Stell dir vor, du jonglierst mit mehreren Hausaufgaben: Mathematik, Geschichte und Programmierung.

How do you decide which one to work on, and for how long, before switching? Wie entscheidest du, an welcher du arbeiten sollst und wie lange, bevor du wechselst?

What factors influence your scheduling decisions to try and get everything done effectively? Welche Faktoren beeinflussen deine Scheduling-Entscheidungen, um zu versuchen, alles effektiv zu erledigen?

Process and Thread Synchronization: Working Together Without Chaos. Prozess- und Thread-Synchronisation: Zusammenarbeiten ohne Chaos.

Often, different processes or threads need to work together or share information. Oft müssen verschiedene Prozesse oder Threads zusammenarbeiten oder Informationen teilen.

For example, one part of a program might be downloading a file, Thread A, while another part updates a progress bar on your screen, Thread B, based on how much of the file is downloaded. Zum Beispiel könnte ein Teil eines Programms eine Datei herunterladen, Thread A, während ein anderer Teil eine Fortschrittsanzeige auf deinem Bildschirm aktualisiert, Thread B, basierend darauf, wie viel von der Datei heruntergeladen wurde.

Multiple users in a collaborative document editor might be trying to make changes to the same paragraph simultaneously. Mehrere Benutzer in einem kollaborativen Dokumenteneditor könnten versuchen, gleichzeitig Änderungen am selben Absatz vorzunehmen.

When multiple threads or processes access and try to modify the same piece of data or resource, like a file, a variable in memory, or a shared document, at the exact same time, things can go very wrong if their actions aren't carefully coordinated. Wenn mehrere Threads oder Prozesse genau zur selben Zeit auf dasselbe Datenstück oder dieselbe Ressource zugreifen und es zu ändern versuchen, wie eine Datei, eine Variable im Speicher oder ein gemeinsames Dokument, können die Dinge sehr schiefgehen, wenn ihre Aktionen nicht sorgfältig koordiniert werden.

This coordination is called synchronization. Diese Koordination wird Synchronisation genannt.

Synchronization mechanisms are rules and tools that ensure processes and threads play nicely together, accessing shared resources in an orderly way to prevent errors and maintain data consistency. Synchronisationsmechanismen sind Regeln und Werkzeuge, die sicherstellen, dass Prozesse und Threads gut zusammenspielen und auf gemeinsame Ressourcen in geordneter Weise zugreifen, um Fehler zu verhindern und die Datenkonsistenz zu wahren.

The Problem: Race Conditions. Das Problem: Race Conditions.

A race condition occurs when the outcome of a computation depends on the unpredictable order in which multiple processes or threads access and modify shared data. Eine Race Condition tritt auf, wenn das Ergebnis einer Berechnung von der unvorhersehbaren Reihenfolge abhängt, in der mehrere Prozesse oder Threads auf gemeinsame Daten zugreifen und diese ändern.

It's like two people trying to update the same cell in a spreadsheet simultaneously, the final value might be the one from the person who saved last, or worse, a garbled mix. Es ist wie wenn zwei Personen gleichzeitig versuchen, dieselbe Zelle in einer Tabelle zu aktualisieren, der endgültige Wert könnte der von der Person sein, die zuletzt gespeichert hat, oder schlimmer noch, eine verzerrte Mischung.

A Simple Race Condition Example. Ein einfaches Race-Condition-Beispiel.

Let's say we have a shared counter, BankAccountBalance, which is initially one hundred dollars. Nehmen wir an, wir haben einen gemeinsamen Zähler, BankAccountBalance, der anfänglich einhundert Dollar beträgt.

Thread 1, Deposit, wants to add fifty dollars. Thread 1, Einzahlung, möchte fünfzig Dollar hinzufügen.

It reads BankAccountBalance, gets one hundred dollars. Er liest BankAccountBalance, erhält einhundert Dollar.

Calculates one hundred plus fifty equals one hundred fifty. Berechnet einhundert plus fünfzig gleich einhundertfünfzig.

Oops, before Thread 1 can save the new balance, the OS switches to Thread 2. Hoppla, bevor Thread 1 den neuen Saldo speichern kann, wechselt das OS zu Thread 2.

Thread 2, Withdraw, wants to withdraw thirty dollars. Thread 2, Abhebung, möchte dreißig Dollar abheben.

Reads BankAccountBalance, still one hundred dollars, because Thread 1 hasn't saved its update. Liest BankAccountBalance, immer noch einhundert Dollar, weil Thread 1 sein Update nicht gespeichert hat.

Calculates one hundred minus thirty equals seventy. Berechnet einhundert minus dreißig gleich siebzig.

Writes seventy to BankAccountBalance, so BankAccountBalance is now seventy. Schreibt siebzig in BankAccountBalance, also ist BankAccountBalance jetzt siebzig.

Now the OS switches back to Thread 1. Jetzt wechselt das OS zurück zu Thread 1.

Thread 1, remember it calculated one hundred fifty way back, writes one hundred fifty to BankAccountBalance, so BankAccountBalance is now one hundred fifty. Thread 1, erinnere dich, er hatte einhundertfünfzig berechnet, schreibt einhundertfünfzig in BankAccountBalance, also ist BankAccountBalance jetzt einhundertfünfzig.

The final balance is one hundred fifty. Der Endsaldo beträgt einhundertfünfzig.

But it should be one hundred plus fifty minus thirty equals one hundred twenty. Aber er sollte einhundert plus fünfzig minus dreißig gleich einhundertzwanzig sein.

The thirty dollar withdrawal was effectively lost because of the unlucky timing of the context switch. Die dreißig-Dollar-Abhebung ging effektiv verloren wegen des unglücklichen Timings des Kontextwechsels.

This is a race condition. Das ist eine Race Condition.

These bugs can be incredibly tricky to find because they might only happen occasionally, depending on the exact timing of operations. Diese Fehler können unglaublich schwierig zu finden sein, weil sie möglicherweise nur gelegentlich auftreten, abhängig vom genauen Timing der Operationen.

The image humorously illustrates a CPU race condition by showing actions happening out of order, like a response arriving before the prompt, just as unsynchronized threads can produce unpredictable results. Das Bild veranschaulicht humorvoll eine CPU-Race-Condition, indem es zeigt, wie Aktionen in falscher Reihenfolge ablaufen, wie eine Antwort, die vor der Aufforderung ankommt, genau wie nicht synchronisierte Threads unvorhersehbare Ergebnisse erzeugen können.

Critical Sections: The Danger Zone. Kritische Abschnitte: Die Gefahrenzone.

The part of a program where shared data is accessed and modified is called a critical section. Der Teil eines Programms, in dem auf gemeinsame Daten zugegriffen und diese geändert werden, wird kritischer Abschnitt genannt.

To prevent race conditions, we need to ensure that only one thread or process can be executing in its critical section, for a particular piece of shared data, at any given time. Um Race Conditions zu verhindern, müssen wir sicherstellen, dass nur ein Thread oder Prozess zu einem bestimmten Zeitpunkt in seinem kritischen Abschnitt, für ein bestimmtes gemeinsames Datenstück, ausgeführt werden kann.

This principle is called mutual exclusion. Dieses Prinzip wird gegenseitiger Ausschluss genannt.

Tools for Synchronization: Locks. Werkzeuge für die Synchronisation: Locks.

To enforce mutual exclusion and protect critical sections, operating systems and programming languages provide synchronization tools. Um gegenseitigen Ausschluss durchzusetzen und kritische Abschnitte zu schützen, stellen Betriebssysteme und Programmiersprachen Synchronisationswerkzeuge bereit.

One of the most common is a lock, often called a mutex, short for mutual exclusion. Eines der häufigsten ist ein Lock, oft Mutex genannt, kurz für mutual exclusion.

Mutexes, Locks: A mutex is like a key to a restricted area, the critical section. Mutexe, Locks: Ein Mutex ist wie ein Schlüssel zu einem eingeschränkten Bereich, dem kritischen Abschnitt.

Before a thread enters a critical section, it must try to acquire or lock the mutex. Bevor ein Thread in einen kritischen Abschnitt eintritt, muss er versuchen, den Mutex zu erwerben oder zu sperren.

If the mutex is available, no other thread has it, the thread acquires the lock, enters the critical section, and does its work. Wenn der Mutex verfügbar ist, kein anderer Thread ihn hat, erwirbt der Thread das Lock, betritt den kritischen Abschnitt und erledigt seine Arbeit.

While one thread holds the lock, any other thread that tries to acquire the same lock will be made to wait, it blocks, until the lock is released. Während ein Thread das Lock hält, wird jeder andere Thread, der versucht, dasselbe Lock zu erwerben, zum Warten gebracht, er blockiert, bis das Lock freigegeben wird.

When the thread that holds the lock finishes its work in the critical section, it releases or unlocks the mutex, allowing one of the waiting threads, if any, to acquire it and proceed. Wenn der Thread, der das Lock hält, seine Arbeit im kritischen Abschnitt beendet, gibt er den Mutex frei oder entsperrt ihn, sodass einer der wartenden Threads, falls vorhanden, ihn erwerben und fortfahren kann.

Using our bank account example, both the deposit and withdrawal operations would need to acquire the same lock before reading or writing the BankAccountBalance. Mit unserem Bankkonto-Beispiel müssten sowohl die Einzahlungs- als auch die Abhebungsoperationen dasselbe Lock erwerben, bevor sie BankAccountBalance lesen oder schreiben.

This way, Thread 1 would complete its deposit, read, calculate, write, before Thread 2 could even start its withdrawal, or vice versa, ensuring the balance is always correct. Auf diese Weise würde Thread 1 seine Einzahlung abschließen, lesen, berechnen, schreiben, bevor Thread 2 überhaupt seine Abhebung starten könnte, oder umgekehrt, wodurch sichergestellt wird, dass der Saldo immer korrekt ist.

Try it yourself. Probier es selbst aus.

Think about a single-lane bridge. Denk an eine einspurige Brücke.

Only one car can be on the bridge at a time going in a particular direction. Nur ein Auto kann gleichzeitig auf der Brücke sein und in eine bestimmte Richtung fahren.

How is this similar to a critical section and a mutex? Wie ähnelt dies einem kritischen Abschnitt und einem Mutex?

What acts as the lock? Was fungiert als das Lock?

What happens if cars from both directions try to enter the bridge at the same time without any signaling system? Was passiert, wenn Autos aus beiden Richtungen versuchen, gleichzeitig ohne Signalsystem auf die Brücke zu fahren?

Potential Problems Even With Synchronization. Potenzielle Probleme selbst mit Synchronisation.

While locks help, improper use or complex interactions can lead to other problems. Während Locks helfen, kann unsachgemäßer Gebrauch oder komplexe Interaktionen zu anderen Problemen führen.

Deadlock: This is a situation where two or more threads are stuck waiting for each other, and neither can proceed. Deadlock: Dies ist eine Situation, in der zwei oder mehr Threads feststecken und aufeinander warten, und keiner fortfahren kann.

Imagine Thread A has locked Resource X and is waiting for Resource Y. Stell dir vor, Thread A hat Ressource X gesperrt und wartet auf Ressource Y.

At the same time, Thread B has locked Resource Y and is waiting for Resource X. Gleichzeitig hat Thread B Ressource Y gesperrt und wartet auf Ressource X.

They are now in a deadlock. Sie befinden sich jetzt in einem Deadlock.

Thread A won't release X until it gets Y, and Thread B won't release Y until it gets X. Thread A wird X nicht freigeben, bis er Y bekommt, und Thread B wird Y nicht freigeben, bis er X bekommt.

Both are stuck indefinitely. Beide stecken auf unbestimmte Zeit fest.

Starvation, Indefinite Blocking: A thread might be repeatedly prevented from acquiring a lock or resource, even though the lock becomes available, because other threads always manage to get it first. Starvation, unbegrenzte Blockierung: Ein Thread könnte wiederholt daran gehindert werden, ein Lock oder eine Ressource zu erwerben, obwohl das Lock verfügbar wird, weil andere Threads es immer zuerst schaffen, es zu bekommen.

The thread starves because it never gets its turn. Der Thread verhungert, weil er nie an die Reihe kommt.

Think about it. Denk darüber nach.

Consider two programs, Program A and Program B, that both need to write messages to the same log file. Betrachte zwei Programme, Programm A und Programm B, die beide Nachrichten in dieselbe Log-Datei schreiben müssen.

Program A opens the log file and starts writing, Program A activity: Started. Programm A öffnet die Log-Datei und beginnt zu schreiben: Programm-A-Aktivität: Gestartet.

Before Program A finishes its line, Program B also opens the log file and writes, Program B report: Initializing. Bevor Programm A seine Zeile beendet, öffnet auch Programm B die Log-Datei und schreibt: Programm-B-Bericht: Initialisierung läuft.

Program A then tries to write, data processing complete. Programm A versucht dann zu schreiben: Datenverarbeitung abgeschlossen.

What might the log file look like? Wie könnte die Log-Datei aussehen?

How could using a lock associated with the log file prevent this jumbled output? Wie könnte die Verwendung eines Locks, das mit der Log-Datei verbunden ist, diese durcheinandergeratene Ausgabe verhindern?

Understanding these concepts of scheduling, who runs when, and synchronization, how they run together safely, is fundamental to grasping how operating systems create a stable, efficient, and seemingly simultaneous multitasking environment on our computers. Das Verständnis dieser Konzepte von Scheduling, wer wann läuft, und Synchronisation, wie sie sicher zusammen laufen, ist grundlegend, um zu begreifen, wie Betriebssysteme eine stabile, effiziente und scheinbar simultane Multitasking-Umgebung auf unseren Computern schaffen.

In our upcoming session, we'll look at how Windows manages these challenges and explore some tools to observe them in action. In unserer kommenden Sitzung werden wir uns ansehen, wie Windows diese Herausforderungen bewältigt, und einige Werkzeuge erkunden, um sie in Aktion zu beobachten.

The slides for the live session can be viewed here. Die Folien für die Live-Sitzung können hier angesehen werden.