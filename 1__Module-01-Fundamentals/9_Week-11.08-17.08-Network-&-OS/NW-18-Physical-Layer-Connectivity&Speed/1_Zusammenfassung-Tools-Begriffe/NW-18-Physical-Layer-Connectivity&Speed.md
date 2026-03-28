Welcome to your pre-class preparation for our session on the Physical Layer of networking. This foundational layer is all about how digital data (those 0s and 1s) gets transformed into signals that can travel over different physical media – like wires, fiber optic cables, or through the air. Understanding this layer is key to grasping how networks physically connect and what determines their speed and reliability.

# The Physical Layer: Data's First Hop

In network models like OSI or TCP/IP, the Physical Layer (Layer 1) is the lowest level. Its job is to manage the actual transmission of raw bits. It defines:

- **How devices are physically connected:** Think cables, connectors, and wireless radio waves.
- **How bits become signals:** Turning 0s and 1s into electrical pulses, light flashes, or radio waves.
- **Data transmission rates:** How fast data can move (e.g., bits per second).
- **Signal timing (synchronization):** Making sure the sender and receiver are on the same page.
- **Direction of data flow:** Whether data can flow one way, or both ways (and if both, simultaneously or one at a time).

Essentially, if the internet is an information superhighway, the physical layer is the asphalt, the fiber optic lines, and the radio waves that make up the road itself.

# Connectivity Components: The Building Blocks

Let's look at the common hardware that makes these connections happen.

## **Cables: The Wired Pathways**

![[Pasted image 20250930061936.png]]

### Twisted Pair (Copper)

This is the most common cable for Local Area Networks (LANs) – like your home or office network. It has pairs of copper wires twisted together, which helps reduce interference.

- **Unshielded Twisted Pair (UTP):**
    - Commonly used for Ethernet. You'll see markings like **Cat 5e** (supports up to 1 Gigabit per second, Gbps) or **Cat 6** (supports 1 Gbps reliably, and 10 Gbps over shorter distances).
    - Uses **RJ45 connectors** (they look like slightly larger phone jacks).
    - Pros: Cheap, flexible. Cons: More prone to electrical noise than shielded types.
- **Shielded Twisted Pair (STP):**
    - Has an extra layer of shielding to protect against interference.
    - Used in environments with more electrical noise (factories, near heavy machinery).
    - Pros: Better noise protection. Cons: More expensive, less flexible.

### Coaxial Cable (Copper)

You might know this from older cable TV setups or as the cable connecting to your internet modem. It has a central copper conductor, insulation, a braided metal shield, and an outer jacket.

- **Connectors:** Commonly **F-type connectors** (screw-on) for cable internet/TV.

### Fiber Optic Cable

These cables use light pulses to transmit data through thin strands of glass (or sometimes plastic).

- **How it works:** A light source (LED or laser) sends light pulses representing 0s and 1s. The light travels down the fiber, reflecting internally, until it reaches a detector.
- **Key Advantages:**
    - **Speed & Bandwidth:** Much higher capacity than copper.
    - **Distance:** Can carry signals much further with less signal loss (attenuation).
    - **Immunity to EMI:** Not affected by electromagnetic interference.
- **Types:**
    - **Single-Mode Fiber (SMF):** Very thin core, uses lasers, for very long distances (e.g., undersea cables, telecom backbones). More expensive equipment.
    - **Multi-Mode Fiber (MMF):** Larger core, uses LEDs or cheaper lasers, for shorter distances (e.g., within a data center, connecting buildings on a campus). Cheaper equipment.
- **Connectors:** Common types include **LC** (small, for high-density) and **SC** (square, push-pull).

### Network Interface Cards (NICs)

![[Pasted image 20250930061945.png]]

A NIC is the hardware in your computer (or other device) that lets it connect to a network. It has a port for a network cable (like an RJ45 port for Ethernet) or an antenna for wireless. Each NIC has a unique physical address called a MAC address (used at Layer 2).

### Modems (Modulator-Demodulator)

![[Pasted image 20250930061952.png]]

A modem is a device that converts signals from one form to another to allow data transmission over different types of media. Your computer speaks digital, but some communication lines (like traditional phone lines or cable TV lines) were originally designed for analog signals.

- **Function:**
    - **Modulation:** Converts digital data from your computer into analog signals suitable for transmission over the analog medium.
    - **Demodulation:** Converts incoming analog signals back into digital data that your computer can understand.
- **Common Types:**
    - **DSL Modems:** Use telephone lines to connect to the internet.
    - **Cable Modems:** Use coaxial cable TV lines.
    - **Fiber Optic Modems (often called Optical Network Terminals - ONTs):** Convert signals to/from light pulses for fiber-to-the-home (FTTH) services. These don't strictly "modulate" in the traditional analog sense but perform the crucial digital-to-optical conversion.

### Think about it

Why do you think fiber optic cables are immune to electromagnetic interference (EMI) when copper cables are susceptible to it?

# Transmission Media Characteristics: Measuring Performance

How do we describe how well a network connection performs?

### Bandwidth

The theoretical maximum amount of data that can be transferred over a connection in a given amount of time. Usually measured in bits per second (bps), Mbps (megabits per second), or Gbps (gigabits per second).

- Think of it as the _width of a pipe_: a wider pipe can carry more water (data).

### Throughput

The _actual_ rate of data transfer that is achieved. This is often lower than the theoretical bandwidth due to various factors like network congestion, latency, and protocol overhead.

- If bandwidth is the pipe's width, throughput is how much water _actually flows_ through it.

### Latency

The delay it takes for data to travel from its source to its destination. Measured in milliseconds (ms). High latency means noticeable delays (e.g., lag in online games or video calls).

- Caused by: distance, speed of the medium, processing time in network devices, and congestion.
    
    ![[Pasted image 20250930062002.png]]
    

### Jitter

The variation in latency over time. If packets arrive with inconsistent delays, it's called jitter.

- Bad for real-time applications like VoIP or video streaming, as it can cause garbled audio or choppy video.

![[Pasted image 20250930062009.png]]

### Attenuation

The gradual loss of signal strength as it travels through a medium. The further the signal goes, the weaker it gets.

- Copper cables are more prone to attenuation over shorter distances than fiber optic cables.
- **Mitigation:** Repeaters or amplifiers can boost the signal, and cables have maximum length specifications (e.g., UTP Ethernet is typically limited to 100 meters).

### Noise and Interference

Unwanted signals that can corrupt or disrupt the data signals.

- **Electromagnetic Interference (EMI):** From motors, power lines, fluorescent lights.
- **Crosstalk:** When the signal in one wire interferes with the signal in an adjacent wire in the same cable. Twisting wire pairs helps reduce this.
- **Mitigation:** Shielded cables (STP), proper grounding. Fiber optic cables are immune to EMI and crosstalk.

## Signaling Methods: The Language of Bits

![[Pasted image 20250930062017.png]]

To send data, those 0s and 1s need to be converted into physical signals:

- **Copper Cables:** Usually different voltage levels (e.g., +5V for a '1', 0V for a '0').
- **Fiber Optic Cables:** Presence or absence of light (light ON for '1', light OFF for '0', or variations).
- **Wireless:** Radio waves with varying characteristics (amplitude, frequency, phase).

**Encoding** and **Modulation** are techniques used to represent these bits as signals in a way that the receiver can understand and to help with things like timing and error detection. For example, modulation is what a modem does to put digital computer signals onto an analog phone line.

# Speed Standards: How Fast Can We Go?

![[Pasted image 20250930062024.png]]

Network speeds are often defined by standards, especially for Ethernet (the most common wired LAN technology).

- **Fast Ethernet (100BASE-TX):** 100 Mbps. Uses Cat 5e UTP.
- **Gigabit Ethernet (1000BASE-T):** 1 Gbps. Uses Cat 5e or Cat 6 UTP. Very common today.
- **10 Gigabit Ethernet (10GBASE-T):** 10 Gbps. Uses Cat 6a or Cat 7 UTP, or fiber.

The names often give clues: "1000" = speed in Mbps, "BASE" = baseband (digital signal), "T" = twisted pair. Suffixes like "SX" or "LR" usually refer to fiber optic types.

# Duplex Modes: Talking and Listening

![[Pasted image 20250930062030.png]]

This refers to whether data can flow in one or both directions on a link.

- **Half-Duplex:** Data can go in both directions, but _not at the same time_. Like a walkie-talkie; one talks, the other listens. Older Ethernet hubs used this, leading to collisions if devices transmitted simultaneously.
- **Full-Duplex:** Data can go in both directions _simultaneously_. Like a telephone call. Modern network switches allow full-duplex, which significantly improves performance.

Most modern wired networks use full-duplex. Devices usually auto-negotiate the highest common speed and duplex mode. A mismatch (e.g., one side full-duplex, other half-duplex) causes major problems.

This preparation should give you a solid base for our upcoming lesson. We'll explore these concepts further and see their relevance in cybersecurity.

<aside> 📌

The slides for the live session can be viewed here: [https://gamma.app/docs/Networking-18-Connectivity-Speed-2wz02w0787zmdrn?mode=doc](https://gamma.app/docs/Networking-18-Connectivity-Speed-2wz02w0787zmdrn?mode=doc)

Try not to peek before class - spoilers inside!

</aside>