#! /usr/bin/env python3

from queue import Queue
import threading

class getter(threading.Thread):
    """
    Пример класса потока, который записывает фразы в указанный файл.

    """

    def __init__(self, queue, thefile):
        """Инициализация потока"""
        threading.Thread.__init__(self)
        self.queue = queue
        self.thefile = thefile

    def run(self):
        """Запуск потока"""
        while True:

            # получить фразу из очереди
            fra = self.queue.get()

            # запустить
            self.printer(fra, self.thefile)

            # Отправляем сигнал о том, что задача завершена
            self.queue.task_done()


    def printer(self, fraza, thefile):
        """Записываем в файл"""
        thefile.write(fraza + "\n")


def main():
    """
    Запускаем программу
    """
    print("Begin")

    queue = Queue()

    fraz = [
        "Первая фраза",
        "Вторая фраза",
        "Третья фраза",
        "Четвертая фраза",
        "Пятая фраза",
        "Шестая фраза",
    ]

    thefile = open("outputter.txt", 'a')

    for i in range(5):
        t = getter(queue, thefile)
        t.setDaemon(True)
        t.start()

    for f in fraz:
        queue.put(f)

    # ждем пока очередь разберется
    queue.join()

    # закрываем файл
    thefile.close()

    print("End")


if __name__ == "__main__":
    try:
        main()
    except:
        raise
