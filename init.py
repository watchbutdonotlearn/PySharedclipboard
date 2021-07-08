import subprocess
from multiprocessing import Process

def a():
    subprocess.run("python server.py", shell=True)
def b():
    subprocess.run("python client.py", shell=True)

if __name__ == '__main__':
  p1 = Process(target=a)
  p1.start()
  p2 = Process(target=b)
  p2.start()
  p1.join()
  p2.join()