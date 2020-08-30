def ltrim (sen):
    a = "first"
    b = ""
    for i in sen:
        if i == " " and a == "first":
            b = b            
        else:
            b = b + i
            a = "trimmed"
def rtrim (sen):
    c = len(sen)
print(ltrim("                          jhefgesghse  wrfseyrfuehafg"))  