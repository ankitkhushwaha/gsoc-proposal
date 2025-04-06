

## Downloading the software
- Download SOURCE CODE DISTRIBUTION 


### Installation for Linux

#### Unpacked the tar file

untar the file in `$HOME` directry.
```
tar zxf [tar file]
```

#### Install the packages

```
sudo apt-get -y install libreadline-dev libncurses5-dev ncurses-dev curl \
libcurl4 libcurl4-gnutls-dev xorg-dev make gcc g++ gfortran perl-modules \
libdevel-checklib-perl libfile-which-perl python3-dev python3-pip python3-setuptools \
python3-astropy python3-numpy python3-scipy python3-matplotlib
```

#### Set a virtual python enviorment
```
# I used this dev env for the package installtion
conda activate stringray-dev   
conda install astropy numpy scipy matplotlib pip
```


#### Environment Variables
```
export CC=/usr/bin/gcc
export CXX=/usr/bin/g++
export FC=/usr/bin/gfortran
export PERL=/usr/bin/perl
export PYTHON=/usr/bin/python3
```

```
unset CFLAGS CXXFLAGS FFLAGS LDFLAGS build_alias host_alias
export PATH="/usr/bin:$PATH"
```


#### Configure
```
cd heasoft-6.35.1/BUILD_DIR/
./configure > config.txt 2>&1
```


#### Build

```
make > build.txt 2>&1
```

#### Install

```
make install > install.txt 2>&1
```