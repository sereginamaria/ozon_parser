import requests


def send_post(**kwargs):
    print(kwargs['category'])
    print(kwargs['sub_category'])
    print('Hello from {kw}'.format(kw=kwargs['my_keyword']))

    new_product = {
        "category": kwargs['category'],
        "sub_category": kwargs['sub_category']
    }

    requests.post("http://127.0.0.1:5000/send_post", json=new_product)