import grequests
import random
import string
import time
import sys

url = "http://putyourfuckingurlhere.com?query="

def generateRandomUrl():
    chars = "".join( [random.choice(string.letters) for i in xrange(15)] )
    return url+"TESTING"+chars

def bulkSiege(numUrls):
    urls = []
    errors = 0 
    for i in xrange(0,numUrls): urls.append(generateRandomUrl())
    rs = (grequests.get(u) for u in urls)
    responses = grequests.map(rs,size=10)
    for resp in responses:
        if resp.status_code == 500:
            errors += 1
    sent = int(sys.argv[1])
    print("Sent : " + str(sent) + "  Errors: " + str(errors))
    

while(1):
    bulkSiege(int(sys.argv[1]))
    time.sleep(0.5)
