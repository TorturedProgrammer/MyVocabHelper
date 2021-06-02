from bs4 import BeautifulSoup
import requests

def Scrape():
    i = 0
    USER_AGENT = {"header":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.272 Whale/2.9.117.22 Safari/537.36"}

    word_list = open("Vocab_Helper\\Word_List\\words.txt", "r")
    def_list = open("Vocab_Helper\\Word_List\\definitions.txt", "w")

    while i < 100:

        word = word_list.readline()
        word = word[:-1]
        if word == '':
            exit()
        
        URL = f"https://www.lexico.com/en/definition/{word}"

        res = requests.get(URL, headers=USER_AGENT)

        soup = BeautifulSoup(res.text, "lxml")

        parent = soup.find(attrs={"class":"ind one-click-content"})
        
        def_list.write(parent.text + "\n")
        i+=1


Scrape()