"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count


def max_workers():    
    return cpu_count()


command = "/var/django_apps/v_envs/vetnow_venv/bin/gunicorn"
pythonpath = "/var/django_apps/vetnow/vetnow/"
bind = "0.0.0.0:8001"
workers = max_workers()
