'''Posts views'''
# Django
from django.http import HttpResponse
from django.shortcuts import render

# Utilities
from datetime import datetime

posts = [
    {
        'title': 'Arduino Wall-E',
        'user': {
            'name': 'Nicolás Albo',
            'picture': 'http://www.nicolasalbo.com/images/hero.png',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'http://www.nicolasalbo.com/images/walle_closeup.jpg',  
    },
    {
        'title': 'Festival de la canción',
        'user': {
            'name': 'Héktar',
            'picture': 'https://instagram.fgdl1-4.fna.fbcdn.net/v/t51.2885-19/s320x320/94711575_229477848498850_1437641075706560512_n.jpg?_nc_ht=instagram.fgdl1-4.fna.fbcdn.net&_nc_ohc=pYjKvYFzi-UAX-Q2VfI&oh=82658dc6f4ddf605bdf0e0c5b46b84ce&oe=5F209D98',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://instagram.fpbc1-2.fna.fbcdn.net/v/t51.2885-15/e35/s1080x1080/92246349_925535884569673_4901783389551597207_n.jpg?_nc_ht=instagram.fpbc1-2.fna.fbcdn.net&_nc_cat=101&_nc_ohc=Wfier7TP8HUAX_2oJgM&oh=f06f2f3823b42960c097440942be6d89&oe=5F1FC751',  
    },
    {
        'title': 'Photoshoot',
        'user': {
            'name': 'Vale <3',
            'picture': 'https://instagram.fgdl1-4.fna.fbcdn.net/v/t51.2885-19/s320x320/101795743_1760779007396842_3478098287628648448_n.jpg?_nc_ht=instagram.fgdl1-4.fna.fbcdn.net&_nc_ohc=x3SkTqPwjfgAX9hndpd&oh=e51e624ed6b78b80b0af03e8d9594b45&oe=5F22C845',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://instagram.fzih1-1.fna.fbcdn.net/v/t51.2885-15/e35/79388982_451792518866774_7112466628630035668_n.jpg?_nc_ht=instagram.fzih1-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=W8yLh3_1DlAAX9M6u3U&oh=c2aa5c18655fbb711283143132cebcf6&oe=5F23718F',  
    },
]

def list_posts(request):
    '''List existing posts'''
    return render(request, 'posts/feed.html', {'posts': posts})