from task_3.sha1 import sha1

if __name__ == '__main__':
    while True:
        message = input("Enter text message: ")
        hashed_message = sha1(message)
        print(f"Hashed message: {hashed_message}")
