# Network Topology with Mininet

This repository is lab for NCTU course "Introduction to Computer Networks 2018".

---
## Abstract

In this lab, we are going to write a Python program which can generate a network topology using Mininet and use iPerf to measure the bandwidth of the topology.

---
## Objectives

1. Learn how to create a network topology with Mininet
2. Learn how to measure the bandwidth in your network topology with iPerf

---
## Execution

> TODO: 
> * Describe how to execute your program

>> In this lab, I modify the example.py, and create another .py file, 0616309_lab2.py

    
>>```bash
>> # Change the directory into /Network_Topology/src/  
>> $ cd /root/Network_Topology/src/
>> # Change to the executable mode of 0616309_lab2.py  
>> $ [sudo] chmod +x 0616309_lab2.py
>> # Run 0616309_lab2.py
>> $ [sudo] ./0616309_lab2.py
>> ```

> * Show the screenshot of using iPerf command in Mininet

>> ![Screenshot_iPerf](https://github.com/nctucn/lab2-allen880117/blob/master/screenshots/Screenshot_iPerf.png)
---
## Description

### Mininet API in Python

> TODO:
> * Describe the meaning of Mininet API in Python you used in detail

### iPerf Commands

> TODO:
> * Describe the meaning of iPerf command you used in detail

### Tasks

> TODO:
> * Describe how you finish this work step-by-step in detail

1. **Environment Setup**
    1. Join this lab on GitHub Classroom by using the link provided in lab2_tasks.pdf
        > https://classroom.github.com/a/K8gaizQG
    
    2. Login to my container using SSH
        1. Open the PieTTY ( Putty is also OK ) and connect to my container
            > * IP address : 140.113.195.69
            > * Port : 16309
        2. Login as root
            > * Login : root
            > * Password : cn2018
        3. For protecting my own work
            > ```bash
            > # Change password
            > $ passwd
            > Enter new UNIX password: <NewPassword> 
            > Retype new UNIX password: <NewPassword>
            > ```   

    3. Clone my GitHub repository to "Network_Topology"
        > ```bash
        > # Clone my GitHub repository to "Network_Topology"
        > $ git clone https://github.com/nctucn/lab2-allen880117.git Network_Topology
        > ```

    4. Run Mininet for testing
        > the result is the following image
        > ![Screenshot_mininet](https://github.com/nctucn/lab2-allen880117/blob/master/screenshots/Screenshot_mininet.png)
2. **Example of Mininet**
    1. Run the example code
        > usually we don't need sudo here since we use root account
        > ```bash
        > # Change the directory into /Network_Topology/src/
        > $ cd /root/Network_Topology/src/
        > # Change to the executable mode of example.py
        > $ [sudo] chmod +x example.py 
        > # Run example code (example.py)
        > $ [sudo] ./example.py
        > ```

    2. Check the result after running example code
        > The result won't be same as the one provided by lab2_tasks.pdf(old version). <br>
        > In older version of lab2_tasks.pdf, there will be 4 hosts, but example.py will only generate 2 hosts and 1 switch. <br>
        > The result will be same as the one provided by  the latest version of lab2_tasks.pdf. <br> 
        > ![Screenshot_example](https://github.com/nctucn/lab2-allen880117/blob/master/screenshots/Screenshot_example.png)
3. **Topology Generator**


4. **Measurement**

---
## References

> TODO: 
> * Please add your references in the following

* **Mininet**
    * [Mininet Walkthrough](http://mininet.org/walkthrough/)
    * [Introduction to Mininet](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet)
    * [Mininet Python API Reference Manual](http://mininet.org/api/annotated.html)
    * [A Beginner's Guide to Mininet](https://opensourceforu.com/2017/04/beginners-guide-mininet/)
    * [GitHub/OSE-Lab - 熟悉如何使用 Mininet](https://github.com/OSE-Lab/Learning-SDN/blob/master/Mininet/README.md)
    * [菸酒生的記事本 – Mininet 筆記](https://blog.laszlo.tw/?p=81)
    * [Hwchiu Learning Note – 手把手打造仿 mininet 網路](https://hwchiu.com/setup-mininet-like-environment.html)
    * [阿寬的實驗室 – Mininet 指令介紹](https://ting-kuan.blog/2017/11/09/%E3%80%90mininet%E6%8C%87%E4%BB%A4%E4%BB%8B%E7%B4%B9%E3%80%91/)
    * [Mininet 學習指南](https://www.sdnlab.com/11495.html)
* **Python**
    * [Python 2.7.15 Standard Library](https://docs.python.org/2/library/index.html)
    * [Python Tutorial - Tutorialspoint](https://www.tutorialspoint.com/python/)
* **Others**
    * [iPerf3 User Documentation](https://iperf.fr/iperf-doc.php#3doc)
    * [Cheat Sheet of Markdown Syntax](https://www.markdownguide.org/cheat-sheet)
    * [Vim Tutorial – Tutorialspoint](https://www.tutorialspoint.com/vim/index.htm)
    * [鳥哥的 Linux 私房菜 – 第九章、vim 程式編輯器](http://linux.vbird.org/linux_basic/0310vi.php)
    * [Markdown 語法說明](https://markdown.tw/)

---
## Contributors

> TODO:
> * Please replace "YOUR_NAME" and "YOUR_GITHUB_LINK" into yours

* [YOUR_NAME](YOUR_GITHUB_LINK)
* [David Lu](https://github.com/yungshenglu)

---
## License

GNU GENERAL PUBLIC LICENSE Version 3