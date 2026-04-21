import docker


def main():
    client = docker.from_env()
    client.containers.run("ubuntu:latest", "echo hello world")


if __name__ == '__main__':
    main()
