from django.contrib import admin
from django.urls import path, include
from . views import*

from cassandra.cluster import Cluster
cluster = Cluster(['127.0.0.1'], control_connection_timeout=10,  port=9042)
session = cluster.connect('tutorialspoint')
try:
    # query = session.execute("""ALTER TABLE example_model DROP emp_email""")
    # print('query', query)
    query = session.execute("ALTER TABLE user_model DROP profile")
    print('query', query)
except:
    pass

urlpatterns = [
    path('', homepage, name='home'),
    path('test', TestView.as_view(), name='test'),
    # path('overview', overview, name='overview'),

    # api 
    path('user_register', UserRegisterView.as_view(), name='user_register'),
    path('user_update/<str:id>/', UserUpdateView.as_view(), name='user_update'),
]
