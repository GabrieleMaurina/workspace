import paramiko.client
import sys


def test(user, password, host='localhost'):
    client = paramiko.client.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, username=user, password=password)
    except:
        valid = False
    else:
        valid = True
    finally:
        client.close()
    return valid


def main():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print('Usage: python ssh_password_test.py <user> <password> <host>?')
        sys.exit(1)
    user = sys.argv[1]
    password = sys.argv[2]
    if len(sys.argv) == 4:
        host = sys.argv[3]
    else:
        host = 'localhost'
    print(test(user, password, host))


if __name__ == '__main__':
    main()
