'''
Gunicorn Configuration Variables
'''

bind = "localhost:8000"
workers = 3 # The number of worker processes for handling requests.

backlog = 64 # The maximum number of pending connections.

# The maximum number of requests a worker will process before restarting.
# This is a simple method to help limit the damage of memory leaks.
max_requests = 1024
# The jitter causes the restart per worker to be randomized by randint(0, max_requests_jitter).
# This is intended to stagger worker restarts to avoid all workers restarting at the same time.
max_requests_jitter = 37

graceful_timeout = 20
timeout = 30

# error log
# errorlog = 'logging/ErrLogFile'
