import threading
import time


displayNumberInterval = 4



class NumberMultiplierThread(threading.Thread):
    def __init__(self):
        super(NumberMultiplierThread, self).__init__()
        
        self.initialCounter = 0
        self.multiplyInterval = 4
        self.initialNumber = 1.05
        self.number = self.initialNumber

    def run(self):
        while True:
            self.initialCounter += 1
            self.number *= self.number
            if self.number >= 1e308:
                print("It took: ", self.initialCounter, " multiplications to get to inf.")
                break

            print("This is the number: ", self.number)

            time.sleep(self.multiplyInterval)

if __name__ == "__main__":
    multiplier_thread = NumberMultiplierThread()
    multiplier_thread.start()

    try:
        while True:
            time.sleep(displayNumberInterval)

    except KeyboardInterrupt:
        print("Exit started ...\nPress again ...")

    finally:
        multiplier_thread.join()
