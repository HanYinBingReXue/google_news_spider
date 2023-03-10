from utils import word_count


total_text = ""
with open("output.text", "r") as f:
    for line in f.readlines():
        total_text += line.strip()
f.close()
# print(total_text)

wordcount = word_count(total_text)
# print(wordcount)
# 字典按键排序
print(sorted(wordcount.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))
