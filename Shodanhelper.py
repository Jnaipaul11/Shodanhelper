import os
import csv
from shodan import Shodan
api = Shodan('XXXXXXX')

def checkmate (*args):
    ip=args[0]
    l=args[1]
    try:
    # Lookup targets
        results = api.search(ip,page='1',limit=l)
        # print(ipinfo)
    except: print('wtf bro?')
    loc={}

    # # # Show the results
    with open('results.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile,delimiter=';',lineterminator='\n',)
        wr.writerow(['IP','hostname','ISP','OS','city','country name','longitude','latitude'])
        for result in results['matches']:
                loc=result['location']
                targetdets=(result['ip_str'],result['hostnames'],result['isp'],result['os'],loc['city'],loc['country_name'],loc['longitude'],loc['latitude'])
                # print(targetdets)
                wr.writerow(targetdets)

        print('Total results found: {}'.format(results['total']))
        print('Results extracted:{}'.format(l))
    # myfile.close()



def info():
    """Shows general information about your account"""
    # key = get_api_key()
    # api = shodan.Shodan(key)
    try:
        results = api.info()
    except: print('error!')

    print("""Query credits available: {0}
Scan credits available: {1}
    """.format(results['query_credits'], results['scan_credits']))


def main (*args):
    print('What do you want to search? ')
    ip=input()
    print('How many ips you want? please be merciful')
    l=input()
    checkmate(ip,l)
    info()



main(1)
