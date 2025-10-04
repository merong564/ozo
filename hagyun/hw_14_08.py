#8
import re
pattern = '[ \w]*Python[ \w]*[.]'
# pattern2 = '.*Python.*\.'
text = "I love Python. Java is also popular. Python is great for AI."
finding = re.findall(pattern, text)
print(finding)