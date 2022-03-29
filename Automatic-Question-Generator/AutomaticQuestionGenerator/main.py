import aqgFunction


# Main Function
def main():
    # Create AQG object
    aqg = aqgFunction.AutomaticQuestionGenerator()

    inputTextPath = "/home/ibtehaj/Documents/ibtehaj/text/Automatic-Question-Generator/AutomaticQuestionGenerator/DB/text.txt"
    readFile = open(inputTextPath, 'r+', encoding="utf8")
    #readFile = open(inputTextPath, 'r+', encoding="utf8", errors = 'ignore')

    inputText = readFile.read()
    #inputText = '''I am Dipta. I love codding. I build my carrier with this.'''

    questionList = aqg.aqgParse(inputText)
    aqg.display(questionList)
#    print(inputText)
#    aqg.DisNormal(questionList)

    return 0


# Call Main Function
if __name__ == "__main__":
    main()

