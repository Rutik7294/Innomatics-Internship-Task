#re.findall(),re.finditer()

import re
vowel = "aeiou"
consonent = "qwrtypsdfghjklzxcvbnm"
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (consonent, vowel, consonent), input(), flags = re.I)
print('\n'.join(m or ['-1']))
