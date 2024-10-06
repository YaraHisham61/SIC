from calc import *
def get_numbers():
    while True:
        numbers = input("Please enter two numbers separated by a space or enter (return) to return to the previous menu: ").strip()
        if numbers == 'return':
            return None
        try:
            x, y = map(float, numbers.split())
            return x, y
        except:
            print("Error: Please enter exactly two numbers separated by a space.")

def main():
    while True:
        command = input("Please enter the command you want to use (add/sub/mult/div) or enter (stop) if you want to exit: ").strip().lower()
        
        if command == "stop":
            break
        if command not in ["add", "sub", "mult", "div"]:
            print("Error: Please enter a valid command.")
            continue

        numbers = get_numbers()
        if numbers is None:
            continue
        
        x, y = numbers
        result = 0  
        operation = '+'
        match command:
            case "add":
                result = add(x,y)
            case "sub":
                result = sub(x,y)
                operation = '-'
            case "mult":
                result = mult(x,y)
                operation = 'x'
            case "div":
                result = div(x,y)
                operation = '/'
        with open("history.txt",'a') as file:
            file.write("{} {} {} = {} \n".format(x,operation,y,result))
        print("{} {} {} = {} \n".format(x,operation,y,result))

if __name__ == '__main__':
    main()