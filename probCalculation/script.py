from probCalculation import ocr

defname1 = "defBody"
defname2 = "defHead"
tname1= "theoremBody"
i = 1
numDef = 2
numThe = 2
outfile = open('test.txt','w')

for i in range(1, numDef):
    file1 = "/Users/mac/Desktop/htn2017/test/pics/"+defname1+str(i)+".jpg"
    file2 = "/Users/mac/Desktop/htn2017/test/pics/" + defname2 + str(i) + ".jpg"
    item = ocr.process_print(file1)
    outfile.write("%s" % item + ',')
    item = ocr.process_print(file2)
    outfile.write("%s\n" % item)


# for i in range(1, numThe):
#     file1 = "/Users/mac/Desktop/htn2017/test/pics/"+ tname1 +str(i)+".jpg"
#     item = ocr.process_print(file1)
#     outfile.write("%s" % item + ',')
#     outfile.write("%s\n" % item)