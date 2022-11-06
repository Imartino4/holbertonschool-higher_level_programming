-- list all genres and display the number of shows linked to each
-- display: TV show genre - Numb of shows linked
-- first column must be called genre and second number_of_shows
-- don't display genre that doesn't have a show linked
SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number_of_shows' FROM tv_genres RIGHT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY tv_genres.name ORDER BY number_of_shows DESC;