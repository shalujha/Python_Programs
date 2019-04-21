# list and string slicing
s	=	"This	is	introduction	to	python	for	web	development"
# obtain each word for string s
for i in range(len(s)):
    print(s[i])
for c in s:
    print(c)
l=list(s)   # conversion into list 
for c in l: # list slicing
    print(c)
