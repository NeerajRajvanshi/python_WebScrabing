



# import bs4,requests,openpyxl
# excel=openpyxl.Workbook()
# print(excel.sheetnames)
# sheet=excel.active
# sheet.title="Top Rated Movies"
# print(excel.sheetnames)
# sheet.append(['Movie Rank','Movie Name','Year of Release','IMDB Rating'])


# url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"
# data=requests.get("https://www.imdb.com/chart/top/")
# soup=bs4.BeautifulSoup(data.text,'html.parser')
# movie=soup.find('tbody',class_="lister-list").find_all('tr')
# for i in movie:
#     n=i.find('td',class_="titleColumn").a.text
#     r=i.find('td',class_="titleColumn").get_text(strip=True).split(".")[0]
#     y=i.find('td',class_="titleColumn").span.text.strip("()")
#     ra=i.find('td',class_="ratingColumn imdbRating").strong.text
#     print(r,n,y,ra)
#     sheet.append([r,n,y,ra])
#     print(type(sheet))
    

# excel.save('Fruits.xlsx')
    

    