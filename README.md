# Project Euler solutions

Python solutions to [Project Euler](https://projecteuler.net/) problems 1–54
and 67. Each numbered directory contains `sol.py` and, where needed, an
`input` file. The `test/` directory preserves three additional solution copies
from the original repository; these are not an automated test suite.

Run a solution from its directory so it can find any input file:

```sh
cd 0011
python3 sol.py
```

Most solutions use only Python's standard library. Problems 17, 19, and 50
also require `inflect`, `python-dateutil`, and `numpy`, respectively. Install
them in a virtual environment if you want to run those solutions:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install inflect python-dateutil numpy
```
