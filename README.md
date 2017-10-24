# OpenCV-Python on Raspberry-Pi Education

## Proxy configuration for various package managers
### APT

open the file `/etc/apt/apt.conf` and edit.
`
$ vi /etc/apt/apt.conf 
`
```
# /etc/apt/apt.conf
Acquire::http::proxy "http://username:password@123.45.6.7:8080"
Acquire::https::proxy "123.45.6.7:8080"
```

### GIT
```
$ git config --global http.proxy "123.45.6.7:8080”
$ git config --global https.proxy ":8080"
```
you can check the result in the file `~/.gitconig	`

```
$ cat ~/.gitconfig 
```

### PIP
```
$ pip install --proxy="123.45.6.7:8080" --index-url=http://pypi.python.org/simple/ --trusted-host pypi.python.org packagename 
```
or 
```
$ pip install --proxy http://123.45.6.7:8080 packagename 
```

### wget
open the file `~/.wgetrc` and edit.
    
```
$ vi ~/.wgetrc 
```

```
use_proxy=yes
http_proxy=168.219.61.252:8080
https_proxy=168.219.61.252:8080
```
or
```
$ wget "url" -e use_proxy=yes -e http_proxy=123.45.6.7:8080 
```


## Setup OpenCV on R-Pi

```
sudo apt-get update
```

```
sudo apt install libxine2
sudo apt install libqtgui4
sudo apt install libjasper1
sudo apt install libqt4-test
sudo apt install libqt4-opengl
```
```
sudo dpkg -i OpenCV*.deb
```
```
pkg-config —modversion opencv
```
