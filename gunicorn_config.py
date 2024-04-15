# gunicorn_config.py

bind = '0.0.0.0:5000'  # Update the host and port if needed
workers = 4
daemon = True

errorlog = 'gunicorn_error.log'  # Specify the path to the log file

raw_env = ['FLASK_APP=app.py', 'FLASK_ENV=production']
