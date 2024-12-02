from django.shortcuts import render


news = {
    "title": "Aloe Vera or Amla: Which Is Better Choice To Promote Hair Growth | Know Here",
    "paras": ["Aloe vera vs Amla: When it comes to hair care, nature offers a plethora of remedies to nurture hair health and hair growth. From herbs to oils, there are a number of ingredients that promote hair strength and vitality. However, two popular ingredients, aloe vera and amla have been revered for centuries for their exceptional hair growth-promoting properties. Incorporating these potent ingredients into your hair care routine can lead to a significant improvement in hair texture, length and overall health.",


              "But have you ever wondered which is a better choice to promote growth? If not, then here we've drawn a comparison which will help you to make an effective choice between the two.",

              "Aloe Vera surpasses Amla in hydration, thanks to its high water content and gel-like texture which deeply penetrates hair shafts, providing intense moisture and soothing dryness, leaving hair soft, silky and supremely hydrated with a healthy shine.",

              "Amla potent antioxidants and vitamins stimulate hair growth, fortify hair follicles and enhance strength, reducing breakage and split ends. Its nourishing properties promote a healthy scalp, encouraging thicker, longer, and more resilient hair with a vibrant shine and luscious texture."
              ]
}

# create a news view function


def new_page(request):
    return render(request, "news_page.html", context={"news": news})

# blog_form url


def blog_form(request):
    # path("blog_form/", view=blog_form, name="blog_form")

    if request.method == 'GET':
        return render(request, "blog_form.html")

    if request.method == "POST":
        title = request.POST.get('title')
        paras = request.POST.get('paragraphs')

        blog = {"title": title, "paras": paras}

        return render(request, "blog_view.html", {"blog": blog})
