from django.conf import settings
from random import choice
from string import ascii_letters, digits

# Try to get the value from the settings module
SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 7)
rand_urls = ascii_letters + digits

def randomed(chars=rand_urls):

    return "".join(
        [choice(chars) for _ in range(SIZE)]
    )

def shorted_url(m_i):
    random_code = randomed()
    model_class = m_i.__class__
    if model_class.objects.filter(url_second=random_code).exists():

        return shorted_url(m_i)

    return random_code