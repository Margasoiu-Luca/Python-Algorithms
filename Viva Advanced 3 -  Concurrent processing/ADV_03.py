import newspaper
import concurrent.futures
from pprint import pprint
import os
from newspaper import Article

URLs = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://www.tagesschau.de/',
        'http://www.bbc.co.uk/',
        'https://theguardian.com', ]


def get_headlines(URL):
    # This prints that the concurrent processing on an url has started, and the other print line outputs when it
    # has finished for this URL
    print(f'Process {os.getpid()} started concurrent work on {URL}')
    result = newspaper.build(URL, memoize_articles=False)
    # headline is used for appending to the list that is returned to the resulting list from the map method
    headline = [URL]
    for i in range(1, 6):
        art = result.articles[i]
        art.download()
        art.parse()
        headline.append(art.title)
        # print(URL + ":  "+art.title,)
    print(f'Process {os.getpid()} finished concurrent work on {URL}')
    return headline


def concurrent_fnc():
    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # The map function does the concurrent processing
            res = executor.map(get_headlines, URLs)
        # Res is returned as an iterator, and to print it we need to use pprint
        # pprint(tuple(res))
    except:
        print("Error has been found")

def get_headlines_non_concurrent():
    try:
        for url in URLs:
            result = newspaper.build(url, memoize_articles=False)
            # print('\n''The headlines from %s are' % url, '\n')
            print(f'Process {os.getpid()} started non-concurrent work on {url}')
            for i in range(1, 6):
                art = result.articles[i]
                art.download()
                art.parse()
                # print(art.title)
            print(f'Process {os.getpid()} finished non-concurrent work on {url}')
    except:
        print("Error has been found")


if __name__ == '__main__':
    import timeit

    elapsed_time_concurrent = timeit.timeit("concurrent_fnc()", setup="from __main__ import concurrent_fnc", number=2)/2
    elapsed_time_not_concurrent = timeit.timeit("get_headlines_non_concurrent()",
                                 setup="from __main__ import get_headlines_non_concurrent", number=2) / 2
    print(f"Concurrent time is {elapsed_time_concurrent} and non-concurrent time is {elapsed_time_not_concurrent}")
    print(f"This means that concurrent processing time is roughly "
          f"{round((elapsed_time_concurrent/elapsed_time_not_concurrent)*100,2)}% faster then non-concurrent professing ")

# Decomment lines with print function to see the information come in real time