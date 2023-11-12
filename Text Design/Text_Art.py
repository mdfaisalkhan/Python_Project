from pyfiglet import figlet_format
from pyperclip import copy

select_banner=input("Type your Banner Text ")
text_banner = figlet_format(select_banner)

print(text_banner)
p