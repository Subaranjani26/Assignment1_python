Question:1

string1="Guvi Greeks Private limited"
print(string1.count('a'))
print(string1.count('e'))
print(string1.count('i'))
print(string1.count('o'))
print(string1.count('u'))
count=0
list1=["a","e","i","o","u"]
for char in string1:
    if char in list1:
        count=count+1
print("Total number of vowels:",count)

Question:2

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()

Question:3

str=input("Enter the string:")
vowel_string="aeiou"
print("Input String",str)
for char in str:
    if char in vowel_string:
        str=str.replace(char,"")
print("Output String without vowels:",str)

Question:4

string="Suba Ranjani"
d={}
for i in string:
    d[i]=0
for i in string:
    d[i]=d[i]+1
print(d)
for i in string:
    if (d[i]==1):
        print(i)

Question:5

s=input("Enter a string:")
revstr=(s[::1])
if revstr==s:
    print("Palindrome")
else:
    print("Not Palindrome")

Question:6

string="Suba ranjani"
sub_string="Bharathiraja"

print(string.find(sub_string))
if(string.find(sub_string)== -1):
    print("Not Found")
else:
    print("Found")

Question:7

string=input("Enter a string:")
count={}
for letter in string:
    if letter in count:
        count[letter]+=1
    else:
        count[letter]=1

print("Count Frequency is ..")
for key,value in count.items():
    print(f"{key} occurs {value}times")

Question:8

str1=input("Enter String1:")
str2=input("Enter String2:")
if len(str1)!=len(str2):
    print("NOT ANAGRAM")
else:
    if sorted(str1)==sorted(str2):
        print("Strings are Anagram")
    else:
        print("trings are Not Anagram")

Question:9

string1="Suba is a teacher"
words=string1.split()
count=len(words)
print("Total Words:",count)


