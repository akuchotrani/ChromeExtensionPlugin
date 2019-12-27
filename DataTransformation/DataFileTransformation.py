import csv
import os

def LoadFile(file_path):
    print("Loading the file into memory...")
    global DataFile
    DataFile = open(os.path.expanduser(file_path))


def TransformDataFile():
    '''
    Creates a dictionary of unique words with emotions value as row.
    Converts all emotional data into a row of emotion numbers
    :return: None
    '''

    word_dict = {}
    for line in DataFile.readlines():
        line = line.rstrip()
        rows = line.split("\t")
        if(len(rows) >= 3):
            if(word_dict.has_key(rows[0])):
                word_dict[rows[0]] += ',' + rows[2]
            else:
                word_dict[rows[0]] = rows[2]

    for word,value in word_dict.items():
        print("key: ",word, " values: ",value)

    print(len(word_dict))


def main():
    file_path = "~/Desktop/emotionlexicon.txt"
    LoadFile(file_path)
    TransformDataFile()

if __name__ == "__main__":
    main()
