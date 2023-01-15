import pexpect
from echo_bot import *


class PythonShell():
    def __init__(self):
        self.proc = None
        self.prompt = r">>>.*"

    def start(self):
        self.proc = pexpect.spawn("python3 -i", timeout=10)
        self.proc.expect(self.prompt, timeout=10)

    def run_command(self, command):
        command = command.strip() + "\n"
        encoded_command = command.encode("utf-8")
        self.proc.sendline(encoded_command)
        self.proc.expect(self.prompt, timeout=10)
        result = self.proc.before.decode("utf-8")
        result = result[result.find("\n") + 1:result.rfind("\n")]
        if not result:
            result = ">>>"
        return result.strip()

    def __del__(self):
        response = self.proc.sendline("exit()")



#def main():
    #proc = subprocess.Popen(['python3', '-i'],
    #                       stdin=subprocess.PIPE,
    #                        stdout=subprocess.PIPE,
    #                        stderr=subprocess.PIPE)

    # To avoid deadlocks: careful to: add \n to output, flush output, use
    # readline() rather than read()
    #proc.stdin.write(b'2+2\n')
    #proc.stdin.flush()
    #print(proc.stdout.readline().decode("utf-8"))

    #proc.stdin.write(b'len("foobar")\n')
    #proc.stdin.flush()
    #print(proc.stdout.readline().decode("utf-8"))



p = PythonShell()
p.start()

replier = RawTextReplier(reply_function=p.run_command, start_message=("Python 3"))
# replier = RawTextReplier(start_message=("Python 3"))

replier.run()

