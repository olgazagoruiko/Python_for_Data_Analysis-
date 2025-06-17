import os.path
import requests
import pandas as pd



# 1. ЗАВАНТАЖЕННЯ ДАНИХ ТА ЗЧИТУВАННЯ У DataFrame

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


file_name='movies.csv'
document_url='https://gist.githubusercontent.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea/raw/0c794a9717f18b094eabab2cd6a6b9a226903577/movies.csv'

download_document(file_name,document_url)
##df_movies=pd.read_table('movies.csv')
df_movies=pd.read_csv('movies.csv')
pd.set_option('display.max_columns', None) # щоб було видно всі колонки
df_movies.drop_duplicates() # вилучаємо дублікати, тобто рядки, які повністю ідентичні
print(df_movies.head(10))

# 2.Перерахуйте всі стовпці набору даних та вивчіть їх типи.
# Вивчіть статистику з різних областей. Опишіть, які дані ми маємо


print(df_movies.info()) # отримання загальної інформації по dataframe
# Можна побачити кількість ненульових значень в кожному стовпчику (77), тип даних кожного стовпчика,
# скільки всього рядків та стовпців має dataframe, який об'єм пам'яті займає

# Окремо можемо вивести:
# df_movies.columns #  назви стовпців
print(f'Список колонок, які є в dataframe movies:  {df_movies.columns}')

# # df_movies.dtypes # тип даних для кожного стовпчика
print(f'Виводимо тип даних кожної колонки:\n{df_movies.dtypes}')

# # df_movies.shape # кількість рядків і стовпчиків у нашому dataframe
print(f'Кількість рядків: {df_movies.shape[0]}, Кількість стовпчиків: {df_movies.shape[1]}')

# # df_movies.size # загальну кількість значень в наборі даних
print(f'Зальна кількість значень в наборі даних становить: {df_movies.size}')

# Статистичний опис даних по стовпцям, що відображають числові характеристики
print(f'Статистиний опис даних:\n {df_movies.describe()}')

# 3. Скільки всього фільмів у наборі даних?

# print(f'Кількість унікальних значень, тобто фільмів у колонці "Film": {len(df_movies['Film'].unique())} ')
# print(f'Кількість ненульових значень у колонці "Film: {df_movies['Film'].count()} ')
# print(f'Кількість повторів кожного фільму у колонці "Film": \n{df_movies['Film'].value_counts()}')

# 4. Скільки фільмів міститься у наборі даних за кожен рік?

# 1-й спосіб
# print(f'Кількість фільмів у наборі даних для кожного року: \n {df_movies['Year'].value_counts()}')

# # 2-й спосіб
# group_by_year=df_movies.groupby('Year') # Групування рядків за значенням у стовпчику 'Year'
# print(f'Кількість фільмів у  наборі даних за кожен рік буде становити: \n {group_by_year['Film'].count()}')

# # 3-й спосіб
# print(f'Кількість фільмів за кожен рік: \n {df_movies.groupby('Year').agg({'Film': 'count'})}')

# 5. Покажіть детальну інформацію про найменш і найприбутковіші фільми в наборі

#Найбільш прибутковий фільм
print('-------')
# print(f'Найбільш прибутковий фільм:\n{df_movies[df_movies['Profitability']==df_movies['Profitability'].max()]}')
# #Найменш прибутковий фільм
# print('-------')
# print(f'Найменш прибутковий фільм:\n{df_movies[df_movies['Profitability']==df_movies['Profitability'].min()]}')
# print('-------')
# TOP 5 найбільш прибуткових фільмів в dataframe
# print(f'TOP 5 найбільш прибуткових фільмів:\n{df_movies.nlargest(n=5,columns='Profitability')}')
# # print('-------')
# # TOP 5 найменш прибуткових фільмів
# print(f'TOP 5 найменш прибуткових фільмів:\n{df_movies.nsmallest(n=5,columns='Profitability')}')

# Через сортування
##Найбільш прибутковий фільм
# print(df_movies.sort_values('Profitability',ascending=False).head(1))
# print('-------')
##Найменш прибутковий фільм
# print(df_movies.sort_values('Profitability').head(5))
# # print('-------')


# 6. Значення "Жанр" часом здається непослідовним;
# спробуйте знайти ці невідповідності та виправити їх

##Виведемо список жанрів у стовпчику "Genre"
# print(df_movies['Genre'].unique())
## Проаналізувавши результат виведення, бачимо, що в деяких назвах жанрів припустилися помилки.
## Отже, потрібно виконати заміну:
# 'Comdy' на 'Comedy'
# 'comedy' на 'Comedy'
# 'Romence' на 'Romance'
# 'romance' на 'Romance'
# # Виконаємо послідовно заміни
# df_movies=df_movies.replace(to_replace=['Comdy','comedy'],value='Comedy')
# df_movies=df_movies.replace(to_replace=['Romence','romance'],value='Romance')
# print('-------')
# print(df_movies['Genre'].unique()) # Перевірка чи відбулася заміна

# 7. Збережіть(у новий файл  CSV) 10 найкращих комедій за кількістю глядачів;
# покажіть лише назву фільму, рік та студію

# 1 спосіб
# Виберемо 10 найкращих комедій за оцінкою  глядачів
# df_movies_the_best_full=df_movies[df_movies['Genre']=='Comedy'].nlargest(n=10,columns='Audience score %')
# print(df_movies_the_best_full)
# print('----------')
# df_movies_best_short=df_movies_the_best_full[['Film','Lead Studio','Year']]
# print(f' Фільми-комедії, top 10: \n {df_movies_best_short}')
# print('----------')

# df_movies_best_short.to_csv('movies_best.csv') # зберігаю в поточному каталозі

# 2 спосіб вибору 10 найкращих комедій за оцінкою  глядачів
# print(df_movies[df_movies['Genre'].isin(['Comedy'])].nlargest(n=10,columns='Audience score %').loc[:,['Film','Lead Studio','Year']])