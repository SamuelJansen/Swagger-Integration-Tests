import StringHelper

def equal(response,expectedResponse) :
    filteredResponse = StringHelper.filterJson(response)
    filteredExpectedResponse = StringHelper.filterJson(expectedResponse)
    return filteredResponse == filteredExpectedResponse

def filterIgnoreKeyList(objectAsString,ignoreKeyList):
    if objectAsString and ignoreKeyList :
        splitedObjectAsStringList = objectAsString.splt('\n')
        for line in splitedObjectAsStringList :
            for key in ignoreKeyList :
                if key in line :
                    if key.strip() == line.split(':').strip() :
                        line = ''
        return '\n'.join(splitedObjectAsStringList)
    return objectAsString
