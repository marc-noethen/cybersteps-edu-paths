Welcome! You've previously explored operating system concepts on macOS and Windows. Now, we'll dive into the world of Linux, a powerful and widely used family of Unix-like operating systems. This pre-class material will introduce you to Linux, its distributions, core philosophies, and essential tools, preparing you for a hands-on experience.

## What are Unix and Linux?

**Unix** is a family of multitasking, multi-user computer operating systems that originated in the late 1960s and early 1970s at Bell Labs. Its design principles—portability, a hierarchical file system, plain text for data storage, and a powerful command-line interface (CLI)—were revolutionary and remain influential.

![image.png](attachment:7b387bd3-6b9a-4583-b69b-ed8005953e90:image.png)

**Linux**, created by Linus Torvalds in the early 1990s, is a Unix-like operating system kernel. What we commonly refer to as "Linux" is actually the Linux kernel combined with a vast collection of software (system utilities, libraries, and applications), many of which come from the GNU Project. This combination is more accurately called **GNU/Linux**.

Linux is open source, meaning its source code is freely available to use, modify, and distribute. This has led to a vast ecosystem of Linux-based operating systems.

Key characteristics of Linux systems:

- **Open Source:** Free to use, distribute, and modify.
- **Stability and Reliability:** Known for being robust, often powering servers that run for years without rebooting.
- **Security:** Strong permission model and active community contribute to its security.
- **Flexibility:** Can be adapted for a wide range of devices, from embedded systems and smartphones (Android is Linux-based) to desktops and the world's most powerful supercomputers.
- **Command-Line Interface (CLI):** The shell provides powerful control over the system.
- **Hierarchical File System:** A tree-like structure starting from the root (`/`).

![image.png](attachment:ed1fd011-f954-45d8-83c7-b839e1de2c51:e5d0bf30-a973-43d6-adfa-6c535b445ec3.png)

### The Unix/Linux Philosophy

This philosophy emphasizes creating simple, short, clear, modular, and extensible software:

1. **Write programs that do one thing and do it well.** Each tool should have a focused purpose.
2. **Write programs to work together.** The output of one program should easily become the input for another (often using "pipes" `|`).
3. **Write programs to handle text streams, because that is a universal interface.** Text is a versatile format for program communication.

### Think about it

- How does the open-source nature of Linux potentially impact its development, security, and adoption compared to proprietary operating systems like Windows or macOS?
- Consider the Unix philosophy. Can you think of examples in software you use (on any OS) that seem to follow or violate these principles?

## What is a Linux Distribution?

Because the Linux kernel is open source, many different organizations and communities have packaged it with various tools, desktop environments, and additional software to create complete operating systems. These are known as **Linux distributions** (or "distros").

Each distribution might cater to different needs: some are designed for beginners, others for servers, specific hardware, or particular tasks like cybersecurity.

Some popular Linux distributions include:

- **Ubuntu:** Very popular, especially for desktops and cloud computing, known for its ease of use. Based on Debian.
- **Debian:** A very stable and influential distribution, the basis for many others, including Ubuntu and Kali Linux.
- **Fedora:** A cutting-edge distribution sponsored by Red Hat, often features the latest software.
- **Linux Mint:** Based on Ubuntu, aims to provide a more traditional desktop experience out of the box.
- **CentOS/Rocky Linux/AlmaLinux:** Popular for servers, focused on stability and long-term support, binary-compatible with Red Hat Enterprise Linux.

For this program, we will primarily use Kali Linux.

![image.png](attachment:abdfd715-b2ee-4ba0-8590-32295e5331b0:image.png)

You can check different Linux Distros from the link below

[DistroWatch.com: Put the fun back into computing. Use Linux, BSD.](https://distrowatch.com/)

## Setup: Installing Kali Linux in a Virtual Machine

To participate fully in the hands-on parts of this lesson and future Linux-based lessons, you will need an Kali Linux environment running in a virtual machine (VM) on your Mac. You will receive a separate video guide detailing the installation process:

[How To Install Kali Linux Using VMware Fusion On M1, M2, M3 Macs In 2024](https://www.youtube.com/watch?v=Vg9zyqZzDeM)

**Key Steps Overview:**

1. **Virtualization Software:** You will use **VMware Fusion Player** (available with a free Personal Use License) on your Arm-based Macs. Ensure it's downloaded and installed.
    
2. **Kali Linux Image (ISO):** Download the latest **Kali Linux for Arm (arm64/aarch64)**. You can find this on the official Kali Linux website ([https://cdimage.kali.org/kali-2025.2/kali-linux-2025.2-installer-arm64.iso](https://cdimage.kali.org/kali-2025.2/kali-linux-2025.2-installer-arm64.iso)), looking specifically for the Arm version.
    
3. **VM Creation & Installation:** Open the downloaded Kali Linux Arm ISO file with VMware Fusion to create a new virtual machine. Follow the on-screen prompts within VMware and the Kali Linux installer.
    
    - For Operating System select Debian 12
        
        ![Screenshot 2025-09-08 at 22.48.07.png](attachment:a287abfd-2f46-4bee-8507-e5fe4ff7c64a:Screenshot_2025-09-08_at_22.48.07.png)
        
4. **VMware Tools:** After Kali is installed and running, ensure VMware Tools are installed or updated within the VM. These tools enhance performance and usability (e.g., screen resolution, shared clipboard). If VMware Tools do not work correctly (eg. you can’t copy from host) try in you Kali terminal:
    

```bash
sudo apt update && sudo apt install open-vm-tools-desktop
sudo reboot
```

Please complete this setup _before_ proceeding with the "Try it yourself" sections below, as they require a running Kali VM. Refer to the provided video guide for detailed, step-by-step instructions.

## Core Components in a Linux System

### 1. The Linux Kernel

This is the core of any Linux distribution. It manages the system's hardware (CPU, memory, storage devices), runs processes, and handles system calls from applications.

### 2. The Shell

The shell is a command-line interpreter that allows you to interact with the kernel by typing commands.

- **Bash (Bourne Again SHell):** A very common default shell in many Linux distributions, including Ubuntu for many years. It's powerful and widely used for scripting.
- **Zsh (Z Shell):** Another powerful shell, gaining popularity. It's the default in macOS and Kali Linux now and can be easily installed on other Linux distributions.
- Other shells like `sh` (Bourne Shell), `ksh` (KornShell), and `fish` also exist.

You'll interact with the shell through a **terminal emulator** application (often just called "Terminal").

### Try it yourself (Once you have Kali running)

1. Open the Terminal application in Kali
2. Find out your default shell: `echo $SHELL` (This will likely show `/usr/bin/zsh` on a default Kali setup).
3. Check the Bash version: `zsh --version`.

### 3. The File System Hierarchy Standard (FHS)

Linux distributions adhere to the FHS, which defines the main directories and their contents. This provides a consistent structure.

Key directories:

- `/` (Root): The top-level directory.
- `/bin`: Essential user command binaries (e.g., `ls`, `cp`, `mv`).
- `/sbin`: Essential system binaries (e.g., `reboot`, `fdisk`).
- `/etc`: System-wide configuration files (traditionally "et cetera").
- `/dev`: Device files (representing hardware).
- `/home`: User home directories (e.g., `/home/yourusername`).
- `/lib`: Essential shared libraries needed by binaries in `/bin` and `/sbin`.
- `/opt`: Optional application software packages.
- `/proc`: A virtual filesystem providing process and kernel information.
- `/tmp`: Temporary files.
- `/usr`: User utilities and applications ("User System Resources").
    - `/usr/bin`: Non-essential command binaries.
    - `/usr/sbin`: Non-essential system binaries.
    - `/usr/local/bin`: Programs installed locally by the administrator.
- `/var`: Variable files—files whose content is expected to continually change during normal operation (e.g., logs in `/var/log`, mail spools).

![image.png](attachment:343b6e65-39af-4a4b-805d-ca28d217cfe2:image.png)

### Try it yourself (Once you have Kali running)

1. In Terminal: `cd /` then `ls`.
2. Explore `/etc`: `ls /etc`.
3. Navigate to your home directory: `cd ~` (or just `cd`). Verify with `pwd`. List its contents: `ls -a`.

## Basic Command Line Interaction (Brief Review)

Commands like `pwd`, `cd`, `ls`, `mkdir`, `touch`, `cp`, `mv`, and `rm` are fundamental. Remember `rm` is permanent. For viewing files, `cat`, `less`, `head`, and `tail` are your go-to tools. Pipes (`|`) and redirection (`>`, `>>`, `<`) are key for combining commands.

## Package Management: `apt` on Kali Linux

Linux distributions use package managers to simplify installing, updating, and removing software. A **package** is an archive containing all the files needed for a piece of software, plus metadata like its version and dependencies (other packages it needs to function). Package managers download packages from **repositories** (servers hosting packages).

Kali Linux (and other Debian-based systems) uses **APT (Advanced Package Tool)**. Key `apt` commands (usually run with `sudo` for administrative privileges):

- `sudo apt update`: Refreshes the local list of available packages from repositories. Do this before installing or upgrading.
- `sudo apt upgrade`: Upgrades all currently installed packages to their newest versions.
- `sudo apt install <package_name>`: Installs a new package.
- `sudo apt remove <package_name>`: Removes a package.
- `sudo apt autoremove`: Removes packages that were automatically installed to satisfy dependencies for other packages and are now no longer needed.
- `apt search <keyword>`: Searches for available packages related to a keyword.
- `apt show <package_name>`: Shows detailed information about a package.

![image.png](attachment:26a0e39b-2325-4429-a388-87a08be1f011:image.png)

### Try it yourself (Once you have Kali running)

1. Update package lists: `sudo apt update`
2. Search for a simple program, e.g., `apt search tree` (tree is a utility to display directory structures).
3. Install it: `sudo apt install tree`
4. Run it in your home directory: `tree ~`
5. Remove it: `sudo apt remove tree`
6. Clean up: `sudo apt autoremove`

## Users, Groups, and Permissions

Linux is multi-user. Permissions control access to files/directories for the **owner (u)**, **group (g)**, and **others (o)**, with **read (r)**, **write (w)**, and **execute (x)** permissions. The `root` user (superuser) has all privileges. Use `sudo` to run commands as root. Commands like `chmod` and `chown` manage permissions and ownership.

## User Account Information

Traditional Unix and Linux systems store user and group information in these files:

- `/etc/passwd`: User account information (username, UID, GID, home directory, shell).
- `/etc/group`: Group information.
- `/etc/shadow`: Securely stores hashed user passwords and password aging information (readable only by root).

The `id` command shows your UID, GID, and group memberships.

### Try it yourself (Once you have Kali running)

1. View your user info: `id`
2. Look at the (non-sensitive parts of) user database: `less /etc/passwd`
3. Look at group information: `less /etc/group`

## Services (Daemons) and Scheduled Tasks

**Daemons** are background processes providing system services.

- **`systemd`**: Most modern Linux distributions, including Kali, use `systemd` as an init system and service manager. It controls what starts at boot and manages services.
    - `systemctl status <service_name>`: Check service status.
    - `sudo systemctl start <service_name>`: Start a service.
    - `sudo systemctl stop <service_name>`: Stop a service.
    - `sudo systemctl enable <service_name>`: Start service on boot.
    - `sudo systemctl disable <service_name>`: Don't start on boot.
- **`cron`**: A time-based job scheduler. Users can schedule commands or scripts to run periodically using a `crontab`file (edit with `crontab -e`).

## Remote Access: SSH (Secure Shell)

While graphical remote access tools exist, **SSH** is the standard for command-line remote access in the Linux/Unix world. It provides an encrypted connection to a remote machine's shell. Tools like `scp` (secure copy) and `sftp` (SSH File Transfer Protocol) use SSH for secure file transfers. SSH is vital for server administration and cybersecurity tasks. Kali includes an SSH client (`ssh`) and can run an SSH server (`openssh-server` package).

This pre-class material provides a foundation for understanding Linux. The live session will delve deeper into these concepts with practical demonstrations and cybersecurity contexts. Make sure to set up your Kali VM before class!

<aside> 📌

The slides for the live session can be viewed here: [https://gamma.app/docs/Operating-Systems-14-Unix-Linux-uoe175a2z7lby8m?mode=doc](https://gamma.app/docs/Operating-Systems-14-Unix-Linux-uoe175a2z7lby8m?mode=doc)

Try not to peek before class - spoilers inside!

</aside>