from datetime import datetime
import socket, sys, argparse, threading, time
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--IP", help="Target IP", required=True)
    parser.add_argument("--portMin", help="Min port", required=True, type=int)
    parser.add_argument("--portMax", help="Max port", required=True, type=int)
    parser.add_argument("-t", "--threads", help="Number of threads (Default 10)", default=10, type=int)
    args = parser.parse_args()
    return args

def banner(IP, portMax, portMin, threads):
    print("*************************************************\n")
    print("[*] Scaning...:\n")
    print("\tIp: {}".format(IP))
    print('\tPorts: {}-{}'.format(portMin,portMax))
    print('\tThreads: {}'.format(threads))
    print('\tDate: ' + str(datetime.now()),"\n")
    print("*************************************************")
    print("Open Ports:")
    time.sleep(1)


def do_threads(IP, ports, num_threads):
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=scan, args=(IP, ports, i+1, num_threads))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

def scan(IP, ports, threads, total_threads):
    for port in range(threads-1, ports, total_threads):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((IP, port))
        if result == 0:
            print("\tThe port {} is open".format(port))
        s.close()




def main():
    args = get_arguments()
    IP = args.IP
    ports = args.portMax - args.portMin
    num_threads = args.threads
    banner(IP, args.portMax, args.portMin, num_threads)
    do_threads(IP, ports, num_threads)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting of program")
        sys.exit(1)
