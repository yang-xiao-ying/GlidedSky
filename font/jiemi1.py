import base64
from fontTools.ttLib import TTFont
import xml.dom.minidom
from bs4 import BeautifulSoup

def getmapping():
    dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    result = []
    for i in range(1, 1001, 1):
        f = open('cached/{}.html'.format(i)).read()
        soup = BeautifulSoup(f, "html.parser")
        html=str(soup.select('style'))
        t = html.split('base64,', 1)[1]
        font_face = t.split(') format', 1)[0]
        print(len(font_face))

        b = base64.b64decode(font_face)
        with open('ttfji/{}.ttf'.format(i),'wb') as f:
            f.write(b)

        font = TTFont('ttfji/{}.ttf'.format(i))
        font.saveXML('dictxml/{}.xml'.format(i))

        newdict = {}
        dom = xml.dom.minidom.parse('dictxml/{}.xml'.format(i))
        root = dom.documentElement
        bb = root.getElementsByTagName('GlyphID')
        for j in range(1,11):
            k = bb[j].getAttribute("name")
            # print(k)
            newdict[dict[k]] = str(j-1)
        result.append(newdict)
    print(result)
    return result

getmapping()


