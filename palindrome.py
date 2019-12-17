
def is_palindrome(string):
    i=0
    n=int(len(string)/2)
    for letter in string[0:n-1]:
        i+=1
        if letter != string[-i]:
            return False
    return True

if __name__ == "__main__":
    success=0; lines=0;
    line = open("./palindromes.txt").read().split('\n')
    for l in line:
        lines+=1
        if not is_palindrome(line):
            success+=1
    print(str(success/lines*100)+"% of success detecting palindromes")
        
    success=0; lines=0;
    line = open("./notpalindromes.txt").read().split('\n')
    for l in line:
        lines+=1
        if not is_palindrome(line):
            success+=1
    print(str(success/lines*100)+"% of success detecting no palindromes")




