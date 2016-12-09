#Affectiva based student learning analysis
This repo consists of files for Affectiva based student learning analysis.
To install affectiva and to run the code samples. Follow the following directions.
This repo makes use of the Affectiva SDK and it's video samples and the running instruction is similar.
Please follow the following instructions which have been modified from the affectiva instructions in order
to build this repo.

- Ubuntu: [![Build Status](https://travis-ci.org/Affectiva/cpp-sdk-samples.svg?branch=master)](https://travis-ci.org/Affectiva/cpp-sdk-samples)

Dependencies
------------

*Windows*
- Affdex SDK 3.1 (64 bit)
- Visual Studio 2013 or higher

*Linux*
- Ubuntu 14.04 or CentOS 7
- Affdex SDK 3.1
- CMake 2.8 or higher
- GCC 4.8

*Additional dependencies*

- OpenCV 2.4
- Boost 1.59

Installation
------------

- Download Affdex SDK [from here](http://developer.affectiva.com/downloads)

*Windows*
- Install the SDK using MSI installer.
- The additional dependencies get installed automatically by NuGet.

*Ubuntu*

```bashrc
sudo apt-get install build-essential libopencv-dev libboost1.55-all-dev cmake
wget https://download.affectiva.com/linux/affdex-cpp-sdk-3.1-396-linux-64bit.tar.gz
mkdir $HOME/affdex-sdk
tar -xzvf affdex-cpp-sdk-3.1-396-linux-64bit.tar.gz -C $HOME/affdex-sdk
export AFFDEX_DATA_DIR=$HOME/affdex-sdk/data
git clone https://github.com/gitaalva/samplerepo.git $HOME/
mkdir $HOME/build
cd $HOME/build
cmake -DOpenCV_DIR=/usr/ -DBOOST_ROOT=/usr/ -DAFFDEX_DIR=$HOME/affdex-sdk $HOME/samplerepo
make
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/affdex-sdk/lib
```


OpenCV-webcam-demo (c++)
------------------

Project for demoing the [FrameDetector class](http://developer.affectiva.com/v3_1/windows/analyze-frames/). It grabs frames from the camera, analyzes them and displays the results on screen.

The following command line arguments can be used to run it:

    -h [ --help ]                        Display this help message.
    -d [ --data ] arg (=data)            Path to the data folder
    -r [ --resolution ] arg (=640 480)   Resolution in pixels (2-values): width
                                         height
    --pfps arg (=30)                     Processing framerate.
    --cfps arg (=30)                     Camera capture framerate.
    --bufferLen arg (=30)                process buffer size.
    --cid arg (=0)                       Camera ID.
    --faceMode arg (=0)                  Face detector mode (large faces vs small
                                        faces).
    --numFaces arg (=1)                  Number of faces to be tracked.
    --draw arg (=1)                      Draw metrics on screen.

Video-demo (c++)
----------

Project for demoing the Windows SDK [VideoDetector class](http://developer.affectiva.com/v3_1/windows/analyze-video/) and [PhotoDetector class](http://developer.affectiva.com/v3_1/windows/analyze-photo/). It processs video or image files, displays the emotion metrics and exports the results in a csv file.

The following command line arguments can be used to run it:

    -h [ --help ]                        Display this help message.
    -d [ --data ] arg (=data)            Path to the data folder
    -i [ --input ] arg                   Video or photo file to process.
    --pfps arg (=30)                     Processing framerate.
    --draw arg (=1)                      Draw video on screen.
    --faceMode arg (=1)                  Face detector mode (large faces vs small
                                         faces).
    --numFaces arg (=1)                  Number of faces to be tracked.
    --loop arg (=0)                      Loop over the video being processed.


For an example of how to use Affdex in a C# application .. please refer to [AffdexMe](https://github.com/affectiva/affdexme-win)


Running ipynb files:

Dependency:

python 2.7
anaconda
scikit-learn
jupyter notebook
ggplot

Reference Link:

https://github.com/Affectiva/cpp-sdk-samples


