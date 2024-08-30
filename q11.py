# 11	Take a sample text file and find the most commonly occurring word.
# Also, find the frequencies of words in the text file.

file = open("sample.txt", "r")
data = file.read().replace("\n", " ").replace(",", " ").replace(".", "").split()
freq = {x: data.count(x) for x in data}
maxn = [x for x, y in freq.items() if y == max(freq.values())]
print(
    f"most commonly occuring word(s)=>{maxn}",
    "frequencies of words in file are=>\nWord\tOccorrences",
    sep="\n",
)
n = [print(x + "\t", y) for x, y in freq.items()]
