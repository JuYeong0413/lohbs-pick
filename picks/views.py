from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from products.models import Product
import pdb
from django.contrib.auth.decorators import login_required

#롭스픽 메인
def lohbs_pick(request):
    user = request.user
    picks = Collection.objects.filter(user=user)
    return render(request, 'picks/lohbs_pick.html', {'picks':picks})

#컬렉션 추가하기
def collection_add(request):
    picks = Collection.objects.filter(user=request.user)
    return render(request, 'picks/choose.html', {'picks':picks})

#컬렉션 삭제하기
def delete(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    collection.delete()
    return redirect('picks:lohbs_pick')

#컬렉션 상품 삭제하기
def delete_cp(request, cp_id, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    cp = get_object_or_404(CollectionProduct, pk=cp_id)
    collection.collection_products.remove(cp)
    collection.collection_total -= cp.sub_total
    collection.save()

    return redirect('picks:lohbs_pick')

#컬렉션 상품 만들고 컬렉션에 저장
def create_cp(request, product_id):
    if request.method == "POST":

        product = Product.objects.get(pk=product_id)
        quantity = request.POST.get('quantity')
        pick = request.POST.get('pick')
        quantity = int(quantity)

        if pick == "new":
            name = request.POST.get('collection_name')
            user = request.user 
            collection = Collection.objects.create(user=user, name=name)
            
        else:
            collection = Collection.objects.get(pk=pick)

            for collection_product in collection.collection_products.all():
                if product == collection_product.product:
                    collection.collection_products.remove(collection_product)
                    collection.collection_total -= collection_product.sub_total
                    
        cp = CollectionProduct.objects.create(product=product, quantity=quantity)        
        collection.collection_products.add(cp)
        collection.collection_total += cp.sub_total
        collection.save()

        return redirect('picks:lohbs_pick')      


## 공유 관련
# 공유된 롭스픽 메인 페이지(목록)
def shared(request):
    posts = Share.objects.all().order_by('-created_at')
    return render(request, 'picks/shared.html', {'posts': posts})


# 롭스픽 공유글 작성 페이지
@login_required
def share_new(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)

    if request.user == collection.user:
        context = {
          'collection_id': collection_id,
          'collection_name': collection.name,
          'collection_products': collection.collection_products.all()
        }
        return render(request, 'picks/share_new.html', context)

    return redirect('picks:lohbs_pick')


# 롭스픽 공유글 생성
@login_required
def share_create(request):
    user = request.user
    if request.method == "POST":
        # pdb.set_trace()
        content = request.POST.get('content')
        collection_name = request.POST.get('collection_name')
        image = request.FILES.get('image')
        products = 'aaa, b, c'
        # products = request.POST.get('')

        Share.objects.create(user=user, image=image, content=content, collection_name=collection_name, collection_products=products)
    return redirect('picks:shared')


# 롭스픽 공유글 수정 페이지
@login_required
def share_edit(request, id):
    share = get_object_or_404(Share, pk=id)
    if request.user == share.user:
        products = share.collection_products
        products_list = products.split(', ')

        context = {
          'share': share,
          'products': products_list
        }
        return render(request, 'picks/share_edit.html', context)
    return redirect('picks:shared')


# 롭스픽 공유글 수정
@login_required
def share_update(request, id):
    share = get_object_or_404(Share, pk=id)
    if request.method == "POST":
        share.image = request.POST.get('')
        share.content = request.POST.get('')
        share.save()
    return redirect('picks:shared')


# 롭스픽 공유글 삭제
@login_required
def share_delete(request, id):
    share = get_object_or_404(Share, pk=id)
    if request.user == share.user:
        share.delete()
    return redirect('picks:shared')
