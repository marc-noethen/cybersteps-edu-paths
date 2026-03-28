Welcome to the world of Virtual Local Area Networks (VLANs)! Before our live session, please go through this material to get a foundational understanding of what VLANs are, why they are used, and how they work at a conceptual level. This will help you make the most of our interactive class.

## What is a LAN? A Quick Refresher

You've already learned about the Datalink Layer and Local Area Networks (LANs). As a quick reminder, a LAN is a network that connects computers and devices in a limited geographical area, such as a home, school, office building, or closely positioned group of buildings. All devices in a traditional LAN are part of the same **broadcast domain**. This means that if one device sends a broadcast message (a message intended for all devices on the network), every other device in that LAN receives it.

## Why Segment Networks?

![[Pasted image 20250930061546.png]]

As networks grow, having a single, large LAN can lead to several problems:

- **Security Risks**: If all devices are on the same network, it's easier for unauthorized users or compromised machines to access sensitive information or affect other systems. For example, if a device in the guest services department gets infected with malware, it could potentially spread to critical servers in the finance department if they share the same LAN.
- **Performance Degradation**: A large number of devices in one broadcast domain can lead to excessive broadcast traffic. While modern switches have eliminated collision domains for the most part, broadcast traffic still consumes bandwidth and processing power on every connected device.
- **Organizational Challenges**: Managing a large, flat network can be complex. It's often desirable to group devices based on department (e.g., Sales, Engineering, HR), function, or security requirements.
- **Lack of Flexibility**: Physically rewiring the network every time an employee moves desks or a department reorganizes is inefficient and costly.

Network segmentation is the practice of splitting a larger network into smaller, isolated subnetworks or segments. VLANs are a primary method for achieving this at the Datalink Layer.

## Introduction to VLANs

![[Pasted image 20250930061554.png]]

**VLAN** stands for **Virtual Local Area Network**.

At its core, a VLAN allows you to take a single physical LAN infrastructure (like one physical switch) and logically segment it into multiple independent broadcast domains. Each VLAN behaves as if it were a separate physical LAN, even though the devices might be connected to the same physical switch.

Think of it like this: imagine an office building with multiple departments. Without VLANs, you might need a separate physical switch for each department to keep their network traffic isolated. With VLANs, you can use a single, more capable switch and configure it to create virtual "mini-switches" inside it, one for each department. Devices plugged into specific ports on the physical switch can be assigned to different VLANs, and they will only be able to communicate directly with other devices in the _same_ VLAN.

## How VLANs Work: The Concept of Tagging

![[Pasted image 20250930061601.png]]

So, how does a switch know which device belongs to which VLAN, especially when traffic needs to pass between switches? The magic lies in **VLAN tagging**.

The most common standard for VLAN tagging is **IEEE 802.1Q**. When an Ethernet frame (the data packet at the Datalink Layer) needs to travel between switches that are aware of VLANs, a special "tag" is inserted into the frame header. This tag contains information, most importantly the **VLAN ID (VID)** – a number (typically between 1 and 4094) that identifies the VLAN to which the frame belongs.

- **Access Ports**: These are switch ports that are assigned to a single VLAN. Devices connected to access ports (like a user's computer or a printer) are typically unaware that VLANs exist. The switch adds the VLAN tag when frames leave an access port to travel over a trunk link and removes the tag when frames destined for a device on that access port arrive.
- **Trunk Ports**: These are switch ports configured to carry traffic for _multiple_ VLANs. Trunk ports are typically used to connect switches to each other, or a switch to a router or firewall that understands VLANs. Frames traversing a trunk port retain their 802.1Q tag so the receiving switch or router knows which VLAN the frame belongs to.

![[Pasted image 20250930061608.png]]

## Benefits of Using VLANs

Implementing VLANs offers several significant advantages:

1. **Improved Security**: By isolating groups of users or devices into different VLANs, you can control which groups can communicate with each other. For example, you can create a separate VLAN for guests, preventing them from accessing internal company resources.
2. **Reduced Broadcast Traffic & Improved Performance**: Broadcasts from a device in one VLAN are not forwarded to other VLANs. This reduces the overall broadcast traffic on the network, conserving bandwidth and improving performance.
3. **Cost Savings**: VLANs can reduce the need for expensive hardware. Instead of buying multiple physical switches to segment a network, you can use a single switch with VLAN capabilities. This also simplifies cabling.
4. **Flexibility and Scalability**: You can easily move a device to a different logical network by reconfiguring the switch port, without any physical rewiring. Adding new users or departments can be managed by assigning them to appropriate VLANs.
5. **Simplified Administration**: Grouping users and devices by logical function rather than physical location makes network management easier. For instance, all accounting department devices can be in "VLAN 10 (Accounting)" regardless of where their desks are located.

## Key Terminology to Remember

- **VLAN (Virtual Local Area Network)**: A logical network segment that allows a single physical network infrastructure to be divided into multiple independent broadcast domains.
- **Broadcast Domain**: A logical area of a computer network where any device connected to the network can transmit directly to any other device in the same domain without going through a routing device. VLANs create separate broadcast domains.
- **IEEE 802.1Q**: The networking standard that defines how VLAN information is added to Ethernet frames (VLAN tagging).
- **VLAN ID (VID)**: A number that uniquely identifies a VLAN.
- **Access Port**: A switch port that belongs to and carries traffic for only one VLAN. Devices connected to access ports are unaware of VLAN tagging.
- **Trunk Port**: A switch port that can carry traffic for multiple VLANs simultaneously. Used for inter-switch links or connections to VLAN-aware routers.
- **Native VLAN**: A specific VLAN on an 802.1Q trunk port where traffic is sent untagged. By default, this is usually VLAN 1. Untagged frames received on a trunk port are assumed to belong to the native VLAN.

### Think about it

Imagine a company with three departments: Sales (needs access to CRM and public internet), Engineering (needs access to development servers and limited internet), and Guests (internet access only). All are connected to a single physical switch.

- How would you use VLANs to meet these requirements?
- What would be the VID for each VLAN (you can pick any valid numbers)?
- Which ports would likely be access ports, and which might be trunk ports if this switch connects to a router for internet access?

### Try it yourself

Conceptually, draw a simple network diagram.

1. Include one switch.
2. Connect four PCs to this switch.
3. You want PC1 and PC2 to be in "VLAN 10 - Marketing".
4. You want PC3 and PC4 to be in "VLAN 20 - Finance".
5. How would the switch ensure that PC1 can talk to PC2, but not to PC3, without a router? (Hint: Think about port assignments on the switch).

This pre-class material should give you a solid understanding of VLAN concepts. We'll build upon this in our live session with more examples and discussions.

<aside> 📌

The slides for the live session can be viewed here: [https://gamma.app/docs/Networking-17-VLANs-ojcyw1p6leloanb?mode=doc](https://gamma.app/docs/Networking-17-VLANs-ojcyw1p6leloanb?mode=doc)

Try not to peek before class - spoilers inside!

</aside>