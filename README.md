usage: regm.py [-h] [-v] [-q] [-s] [-r] file [registers [registers ...]]

Runs code for a Register Machine.

positional arguments:
  file
  registers

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Show state after execution of each instruction
  -q, --quiet           Print nothing except final output
  -s, --step            Step through execution of each instruction manually
  -r, --return-registers
                        Return all registers as output
