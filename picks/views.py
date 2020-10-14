from django.shortcuts import render, redirect

def lohbs_pick(request):
    return render(request, 'picks/lohbs_pick.html')


## 공유 관련
# 공유된 롭스픽 메인 페이지(목록)
def shared(request):
    return render(request, 'picks/shared.html')


# 롭스픽 공유글 작성
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
