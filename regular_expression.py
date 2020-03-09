import re

tex = "Привидение прошуршало и исчезло в углу."

m = re.findall(".ло", tex)
print(m)
