# Merge two sorted files into another sorted file


def merge(file1, file2, out_file, mem):
    fp1 = open(file1, 'r')
    fp2 = open(file2, 'r')
    fp_out = open('merge_out1.txt', 'w')

    entry1 = fp1.readline()
    entry2 = fp2.readline()

    # loop until one of them files are empty
    while True:

        if(not entry1 and entry2):
            fp_out.write(entry2)
            fp_out.write(fp2.read())
            break

        if (not entry2 and entry1):
            fp_out.write(entry1)
            fp_out.write(fp1.read())
            break

        if (not entry1 and not entry2):
            break

        print(f"comp: [{entry1[:-1]}] - [{entry2[:-1]}]")
        if(int(entry1) <= int(entry2)):
            fp_out.write(entry1)
            entry1 = fp1.readline()

            if (entry1 == entry2):
                entry2 = fp2.readline()

        else:
            fp_out.write(entry2)
            entry2 = fp2.readline()

    fp1.close()
    fp2.close()
    fp_out.close()


merge("in1.txt", "in2.txt", "merge_out1.txt", 1024)
