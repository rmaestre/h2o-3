import sys
sys.path.insert(1, "../../../")
import h2o

def asnumeric(ip,port):
    # Connect to h2o
    h2o.init(ip,port)

    h2oframe =  h2o.import_frame(path=h2o.locate("smalldata/junit/cars.csv"))
    rows = h2oframe.nrow()

    h2oframe['cylinders'] = h2oframe['cylinders'].ascharacter()
    assert h2oframe["cylinders"].isfactor(), "expected the column to be a factor"

    h2oframe = h2o.asnumeric(h2oframe)
    h2oframe['cylinders'] = h2oframe['cylinders'] - h2oframe['cylinders']
    h2oframe = h2oframe[h2oframe['cylinders'] == 0]
    assert h2oframe.nrow() == rows, "expected the same number of rows as before {0}, but got {1}".format(rows, h2oframe.nrow())

if __name__ == "__main__":
    h2o.run_test(sys.argv, asnumeric)