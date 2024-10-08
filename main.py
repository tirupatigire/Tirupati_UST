import threading

from program1 import check_frequency_of_words
from program2 import check_the_validity_of_password


def main():
    thread1 = threading.Thread(target=check_frequency_of_words, args="which is better python 2 or python 3",)
    thread2 = threading.Thread(target=check_the_validity_of_password, args="asqwr1234@1,aF145#,2w3E*,2We3345")
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()
