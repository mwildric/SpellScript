from lxml import html
import requests

page = requests.get('https://2e.aonprd.com/Spells.aspx?ID=1')
tree = html.fromstring(page.content)

name = tree.xpath('//h1[@class="title"]/text()')
traits = tree.xpath('//span[@class="trait"]/a/text()')

level = tree.xpath('//h1[@class="title"]/span/text()')
traditions = tree.xpath('//span/a[contains(@href,"Tradition")]/text()')

actions = tree.xpath('//b[starts-with(text(),\'Cast\')]/following-sibling::img/following-sibling::img/following-sibling::text()')
print(actions)

spellrange = tree.xpath('//b[starts-with(text(),\'Range\')]/following-sibling::text()[1]')
duration = tree.xpath('//b[starts-with(text(),\'Duration\')]/following-sibling::text()[1]')
targets = tree.xpath('//b[starts-with(text(),\'Targets\')]/following-sibling::text()[1]')
throw = tree.xpath('//b[starts-with(text(),\'Saving Throw\')]/following-sibling::text()[1]')


text = tree.xpath('//span/hr/following-sibling::text()[1]')
print(text)


heightened = tree.xpath('//b[starts-with(text(),\'Heightened\')]/following-sibling::text()')
print(heightened)

