from bs4 import BeautifulSoup
import requests
import re


def main(url):
    headers = {'user-agent': 'my-app/0.0.1'}
    content = requests.get(url, headers=headers).text
    soup = BeautifulSoup(content, 'html.parser')
    count = 0
    with open('urls.txt', 'a') as writer:
        for i in soup.find_all('a'):
            res = re.match(r'.*?index.php\?md5=(.+?)"', str(i))
            if res is not None:
                url = 'http://library.lol/main/%s' % res.groups()[0]
                content = requests.get(url, headers=headers).text
                res = re.match('[\s\S]*href="(.+?)">IPFS.*', content).groups()[0]
                writer.write('%s\n' % res)
                print(count)
                count += 1


if __name__ == '__main__':
    url = 'http://libgen.rs/search.php?&res=100&req=Student+Mathematical+Library&phrase=1&view=simple&column=def&sort=def&sortmode=ASC&page=3'
    main(url)
