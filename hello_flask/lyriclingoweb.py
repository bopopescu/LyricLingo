#!/usr/bin/env python

from flask import Flask, render_template


# Create the application.
APP = Flask(__name__)

with open("../translated_lyrics.txt", "r") as f:
    content = f.read()
    songs = []
    songs = content.split("*[")
    songs.remove('')
    
    titles = []
    for song in songs:
        x = song.split("\n")
        titles.append(x[0])


    # Formatting title
    for i in range(len(titles)):
        titles[i] = titles[i][:-1]

    # Formatting song lyrics
    for i in range(len(songs)):
        songs[i] = songs[i].replace("]", "", 1)
        


with open("../original_lyrics.txt", "r") as f:
    contentO = f.read()
    songsO = []
    songsO = contentO.split("*[")
    songsO.remove('')
    
    titlesO = []
    for songO in songsO:
        xO = songO.split("\n")
        titlesO.append(xO[0])


    # Formatting title
    for i in range(len(titlesO)):
        titlesO[i] = titlesO[i][:-1]

    # Formatting song lyrics
    for i in range(len(songsO)):
        songsO[i] = songsO[i].replace("]", "", 1)
        
   # print(titlesO)


@APP.route("/")
def index():
    """ Displays the index page accessible at '/'
    """
    return render_template("index.html", content=songs, titles=titles, contentO=songsO, titlesO=titlesO)


@APP.route('/spanish/')
def spanish():
    return render_template('spanish.html', content=songs, titles=titles, contentO=songsO, titlesO=titlesO)

@APP.route('/song0/')
def song0():
    return render_template('song0.html', content=songs, titles=titles, contentO=songsO, titlesO=titlesO)
    
@APP.route('/song1/')
def song1():
    return render_template('song1.html', content=songs, titles=titles, contentO=songsO, titlesO=titlesO)
    
@APP.route('/song2/')
def song2():
    return render_template('song2.html', content=songs, titles=titles, contentO=songsO, titlesO=titlesO)
    
@APP.route('/song3/')
def song3():
    return render_template('song3.html', content=songs, titles=titles, contentO=songsO, titlesO=titlesO)

@APP.route('/song4/')
def song4():
    return render_template('song4.html', content=songs, titles=titles, contentO=songsO, titlesO=titlesO)

@APP.route('/song5/')
def song5():
    return render_template('song5.html', content=songs, titles=titles, contentO=songsO, titlesO=titlesO)
    
@APP.route('/song6/')
def song6():
    return render_template('song6.html', content=songs, titles=titles, contentO=songsO, titlesO=titlesO)
    
@APP.route('/song7/')
def song7():
    return render_template('song7.html', content=songs, titles=titles, contentO=songsO, titlesO=titlesO)

@APP.route('/english/')
def english():
    return render_template('english.html', content=songs, titles=titles, contentO=songsO, titlesO=titlesO)
   
@APP.route('/song0E/')
def song0E():
    return render_template('song0E.html', content=songs, titles=titles, contentO=songsO, titlesO=titlesO)
    
@APP.route('/song1E/')
def song1E():
    return render_template('song1E.html', content=songs, titles=titles, contentO=songsO, titlesO=titlesO)
    
@APP.route('/song2E/')
def song2E():
    return render_template('song2E.html', content=songs, titles=titles, contentO=songsO, titlesO=titlesO)
    
@APP.route('/song3E/')
def song3E():
    return render_template('song3E.html', content=songs, titles=titles, contentO=songsO, titlesO=titlesO)

@APP.route('/song4E/')
def song4E():
   return render_template('song4E.html', content=songs, titles=titles, contentO=songsO, titlesO=titlesO)

@APP.route('/song5E/')
def song5E():
    return render_template('song5E.html', content=songs, titles=titles, contentO=songsO, titlesO=titlesO)
    
@APP.route('/song6E/')
def song6E():
    return render_template('song6E.html', content=songs, titles=titles, contentO=songsO, titlesO=titlesO)
    
@APP.route('/song7E/')
def song7E():
    return render_template('song7E.html', content=songs, titles=titles, contentO=songsO, titlesO=titlesO)



if __name__ == '__main__':
    APP.run(debug=True)