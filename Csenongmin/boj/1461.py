def main():
    books = input("Enter the number of books: ")
    maximum = input("Enter the maximum: ")
    upper=[]
    lower=[]
    for i in range(books):
        locate = input("Enter the {}번째 book's location: ".format(i+1))
        if locate >= 0:
            upper.append(locate)
        else: 
            lower.append(locate)


def findWay(upper, lower, maximum):
    newUpper = upper[:].sort()
    newLower = lower[:].sort()
    for i in newUpper:

