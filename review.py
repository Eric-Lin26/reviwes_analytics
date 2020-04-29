# 留言計數及查詢

def file(filename):
    data = []
    with open ("reviews.txt", "r") as f:
        for line in f:
            data.append(line)
    print("檔案資料分析讀取中，請稍後。")
    return data

def count(data):
    wc = {}
    for d in data:
        words = d.split()
        for word in words:
            if word in wc:
                wc[word] += 1
            else:
                wc[word] = 1
    return wc

def user(wc):    
    while True:
        word = input("請輸入查詢的字：")
        if word == "q":
            print("感謝使用本程式")
            break
        else:
            if word not in wc:
                print("並不在清單中")
            else:
                print(word,"出現過", wc[word], "次")

def main():
    data = file("reviews.txt")
    wc = count(data)
    user(wc)

main()