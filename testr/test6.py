
import string

words = list(string.ascii_lowercase) #out-> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(f'パスワード総数：{26**6}')
#約31億パターンあるためリストに入れるとメモリに乗らないのでリスト化はしない。
for word_1 in words:
   for word_2 in words:
       for word_3 in words:
           for word_4 in words:
               print(word_1+word_2+word_3+word_4+"@gmail.com")
                                                       