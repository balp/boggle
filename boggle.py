import argparse
import sys

parser = argparse.ArgumentParser(
    description = "Boggle solver")
parser.add_argument("--dictionary", default="./words", metavar="FILENAME",
                    dest="dictfile",
                    type=argparse.FileType("r"),
                    help="filename containing valid words (one word per line)")
parser.add_argument("--html", action="store_true",
                    help="generate the output as HTML")
parser.add_argument("board", default=None, nargs="?",
                    help="specify 16 letters for the board (default uses a random board)")

class Solution(object):
    def __init__(self, word, positions):
        self.word = word
        self.positions = positions

def random_board():
    return "pythabcoqwenzxcv"

def load_wordlist(dictfile):
    return ["python"]

def solve_boggle(board, wordlist):
    return [Solution("python",
                     [(0,0), (0,1), (0, 2), (0,3), (1,3), (2,3)])]

def write_html(outfile, board, solutions):
    body = "\n".join([solution.word for solution in solutions])
    outfile.write("<html><body>\n%s\n</body></html>\n" % body)

def main(args):
    opts = parser.parse_args(args)
    board = opts.board
    if opts.board is None:
        board = random_board()
    board = board.replace(" ", "")
    if len(board) != 16:
        parser.error("board must contain only 16 letters")

    wordlist = load_wordlist(opts.dictfile)
        
    solutions = solve_boggle(board, wordlist)

    if opts.html:
        write_html(sys.stdout, board, solutions)
    else:
        for solution in solutions:
            print solution.word, " ".join("ABCD"[i]+str(j) for (i,j) in solution.positions)


if __name__ == "__main__":
    main(sys.argv[1:])
