def findStartAndEndLocations(pairs):
    child = {}
    parent = {}

    for val in range(0,len(pairs)):
        if(pairs[val][1] in child.keys()):
            newParent = child[pairs[val][1]]
            child[pairs[val][1]].append(pairs[val][0])
          #  if newParent in child.keys():
          #      newParent = child[newParent]
        else:
            child[pairs[val][1]] = [pairs[val][0]]
            newParent = pairs[val][0]

        if newParent in child.keys():
            newParent = child[newParent]

        if(newParent in parent.keys()):
            #val1 = pairs[val][1]
            if pairs[val][1] not in parent[newParent]:
                parent[newParent].append(pairs[val][1])
               # print(parent[newParent])
        else:
            parent[newParent] = [pairs[val][1]]
            #print(parent[newParent])

    return parent








#paris = [['A','B'],['A','C'], ['B','K'], ['C','K'] ,['E','L'],['F','G'], ['J','M'], ['E','F'],['G','H'],['G','I']]
pairs = [['B','A'], ['C','A'],['D','A'],['A','F']]
findStartAndEndLocations(pairs)