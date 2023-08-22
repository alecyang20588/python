
# For documentation of the webbrowser module,
# see http://docs.python.org/library/webbrowser.html


import webbrowser

new = 2 # open in a new tab, if possible

# open a public URL, in this case, the webbrowser docs

url = "http://docs.python.org/library/webbrowser.html"
webbrowser.open(url,new=new)

# open an HTML file on my own (Windows) computer

url = "file://X:/MiscDev/language_links.html"
webbrowser.open(url,new=new)