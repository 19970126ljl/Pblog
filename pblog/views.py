from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from .models import MUSER,MARTICLE,MCOMMENT,MPHOTO,MALBUM,MPUBLISH
from django.conf import settings
from .forms import infoform
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def mhome(request):
    allarticles = MARTICLE.objects.all()
    content = {'allarticles':allarticles}
    return render(request,'pblog/home.html',content)

def mlogin(request):
    # print(request.POST)
    # print('types' in request.POST)
    if request.method == 'POST':
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'pblog/login.html',{'warning':'用户名或密码错误!'})
        elif 'types' in request.POST and user.muser.types:
            login(request,user)
            return redirect('pblog:adminhome')
        else:
            login(request,user)
            return redirect('pblog:home')
    else:
        return render(request,'pblog/login.html')

def mregister(request):
    if request.method =='POST':
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            regform.save()
            user = authenticate(username=regform.cleaned_data['username'],password=regform.cleaned_data['password1'])
            login(request,user)
            return redirect('pblog:home')
    else:
        regform = UserCreationForm()
    content = {'regform':regform}
    return render(request,'pblog/register.html',content)    

def mlogout(request):
    logout(request)
    return redirect('pblog:home')

@login_required(login_url='pblog:login')
def mdetail(request,article_id):
    article = MARTICLE.objects.get(id = article_id)
    comments = MCOMMENT.objects.filter(article = article)
    content = {'article':article,'comments':comments}
    return render(request,'pblog/detail.html',content)

@login_required(login_url='pblog:login')
# 添加文章
def medit(request):
    # if request.method == 'POST':
    if request.POST['title'] and request.POST['content']:
        article=MARTICLE(writer=request.user,title=request.POST['title'],content=request.POST['content'])
        article.save()
        MPUBLISH(article=article).save()
        return redirect('pblog:home')
    else:
        return render(request,'pblog/home.html',{'error':'失败！'})

@login_required(login_url='pblog:login')
def mcomment(request):
    # if request.method == 'POST':
    if request.POST['content']:
        comment=MCOMMENT(user=request.user,article=MARTICLE.objects.get(id=request.POST['articleid']),content=request.POST['content'])
        comment.save()
        MPUBLISH(types=3,comment=comment).save()
        return redirect('pblog:detail',request.POST['articleid'])
    else:
        return render(request,'pblog/detail.html',{'error':'失败！'})

def musercenter(request):
    return redirect('pblog:myarticle')
# 用户中心的用户的文章
def myarticle(request):
    return render(request,'pblog/myarticle.html',{'allarticles':MARTICLE.objects.filter(writer=request.user)})
# 用户中心的用户的信息
def myinfo(request):
    form=infoform(instance=request.user)
    changepwdform = PasswordChangeForm(user=request.user)
    content={'infoform':form,'changepwdform':changepwdform}
    return render(request,'pblog/myinfo.html',content)

def myalbum(request):
    if request.method == 'POST':
        if request.POST['title']:
            album=MALBUM(title=request.POST['title'],user=request.user)
            if request.POST['description']:
                album.description=request.POST['description']
            if request.FILES.get('cover'):
                f=request.FILES.get('cover')
                album.cover='imgs/'+f.name
                fname = settings.MEDIA_ROOT + '\imgs\\' + f.name
                with open(fname,'wb+') as pic:
                    for c in f.chunks():
                        pic.write(c)
            album.save()
    return render(request,'pblog/myalbum.html',{'allalbums':MALBUM.objects.filter(user=request.user)})



def malbumdetail(request,album_id):
    # 改变相册
    album=MALBUM.objects.get(id=album_id)
    if request.method == 'POST':
        album.title = request.POST['title']
        album.description = request.POST['description']
        album.save()
        return redirect('pblog:myalbum')
    else:
        # album=MALBUM.objects.get(id=album_id)
        photos=MPHOTO.objects.filter(album=album)
        content={'album':album,'photos':photos}
        return render(request,'pblog/albumdetail.html',content)

def mphotodetail(request,photo_id):
    if request.method == 'POST':
        photo=MPHOTO.objects.get(id=photo_id)
        photo.title=request.POST['title']
        photo.description=request.POST['description']
        photo.save()
    return render(request,'pblog/photodetail.html',{'photo':MPHOTO.objects.get(id=photo_id)})

# 上传图片
def maddphoto(request,album_id):
    if request.method == 'POST':
        if request.FILES.get('pic') and request.POST['title']:
            album=MALBUM.objects.get(id=album_id)
            title=request.POST['title']
            description=request.POST['description']
            f=request.FILES.get('pic')
            pic="imgs/"+f.name
            photo=MPHOTO(album=album,title=title,description=description,pic=pic)
            photo.save()
            MPUBLISH(types=2,photo=photo).save()
            fname = settings.MEDIA_ROOT + '\imgs\\' + f.name
            with open(fname,'wb+') as pic:
                for c in f.chunks():
                    pic.write(c)
        else:
            album=MALBUM.objects.get(id=album_id)
            photos=MPHOTO.objects.filter(album=album)
            content={'album':album,'photos':photos,'warning':'图片没上传或图片标题为空'}
            return render(request,'pblog/albumdetail.html',content)
    albumid=album_id
    return redirect('pblog:albumdetail',albumid)

def mchangearticle(request,article_id):
    article = MARTICLE.objects.get(id = article_id)
    comments = MCOMMENT.objects.filter(article = article)
    if request.method == 'POST':
        article.content=request.POST['content']
        article.save()
    content = {'article':article,'comments':comments}
    return render(request,'pblog/changearticle.html',content)

def mdeletearticle(request,article_id):
    article = MARTICLE.objects.get(id = article_id)
    article.delete()
    return redirect('pblog:usercenter')

def mdeletecomment(request,comment_id):
    comment=MCOMMENT.objects.get(id=comment_id)
    if comment.article:
        comment.delete()
        return redirect('pblog:changearticle',comment.article.id)
    elif comment.album:
        comment.delete()
        return redirect('pblog:malbum')
    else:
        comment.delete()
        return redirect('pblog:photodetail',comment.photo.id)

# 修改个人信息
def mchangeinfo(request):
    form=infoform(request.POST,instance=request.user)
    if form.is_valid():
        form.save()
        if request.POST['gender'] == 'male':
            request.user.muser.gender=True
        else:
            request.user.muser.gender=False
        request.user.muser.save()
        if request.FILES.get('head'):
            name=request.user.muser.head
            # print(settings.MEDIA_ROOT+'\\'+str(name).replace('/', '\\'))
            f=request.FILES.get('head')
            fname = settings.MEDIA_ROOT+'\\'+str(name).replace('/', '\\')
            with open(fname,'wb+') as pic:
                for c in f.chunks():
                    pic.write(c)
        
    return redirect('pblog:myinfo')

def mpublish(request):
    allpublishs=MPUBLISH.objects.all()
    content={'allpublishs':allpublishs}
    return render(request,'pblog/publish.html',content)


def mdeletealbum(request,album_id):
    album=MALBUM.objects.get(id=album_id)
    # album.delete()
    print(album)
    return redirect('pblog:myalbum')

def mdeletephoto(request,photo_id):
    photo=MPHOTO.objects.get(id=photo_id)
    # photo.delete()
    print(photo)
    return redirect('pblog:albumdetail',photo.album.id)


def msearch(request):
    search=request.GET['search']
    categ=request.GET['category']
    users=None
    articles=None
    if categ=='用户':
        if search:
            users=User.objects.filter(username__icontains=search)
            print(users)
    elif categ=='文章':
        if search:
            articles=MARTICLE.objects.filter(title__icontains=search)
    result={'users':users,'articles':articles}
    print(result)
    return render(request,'pblog/search.html',result)
    # print(search,categ)
    
def madminhome(request):
    allarticles = MARTICLE.objects.all()
    content = {'allarticles':allarticles}
    return render(request,'pblog/adminhome.html',content)

def madminarticle(request,article_id):
    if request.method == 'POST':
        article = MARTICLE.objects.get(id = article_id)
        article.audit = True
        article.save()
    article = MARTICLE.objects.get(id = article_id)
    comments = MCOMMENT.objects.filter(article = article)
    content = {'article':article,'comments':comments}
    return render(request,'pblog/adminarticle.html',content)

        
def madminuser(request):
    users=MUSER.objects.all()
    return render(request,'pblog/adminuser.html',{'users':users})

def madminuserinfo(request,user_id):
    if request.method == 'POST':
        user=User.objects.get(id=user_id)
        form=infoform(request.POST,instance=user)
        print(user.muser.head)
        if form.is_valid():
            form.save()
            if request.POST['gender'] == 'male':
                user.muser.gender=True
            else:
                user.muser.gender=False
            user.muser.save()
            if request.FILES.get('head'):
                name=user.muser.head
                print(settings.MEDIA_ROOT+'/'+str(name))
                f=request.FILES.get('head')
                fname = settings.MEDIA_ROOT+'/'+str(name)
                with open(fname,'wb+') as pic:
                    for c in f.chunks():
                        pic.write(c)
        return redirect('pblog:adminuserinfo',user_id)   
    user=MUSER.objects.get(id=user_id)
    return render(request,'pblog/adminuserinfo.html',{'muser':user})

def mchangepassword(request):
    if request.method == 'POST':
        changepwdform = PasswordChangeForm(data=request.POST,user=request.user)
        if changepwdform.is_valid():
            changepwdform.save()
            return redirect('pblog:login')
        else:
            errors=changepwdform.errors
            print(errors)
            form=infoform(instance=request.user)
            changepwdform = PasswordChangeForm(user=request.user)
            content={'infoform':form,'changepwdform':changepwdform,'errors':errors}
            return render(request,'pblog/myinfo.html',content)
    else:
        form=infoform(instance=request.user)
        changepwdform = PasswordChangeForm(user=request.user)
        content={'infoform':form,'changepwdform':changepwdform}
        return redirect('pblog:myinfo')
def mothersusercenter(request,other_id):
    otheruser=User.objects.get(id=other_id)
    return render(request,'pblog/othersusercenter.html',{'otheruser':otheruser})





    
