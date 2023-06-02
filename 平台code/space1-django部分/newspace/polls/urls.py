from django.urls import path


from polls import views
urlpatterns=[
    path('', views.toLogin_view),
    path('index/',views.Login_view),
    path('toregister/',views.toregister_view),  # 在polls中进入
    path('toforget/',views.toforget_view),  # 在polls中进入
    path('register/',views.register_view),
    path('tosuccess/',views.tosuccess_view),
    path('success/',views.success_view),
    path('success/tohelp/',views.tohelp_view),
    path('help/',views.help_view),
    path('success/tomy/',views.tomy_view),
    path('my/',views.my_view),
    path('success/tonewguide/', views.tonewguide_view),
    path('newguide/', views.newguide_view),
    path('success/toshuju/', views.toshuju_view),
    path('shuju/', views.shuju_view),
    path('success/toknow/', views.toknow_view),
    path('know/', views.know_view),
    path('yusuan/', views.yusuan_view),
    path('zme/', views.zme_view),
    path('China/', views.China_view),
    path('zm/', views.zm_view),
]