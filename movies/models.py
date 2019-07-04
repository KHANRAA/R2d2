from django.db import  models
import  urllib.request
import urllib
import json
from urllib.parse import quote
class Movie(models.Model):
    def getMovie(self, title):
        title=urllib.parse.quote(title)
        first_sug=title[0]
        request=urllib.request.Request("https://v2.sg.media-imdb.com/suggestion/"+first_sug+"/"+title+".json")
        response=urllib.request.urlopen(request)
        json_string=response.read().decode('utf-8')
        moviedata = json.loads(json_string)
        self.res={}
        if (response.status == 200):
            data = moviedata.get('d', [])
            for i in data:
                self.res['title']=i.get('l')
                self.res['cast'] = i.get('s')
                self.res['year'] = i.get('y')
                newid=i.get('id')
                request1 = urllib.request.Request("http://www.omdbapi.com/?i="+newid+"&apikey=PlzBanMe")
                response1 = urllib.request.urlopen(request1)
                json_string1 = response1.read().decode('utf-8')
                moviedata1 = json.loads(json_string1)
                self.res['imdbRating']=moviedata1.get('imdbRating')
                self.res['poster']=moviedata1.get('Poster')
                return self.res




