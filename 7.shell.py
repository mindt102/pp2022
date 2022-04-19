import subprocess
import re
PROMPT = "$ "
REGEX_STR = {
    "out" : "^(.*[^<>|])\s*>\s*\"?([^<>|][\w.]*)\"?$",
    "append" : "^(.*[^<>|])\s*>>\s*\"?([^<>|][\w.]*)\"?$",
    "in" : "^(.*[^<>|])\s*<\s*\"?([^<>|][\w.]*)\"?$",
    "pipe" : "^(.*?[^<>|])\s*?\|\s*?([^<>|].*?)$",
    "exit" : "^exit($|\s*.*$)",
}

# Run a command and handle error if the command is not found
def run_subprocess(cmd, stdout=None, stdin=None):
    try:
        proc = subprocess.Popen(cmd.split(), stdout=stdout, stdin=stdin)
        proc.wait()
        return proc
    except FileNotFoundError:
        print(f"{cmd[0]}: command not found")
        return True

# Redirect the stdout to write to a file
def redirect_out(m, stdout, stdin):
    cmd = m.group(1)
    outfile = m.group(2)
    with open(outfile, "w") as f:
        return run_subprocess(cmd, stdout=f, stdin=stdin)

# Redirect the stdout to append to a file
def redirect_append(m, stdout, stdin):
    cmd = m.group(1)
    outfile = m.group(2)
    with open(outfile, "a") as f:
        return run_subprocess(cmd, stdout=f, stdin=stdin)

# Redirect the stdin to read from a file
def redirect_in(m, stdout, stdin):
    cmd = m.group(1)
    outfile = m.group(2)
    try:
        with open(outfile, "r") as f:
            return run_subprocess(cmd, stdin=f, stdout=stdout)
    except FileNotFoundError:
        print(f"No such file or directory: '{outfile}'")

# 
def pipe(m, stdout, stdin):
    cmd = m.group(1)
    next_cmd = m.group(2)

    proc = run(cmd, stdout=subprocess.PIPE, stdin=stdin)
    run(next_cmd, stdin=proc.stdout)
    proc.stdout.close()
    return proc
 
regex_dict = {
    REGEX_STR["pipe"]: pipe,
    REGEX_STR["out"]: redirect_out,
    REGEX_STR["append"]: redirect_append,
    REGEX_STR["in"]: redirect_in,
}

# Check for exit, pipe and redirect before running the command
def run(cmd, stdout=None, stdin=None):
    if re.search(REGEX_STR["exit"], cmd):
        return None
    proc = None
    for rg in regex_dict:
        m = re.search(rg, cmd)
        if m:
            proc = regex_dict[rg](m,stdout=stdout,stdin=stdin)
            break
    else:
        proc = run_subprocess(cmd, stdout=stdout, stdin=stdin)
    return proc

# The main loop
def main():
    while True:
        cmd = input(PROMPT)
        if cmd == "":
            continue
        proc = run(cmd)
        if proc is None:
            break

if __name__ == "__main__":
    main()

