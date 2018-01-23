import argparse

parser = argparse.ArgumentParser(description="Runs code for a Register Machine.")
parser.add_argument("file", type=file)
parser.add_argument("-v", "--verbose", action="store_true", help="Show state after execution of each instruction")
parser.add_argument("-q", "--quiet", action="store_true", help="Print nothing except final output")
parser.add_argument("-s", "--step", action="store_true", help="Step through execution of each instruction manually")
parser.add_argument("-r", "--return-registers", action="store_true", help="Return all registers as output")
parser.add_argument("registers", nargs="*", type=int, default=[0])

def zero(n, regs=[], ln=0):
    if n > len(regs):
        regs.append(0)
    elif n > 0: # indexing starts at 1
        regs[n - 1] = 0
    else:
        raise Exception("Indexing error")
    return regs, ln + 1

def successor(n, regs=[], ln=0):
    if n > len(regs):
        regs.append(1)
    elif n > 0: # indexing starts at 1
        regs[n - 1] += 1
    else:
        raise Exception("Indexing error")
    return regs, ln + 1

def transfer(m, n, regs=[], ln=0):
    regs[n - 1] = regs[m - 1]
    return regs, ln + 1

def jump(m, n, q, regs=[], ln=0):
    if regs[m-1] == regs[n-1]:
        return regs, q - 1
    else:
        return regs, ln + 1

def parse_op_arg(arg):
    if arg == "_":
        return float('inf')
    else:
        return int(arg)

operations = {
    "Z": zero,
    "S": successor,
    "T": transfer,
    "J": jump
}

if __name__ == "__main__":
    args = parser.parse_args()
    if args.verbose:
        print args

    lines = args.file.readlines()
    args.file.close()

    regs = args.registers
    ln = 0
    while True:
        instr = lines[ln].split()
        op, op_args = instr[0], map(parse_op_arg, instr[1:])
        regs, next_ln =  operations[op](*op_args, regs=regs, ln=ln)
        if args.verbose and not args.quiet:
            print "Line {}: {}\nRegisters: {}\nNext: {}".format(ln + 1, lines[ln], regs, next_ln + 1)
        if next_ln + 1 > len(lines):
            if not args.quiet:
                print "Halting. Output:"
            if args.return_registers:
                print " ".join(map(str, regs))
            else:
                print regs[0]
            break
        if args.step:
            if raw_input() == "exit":
                break
        ln = next_ln
