import pyarabic.araby as araby


def convertArrayToStr(arr):
    strIng = ''
    for a in arr:
        strIng += a + ' '
    return strIng


if __name__ == '__main__':
    inputVar = input('type your sentence ?')
    targetWords = [
        ['احمد', 'أحمد'],
        ['المدرسه', 'المدرسة'],
        ['الي', 'إلى'],
        ['شاطئ', 'شاطيء'],
        ['بادئ', 'باديء'],
        ['ناشئ', 'ناشيء'],
        ['لاجئ', 'لاجيء'],
    ]
    try:
        inputVar = str(inputVar)
        errorCount = 0
        sentenceSplitter = araby.tokenize(inputVar)
        print(sentenceSplitter)
        correctCount = len(sentenceSplitter)
        lenOfsentence= len(sentenceSplitter)
        for n, s in enumerate(sentenceSplitter):
            for n2, x in enumerate(targetWords):
                if str(s) == x[0]:
                    errorCount += 1
                    correctCount -= 1
                    sentenceSplitter[n] = x[1]
        print(convertArrayToStr(sentenceSplitter))
        print('Wrong : {}, Correct : {}, Total : {}'.format(\
            errorCount, correctCount, lenOfsentence))
    except Exception as e:
        print('we have error in ', e)