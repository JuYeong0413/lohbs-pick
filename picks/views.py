from django.shortcuts import render, redirect
from .models import *
from products.models import Product
import pdb

#롭스픽 메인
def lohbs_pick(request):
    user = request.user
    picks = Collection.objects.filter(user=user)
    return render(request, 'picks/lohbs_pick_acc.html', {'picks':picks})

#롭스픽 생성         
def create(request):
    if request.method == "POST":
        user = request.user
        name = request.POST.get('name')
        period = request.POST.get('period')
        Collection.objects.create(user=user, name=name, period=period)
        return redirect('picks:lohbs_pick')

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
        collection_id = request.POST.get('pick')
        quantity = int(quantity)
        collection = Collection.objects.get(pk=collection_id)

        for collection_product in collection.collection_products.all():
            if product == collection_product.product:
                collection.collection_products.remove(collection_product)
                collection.collection_total -= collection_product.sub_total

        cp = CollectionProduct.objects.create(product=product, qunatity=quantity)        
        collection.collection_products.add(cp)
        collection.collection_total += cp.sub_total
        collection.save()

        return redirect('picks:lohbs_pick')      


## 공유 관련
# 공유된 롭스픽 메인 페이지(목록)
def shared(request):
    return render(request, 'picks/shared.html')


# 롭스픽 공유글 작성 페이지
def share_new(request):
    return render(request, 'picks/share_new.html')


# 롭스픽 공유글 생성
def share_create(request):
    return redirect('picks:shared')


# 롭스픽 공유글 수정 페이지
def share_edit(request, id):
    return render(request, 'picks/share_edit.html')


# 롭스픽 공유글 수정
def share_update(request, id):
    return redirect('picks:shared')


# 롭스픽 공유글 삭제
def share_delete(request, id):
    return redirect('picks:shared')
