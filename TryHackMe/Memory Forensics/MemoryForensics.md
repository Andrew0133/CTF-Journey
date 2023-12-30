# Memory Forensics

## Room Info

Room: [Here](https://tryhackme.com/room/memoryforensics)

Difficulty: **Easy**

## Description

Perform memory forensics to find the flags

## Task 1 - Introduction

In this task, there isn't much we can do, but the challenge suggests that we start by exploring the volatility room first. So, we're going to use it. 

I know that there are two versions: Volatility 2, which is built using Python 2, and Volatility 3, which uses Python 3. There are different use cases for each version, and depending on this, we might choose either one over the other.

As the [github](https://github.com/volatilityfoundation/volatility/) page informs us: "*The Volatility Framework is a completely open collection of tools, implemented in Python under the GNU General Public License, for the extraction of digital artifacts from volatile memory (RAM) samples. The extraction techniques are performed completely independent of the system being investigated but offer visibilty into the runtime state of the system.*"

## Task 2 - Login

### Context

*The forensic investigator on-site has performed the initial forensic analysis of John's computer and handed you the memory dump he generated on the computer. As the secondary forensic investigator, it is up to you to find all the required information in the memory dump.*

### Question - What is John's password?

#### Hint: Rockyou.txt

For this purpose we can use a plugin that Volatility3 offers: ```windows.hashdump```. This plugin will helps us to list the hashes of the users in the system.

![Alt text](./imgs/task2/windows_hashdump.png?raw=true "windows hashdump plugin output")

If we are lucky, we can attempt to crack the password hash using the [CrackStation](https://crackstation.net/) website.

![Alt text](./imgs/task2/crackstation.png?raw=true "windows hashdump plugin output")

We got a match, the answer! 

## Task 3 - Analysis

### Context

*On arrival a picture was taken of the suspect's machine, on it, you could see that John had a command prompt window open. The picture wasn't very clear, sadly, and you could not see what John was doing in the command prompt window. To complete your forensic timeline, you should also have a look at what other information you can find, when was the last time John turned off his computer?*

### Question 1 - *When was the machine last shutdown?*

#### Hint: Format: YYYY-MM-DD HH:MM:SS

For this question we know that this information, in a Windows machine, is stored inside a Windows Registry: ```SYSTEM\CurrentControlSet\Control\Windows```.

For this purpose we can use a plugin that Volatility3 offers: ```windows.registry.printkey.PrintKey```. This plugin will helps us to to look at the windows registries.

![Alt text](./imgs/task3/win_shutdown_time.png?raw=true "windows printkey plugin output")

I found [this](https://renenyffenegger.ch/notes/Windows/registry/tree/HKEY_LOCAL_MACHINE/System/CurrentControlSet/Control/Windows/index) link that helps us understand how the data is stored: "*ShutdownTime contains an 64-bit RegBinary value that contains the last shutdown time encoded as a FILETIME.*"

From here, I searched for information about the **FILETIME** data structure. The [Microsoft documentation](https://learn.microsoft.com/en-US/windows/win32/api/minwinbase/ns-minwinbase-filetime) explains the **FILETIME** structure perfectly: "*Contains a 64-bit value representing the number of 100-nanosecond intervals since January 1, 1601 (UTC).*"

For this purpose, I wrote a Python [script](get_windows_shutdown_time.py) that interprets and transforms the information from the Volatility output into a human-readable format. In this case, I used the hint provided by TryHackMe to determine the answer format.

The output of the script will print the answer.

![Alt text](./imgs/task3/answer2.png?raw=true "output of the script for the second answer")

### Question 2 - *What did John write?*

#### Hint: It's written between curly brackets: THM{XXXX}

From the description of the task we know that John was doing something in the command prompt window. So we are interested about what he did in that process. 

For this task, I will be utilizing Version 2 of Volatility. One notable distinction from Version 3 is the **Volatility Profiles**. A profile guides Volatility in correctly interpreting the data, providing essential information about the memory layout, data structures, and other system characteristics from which the memory dump originated.

We can use the ```imageinfo``` command in Volatility to determine the appropriate profile. It will provides us a list of suggested profiles based on the characteristics of the memory image.

Since we didn't know any information about the system from which the memory dump was obtained, I will proceed with the first suggested profile. To set the profile for subsequent steps we can use the ```--profile``` argument.

For this step we can use the ```pslist``` module to print all running processes.

![Alt text](./imgs/task3/pslist_module_output.png?raw=true "ps list module output")

Since the description highlighted the command prompt window we are interested in the process highlighted in the picture: ```cmd.exe```

Since we are interested on what he did on that process we can try to use the ```procdump``` module. This will dump a process to an executable file sample.

![Alt text](./imgs/task3/procdump_module_output.png?raw=true "procdump list module output")

Here we did a couple of things:
- ```--pid``` will tell the framework on which process operate based on the PID. From the previous image, the PID of the targeted process is **1920**;
- ```--dump-dir```: directory in which to dump executable files.

Thanks to the hint provided I printed the content of the process dump with a regex to match the flag format. We got a match.

![Alt text](./imgs/task3/flag.png?raw=true "task 3 flag")

## Task 4 - TrueCrypt

### Context

*A common task of forensic investigators is looking for hidden partitions and encrypted files, as suspicion arose when TrueCrypt was found on the suspect's machine and an encrypted partition was found. The interrogation did not yield any success in getting the passphrase from the suspect, however, it may be present in the memory dump obtained from the suspect's computer.*

### Question - What is the TrueCrypt passphrase?

I am currently reading the book 'The Art of Memory Forensics,' written by the creators of the Volatility framework. I found a section very useful, particularly on this topic. 

TrueCrypt was a widely used open-source disk encryption software for Windows, macOS, and Linux. It allowed users to create virtual encrypted disks within a file or encrypt an entire partition or storage device.

As mentioned on the book: "*TrueCrypt supports caching passwords and key files in memory. Although this feature is disabled by default, many users enable it for convenience. This unprotected data in memory is the “low-hanging fruit” so to speak. If exposed in a memory capture, investigators can use the credentials to fully reveal data on the encrypted media.*"

So we can use the ```truecryptsummary``` plugin to extract information about TrueCrypt volumes and their associated metadata.

![Alt text](./imgs/task4/answer.png?raw=true "answer of task 4")

We got the password and the answer of the task.
