from lxml import html
import requests
import re
import yaml

def formatHeightened(heightened):
    return heightened

def cleanupList(list):
    formattedList = []
    for item in list:
        formattedList.append(item.strip())
    return formattedList

def cleanup(attr):
    if(len(attr) != 0):
        return attr[0].strip()
    else:
        return 


page = requests.get('https://2e.aonprd.com/Spells.aspx?ID=4')
tree = html.fromstring(page.content)

name = tree.xpath('//h1[@class="title"]/text()')[0].strip()
traits = tree.xpath('//span[@class="trait"]/a/text()')

title = tree.xpath('//h1[@class="title"]/span/text()')[0]
titleList = title.split(' ')
spelltype = titleList[0]
level = titleList[1]

traditions = tree.xpath('//span/a[contains(@href,"Tradition")]/text()')

actions = tree.xpath('//b[starts-with(text(),\'Cast\')]/following-sibling::img/following-sibling::img/following-sibling::text()')

rarity = tree.xpath('//b[starts-with(text(),\'Rarity\')]/following-sibling::text()[1]')
area = tree.xpath('//b[starts-with(text(),\'Area\')]/following-sibling::text()[1]')
spellrange = tree.xpath('//b[starts-with(text(),\'Range\')]/following-sibling::text()[1]')
duration = tree.xpath('//b[starts-with(text(),\'Duration\')]/following-sibling::text()[1]')
targets = tree.xpath('//b[starts-with(text(),\'Targets\')]/following-sibling::text()[1]')
throw = tree.xpath('//b[starts-with(text(),\'Saving Throw\')]/following-sibling::text()[1]')

description = re.findall( r'DetailedOutput.*?<hr />(.*?)<hr|<span/>', page.content.decode('utf-8'),  re.DOTALL)

heightened = re.findall( r'(?<=Heightened )\((.*?)\)</b> (.*?)(<b>|</span>)' , page.content.decode('utf-8'), re.IGNORECASE)

f = open("all.yaml", "w")
yaml.dump(
    { 
        name.replace(' ','-'):{
            'name': name,
            'traits': cleanupList(traits),
            'traditions': cleanupList(traditions),
            'level': level,
            'type': spelltype,
            'rarity': "",
            'casting': "",
            'area':cleanup(area),
            'range':cleanup(spellrange),
            'target': cleanup(targets),
            'saving throw': cleanup(throw),
            'duration': cleanup(duration),
            'description':{
                'main':description
            },
            'heightened':formatHeightened(heightened)    
        }
    }, f
    
    )
f.close



#(?<=<hr>).*(?=(<hr>|$))
#'((?<=<hr>)|(?<=<hr />)).*?(?=(<hr ?/?>|</span>))' 
