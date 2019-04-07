from django.urls import path,include
from . import views

app_name='pblog'
urlpatterns = [
    # 主页
    path('',views.mhome,name='home'),
    # 文章详情
    path('detail/<article_id>',views.mdetail,name='detail'),
    # 登陆
    path('login/',views.mlogin,name='login'),
    # 注册
    path('register/',views.mregister,name='register'),
    # 登出
    path('logout/',views.mlogout,name='logout'),
    #写文章
    path('edit/',views.medit,name='edit'),
    #写评论
    path('comment/',views.mcomment,name='comment'),
    #个人中心
    path('usercenter/',views.musercenter,name='usercenter'),
    #我的文章
    path('myarticle/',views.myarticle,name='myarticle'),
    #我的资料信息
    path('myinfo/',views.myinfo,name='myinfo'),
    #我的相册
    path('myalbum/',views.myalbum,name='myalbum'),
    #相册详细页
    path('albumdetail/<album_id>',views.malbumdetail,name='albumdetail'),
    #图片详细页
    path('photodetail/<photo_id>',views.mphotodetail,name='photodetail'),
    #添加图片
    path('addphoto/<album_id>',views.maddphoto,name='addphoto'),
    #修改文章
    path('changearticle/<article_id>',views.mchangearticle,name='changearticle'),
    #删除文章
    path('deletearticle/<article_id>',views.mdeletearticle,name='deletearticle'),
    #删除评论
    path('deletecomment/<comment_id>',views.mdeletecomment,name='deletecomment'),
    #修改个人资料
    path('changeinfo/',views.mchangeinfo,name='changeinfo'),
    #动态页面
    path('publish/',views.mpublish,name='publish'),
    # 删除相册
    path('deletealbum/<album_id>',views.mdeletealbum,name='deletealbum'),
    # 删除照片
    path('deletephoto/<photo_id>',views.mdeletephoto,name='deletephoto'),
    # 搜索文章
    path('search/<keywords>',views.msearch,name='articlesearch'),
    # 搜索
    path('search/',views.msearch,name='search'),
    # 管理员审核所有文章
    path('adminhome/',views.madminhome,name='adminhome'),
    # 管理员审核文章内容
    path('adminarticle/<article_id>',views.madminarticle,name='adminarticle'),
    # 用户列表管理
    path('adminuser',views.madminuser,name='adminuser'),
    # 用户详细信息管理
    path('adminuserinfo/<user_id>',views.madminuserinfo,name='adminuserinfo'),
]