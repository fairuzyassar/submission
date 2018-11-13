result = []
def permutation(data, size):
    if size == 1 :
        result.append(data)
        print(data) 

    for x in range(size):
        permutation(data, size-1)

        if size%2 == 1:
            temp = data[0]
            data[0] = data[size-1]
            data[size-1] = temp 

        else :
            temp = data[x]
            data[x] = data[size-1]
            data[size-1] = temp

def main(number_of_question):
    data = list(range(1, number_of_question+1))
    permutation(data, len(data))

N = input("Number of question ? \n")
if isinstance(N, int):
    main(N)
print(len(result))