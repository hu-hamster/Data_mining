import csv
import string

"""
** usage: get DataFrame from csv file and isolate useful information
** arguments:
**** spark: SparkSession
**** read_filename: The path of source file
**** save_filename: The path of save file
**** filter_items: filter values, such as: [“name”, "age"]
"""
def filter_data(spark, read_filename, save_filename, filter_items):
    df = spark.read.csv(read_filename, header=True)
    df = df.select(filter_items)
    df.toPandas().to_csv(save_filename)
    # df.show(10)
    # df.map(lambda x: change_heartDisease(x))
    # return df


"""
** usage: change element from No or Yes
** argument: element
"""
def change_elem_binary(element):
    if element == "No":
        return 0
    else:
        return 1


"""
** usage: change MentalHealth element
** argument: element
"""
def change_elem_MentalHealth(element):
    num = float(element)
    if 0.0 <= num < 5.0:
        return 0
    elif 5.0 <= num < 15.0:
        return 1
    else:
        return 2


"""
** usage: Replace elements in a file with fractions, such as: No - 0, Yes - 1
** arguments:
**** sourcefile: The path of source file
**** savefile: The path of save file
"""
def replace_elem(sourcefile, savefile):
    csv_reader = csv.reader(open(sourcefile))
    head = []
    body = []
    for line in csv_reader:
        if line[0] == "":
            head = line[1:]
            continue
        for i in range(1, len(line)-1):
            line[i] = change_elem_binary(line[i])
        line[len(line)-1] = change_elem_MentalHealth(line[len(line)-1])
        body.append(line[1:])
    csv_writer = csv.writer(open(savefile, "w", newline=''))
    csv_writer.writerow(head)
    csv_writer.writerows(body)

