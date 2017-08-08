import media
import fresh_tomatoes

#Details of the movies that will show up on the website
the_avengers = media.Movie("The avengers",
                        "A group of super heros must overcome their relationship issues in order to protect the planed from an alien invasion",
                        "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                        "https://www.youtube.com/watch?v=eOrNdBpGMv8")

avatar = media.Movie("Avatar",
                     "Un soldado liciado se mete dentro del cuerpo clonado de un alienigena",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

matrix = media.Movie("Matrix",
                     "Un hombre comun que quiere saber la verdad de donde venimos las personas",
                     "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

prometheus = media.Movie("Prometheus",
                        "The quest for the human creators takes a group of cientifics to land full of death",
                        "https://upload.wikimedia.org/wikipedia/en/a/a3/Prometheusposterfixed.jpg",
                        "https://www.youtube.com/watch?v=34cEo0VhfGE")

interestellar =  media.Movie("Interestellar",
                        "Trying to save humanity from starbing a grup of people travel to the unknown",
                        "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                        "https://www.youtube.com/watch?v=zSWdZVtXT7E")

inception =  media.Movie("Inception",
                        "To find a way to go back home, this man will try an almost impossible mission",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")


#The array of the movies that will show up on the website
movies = [the_avengers, avatar, matrix, prometheus, interestellar, inception]

#The inicialization of the program
fresh_tomatoes.open_movies_page(movies)
