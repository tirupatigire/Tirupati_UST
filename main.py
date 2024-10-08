import threading

from program1 import check_frequency_of_words
from program2 import check_the_validity_of_password


def main():
    thread1 = threading.Thread(target=check_frequency_of_words,)
    thread2 = threading.Thread(target=check_the_validity_of_password,)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()
