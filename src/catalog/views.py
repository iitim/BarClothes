from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from operator import itemgetter

def search(request, product_type, num):
    current_state = State(request.GET, product_type, num)
    if current_state.must_redirect():
        return redirect(current_state.get_redirect_path())
    context = init_context(current_state)
    context['all_product'], all_product_length = query_product(product_type,current_state)
    context['last_page'] = set_last_page(current_state, all_product_length)
    context['tags'] = query_tag()
    return render(request, 'catalog.html', context)

def init_context(current_state):
    context = {
        'page': current_state.page,
        'default_product_name': current_state.product_name,
        'default_seller_name': current_state.seller_name,
        'default_sort_type': current_state.sort_type,
        'search_path': current_state.get_search_path(),
    }
    if current_state.use_category_All():
        context['type'] = ''
    else:
        context['type'] = '/' + current_state.real_product_type
    return context

def query_product(product_type, current_state):
    if current_state.use_search_or_sort():
        user_list = User.objects.filter(username__icontains=current_state.seller_name)
        user_extend_data_list = UserExtendData.objects.filter(user__in=user_list)
        all_product = Product.objects.order_by(current_state.how_to_order_by())
        all_product = all_product.filter(seller__in=user_extend_data_list, name__icontains=current_state.product_name)
    else:
        all_product = Product.objects.order_by('-create_date')
    if not current_state.use_category_All():
        all_product = all_product.filter(type=product_type)
    #all_product = filter_by_tag(all_product)
    all_product = filter_out_of_product(all_product)
    all_product_length = len(all_product)
    all_product = all_product[current_state.first_product:current_state.last_product]
    return all_product, all_product_length

def filter_by_tag(all_product):
    all_product_filter = []
    tags = Tag.objects.all()
    for product in all_product:
        if set(tags).issubset(product.tags.all()):
            all_product_filter.append(product)
    return all_product_filter

def filter_out_of_product(all_product):
    all_product_filter = []
    for product in all_product:
        if product.remain() > 0:
            all_product_filter.append(product)
    return all_product_filter

def set_last_page(current_state, all_product_length):
    last_page = int(all_product_length / current_state.product_per_page)
    if all_product_length % current_state.product_per_page != 0:
        last_page += 1
    return last_page

def query_tag():
    tag_count = []
    for tag in Tag.objects.all():
        tag_count.append([tag,0])
    for product in Product.objects.all():
        index = 0
        for tag in product.tags.all():
            while tag != tag_count[index][0]:
                index += 1
            tag_count[index][1] += 1
            index += 1
    tag_count.sort(key=itemgetter(1), reverse=True)
    tag_context = []
    for tag in tag_count:
        tag_context.append(tag[0])
    return tag_context

def catalog(request, num='1'):
    return search(request, '', num)

def top(request, num='1'):
    return search(request, 'Top', num)

def jacket(request, num='1'):
    return search(request, 'Jac', num)

def dress(request, num='1'):
    return search(request, 'Dre', num)

def skirt(request, num='1'):
    return search(request, 'Ski', num)

def pants(request, num='1'):
    return search(request, 'Pan', num)

def shorts(request, num='1'):
    return search(request, 'Sht', num)

def tshirt(request, num='1'):
    return search(request, 'T-s', num)

def suits(request, num='1'):
    return search(request, 'Sui', num)

def bag(request, num='1'):
    return search(request, 'Bag', num)

def shoes(request, num='1'):
    return search(request, 'Sho', num)

def accessory(request, num='1'):
    return search(request, 'Acc', num)

class State:
    product_per_page = 18

    def __init__(self, request, product_type, num):
        self.request = request
        self.decode_request(request)
        self.real_product_type = self.decode_product_type(product_type)
        self.page = int(num)
        self.first_product = self.product_per_page * (self.page - 1)
        self.last_product = self.product_per_page * self.page

    def decode_request(self, request):
        if self.use_search_or_sort():
            self.product_name = request['product_name']
            self.seller_name = request['seller_name']
            self.sort_type = request['sort']
        else:
            self.product_name = ''
            self.seller_name = ''
            self.sort_type = ''

    def decode_product_type(self, product_type):
        if product_type != '':
            for choice in PRODUCT_TYPE_CHOICES:
                if choice[0] == product_type:
                    return choice[1]
        else:
            return ''

    def get_redirect_path(self):
        if self.use_category_All():
            return '/shop' + self.get_search_path()
        else:
            return '/shop/' + self.real_product_type + self.get_search_path()

    def get_search_path(self):
        if self.use_search_or_sort():
            return '/?product_name=' + self.product_name + '&seller_name=' + self.seller_name + '&sort=' + self.sort_type
        else:
            return ''

    def use_search_or_sort(self):
        return ('product_name' in self.request) and ('seller_name' in self.request) and ('sort' in self.request)

    def must_redirect(self):
        return (self.page < 1) or ('submit_search' in self.request)

    def use_category_All(self):
        return self.real_product_type == ''

    def how_to_order_by(self):
        if self.sort_type == 'low':
            return 'price'
        elif self.sort_type == 'high':
            return '-price'
        elif self.sort_type == 'old':
            return 'create_date'
        else:
            return '-create_date'