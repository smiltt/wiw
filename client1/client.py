import net
import threading

def main():
    listen_thread = threading.Thread(net.listen())


main()