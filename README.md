#BrowserPlus

##Description
BrowserPlus is an extension of the mechanize Browser and utilises lxml to
provide simple methods to select elements from the current page.

##Dependencies
BrowserPlus depends on the following packages:

* mechanize
* lxml
* cssselect

You can install this by executing:

```bash
sudo pip install mechanize lxml cssselect
```

##Setting up
To install browserplus, you can simply download a copy of the browserplus.py
file and put it in the same directory as your python program.

Or you can clone the entire directory using:

```bash
git clone https://github.com/vinceau/browserplus
```

Once you have a copy of browserplus, import the package using:
```python
from browserplus import BrowserPlus
```

And create an instance of the BrowserPlus using:
```python
b = BrowserPlus()
```
##Usage
###Opening a web page
```python
b.open('https://google.com')
```
