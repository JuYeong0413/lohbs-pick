from django.shortcuts import render, redirect

# 주문 목록 페이지
def main(request):
    return render(request, 'orders/main.html')


# 주문 상세보기 페이지
def show(request, id):
    return render(request, 'orders/show.html')


# 새로운 주문 작성 페이지
def new(request):
    return render(request, 'orders/new.html')


# 새로운 주문 생성
def create(request):
    return redirect('orders:show')
