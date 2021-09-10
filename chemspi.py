from chemspipy import ChemSpider

cs = ChemSpider('I908Dobk2EgV7gBnQpUHPhP3eYaRHRhg')

for result in cs.search('glucose?'):
    print(result.record_id)

