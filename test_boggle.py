import sys
import unittest
from cStringIO import StringIO

import boggle
_original_stdout = sys.stdout
_original_stderr = sys.stderr

def run(*args, **kwargs):
    expect_exit = kwargs.get("exit", False)
    sys.stdout = stdout = StringIO()
    sys.stderr = stderr = StringIO()
    try:
        try:
            boggle.main(args)
        finally:
            sys.stdout = _original_stdout
            outmsg = stdout.getvalue()
            sys.stderr = _original_stderr
            errmsg = stderr.getvalue()

    except SystemExit:
        if expect_exit:
            # This failed, as expected
            return outmsg, errmsg
        else:
            # This failed, unexpectedly
            raise AssertionError("Exited unexpectedly", outmsg, errmsg)

    if expect_exit:
        # It was supposed to exit, but didn't.
        raise AssertionError("Expected SystemExit", outmsg, errmsg)

    return outmsg, errmsg


class TestCommandLine(unittest.TestCase):
    def test_board(self):
        outmsg, errmsg = run("pyth asdo wern nmkl")
        assert "python" in outmsg

if __name__ == "__main__":
    unittest.main()
