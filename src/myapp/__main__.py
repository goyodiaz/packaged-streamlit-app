import sys

import streamlit.__main__

from myapp import streamlit_app


def main():
    sys.argv.extend(["run", streamlit_app.__file__])
    streamlit.__main__.main(prog_name="streamlit")


if __name__ == "__main__":
    main()
