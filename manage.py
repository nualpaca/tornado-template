import sys

def parse_args():
	if sys.argv[1] == "runserver":
		from app import main
		main()

if __name__ == "__main__":
    parse_args()