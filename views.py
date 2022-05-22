from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import UpimageForm
from .models import Upimage

# Create your views here.
@login_required(login_url='login')
def uploadimg(request):
    loginuser = request.user
    if request.method == "POST":
        upimg = Upimage(owner=loginuser)
        upimgform = UpimageForm(request.POST, request.FILES, instance=upimg)
        upimgform.save()
        # img = Upimage(owner=loginuser, img=request.POST['img'])
        # img.save()
        params={
            'title':'Upload Completion',
            'head':'画像はアップロードされました!!',
        }
        #レンダリングするhtml用意
        #バリデーションも
        return render(request, 'imgadmin/standard.html', params)
    else:
        params={
            'title':'Upload Image',
            'head':'アップロードしたい画像を選択しましょう',
            'form':UpimageForm(),
        }
        #レンダリングするhtml用意
        return render(request, 'imgadmin/upimg.html', params)

#ログイン中ユーザのアップロード画像を一覧表示
@login_required(login_url='login')
def loginuser_imglist(request):
    loginuser = request.user
    params = {
        'title':'Image List View',
        'head':str(loginuser.username)+'さんがアップロードしている画像の一覧です。選択して使いたい機能を選びましょう',
        'loginuser':loginuser,
    }
    return render(request, 'imgadmin/imglist.html', params)


#パラメータとして送られてきたupimgのidを検索して画像を返す
@login_required(login_url='login')
def imgselect(request, id):
    slctupimg = Upimage.objects.filter(id=id)[0]
    loginuser=request.user
    if loginuser==Upimage.objects.filter(id=id)[0].owner:
        #画像所有者とログインユーザが同一の場合
        head='表示の画像に対して、どの機能を使いますか？'
    else:
        #画像所有者とログインユーザが異なる場合
        head='画像所有者はあなたではありません！'
        slctupimg=None
    params={
        'title':'Select function',
        'slctupimg':slctupimg,
        'head':head,
    }
    #selectimgを表示させながら、使いたい機能を選択できるhtmlをつくる
    return render(request, 'imgadmin/selectfunc.html', params)
