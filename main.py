

import requests
for i in range(0,5000):
    url=(f'https://www.sdccampuscare.in/ExamPDF/RC_{i}~Annual~2022~11417.pdf')
    response=requests.get(url)
    code=response.status_code

    if code == 200:
       print(code)
       print(url)
       f = open("myfile.txt", "x")
       f.write(url)
       f.close()
       break
