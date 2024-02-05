# pySSLVision
Easily create a network socket between the SSL Vision and your VSSS or SSL software.


## Requirements
- protobuf==3.6.1

## Installation
Use the code below to install the package from PyPI:

`pip install pySSLVision`

## A Simple Example
1. In a test folder, save the code below as config.json

```
{
    "network" : {
        "multicast_ip": "224.0.0.1",
        "vision_port": 10002
    }
}
```

2. In the same folder, save the code below as test.py and run it while the referee is running

```
from pySSLVision.VisionComm import SSLVision

v = SSLVision()
v.start()

while True:
    time.sleep(1)
    print(v.frame)

```

## Important Methods and Attributes
Some important methods are:
| Method | Description |
| ------ | ------ |
| SSLVision.assign_vision | Defines a callback function to be called when a new frame is received |
| assign_empty_values | Process vision frame placing the origin at the right edge of the field relative to your defending goal |


Some important attributes are:
| Attribute | Description |
| ------ | ------ |
| SSLVision.frame | Stores the last received frame |
| SSLVision.last_frame | Can be used to store one frame |
## Colaboration Guide
In order to colaborate with this repository, clone this repository:

`git clone https://github.com/project-neon/pySSLVision`

Open directory

`cd pySSLVision`

Then install dependencies

`pip install -r requirements.txt`

Finally, install the package

`python3 setup.py install`


Remember to use the Project Neon guidelines to git:
https://github.com/project-neon/codestyleguide/blob/master/git.md