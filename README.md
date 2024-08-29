<h1>MARS ROVER</h1>

> **CODE CONTROLLING A 1:4 SCALE OF A MARS ROVER WITH PYTHON AND ARDUINO**

⚠ **CODE IS STILL UNDER HEAVY DEVELOPMENT**

<h3>How to use</h3><hr>

> **Clone the Github Repository**
```
git clone https://github.com/Coolstormaction/rover
```

```
> cam
> github
> gui
> mount
> arduino
> test
.gitignore 
README.md
```

<h3>Components</h3><hr>

> `cam` **contains code for camera**<br/>
> `arduino` **is under development and will contain arduino** <br/>
> `github` **contains code cloned from GitHub** <br/>
> `gui` **contains Joystick and Robotic Arm Control GUI** <br/>
> `mount` **contains selection mechanism and pre-defined data**
> `test` **contain unit-tests and other new detection algorithms**


<h3>Usage</h3><hr/>
<h4>GUI</h4><hr/>

> **Clone the Github Repository**
```
git clone https://github.com/Coolstormaction/rover
```


```
> gui
   > coco.names
   > main.py
   > Makefile
   > yolov3.cfg
   > yolov3.weights
```

**RUN `make` after heading into the GUI directory** <br/>
🔴 **MUST HAVE MAKE/CMAKE INSTALLED!**

<h4>CAMERA/OBJECT DETECTION</h4><hr/>

**AS THE CODE IS STILL UNDER DEVELOPMENT, THE OBJECT DETECTION WILL NOT CONTAIN ARDUINO CODE AND WILL ONLY BE A DEMO OF THE ALGORITHMS WE USE** 

<h5>ALGORITHM #1</h5><hr/>

**FOR EXISTING VIDEO**

> **Clone the Github Repository**
```
git clone https://github.com/Coolstormaction/rover
```

```
> cam 
    > yolov5
    > main.py
    > your_video.mp4
```

**HEADING INTO THE CAMERA DIRECTORY PUT YOUR VIDEO FILE IN IT AND THEN RUN THIS COMMAND**

```
cd yolov5
python detect.py --weights yolov5x.pt --source <PASTE DIRECTORY PATH HERE> --view-img
```

**FOR USING WEBCAM**<br/>

> **Clone the Github Repository**
```
git clone https://github.com/Coolstormaction/rover
```

```
> cam 
    > yolov5
    > main.py
    > your_video.mp4
```

**HEAD INTO THE `camera/yolov5` DIRECTORY IN YOUR SHELL AND RUN THIS COMMAND**

```
python detect.py --weights yolov5x.pt --source 0
```

<h5>ALGORITHM #1</h5><hr/>

**THIS WILL NOT WORK ON EXISTING VIDEO**

> **Clone the Github Repository**
```
git clone https://github.com/Coolstormaction/rover
```

```
> test 
    > deploy.protoxt
    > main.py
    > Makefile 
    > mobilenet_iter_73000.caffemodel
```

**HEAD INTO THE TEST DIRECTORY AND RUN MAKE**<br/>
**⚠ MUST HAVE MAKE/CMAKE INSTALLED**

<h4>JOYSTICK AND ROBOTIC ARM</h4><hr/>

> **Clone the Github Repository**
```
git clone https://github.com/Coolstormaction/rover
```

```
> gui
    > coco.names
    > main.py
    > Makefile
    > yolov3.cfg
    > yolov3.weights
```

**HEAD INTO THE GUI DIRECTORY IN YOUR SHELL AND RUN `make`**
**⚠ MUST HAVE MAKE/CMAKE INSTALLED**

> **CONTROLLING** <br/>

1. **WASD TO MOVE THE JOYSTICK** <br/>
2. **CLICK ON THE BUTTONS (GRAB/RELEASE) TO CONTROL THE ROBOTIC ARM**

<h1>Conclusion</h1>

**THIS CODE IS STILL UNDER HEAVY DEVELOPMENT AND DOES CONTAIN THE ACTUAL ARDUINO CODE TO COMMUNICATE WITH ACTUAL PHYSICAL HARDWARE AND ON LATER RELEASES IT WILL COMMUNICATE WITH A ESP32-CAMERA MODULE AND OBJECT DETECTION WITH THAT SO AGAIN THIS IS JUST A DEMO**

<h2>CREDITS</h2>

> **OBJECT DETECTION ALGORITHMS** <br>
1. **YOLO v5** <br/>
2. **MobileNet SSD** <br/>