# Mission: Telnet

_Why don’t they use it anymore?_

**Goal**

Connect to a public Telnet server (`telehack.com`), interact with it using several commands, capture the traffic with Wireshark, and analyze the captured data to understand how Telnet handles commands, responses, and control signals.

**Instructions**

1. **Target Server:** We'll use `telehack.com`, which provides various text-based services and commands.
    
2. **Start Capture:** Open Wireshark and start capturing on your **active network interface** (e.g., Wi-Fi/en0 or Ethernet). Use the capture filter `telnet` or `tcp.port == 23`.
    
3. **Connect via Telnet:** Open your Terminal. Run `telnet telehack.com`.
    
4. **Interact:** Once connected, you'll see a welcome message and prompt. Try 5 of the possible commands eg. `starwars`, pressing Enter after each. Observe the output on your screen for each command.
    
    Also try typing some random text like `Is anyone listening?` and press Enter.
    
5. **Close Connection:** Press `Ctrl + ]`, then type `quit` and press Enter. Pay attention to any characters echoed when you press Ctrl+].
    
6. **Stop Capture:** Stop the Wireshark capture.
    
7. **Analyze in Wireshark:**
    
    - Find the TCP conversation for port 23 to `telehack.com`.
    - Right-click on a packet and select "Follow" -> "TCP Stream".
    - Examine the stream content carefully. Confirm you can see both your commands and the server's responses clearly.
    - **Deeper Dive:** Telnet uses special control sequences for out-of-band signaling (like handling interrupts or negotiating options), often starting with the IAC (Interpret as Command - byte 0xFF) character. Did you notice any non-printable characters or brief command sequences in the TCP stream, particularly around the time you typed `Ctrl + ]` and `quit`? Briefly research Telnet control sequences (RFC 854 is the primary source, look for IAC) - what is their purpose compared to just sending user data?

**Submission**

Submit a screenshot of the Wireshark "Follow TCP Stream" window. Scroll the window so that it clearly shows at least two different commands you typed and their corresponding responses from the server. Add text answers addressing:

1. Was all the user input and server output readable plain text?
2. What is the purpose of Telnet control sequences (like IAC) according to your research, and did you see any evidence of them in the stream?