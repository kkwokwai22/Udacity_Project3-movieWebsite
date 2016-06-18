import media
import fresh_tomatoes


spiderman = media.Movie("Spider Man 2",
                        "A  person who became a hero from a spider bite",
                        "http://vignette1.wikia.nocookie.net/toonami/images/e/eb/The_Amazing_Spider-Man_2.jpg",
                        "https://www.youtube.com/watch?v=DlM2CWNTQ84")

hunger_game = media.Movie("Hunger game",
                          "A girl who got put into a battle",
                          "http://ia.media-imdb.com/images/M/MV5BMjA4NDg3NzYxMF5BMl5BanBnXkFtZTcwNTgyNzkyNw@@._V1_SX640_SY720_.jpg",
                          "https://www.youtube.com/watch?v=n-7K_OjsDCQ")

frozen = media.Movie("Frozen",
                     "The film tells the story of a fearless princess who sets off on an epic journey al winter.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Frozen_%282013_film%29_poster.jpg/220px-Frozen_%282013_film%29_poster.jpg",
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")

lord_of_the_ring = media.Movie("Lord of the Ring",
                               "The future of civilization rests in the fate of the One Ring, which has been lost for centuries. \
                               Powerful forces are unrelenting in their search for it. But fate has placed it in the hands of a \
                               young Hobbit named Frodo Baggins (Elijah Wood), who inherits the Ring and steps into legend. A daunting task lies ahead for Frodo when he becomes the Ringbearer - \
                               to destroy the One Ring in the fires of Mount Doom where it was forged.",
                               "http://img2.wikia.nocookie.net/__cb20070806215413/lotr/images/8/87/Ringstrilogyposter.jpg",
                               "https://www.youtube.com/watch?v=V75dMMIW2B4")

deathpool = media.Movie("Deathpool",
                        "A super hero who is like a ninji",
                        "http://static1.squarespace.com/static/53323bb4e4b0cebc6a28ffa2/55992e15e4b040c14b12724f/55992e15e4b0eb5f8383b7b5/1436102166447/deadpool-promopic.jpg",
                        "https://www.youtube.com/watch?v=FyKWUTwSYAs")

good_dinosaur = media.Movie("Good Dinosaur",
                            "a dinosaur who got lost",
                            "http://i.kinja-img.com/gawker-media/image/upload/s--hrzNuDsV--/c_scale,fl_progressive,q_80,w_800/194ejrsupsajijpg.jpg",
                            "https://www.youtube.com/watch?v=daFnEiLEx70"
                            )



movies = [spiderman,hunger_game, frozen,lord_of_the_ring,deathpool,good_dinosaur]
# this array is for all the movie on top to be open
fresh_tomatoes.open_movies_page(movies)
# this function is to open website






