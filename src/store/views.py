from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from operator import attrgetter, itemgetter
from main.models import *
from django.contrib.auth.models import User

def store(request, num='1'):
    current_state = State(request.GET, num)
    if current_state.must_redirect():
        return redirect(current_state.get_redirect_path())
    context = init_context(current_state)
    context['all_store'], all_store_length = query_store(current_state)
    context['last_page'] = set_last_page(current_state, all_store_length)
    return render(request, 'store_catalog.html', context)

def init_context(current_state):
    context = {
        'page': current_state.page,
        'default_seller_name': current_state.seller_name,
        'search_path': current_state.get_search_path(),
    }
    return context

def query_store(current_state):
    all_store = filter_user_can_sell(current_state.seller_name)
    all_store_length = len(all_store)
    all_store = all_store[current_state.first_store:current_state.last_store]
    return all_store, all_store_length

def filter_user_can_sell(seller_name):
    all_user_list = User.objects.filter(username__icontains=seller_name)
    all_user_extend_data_list = UserExtendData.objects.filter(user__in=all_user_list)
    filter_username = []
    for user_extend_data in all_user_extend_data_list:
        if user_extend_data.can_sell():
            filter_username.append(user_extend_data.user.username)
    filter_user_list = User.objects.filter(username__in=filter_username)
    filter_user_extend_data_list = UserExtendData.objects.filter(user__in=filter_user_list)
    return filter_user_extend_data_list

def set_last_page(current_state, all_store_length):
    last_page = int(all_store_length / current_state.store_per_page)
    if all_store_length % current_state.store_per_page != 0:
        last_page += 1
    return last_page

def store_detail(request): #num
    store_extend = get_object_or_404(UserExtendData, id_num=1000000000000)
    store = store_extend.user
    products = store_extend.product_set.all()

    products_latest = sorted(products, key=attrgetter('create_date'), reverse=True)
    products_oldest = sorted(products, key=attrgetter('create_date'))
    products_lowest_price = sorted(products, key=attrgetter('price'))
    products_highest_price = sorted(products, key=attrgetter('price'), reverse=True)

    context = {
        'store': store,
        'products_latest': products_latest,
        'products_oldest': products_oldest,
        'products_lowest_price': products_lowest_price,
        'products_highest_price': products_highest_price
    }
    return render(request, 'store_detail.html', context)

class State:
    store_per_page = 18

    def __init__(self, request, num):
        self.request = request
        self.decode_request(request)
        self.page = int(num)
        self.first_store = self.store_per_page * (self.page - 1)
        self.last_store = self.store_per_page * self.page

    def decode_request(self, request):
        if self.use_search():
            self.seller_name = request['seller_name']
        else:
            self.seller_name = ''

    def get_redirect_path(self):
        return '/store' + self.get_search_path()

    def get_search_path(self):
        if self.use_search():
            return '/?seller_name=' + self.seller_name
        else:
            return ''

    def use_search(self):
        return 'seller_name' in self.request

    def must_redirect(self):
        return (self.page < 1) or ('submit_search' in self.request)