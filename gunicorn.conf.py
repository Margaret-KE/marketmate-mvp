# Gunicorn Configuration for MarketMate

# Listen on all interfaces on port 8000
bind = '0.0.0.0:8000'

# Number of worker processes (adjust based on server resources)
workers = 4

# Logging settings
accesslog = '-'  # Log to stdout
errorlog = '-'   # Log to stdout

# Set timeout to 60 seconds
timeout = 60

# Maximum number of requests a worker will process before restarting
max_requests = 1000

# Maximum number of requests a worker will process before graceful restart
max_requests_jitter = 100

# Set the worker class to 'gevent' for async handling
worker_class = 'gevent'
