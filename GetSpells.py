from lxml import html
import requests
import re
import yaml



page = requests.get('https://2e.aonprd.com/Spells.aspx?ID=500')
tree = html.fromstring(page.content)

name = tree.xpath('//h1[@class="title"]/text()')
traits = tree.xpath('//span[@class="trait"]/a/text()')

level = tree.xpath('//h1[@class="title"]/span/text()')
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
        'name': name,
        'traits': traits,
        'traditions': traditions,
        'level': level,
        'type': "",
        'rarity': "",
        'casting': "",
        'area':area,
        'range':spellrange,
        'target': targets,
        'saving throw': throw,
        'duration': duration,
        'description':{
            'main':description
        },
        'heightened': heightened     

    }, f
    
    )
f.close


#(?<=<hr>).*(?=(<hr>|$))
#'((?<=<hr>)|(?<=<hr />)).*?(?=(<hr ?/?>|</span>))' 
