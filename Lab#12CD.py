#password is @#naim
import PyPDF2, random,time

pdfFileObj=open('Hello.pdf','rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)


testedPassword = []
def randomPassword():
    specialCharacter = ["!", "@", "#", "$", "%", "^", "&", "*"]
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v',
                'z']
    randomPassword = ""
    specialCharNum = 2
    alphabetCharNum = 4
    for i in range(specialCharNum):
        randomPassword += random.choice(specialCharacter)
    # for i in range(alphabetCharNum):
    #     randomPassword += random.choice(alphabet)
    # You can the code below
    randomPassword = randomPassword + "naim"
    testedPassword.append(testedPassword)
    return randomPassword

print(randomPassword())

content = ""
print(len(content))
startTime=time.time()
while (len(content) <= 0):
    password = randomPassword()
    if not (password in testedPassword):
        
        if pdfReader.is_encrypted:
            try:
                pdfReader.decrypt(password)
                pdfFileObj = pdfReader.pages[0]
                content = pdfFileObj.extract_text()
                print("Brute Force Success!")
                print(content)
                break
            except:
                print("Attempting..")
endTime=time.time()
elapsedTime=time.time()
print("It took "+ str(elapsedTime)+" to bruteforce")