from konlpy.tag import Komoran


text = "액션이 어떻게 되는지 아세요? 무한! 무~야~호"

filter = ['~', '!', '@', '*','%', '^', '&', '?']

for i in filter:
    text = text.replace(i, '')      #액션이 어떻게 되는지 아세요 무한 무야호

text_token = text.split()
print(text_token)                   #['액션이', '어떻게', '되는지', '아세요', '무한', '무야호']



komoran = Komoran()

result = komoran.morphs(text)
print(result)

import platform
print(platform.architecture())

