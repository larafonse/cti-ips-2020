def favorite_genres(users, movies, movie_ratings):
  
  for user in users:
    rank = 0
    
    user.update({"genre":{}})
    
    for movie_rating in movie_ratings:
      if movie_rating["user_id"] == user["id"]:
        
        for movie in movies:
          
          if movie_rating["movie_id"] == movie["id"]:
          
            if movie["genre"] not in user["genre"]:
              
              user["genre"].update({movie["genre"]:[movie_rating["rating"]]})
              
            else:
              user["genre"][movie["genre"]].append(movie_rating["rating"])
              
          
    
    for genre,rating in user["genre"].items():
      average_rating = 0
      
      for i in rating:
        average_rating+=i
        
      average_rating /=len(rating)
      
      if average_rating > rank:
        rank = average_rating
        
        fav_genre = genre
      
    
    
    
    user.update({"favorite_genre":fav_genre})
    print(fav_genre)
  
  return(users)
    
    
    
    
movie_ratings = [
  {
    "movie_id": "20jfcf02341kwd",
    "user_id": "92387rergrge", 
    "rating": 5
  },
  {
    "movie_id": "20dfvsdst",
    "user_id": "92387rergrge", 
    "rating": 1
    
  },
  {
    "movie_id": "20jffrbtgrbtbt",
    "user_id": "92387rergrge", 
    "rating": 5
  },
  {
    "movie_id": "2aefefasefe",
    "user_id": "92387rergrge", 
    "rating": 1
  }
  
]
    
movies = [
  {
     "id": "20jfcf02341kwd",
     "genre": "animated"
  },
  {
     "id": "2aefefasefe",
     "genre": "horror"
  },
  {
     "id": "20jffrbtgrbtbt",
     "genre": "animated"
  },
  {
     "id": "20dfvsdst",
     "genre": "horror"
  }
]
        
users = [{
    "id": "92387rergrge",
  }
]

print(favorite_genres(users,movies,movie_ratings))