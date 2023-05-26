import requests
#to process images need
from io import BytesIO
from PIL import Image



'''
#can now access urls and such
r = requests.get('https://www.bing.com')

# give the website status | to check the html status code ->  (https://www.tutorialrepublic.com/html-reference/http-status-codes.php#:~:text=HTTP%20Status%20Code.%20The%20status%20code%20provides%20information,page.%20404%20-%20the%20requested%20page%20doesn%27t%20exist.)
r.status_code

# getting url
r.url

# using the url and putting in a html file
f = open("./page.html", "w+")
f.write(r.text)

# doing a google search using html
params = {"q=": "code"}
# html.code.fo.search : search query
r = requests.get("https://www.bing.com/search" , params= params)
f = open("./page.html", "w+")
f.write(r.text)
'''


'''
#for images

r = requests.get('https://th.bing.com/th/id/OIP.DP48uGkldTg01Wx5KTExXAHaE6?pid=ImgDet&rs=1')
image = Image.open(BytesIO(r.content))
#info about image
print(image.size ,image.format, image.mode)
path = "./image119.jpeg"
try:
    image.save(path,image.format)
except IOError:
    print('cannot save image ')
'''


'''
# writing data onto a htmp page (same as editing the html/php code)
variable = 'data regarding what to enter in the webiste '
r = requests.post('website link', data=variable)
f = open("myfile.html","w+")
f.write(r.text)
'''


'''
#to get webiste headers
r.headers
'''