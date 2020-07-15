import requests

def main():
    res = requests.get('https://jsonplaceholder.typicode.com/todos/1').json()
    print(res)


if __name__ == '__main__':
    main()
