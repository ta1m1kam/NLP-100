'''
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
'''
# -*- coding: utf-8 -*-

sentence = "パタトクカシーー"
result = sentence[::2]
print(result)

# ついでにタクシーも取り出す
result = sentence[1::2]
print(result)
