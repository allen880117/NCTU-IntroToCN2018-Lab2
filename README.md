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
> Remember install Python and mininet package first.
> ```bash
> # Change the directory into /Network_Topology/src/  
> $ cd /root/Network_Topology/src/
> # Change to the executable mode of topology.py  
> $ [sudo] chmod +x topology.py
> # Run topology.py
> $ [sudo] topology.py
> ```
> * Show the screenshot of using iPerf command in Mininet
    >> ![Screenshot_iPerf](https://github.com/nctucn/lab2-allen880117/blob/master/screenshots/Screenshot_iPerf.png)
---
## Description

### Mininet API in Python

> TODO:
> * Describe the meaning of Mininet API in Python you used in detail
```py
from mininet.net  import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log  import setLogLevel
from mininet.cli  import CLI    
```
* All the module of mininet we import.
```py
class MyOwnSwitchTopo(Topo) :
    def build(self) : 
        self.addSwitch('s1')
        self.addHost('h1')
        self.addLink( h1, s1, bw = 18, delay = '6ms', loss = 2)
```
* "MyOwnSwitchTopo" 
* * is a class which is defined by ourselves and inherits the class "mininet.topo.Topo".
* "def build(self)" 
* * override the function "mininet.topo.Topo.build()" to build my own topo.
* "self.addSwitch('s1')" 
* * add a switch node named 's1' into topo. 
* * Return value is 's1'.
* "self.addHost('h1')" 
* * add a host node named 'h1' into topo. 
* * Return value is 'h1'.
* "self.addLink(node1, node2, bw = 18, delay = '6ms', loss = 2)" 
* * add a link between node1 and node2 in topo with bandwith is 18 mbps, delay is 6ms, and loss rate is 2%.
* All of three "add" functions are class function of "mininet.topo.Topo".
* Actually, the "SingleSwitchTopo" was a pre-defined class in "mininet.topo".
```py
topo = MyOwnSwitchTopo()
``` 
* Create my own topology "topo".
```py
net = Mininet(
    topo = topo, 
    controller = OVSController,
    link = TCLink)
```
* "Mininet" is a class from "mininet.net".
* Create a network of which topology is "topo".
* This network, "net", is managed by a controller, "OVSController"(mininet.node.OVSController).
* This network, "net",uses "TCLink"(mininet.link.TCLink).
```py
net.start()
```
* Start the network, "net".
* This is a class function of "mininet.net.Mininet".
```py
net.stop()
```
* Stop the network, "net".
* Since we have to use CLI mode to do other work, we don't need this function here.
* This is a class function of "mininet.net.Mininet".
```py
net.pingALL()
```
* Test connectivity by trying to have all nodes ping each other.
* This is a class function of "mininet.net.Mininet".
```py
dumpNodeConnections(net.host)
dumpNodeConnections(net.switches)
```
* Dump every hosts' and switches' connections.
* "dumpNodeConnections( nodes )" is a function from "mininet.util", and we can use it to dump the information of connections between nodes.
```py
CLI(net)
```
* Start and run interactive or batch mode CLI with "Mininet network object", here is the network we create, "net".
* This is a function from "mininet.cli"
```py
setLogLevel('info')
```
* Tell mininet to print useful information.
* This function is from "mininet.log".
### iPerf Commands

> TODO:
> * Describe the meaning of iPerf command you used in detail
```bash
$ h4 iperf -s -u -i 1 > ./out/result &
$ h2 iperf -c 10.0.0.4 -u -i 1
```

| parameter | explanation |
| --------- | ------------|
| -s |Run iPerf in server mode. (This will only allow one iperf connection at a time)
| -c **host** |Run iPerf in client mode, connecting to an iPerf server running on host.
| -u |Use UDP.
| -i **time** |Sets the interval time in seconds between periodic bandwidth, jitter, and loss reports. Default is zero, which means no report. 
| \> **file_path** |Dump the result log to the location you assigned.
| & |Linux command, put \"&\" at the end of command line , then it will not execute this line immediately but wait the next command line.
    
>You can translate this two command line like this \: <br>
>> **FIRST** <br>
>> Run iPerf in server mode in host 4. <br> 
>> Use UDP to transist. <br>
>> The time interval of log is 1(s). <br>
>> Save the log at ./out/result . <p></p>
>> **THEN** <br>
>> Run iPerf in client mode in host 2, and connect to host 4 of which ip is 10.0.0.4 . <br>
>> Use UDP to transist. <br>
>> The time interval of log is 1(s).

> * Miniset set the ip of first host in network to 10.0.0.1, and the ip of second host in network is 10.0.0.2, etc. <br> So the ip of h4 is 10.0.0.4 .

### Tasks

> TODO:
> * Describe how you finish this work step-by-step in detail

1. **Environment Setup**
    1. Join this lab on GitHub Classroom by using the link provided in lab2_tasks.pdf
        > [NCTU CN](https://classroom.github.com/a/K8gaizQG)

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

        > the first time we execute the mininet, we will face a problem, that is a service didn't start.
        > ![Screenshot_problem_1](https://github.com/nctucn/lab2-allen880117/blob/master/screenshots/Screenshot_problem_1.png)

        > to solve the problem, just start the service
        > ```bash
        > # Start the service of Open vSwitch
        > $ [sudo] service openvswitch-switch start
        > ```

2. **Example of Mininet**
    1. Run the example code
        > ```bash
        > # Change the directory into /Network_Topology/src/
        > $ cd /root/Network_Topology/src/
        > # Change to the executable mode of example.py
        > $ [sudo] chmod +x example.py 
        > # Run example code (example.py)
        > $ [sudo] ./example.py
        > ```

    2. Check the result after running example code
        > The result will be same as the one provided by the latest version of lab2_tasks.pdf. <br> 
        > ![Screenshot_example](https://github.com/nctucn/lab2-allen880117/blob/master/screenshots/Screenshot_example.png)

    3. The following error may occur when you run example.py or Mininet's program
        > (I forget how I tigger this problem, but I'm sure that I met it when doing task)
        > ```bash
        > # Run the example code (example.py)
        > $ [sudo] ./example.py
        > *** Creating network
        > ...
        > Exception: Error creating interface pair (s1-eth1,s2-eth1): RTNETLINK answers: File exists
        > ```

        > It seems like that we have create the file before, so just clean it up!
        > ```bash
        > $ [sudo] mn -c
        > ```

3. **Topology Generator**
    1. View the topology you should generate
        > * 16309 % 3 = 1, so I should generate the topoplogy of topo1.png.
        > ![topo1](https://github.com/nctucn/lab2-allen880117/blob/master/src/topo/topo1.png)

    2. Generate the topology via Mininet
        > Refer to example.py
        ```py
        '''
        Single switch connected to n hosts.
        '''
        class SingleSwitchTopo(Topo):
            def build(self, n = 2):
                # Add a switch to a topology
                switch = self.addSwitch('s1')
                # Add the host and link to a topology
                for h in range(n):
                    # Add a host to a topology
                    host = self.addHost('h%s' % (h + 1))
                    # Add a bidirectional link to a topology
                    self.addLink(
                        host, 
                        switch, 
                        bw = 10, 
                        delay = '5ms', 
                        loss = 0)
        ```
        > We can modify this class and its function to create the topo
        ```py
        '''
        MyOwnSwitchTopo
        modified it to generate 9 switches and 6 hosts
        and link them as topo1.png
        '''
        class MyOwnSwitchTopo(Topo):
            def build(self):
                # Add 9 switches to a topology
                switch = []
                for num in range(10): #0~9
                    if( num == 0 ):
                        switch.append( 'NULL' )
                    else:
                        switch.append( self.addSwitch('s%s' % num ) )
                
                # Add 6 hosts to a topology
                host = []
                for h in range(7): #0~6
                    if( h == 0 ):
                        host.append( 'NULL' )
                    else:
                        host.append( self.addHost('h%s' % h) )

                # Add links to a topology
                self.addLink( host[1], switch[1], bw = 12, delay = '6ms', loss = 2)
                self.addLink( switch[1], switch[8], bw = 20, delay = '7ms', loss = 15)
                self.addLink( switch[6], host[2], bw = 18, delay = '2ms', loss = 3)
                self.addLink( switch[4], host[5], bw = 14, delay = '5ms', loss = 2)
                self.addLink( switch[8], switch[4], bw = 23, delay = '6ms', loss = 10)
                self.addLink( switch[8], switch[2], bw = 25, delay = '6ms', loss = 14)
                self.addLink( switch[8], switch[6], bw = 30, delay = '1ms', loss = 12)
                self.addLink( switch[2], switch[9], bw = 30, delay = '3ms', loss = 18)
                self.addLink( switch[9], switch[7], bw = 33, delay = '8ms', loss = 10)
                self.addLink( switch[5], host[6], bw = 15, delay = '4ms', loss = 3)
                self.addLink( switch[9], switch[5], bw = 30, delay = '3ms', loss = 20)
                self.addLink( switch[3], switch[9], bw = 35, delay = '2ms', loss = 17)
                self.addLink( switch[7], host[3], bw = 18, delay = '6ms', loss = 6)
                self.addLink( host[4], switch[3], bw = 13, delay = '3ms', loss = 5)
        ```
        > Two list, "switch[]" and "host[]", are the set of switches and hosts. <br>
        > Switch[0] and host[0] is null, just for adjusting the index of switch and host. <br>
        > Use for loop to create a list of 9 switches and a list of 6 hosts. <br>

        |code|explanation|
        |----|-----------|
        |class MyOwnSwitchTopo( Topo ) | a class that inherit the object "Topo" in "mininet.topo".
        |self.addSwitch( 'name' ) | create a switch and add it into topo.
        |self.addHost( 'name' ) | create a host and add it into topo.
        |self.addLink( A, B, bw(Mbps), delay, loss(%) ) | create a link between two devices A and B and configure the parameter of bandwith, delay, and loss rate. 
        > Now modify and add some code, to complete other requirements. <br>
        > for some functions, we need import some module first.
        ```py
        '''
        Remember to import the following module first!
        '''
        from mininet.util import dumpNodeConnections
        from mininet.cli  import CLI
        ```
            
        ```py
        '''
        Create and test a simple network
        '''
        def simpleTest():
            # Create a topology with 6 hosts and 9 swithces //topo1.png
            topo = SingleSwitchTopo()
            # Create and manage a network with a OvS controller and use TCLink
            net = Mininet(
                topo = topo, 
                controller = OVSController,
                link = TCLink)
            # Start a network
            net.start()
            # Test connectivity by trying to have all nodes ping each other
            print("Testing network connectivity")
            net.pingAll()

            # Dump every hosts' and switches' connections
            dumpNodeConnections(net.hosts)
            dumpNodeConnections(net.switches)

            # Add the following code and do NOT use net.stop()
            CLI(net)
            # Stop a network
            # net.stop()
        ```
        > Originally, the function "simpleTest()" in example.py has "net.stop()" in the end of function. <br>
        > However, we can't let the network stop, since we have other work have to do with this network, so delete "net.stop()".

        |code|explanation|
        |----|-----------| 
        |dumpNodeConnections(net.hosts) | dump hosts' connections in the "net" network.
        |dumpNodeConnections(net.switches) | dump switches' connections in the "net" network.
        | CLI(net) | enter in Mininet's CLI mode with "net" network.

4. **Measurement**
    1. Use the iPerf command to measure the topology you built.
        > My own topology is topo1.png
        ```bash
        $ h4 iperf -s -u -i 1 > ./out/result &
        $ h2 iperf -c 10.0.0.4 -u -i 
        ```
    2. The expected result from the topo1.png
        > The following image is the result after running iPerf command, the expected result of packet loss is around 51% to 55%, so the result is same as expected.<br>
        > ![Screenshot_iPerf](https://github.com/nctucn/lab2-allen880117/blob/master/screenshots/Screenshot_iPerf.png)
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
    * [iPerf](https://iperf.fr/iperf-doc.php)
    * [CN18 lab2(Youtube)](https://youtu.be/09HHvY9FSQM)
---
## Contributors

> TODO:
> * Please replace "YOUR_NAME" and "YOUR_GITHUB_LINK" into yours

* [allen880117](https://github.com/allen880117)

---
## License

GNU GENERAL PUBLIC LICENSE Version 3