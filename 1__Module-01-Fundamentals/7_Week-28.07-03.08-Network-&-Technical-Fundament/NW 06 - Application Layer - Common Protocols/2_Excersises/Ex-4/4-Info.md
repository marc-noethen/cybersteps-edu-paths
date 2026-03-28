# Mission: SSH

_What happens when client and server disagree on how to talk securely?_

## Goal

Capture a standard SSH connection to a real public server, analyze the algorithm negotiation, then attempt a connection while forcing the client to offer only an older, likely unsupported algorithm. Observe the effect on the handshake and connection success.

## Instructions

### 1. Start Wireshark

- Start capturing on your main internet interface (e.g., `en0`, `eth0`)
    
- Use this capture filter:
    
    ```
    tcp.port == 22
    ```
    

### 2. Capture Baseline Connection

- In Terminal, connect normally:
    
    ```
    ssh demo@test.rebex.net
    ```
    
- When prompted, enter the password:
    
    ```
    password
    ```
    
- After login, type:
    
    ```
    exit
    ```
    
    to disconnect.
    
- Stop the Wireshark capture.
    

### 3. Analyze Baseline Handshake

- In Wireshark, find the Key Exchange Init (`KEXINIT`) packet sent by your client.
- Look at the proposed lists of algorithms (`KexAlgorithms`, `Ciphers`, etc.).
- Note how many algorithms the client offers by default.

### 4. Attempt a Connection with a Legacy Algorithm

- Start a new capture in Wireshark (same filter).
    
- In Terminal, run:
    
    ```
    
    ssh -oKexAlgorithms=diffie-hellman-group1-sha1 demo@test.rebex.net
    ```
    
- Observe:
    
    - Did the connection succeed or fail?
        
    - Was there an error like:
        
        ```
        Unable to negotiate with ...
        ```
        
- Stop the capture.
    

### 5. Analyze the Modified Handshake

- In Wireshark, find the client's new `KEXINIT` packet.
- Verify that only `diffie-hellman-group1-sha1` was proposed.
- Look for a rejection or disconnect message in the packet flow.

### 6. Deeper Dive

Answer these:

- Why did the connection likely fail?
- What does this demonstrate about SSH algorithm negotiation?
- Why is it important that old algorithms are rejected?

## Submission

1. A screenshot from the baseline capture showing the client's `KEXINIT` packet and full list of `KexAlgorithms`.
2. A screenshot from the modified capture showing the `KEXINIT` packet listing only `diffie-hellman-group1-sha1`.
3. A text explanation:
    - Did the modified connection work?
    - Why or why not?
4. A text reflection answering:
    - What does this show about the importance of algorithm negotiation in SSH?