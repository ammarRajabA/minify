import requests
import sys

cssMinify='https://cssminifier.com/raw'
jsMinify='https://javascript-minifier.com/raw'

if sys.argv[1].find('.css')<>-1:
    minify=cssMinify
    ext='.css'
elif sys.argv[1].find('.js')<>-1:
    minify=jsMinify
    ext='.js'
else:
    sys.exit('Please set file ext to css or js')

o=open(sys.argv[1],'rb')
content=o.read()
o.close()
req=requests.post(minify,data={'input':content})
o=open(sys.argv[1].replace(ext,'.min'+ext),'wb')
o.write(req.text)
o.close()

