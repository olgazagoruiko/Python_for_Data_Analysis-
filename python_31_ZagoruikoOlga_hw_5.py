import os.path
import requests # використовується, щоб зробити запит і отримати файл
import collections
import itertools

# Вітаю!
# Варіант-1 - це те, що мені вдалося зробити самостійно.
# Варіант 2 - повністю розібрала  по відео, яке  ви надіслали.
# Відверто кажучи, 5 завдання нізащо не зробила б без допомоги.

# Варіант-1.

# 1. ЗАВАНТАЖЕННЯ ДАНИХ

# def download_document(file_name, document_url):
#     if os.path.exists(file_name):
#         pass
#     else:
#         response=requests.get(document_url)
#         if response.status_code==200:
#             with open(file_name,'wb') as file:
#                 file.write(response.content)
#         else:
#             print(f"Failed to download the document. Status code: {response.status_code}")
#
# file_name='orders.txt'
# document_url='https://drive.google.com/uc?id=1IOPTVq2ooQfZRkF3rAjGkTjRtbotG7FF'
#
#
# download_document(file_name,document_url)
#
# # 2. ЧИТАННЯ ТА ОБРОБКА ДАНИХ

# with open('orders.txt','r',encoding='utf-8') as file:
#     data_lines=file.readlines()
#     data_orders=[]
#     for line in data_lines:
#         if line.strip()!='':
#             order=line.strip().split('@@@')
#             # print(oder)
#             data_orders.append(order)
#
# # print(f"Кількість замовлень: {len(data_orders)}") #Довжина списку із замовленнями
#
# # 3. СЛОВНИК З КІЛЬКІСТЮ КОЖНОГО ПРОДУКТУ
#
# # def dict_prod_count(list_orders):
# #     list_all_products=list((itertools.chain.from_iterable(list_orders)))
# #     # print(list_all_orders)
# #     print("f Кількість унікальних товарів: {len(set(list_all_product))}")#Кількість унікальних товарів
# #     print(len(dict(collections.Counter(list_all_products))))# Кількість унікальних товарів 2-й спосіб
# #     return dict(collections.Counter(list_all_products))
#
# # print(dict_prod_count(data_orders))
#
# #4. CЛОВНИК ПІДРАХУНКУ КОЖНОЇ ПАРИ ПРОДУКТУ
#
# def dict_prod_pair_count(list_orders):
#     prod_pair_count=[]
#     for i in range(len(list_orders)):
#         prod_pairs=list(itertools.combinations(list_orders[i],2))
#         for j in range(len(prod_pairs)):
#             sort_prod_pair=sorted(prod_pairs[j])
#             prod_pair_count.append(sort_prod_pair)
#     print(len(prod_pair_count))
#     all_prod_pair_count=[tuple(elem) for elem in prod_pair_count]
#     print(len(all_prod_pair_count)) # Кількість створених пар
#     print(len(dict(collections.Counter(all_prod_pair_count))))# Кількість унікальних пар
#     return dict(collections.Counter(all_prod_pair_count))
#
#
# print(dict_prod_pair_count(data_orders))


# 5. ВИКОРИСТАЙТЕ ДВА СЛОВНИКИ, ЩОБ РОЗРАХУВАТИ ВПЕВНЕНІСТЬ ДЛЯ КОЖНОЇ ПАРИ ПРОДУКТІВ
# ???


# Варіант-2 (по відео)

# 1. ЗАВАНТАЖЕННЯ І ПАРСИНГ ДАНИХ

def download_document(file_name, document_url):
    if os.path.exists(file_name):
        pass
    else:
        response=requests.get(document_url)
        if response.status_code==200:
            with open(file_name,'wb') as file:
                file.write(response.content)
        else:
            print(f"Failed to download the document. Status code: {response.status_code}")


file_name='orders.txt'
document_url='https://drive.google.com/uc?id=1IOPTVq2ooQfZRkF3rAjGkTjRtbotG7FF'

download_document(file_name,document_url)

#  ПАРСИНГ!!!

def from_file_to_list(file_name, orders_sep='\n\n', product_sep='@@@'):
    with open(file_name,'r') as f:
        orders=f.read().split(orders_sep)
    for i in range(len(orders)):
        orders[i]=orders[i].strip().split(product_sep)
    print (f"Prepared {len(orders)} orders with product lists")
    return orders

orders_list=from_file_to_list(file_name)
# print (orders_list[:3])

# 2. СЛОВНИК ПРОДУКТІВ

def get_counted_product_dict(orders):
    products=[]
    for o in orders:
        products.extend(o)
    products_dict=dict(collections.Counter(products))
    print (f"Products were counted. Number of unique product={len(products_dict)}")
    return  products_dict

ordered_products=get_counted_product_dict(orders_list)
# print(ordered_products)

# 3. СЛОВНИК ПАР ПРОДУКТІВ (РОЗРАХУНОК ПІДТРИМКИ)

def get_pair_combos(orders):
    product_pairs={}
    for o in orders:
        unique_products=list(set(o))
        unique_combination=(itertools.combinations(unique_products,2))

        for unq_combo in unique_combination:
            pair_list=list(unq_combo)
            pair_list.sort()
            pair_key='<=>'.join(pair_list)
            key_value=product_pairs.setdefault(pair_key,0)
            product_pairs[pair_key]=key_value+1

    n=len(list(product_pairs.keys()))
    print(f'Found {n} pairs of products in {len(orders)} orders')
    return product_pairs


product_pairs=get_pair_combos(orders_list)
# print(product_pairs)

# 4. ОБЧИСЛЕННЯ ПОКАЗНИКА ВПЕВНЕНОСТІ ДЛЯ ПРОДУКТІВ
#
# фУНКЦІЯ РОЗРАХУНКУ ВПЕВНЕНОСТІ

def get_confidence(n_orders_with_pair, n_orders_with_X):
    return round(n_orders_with_pair/n_orders_with_X*100,2)

# ФУНКЦІЯ ЩО ВИЗНАЧАЄ, ЧИ ПРОХОДИТЬ ПАРА MIN_SUPPORT

def get_product_pair_result(current_support, product_X, product_Y, ordered_products, min_confidence, product_index):
    n_product_X_orders=ordered_products[product_X]
    current_confidence=get_confidence(current_support, n_product_X_orders)
    if current_confidence>=45:
        key=f'{product_X}=>{product_Y}'
        return {key: (current_support, current_confidence, product_index)}
    else:
        return{}


# РОЗРАХУНОК ПОКАЗНИКА ВПЕВНЕНОСТІ ДЛЯ ПРОДУКТІВ

def get_pair_with_limits(product_pairs, ordered_products,min_support=15, min_confidence=45):
    result_dict={}
    for k,current_support in product_pairs.items():
        if current_support>=min_support:
            p=k.split('<=>')
            result_dict.update(
                get_product_pair_result(current_support,p[0],p[1],ordered_products, min_confidence,'p1'))
            result_dict.update(
                get_product_pair_result(current_support, p[1], p[0], ordered_products, min_confidence, 'p2'))
    print(
        f'According to min support={min_support} and min confidence={min_confidence}%, prepared {len(list(result_dict.keys()))} pairs of product')

    return  result_dict


limited_pairs=get_pair_with_limits(product_pairs,ordered_products)
# print(limited_pairs)


# ДЕМОНСТРАЦІЯ РЕЗУЛЬТАТІВ
def show_results(result_dict):
    i=1
    for k, (support, confidence, product_index) in result_dict.items():
        print(f'{i}. {product_index} {k} ({confidence:.2f}% confidence, {support} support)')
        i+=1
show_results(limited_pairs)
