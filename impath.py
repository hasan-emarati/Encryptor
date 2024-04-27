# created from SHe
# Import modules
import os
import sys
import argparse

# Go to current dir
os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    from main import main
    from Tools.Code import Encryptor
    

except ImportError as err:
    main("Failed import some modules", err)
    sys.exit(1)


if __name__ == "__main__":
    MyMain = main()
    MyMain.Selector()
    sys.exit(1)

