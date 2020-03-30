# 留言分析

data = []
count = 0

x = 0
y = 0
with open ("reviews.txt", "r") as f:
    for line in f:
        count += 1
        data.append(line)
        if count % 10000 == 0:
            print(count)

print("檔案讀取完了，總共有", count, "筆資料。")

sum_len = 0
for avg in data:
    sum_len += len(avg)
    
print("留言平均長度為：", sum_len / len(data))
