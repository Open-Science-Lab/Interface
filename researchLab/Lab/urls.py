from unicodedata import name
from . import views
from django.urls import path
from .views import ExperimentViewSet, UserRegisterAPI,SignInAPI,OperationViewSet,StreamViewSet
    
urlpatterns=[
    path('',views.index,name='index'),
    path('people/',views.people,name='people'),
    path('research/',views.research,name='instrumentation'),
    path('publication/',views.publication,name='publication'),
    path('gallery/',views.gallery,name='gallery'),
    path('news/',views.news,name='news'),
    path('teaching/',views.teaching,name='teaching'),
    path('contact/',views.contact,name='contact'),
    path('registration/',views.registration,name='registration'),
    path('login/',views.login,name='login'),
    # path('expirement/',views.expirement,name='expirement'),
    path('work/',views.work,name="work"),
    path('useLab/',views.useLab,name='use'),
    path('demo/',views.demo,name='demo'),
    path('logout/',views.logout,name="logout"),
    path('dequeue/',views.dequeue,name='dequeue'),

    # peak from the queue
    path('peak/',views.peak,name='peak'),


     # refined pages
     path('work1/',views.work1,name='work1'),
     path('use1/',views.use1,name="use1"),
     path('research1/',views.research1,name='instrumentation1'),
     path('expirement1/',views.expirement1,name="expirement1"),


     # beakerTest
     path('beaker/',views.beakerTest,name='beakerTest'),

          # rest apis
      path('userRegister/', UserRegisterAPI.as_view(), name='userRegister'),
      path('userlogin/',SignInAPI.as_view(),name="userLogin"),

       

       # VERSION-2 URLS

       path('expirementVer2/',views.expirementVer2,name='expirementVer2'),
       path('msg/',views.msg,name='msg'),


      # operations rest urls

       path('operations/', OperationViewSet.as_view({
        'get':'list',
        'post':'create'
        
    })),

    path('operations/<str:pk>',OperationViewSet.as_view({
        'get':'retrive',
        'put':'update',
        'delete':'delete'
    })),


    # video stream rest urls

      path('streams/', StreamViewSet.as_view({
        'get':'list',
        'post':'create'
        
    })),

    path('streams/<str:pk>',StreamViewSet.as_view({
        'get':'retrive',
        'put':'update',
        'delete':'delete'
    })),


     # video stream rest urls

      path('experiment/', ExperimentViewSet.as_view({
        'get':'list',
        'post':'create'
        
    })),

    path('experiment/<str:pk>',ExperimentViewSet.as_view({
        'get':'retrive',
        'put':'update',
        'delete':'delete'
    })),

   
  
]