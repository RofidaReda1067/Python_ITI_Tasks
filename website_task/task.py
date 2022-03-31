import random
import webbrowser

lst = ["https://www.udemy.com/",
       "https://www.python.org/",
       "https://www.redhat.com/en",
       "https://www.microsoft.com/en-eg",
       "https://www.google.com"]
opt = random.choice(lst)
webbrowser.open(opt, new=2)