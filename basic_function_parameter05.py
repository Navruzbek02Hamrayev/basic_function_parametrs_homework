# Create a function named count_vowels that takes a string as a parameter.
def count_vowels(string):
# Inside the function, count the number of vowels (a, e, i, o, u, A, E, I, O, U) in the given string.
    s=0
    l=[]
    while s<len(string):
        if string[s]=='a' or string[s]=='A' or string[s]=='e' or string[s]=='E' or string[s]=='i' or string[s]=='I' or string[s]=='o' or string[s]=='O' or string[s]=='u' or string[s]=='U' :
            l.append(string[s])
        s+=1
# Return the count of vowels.
    return l,len(l)
print(count_vowels("Hello, world!"))