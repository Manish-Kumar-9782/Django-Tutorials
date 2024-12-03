from django.shortcuts import render

# Create your views here.


def blog_form(request):
    # path("blog_form/", view=blog_form, name="blog_form")

    if request.method == 'GET':
        return render(request, "blog_form.html")

    if request.method == "POST":
        title = request.POST.get('title')
        paras = request.POST.get('paragraphs')

        blog = {"title": title, "paras": paras}

        return render(request, "blog_view.html", {"blog": blog})
