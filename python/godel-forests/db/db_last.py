from db import DB

def main():
    f = DB('fine.db', cache_size=0)
    print(f.size-1, f.get())

if __name__ == '__main__':
    main()