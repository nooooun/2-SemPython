
"""with open("number.txt", "r") as file:
    mas = file.read()
    mas = [int(i) for i in mas.split(",")]

with open("step.txt", "r") as file:
    step = int(file.read())

count = 0
def fib(a, b, count):
    temp = mas[count] + mas[count + 1]
    mas.append(temp)
    if(count != step):
        count += 1
        fib(mas, step, count)
    else:
        print("[", mas, "]")
        pass

fib(mas, step, count)"""

def main():
    try:
        with open("number.txt", "r") as file:
            list = file.read()
            list = [int(i) for i in list.split(",")]
        with open("step.txt", "r") as file:
            step = int(file.read())
    except FileNotFoundError as e:
        print("Error: file not found - " + str(e.filename))

    count = 0
    def fib(list, step, count):
        temp = list[count] + list[count + 1]
        list.append(temp)
        if(count < step):
            count += 1
            return fib(list, step, count)
        else:
            return list

    result = fib(list, step, count)

    try:
        output_str = ', '.join(str(i) for i in result)
        with open("result.txt", "w") as file:
            file.write(output_str)
    except FileNotFoundError as e:
        print("Error: file not found - " + str(e.filename))

if __name__ == '__main__':
    main()