
<br/>
<br/>
<img src="https://dewey.tailorbrands.com/production/brand_version_mockup_image/818/5112570818_02c498e2-a7fb-423e-8f95-82e7be54f2c3.png?cb=1619086571" algn="center" width="800" height="110"/>

<br/>
<br/>

## Phase-1: Virtual Network using mininet, MPTCP and MPQUIC Setups

<p>
We designed a virtual network suing a python script with the help of mininet library. It has two hosts connected through a router
</p>

<br/>

## Network Topology
```
Hosts: client, server
Router: router
Interfaces: client to router 1, client to router 2, router to server
```
<img src="https://i.ibb.co/jf7Z0rD/img.png"/>

<br/>

## Phase-2: Video Streaming based on MP-TCP and MP-QUIC

```
Innovation: It allows you to stream your webcam video from one system to the other.You can separately try out MP-TCP or MP-QUIC while using this code. Please check the requirement below for running MP-TCP or MP-QUIC.
```
<br/>

## Requirements:
### MP-TCP
- MP-TCP Kernel (Not supported on all OS):
For Linux based OS, please refer to the following [link](https://multipath-tcp.org/pmwiki.php/Users/AptRepository/ "link") for installing MP-TCP protocol on your kernel.

- Python (Python 3.5 recommended)

- Python libraries - **numpy** **opencv-python**
```
python3 -m pip install numpy, opencv-python
```

<br/>

### MP-QUIC
- GO Language
- [quic](https://github.com/lucas-clemente/quic-go "quic Library")
- [mp-quic](https://github.com/qdeconinck/mp-quic "mpquic Library")
- GOCV - [link](https://gocv.io/ "link") - Refer to the installation instructions for GoCV

<br/>

## Installation
- Clone this repository in your preferred directory

```
git clone https://github.com/prat-bphc52/VideoStreaming-MPTCP-MPQUIC
```
- Or you can also download the source code as a zip file

<br/>

## Execution
### MP-TCP
Start the server on the Video Streaming Source Host

``` 
python3 server_mptcp.py localhost -p <port_number>
```

Start the client on the target machine
```
python3 client_mptcp.py <source_machine_IPv4_Addres> -p <port_number>
```
<br/>

### MP-QUIC
Build and execute server on one host
```
go build server-mpquic.go
./server-mpquic
```
Specify the server's host name in client-mpquic.go
Build and execute client on the other host
```
go build client-mpquic.go
./client-mpquic
```
<br/>

### Team Members
- ### Sukrit (2018A7PS0205H)
- ### Karthik Shetty (2018A7PS0141H)
- ### Thakkar Preet Girish (2018A7PS0313H)
- ### Koustubh Sharma (2018A7PS0114H)

<br/>

