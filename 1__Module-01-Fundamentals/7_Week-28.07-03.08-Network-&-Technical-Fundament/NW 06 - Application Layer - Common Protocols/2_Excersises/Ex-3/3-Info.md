# Mission: FTP

_Be the master of your own (temporary) file domain._

**Goal**

Set up a simple, temporary FTP server on your local machine, connect to it, capture the traffic, and analyze the commands and the two-channel communication model.

**Instructions**

1. **Install FTP Server Library:** Open Terminal. Install `pyftpdlib` using pip: `pip3 install pyftpdlib`
2. Install Inetutils package with `ftp` - open terminal and type: `brew install inetutils`
3. **Prepare Directory:** Create a directory for your FTP server, e.g., `mkdir ~/my_ftp_test` and `cd ~/my_ftp_test`. Create a dummy file inside it: `echo "FTP test data" > testfile.txt`
4. **Run Local FTP Server:** In the _same terminal window_ (now inside `~/my_ftp_test`), start the server: `python3 -m pyftpdlib -w -p 21`
    - Keep this running.
5. **Start Capture:** Open Wireshark and start capturing on the **Loopback interface** (`lo0`). Use the capture filter `tcp.port == 21 or ftp-data`.
6. **Connect via FTP Client:** Open a _second_ Terminal window. Connect to your local server: `sudo ftp localhost` Use credentials : user: anonymous, password: [hit enter]
7. **Interact:** Since it's anonymous, just press Enter if prompted for Name/Password. Then, perform these commands:
    - `ls` (List files on the server)
    - `get testfile.txt` (Download the file)
    - `put testfile.txt uploaded_file.txt` (Upload the file back with a new name)
    - `ls` (Verify the uploaded file exists)
    - `quit`
8. **Stop Server & Capture:** Stop the FTP server (Ctrl+C). Stop the Wireshark capture.
9. **Analyze in Wireshark:**
    - Filter for `ftp || ftp-data`.
    - Examine the **control connection** (port 21). Confirm `RETR` (get) and `STOR` (put) are clear text.
    - **Deeper Dive 1:** Besides `USER`/`PASS`/`RETR`/`STOR`/`LIST`, what other FTP commands did you observe on the control channel (e.g., `SYST`, `TYPE`, `PASV`/`EPSV`, `QUIT`)? Briefly look up the purpose of the `TYPE` command in RFC 959. Why might specifying the data type (like ASCII vs. Binary/Image) be important for file transfers?
    - **Deeper Dive 2:** Examine the **data connections**. Confirm the file content is visible. Why does FTP's standard use of separate, dynamically negotiated ports for data transfer often cause problems for network firewalls compared to protocols that use a single connection (like SSH/SFTP)?

**Submission**

Submit two screenshots from Wireshark:

1. The packet details pane for the `STOR` command on the control connection (port 21).
2. The "Follow TCP Stream" window for the data connection associated with the `RETR` command, showing the clear text file content. Add text answers addressing the "Deeper Dive" questions in step 8 (Purpose of `TYPE` command? Why does the separate data channel cause firewall issues?).