import sys

def parse_args():
	if sys.argv[1] == "runserver":
		import app

if __name__ == "__main__":
    parse_args()