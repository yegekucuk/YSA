def kaldir(string):
    """
    Removing the spaces in the script
    """
    bosluklar = ["  ","   ","    ","     ","      ","       ","        ","         ","          "]
    string = string.replace("\n"," ")
    string = string.replace("\t","")
    
    for i in bosluklar:
        string = string.replace(i," ")
    return string