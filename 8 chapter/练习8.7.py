def make_album(artist, title, number=None):
      album= {'artist': artist, 'title': title}
      if number:
                album['number'] = number
      return album
while True:
        print('\n please enter the album information:')
        print('enter "q" at any time to quit.')
        artist = input('artist name:')
        if artist.lower() == 'q':
                break
        title = input('album title:')
        if title.lower() == 'q':
                break
        number = input('number of songs:')
        print('\nthe album information is as follows:')
        for key, value in make_album(artist, title, number).items():
                print(f"{key.title()}: {value}")
        