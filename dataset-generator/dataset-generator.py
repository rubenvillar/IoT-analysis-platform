import sys
import getopt
import csv
import time
import random
from collections import namedtuple

NormalizedParams = namedtuple(
    'NormalizedParams', ['outputfile', 'rows', 'type'])


def currentMilliTime(): return int(round(time.time() * 1000))


def main():
    params = processParams()
    if params.type == 'WET':
        generateWeatherDataset(params.outputfile, params.rows)
    elif params.type == 'WAC':
        generateWaterConsuptionDataset(params.outputfile, params.rows)
    else:
        print("invalid type "+params.type)
        sys.exit(2)


def generateWaterConsuptionDataset(outputfile, rows):
    with open(outputfile, 'w') as csvoutput:
        fieldnames = ["water_tower", "measurement_timestamp",
                      "consumption", "preassure"]
        writer = csv.DictWriter(csvoutput, fieldnames=fieldnames)
        writer.writeheader()
        i = 0
        while i < int(rows):
            row = {}
            row['water_tower'] = random.choice(
                ['Alicante Metropolitana', 'Alicante Diseminado', 'Elche Metropolitana', 'Elche Diseminado', 'Santa Pola'])
            row['measurement_timestamp'] = random.randint(
                1514764800000, currentMilliTime())
            row['consumption'] = random.uniform(0.0, 10000.0)
            row['preassure'] = random.uniform(1.0, 10.0)
            writer.writerow(row)
            i = i + 1


def generateWeatherDataset(outputfile, rows):
    with open(outputfile, 'w') as csvoutput:
        fieldnames = ["beach_name", "latitude", "longitude", "measurement_timestamp",
                      "water_temperature", "turbidity", "transducer_depth", "wave_height"]
        writer = csv.DictWriter(csvoutput, fieldnames=fieldnames)
        writer.writeheader()
        i = 0
        while i < int(rows):
            row = {}
            beach = random.choice([('San Juan', (38.3751327, -0.4257402)),
                                   ('Muchavista', (38.3949614, -0.4255705)),
                                   ('Urbanova', (38.2749245, -0.5216082)),
                                   ('Postiguet', (38.3468118, -0.4630523)),
                                   ('Carabassi', (38.2420529, -0.5151545))])
            row['beach_name'] = beach[0] + ' Beach'
            row['latitude'] = beach[1][0]
            row['longitude'] = beach[1][1]
            row['measurement_timestamp'] = random.randint(
                1514764800000, currentMilliTime())
            row['water_temperature'] = random.uniform(12.0, 26.0)
            row['turbidity'] = random.uniform(1.0, 2.0)
            row['transducer_depth'] = random.uniform(0.0, 1.0)
            row['wave_height'] = random.uniform(0.2, 10.0)
            writer.writerow(row)
            i = i + 1


def processParams():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:r:t:", [
                                   "help", "ofile", "rows=", "type="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    rows = None
    output = None
    typeData = None
    if len(opts) == 0:
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--ofile"):
            output = a
        elif o in ("-r", "--rows"):
            rows = a
        elif o in ("-t", "--type"):
            typeData = a
        else:
            assert False, "unhandled option"
    return NormalizedParams(output, rows, typeData)


def usage():
    print sys.argv[0]+' -r <num_rows> -t <WET>'


if __name__ == "__main__":
    main()
