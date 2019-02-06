def findDuplicate(paths):
    """
    :type paths: List[str]
    :rtype: List[List[str]]
    """
    fileMap = dict()
    temp = ""
    duplicates = list()
    for s in paths:
        tempFile = s.split(" ")
        for i in range(len(tempFile)):
            if i == 0:
                filePath = tempFile[0]
            else:
                content = tempFile[i].split("(")
                if content[1] not in fileMap:
                    temp = filePath+content[0]
                    tempList = list()
                    tempList.append(temp)
                    fileMap[content[1]] = tempList
                else:
                    tempList = fileMap[content[1]]
                    temp = filePath+content[0]
                    tempList.append(temp)
                    fileMap[content[1]] = tempList
    for key,value in fileMap.items():
        if len(value) > 1:
            duplicates.append(value)
    return duplicates


files = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
res = findDuplicate(files)
print(res)