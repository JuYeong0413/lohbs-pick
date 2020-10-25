from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from products.models import Product
from django.contrib.auth.decorators import login_required
import pdb

#롭스픽 메인
@login_required
def lohbs_pick(request):
    user = request.user
    picks = Collection.objects.filter(user=user).order_by('-created_at')
    return render(request, 'picks/lohbs_pick.html', {'picks':picks} )

#컬렉션 추가하기
def collection_add(request):
    picks = Collection.objects.filter(user=request.user)
    return render(request, 'picks/choose.html', {'picks':picks})

#컬렉션 수정하기
def collection_update(request, collection_id):
    pick = get_object_or_404(Collection, pk=collection_id)
    pick.collection_total = 0

    if request.method == "POST":
        name  = request.POST.get('name')
        picks = Collection.objects.filter(user=request.user).order_by('-created_at')
        for c in picks:
            if c == pick:
                continue
            elif c.name == name:
                message = "True"
                return render(request, 'picks/lohbs_pick.html', {'picks':picks, 'message':message})

        period = request.POST.get('period')

        pick.name = name
        pick.period = period

        for i in range(0, len(pick.collection_products.all())):
            key = request.POST.get('num'+str(i))
            quantity = request.POST.get('quantity'+str(i))
            cp = CollectionProduct.objects.get(pk=key)
            cp.quantity = int(quantity)
            cp.sub_total = cp.product.price*cp.quantity
            pick.collection_total += cp.sub_total
            cp.save()

        pick.save()
        return redirect('picks:lohbs_pick')

    return render(request, 'picks/collection_update.html', {'pick':pick})

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
    return redirect('picks:collection_update', collection_id)

#컬렉션 상품 만들고 컬렉션에 저장
def create_cp(request, product_id):
    if request.user.is_active:
        if request.method == "POST":

            product = get_object_or_404(Product, pk=product_id)
            quantity = request.POST.get('quantity')
            pick = request.POST.get('pick')
            quantity = int(quantity)

            if pick == "new":
                name = request.POST.get('collection_name')
                user = request.user 
                picks = Collection.objects.filter(user=user).order_by('-created_at')
                for c in picks:
                    if c.name == name:
                        message = "True"
                        return render(request, 'picks/lohbs_pick.html', {'picks':picks, 'message':message})
                collection = Collection.objects.create(user=user, name=name)
                
            else:
                collection = get_object_or_404(Collection, pk=pick)

                for collection_product in collection.collection_products.all():
                    if product == collection_product.product:
                        collection.collection_products.remove(collection_product)
                        collection.collection_total -= collection_product.sub_total
                        
            cp = CollectionProduct.objects.create(product=product, quantity=quantity)        
            collection.collection_products.add(cp)
            collection.collection_total += cp.sub_total
            collection.save()

            return redirect('picks:lohbs_pick')      
    else:
      return redirect('account_login')


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
    products_list = []
    user = request.user
    if request.method == "POST":
        c_id = request.POST.get('collection_id')
        collection = get_object_or_404(Collection, pk=c_id)
        c_products = collection.collection_products.all()
        for cp in c_products:
            p = cp.product
            p_str = f"[{p.brand}] {p.name}"
            products_list.append(p_str)

        content = request.POST.get('content')
        collection_name = request.POST.get('collection_name')
        image = request.FILES.get('image')
        products = ', '.join(products_list)

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
        image = request.FILES.get('image')
        
        if image :
            share.image = image

        share.content = request.POST.get('content')
        share.save()
    return redirect('picks:shared')


# 롭스픽 공유글 삭제
@login_required
def share_delete(request, id):
    share = get_object_or_404(Share, pk=id)
    if request.user == share.user:
        share.delete()
    return redirect('picks:shared')
