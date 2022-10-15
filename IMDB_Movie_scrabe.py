



# from textwrap import indent
# from bs4 import BeautifulSoup
# import requests

# url = "https://www.imdb.com/india/top-rated-indian-movies/"
# page = requests.get(url)
# soup = BeautifulSoup(page.text,'html.parser')
# def scrap_top_list():
#     main_div = soup.find('div',class_='lister')
#     tbody = main_div.find('tbody',class_='lister-list')
#     trs = tbody.find_all('tr')
#     movie_ranks =[]
#     movie_name = []
#     yeaar_of_realease = []
#     movie_urls = []
#     movie_ratings = [] 
    
#     for tr in trs:
#         position = tr.find('td',class_="titleColumn").get_text().strip()
        
#         rank = ''
#         for i in position:
#             if '.' not in i:
#                 rank = rank+i 
#             else:
#                 break
#         movie_ranks.append(rank)
        
#         title = tr.find('td',class_="titleColumn").a.get_text()
#         movie_name.append(title)
 
#         year = tr.find('td',class_="titleColumn").span.get_text()
#         if year == None:
#             pass
#         else:
#               yeaar_of_realease.append(year)
        
#         imdb_rating = tr.find('td',class_="ratingColumn imdbRating").strong.get_text()
#         movie_ratings.append(imdb_rating)

#         link =tr.find('td',class_="titleColumn").a['href']
#         movie_link ="https://www.imdb.com"+link
#         movie_urls.append(movie_link)
#     top_movies = []
#     details = {'position':'','name':'','year':'','rating':'','url':''}
#     for i in range(0,len(movie_ranks)):
#         details['position'] = int(movie_ranks[i])
#         details['name'] = str(movie_name[i])
#         yeaar_of_realease[i] = yeaar_of_realease[i][1:5]
#         details['year'] = int(yeaar_of_realease[i])
#         details['rating'] =float(movie_ratings[i])
#         details['url'] =movie_urls[i]
#         top_movies.append(details.copy())
#     return (top_movies)

# scrab = scrap_top_list()
# print(scrab)

# import pprint
# pprint.pprint(scrap_top_list())


# Task 2


# def group_by_year(movies):
#     years = []
#     for i in movies:
#         year = i["year"]
#         if year not in years:
#             years.append(year)
#     movie_dict = {i:[]for i in years}
#     for i in movies:
#         year = i['year']
#         for x in movie_dict:
#             if str(x) == str(year):
#                 movie_dict[x].append([i])
#     return movie_dict


# # # import pprint
# # # pprint.pprint(group_by_year(scrab))

# # print(group_by_year(scrab))

# dec_arg = group_by_year(scrab)
