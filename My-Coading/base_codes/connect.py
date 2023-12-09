import subprocess

def check_internet_connection():
    try:
        subprocess.check_output(['ping', '-c', '1', 'google.com'])
        return True
    except subprocess.CalledProcessError:
        return False

print(check_internet_connection())
