# This code should run automatically via site.py when the python interpreter starts.
import pth_execution_checker
pth_execution_checker.pth_executed = True

print("Yay! This is a message called from a .pth file :)")

try:
    import socket
    pth_execution_checker.import_socket_possible = True
    pth_execution_checker.import_socket_exception = None
except Exception as e:
    pth_execution_checker.import_socket_possible = True
    pth_execution_checker.import_socket_exception = e
