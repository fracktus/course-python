import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    with open(INPUT_FILENAME, 'r') as file_csv:
        read = csv.DictReader(file_csv, delimiter=',', quotechar='"')
        json_d = [i for i in read]

    with open(OUTPUT_FILENAME, 'w') as file_json:
        json.dump(json_d, file_json, indent=4)
task()

if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")