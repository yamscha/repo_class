use favorite_db;

INSERT INTO favorite_foods (food, score)
VALUES ("Spaghetti", 8);

INSERT INTO favorite_foods (food, score)
VALUES ("Pizza", 10);

INSERT INTO favorite_foods (food, score)
VALUES ("Tuna Casserole", 2);

SELECT * FROM favorite_foods;

--

INSERT INTO favorite_songs (song, artist, score)
VALUES ("All you had to do was stay", "Taylor Swift", 8);

INSERT INTO favorite_songs (song, artist, score)
VALUES ("All the Stars", "Kendrick Lamar", 7);

INSERT INTO favorite_songs (song, artist, score)
VALUES ("Silence", "Illenium", 10);

INSERT INTO favorite_songs (song, artist, score)
VALUES ("Subeme la Radio", "Enrique Iglesias", 10);


SELECT * FROM favorite_songs;

--

INSERT INTO favorite_movies (movie, five_times, score)
VALUES ("Black Panther", true, 9),("Game Night", true, 10), ("A Wrinkle in Time", false, 2);

SELECT * FROM favorite_movies;

