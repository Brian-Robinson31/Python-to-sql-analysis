/*CREATE PROCEDURE GetAverageIMDBRatingPerYear()
 BEGIN
 SELECT Released_Year, AVG(IMDB_Rating) AS AverageRating
 FROM movies
 GROUP BY Released_Year;
 END;
 
 CREATE PROCEDURE SortMoviesByRuntime()
 BEGIN
 SELECT * FROM movies
 ORDER BY Runtime;
 END;
 CREATE PROCEDURE BestMovies()
 BEGIN
 SELECT * FROM movies
 ORDER BY IMDB_Rating DESC;
 END;
 CREATE PROCEDURE MoviesPerYear()
 BEGIN
 SELECT Released_Year, COUNT(*) AS TotalMovies
 FROM movies
 GROUP BY Released_Year
 ORDER BY Released_Year;
 END;
 */