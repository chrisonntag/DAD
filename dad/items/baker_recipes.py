from model_bakery.recipe import Recipe, foreign_key, related
from .models import Exhibition, MediaType, Item, Favorite, Like, Comment
from django.contrib.auth.models import User
from datetime import datetime
from model_bakery.random_gen import gen_email, gen_text


user_ad = Recipe(
    User,
    username=gen_email,
    email=gen_email,
    password='hihi123',
)

user_el = Recipe(
    User,
    username=gen_email,
    email=gen_email,
    password='ohymgos5',
)

exhibition_artscape = Recipe(
        Exhibition,
        name='ArtScape',
        description='The ArtScape is a multidisciplinary festival that showcases the best in contemporary visual art, film, and new media. The festival takes place over a week and features a diverse array of exhibitions, screenings, workshops, and talks from emerging and established artists from around the world. The festival is designed to be inclusive, engaging and accessible, with a focus on fostering connections between artists, audiences, and creative communities.'
)

media_img = Recipe(
        MediaType,
        description='A digital file that contains visual content that can be shown on a computer or other digital device.',
        media_type_name='IMAGE'
)

item_fourtytwo = Recipe(
        Item,
        name='The Meaning of 42: A Video Installation',
        description='This thought-provoking video installation explores the significance and symbolism of the number 42. Through a series of mesmerizing projections and immersive soundscapes, viewers are transported on a journey that delves into the cultural, mathematical, and philosophical significance of this enigmatic number. From its appearance in science fiction literature to its role in mathematics and physics, the installation leads the audience to question the importance of 42 in our understanding of the world. With its striking visual and audio effects, this installation is not just a feast for the senses, but also a stimulating exploration of the mysteries of the universe. It\'s a must-see for any visitors of the ArtScape Festival who are seeking an intellectually stimulating and visually striking experience.',
        part_of=foreign_key(exhibition_artscape),
        type_of=foreign_key(media_img),
        digital_copy='myimg.jpg'
)


item_echoes = Recipe(
        Item,
        name='Echoes of Time',
        description='Echoes of Time is an evocative oil painting that explores the passage of time and its impact on our lives. The painting features a series of overlapping, abstract shapes that seem to be in a constant state of flux, creating a sense of movement and change. The use of rich, warm colors and bold brushstrokes creates a sense of depth and complexity, drawing the viewer into the painting and inviting them to explore its many layers. The artists use of light and shadow adds to the sense of movement and change, creating a sense of timelessness. The painting is both mesmerizing and thought-provoking, a must-see for any visitors of the ArtScape Festival who appreciate contemporary abstract art.',
        part_of=foreign_key(exhibition_artscape),
        type_of=foreign_key(media_img),
        related_to=related(item_fourtytwo),
        digital_copy='myimg_echoes.jpg'
)

fav = Recipe(
        Favorite,
        user=foreign_key(user_ad),
        item=foreign_key(item_echoes),
        date=datetime.now()
)

comment_el = Recipe(
        Comment,
        user=foreign_key(user_el),
        item=foreign_key(item_echoes),
        title='Marvelous work',
        content='Echoes of Time is a truly captivating piece. The way she uses color and brushstrokes to convey a sense of movement and change is truly masterful. It\'s a powerful reminder of the passage of time and its impact on our lives. I was struck by the depth and complexity of the painting, it\'s definitely a must-see for any art lover visiting the ArtScape Festival.',
        date=datetime.now()
)




