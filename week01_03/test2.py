#regex shits
import re

txt = "This is some txt for regex text Bitch!!   $zzz"
matches = re.search("[a-zA-Z]+", txt)
matches1 = re.search("[/w]", txt)


print(matches)