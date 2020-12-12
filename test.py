import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}


def get_info(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    ranks = soup.select('span.pc_temp_num')
    titles = soup.select('div.pc_temp_songlist>ul>li>a')
    times = soup.select('span.pc_temp_tips_r>span')
    for rank, title, time in zip(ranks, titles, times):
        data = {
            'rank': rank.get_text().strip(),
            'singer': title.get_text().split(' - ', 1)[0],
            'song': title.get_text().split(' - ', 1)[-1].strip(),
            'time': time.get_text().strip(),
        }
        print('歌曲名: {}'.format(data['song']))


if __name__ == '__main__':
    urls = ['https://www.kugou.com/yy/rank/home/1-4681.html'.format(str(i)) for i in range(1, 20)]
    for url in urls:
        get_info(url)
        time.sleep(1)
