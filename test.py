import sys, os

sys.path.append("..")
from fcad_pcb_ftl import kicad

testfile_easy = "test.kicad_pcb"
testfile_meander = "MeanderTest.kicad_pcb"

def test_easy():
    print("Easy Test. Starting parser...")

    pcb = kicad.KicadFcad(testfile_easy)

    print("Success!")

if __name__ == "__main__":
    test_easy()