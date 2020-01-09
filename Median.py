def median(data):
    data.sort()
    if len(data) % 2 == 0:
        first = data[len(data)//2 - 1]
        second = data[len(data)//2]
        return (first + second)/2
    else:
        return data[len(data) // 2]

if __name__ == '__main__':
    print(median([3, 6, 20, 99, 10, 15]))