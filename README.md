## DASL-TAP-RECORD

This is the software for the test-tap interface.

## Get Started

### Prerequisites
This assumes your are using Ubuntu 16.04 LTS
You will need screen, python serial to run this software.

```
sudo apt-get update
sudo apt-get install screen
sudo apt-get install python-serial
sudo apt-get install python-numpy
```

For human-robot interactions, you will need the packages for human-human interactions and naopy and numpy

```
sudo apt-get update
sudo apt-get install python-numpy

```

For Naoqi for python refer to the follow website
* [NAOqi](http://doc.aldebaran.com/2-5/dev/python/install_guide.html) - aldebaran documentation

### Run the software

```
./dasl-tap-record install
dasl-tap-record start # this will start the audio recording and data loggin script
```

to stop 

```
dasl-tap-record stop
and press the center button or CTRL-C
```

or CTRL-C if not sent to the background.
