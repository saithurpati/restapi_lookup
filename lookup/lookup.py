import click, requests,os
import json


API_URL = 'https://www.travel-advisory.info/api'

def lookup(countrycode):

    r = requests.get(API_URL)
    #data = json.loads(r.text)
    #print(json.dumps(data, indent=4))
    # qprint(data)
    #Write data to file
    #create output directory
    # try:
    #     os.mkdir("output")
    # except FileExistsError:
    #     pass

    with open('data.json', 'w') as outputfile:
        json.dump(json.loads(r.text), outputfile)

    with open('data.json') as json_file:
        data = json.load(json_file)

    for cc in countrycode:
        try:
            print(data["data"][cc.upper()]["name"])
        except:
            print("Country code:",C_YELLO,cc.upper(),"not Found")



if __name__ == '__main__':
    @click.command()
    @click.option('-c', '--countryCode', nargs=1 , required=True, help="Country code or list of CC Eg: \"AU,AE,IN\"")

    def main(countrycode):
        formated_cc = countrycode.split(",")
        lookup(formated_cc)
    main()