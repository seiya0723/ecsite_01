from django.shortcuts import render, redirect
from django.views import View
from .models import GoodsCreate, GoodsGroup
from .forms import GoodsCreateForm, GroupCreateFrom

class GroupCreateView(View):

    def get(self, request, *args, **kwargs):

        goods = GoodsCreate.objects.all()
        groups = GoodsGroup.objects.all()
        context = {"groups": groups,
                   "goods":goods}

        return render(request, "goods/group_create.html", context)

    def post(self, request, *args, **kwargs):

        form = GroupCreateFrom(request.POST)

        if form.is_valid():
            print("バリデーションOK")
            # 保存する
            form.save()
        else:
            print("バリデーションNG")

        return redirect("goods:group_create")

groupcreate = GroupCreateView.as_view()

class GoodsCreateView(View):

    def post(self, request, *args, **kwargs):

        form = GoodsCreateForm(request.POST)

        if form.is_valid():
            print("バリデーションOK")
            form.save()
        else:
            print("バリデーションNG")
            print(form.errors)

            
        return redirect("goods:group_create")

goodscreate = GoodsCreateView.as_view()
