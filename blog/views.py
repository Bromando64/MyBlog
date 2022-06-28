from datetime import date
from django.shortcuts import render


all_posts = [
    {
        "slug": "anime-girls",
        "image": "megumin.png",
        "author": "Nishant",
        "date": date(2021, 7, 21),
        "title": "Anime Girls",
        "excerpt": "There's nothing like the moment when you watch an anime girl and some eldrich being just sucks you into a void of nothing",
        "content": """
            Praesentium commodi voluptate id quis eaque dolore accusamus,
            illo tempore eos fugit optio, quibusdam est voluptate explicabo 
            veritatis nulla facilis quod reiciendis error, eaque natus repudiandae 
            sunt cupiditate? Rerum animi nihil ratione maiores ea sapiente. 
            Non earum facilis exercitationem beatae molestiae aliquid minima culpa repellendus laudantium quod, 
            consequatur quas quod minima. Aspernatur sint veniam eum nisi accusamus harum vitae sed consequatur laborum, 
            iste unde nostrum laboriosam quis excepturi veritatis, corporis aperiam obcaecati quasi unde 
            ipsum quam facilis assumenda labore ratione.

            Vitae temporibus alias corrupti eveniet repudiandae aspernatur expedita dicta, 
            dolor suscipit praesentium quo vero, vel vitae vero, voluptate saepe sunt reiciendis 
            natus exercitationem officiis, cupiditate error hic.

            Nobis beatae consequuntur perspiciatis fugiat accusantium itaque iusto nostrum commodi dolorum reiciendis, 
            inventore doloremque consequuntur consequatur libero, ut voluptatem voluptatum nulla, 
            perspiciatis similique expedita quas quaerat enim a quisquam repellat eius hic dignissimos, 
            praesentium amet cum libero vel numquam ea voluptatum molestiae culpa? Veritatis illum libero 
            eveniet iure molestias ex ipsa unde soluta officiis iste, cum laudantium facere eligendi fugit?
        """
    },
    {
        "slug": "yandare-girls",
        "image": "yandare.jpg",
        "author": "Nishant",
        "date": date(2022, 3, 10),
        "title": "Yandare Girls",
        "excerpt": "I love getting stabbed over 50 times by a yandare after walking past a guy who sligtly looked like an abomination that doesn't belong to this world.",
        "content": """
            Praesentium commodi voluptate id quis eaque dolore accusamus,
            illo tempore eos fugit optio, quibusdam est voluptate explicabo 
            veritatis nulla facilis quod reiciendis error, eaque natus repudiandae 
            sunt cupiditate? Rerum animi nihil ratione maiores ea sapiente. 
            Non earum facilis exercitationem beatae molestiae aliquid minima culpa repellendus laudantium quod, 
            consequatur quas quod minima. Aspernatur sint veniam eum nisi accusamus harum vitae sed consequatur laborum, 
            iste unde nostrum laboriosam quis excepturi veritatis, corporis aperiam obcaecati quasi unde 
            ipsum quam facilis assumenda labore ratione.

            Vitae temporibus alias corrupti eveniet repudiandae aspernatur expedita dicta, 
            dolor suscipit praesentium quo vero, vel vitae vero, voluptate saepe sunt reiciendis 
            natus exercitationem officiis, cupiditate error hic.

            Nobis beatae consequuntur perspiciatis fugiat accusantium itaque iusto nostrum commodi dolorum reiciendis, 
            inventore doloremque consequuntur consequatur libero, ut voluptatem voluptatum nulla, 
            perspiciatis similique expedita quas quaerat enim a quisquam repellat eius hic dignissimos, 
            praesentium amet cum libero vel numquam ea voluptatum molestiae culpa? Veritatis illum libero 
            eveniet iure molestias ex ipsa unde soluta officiis iste, cum laudantium facere eligendi fugit?
        """
    },
    {
        "slug": "help",
        "image": "help.jpg",
        "author": "Nishant",
        "date": date(2022, 6, 27),
        "title": "Help",
        "excerpt": "Its comming. I can't stop it. The figure is growing and its approaching me.",
        "content": """
            Praesentium commodi voluptate id quis eaque dolore accusamus,
            illo tempore eos fugit optio, quibusdam est voluptate explicabo 
            veritatis nulla facilis quod reiciendis error, eaque natus repudiandae 
            sunt cupiditate? Rerum animi nihil ratione maiores ea sapiente. 
            Non earum facilis exercitationem beatae molestiae aliquid minima culpa repellendus laudantium quod, 
            consequatur quas quod minima. Aspernatur sint veniam eum nisi accusamus harum vitae sed consequatur laborum, 
            iste unde nostrum laboriosam quis excepturi veritatis, corporis aperiam obcaecati quasi unde 
            ipsum quam facilis assumenda labore ratione.

            Vitae temporibus alias corrupti eveniet repudiandae aspernatur expedita dicta, 
            dolor suscipit praesentium quo vero, vel vitae vero, voluptate saepe sunt reiciendis 
            natus exercitationem officiis, cupiditate error hic.

            Nobis beatae consequuntur perspiciatis fugiat accusantium itaque iusto nostrum commodi dolorum reiciendis, 
            inventore doloremque consequuntur consequatur libero, ut voluptatem voluptatum nulla, 
            perspiciatis similique expedita quas quaerat enim a quisquam repellat eius hic dignissimos, 
            praesentium amet cum libero vel numquam ea voluptatum molestiae culpa? Veritatis illum libero 
            eveniet iure molestias ex ipsa unde soluta officiis iste, cum laudantium facere eligendi fugit?
        """
    }
]


def get_date(post):
    return post['date']

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts,
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    id_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": id_post
    })
