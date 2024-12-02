from django.shortcuts import render

# news_report = {
#     "heading": "Cinnamic acid's impact on hair growth",
#     "paras": [
#         "However, simply eating cinnamon may not help in regenerating hair growth. The study suggested that a lot more scope of research is there in this space. The study added that oxytocin can stimulate hair growth by targeting a receptor called OXTR in hair follicles. However, oxytocin is a large molecule and cannot penetrate the skin – making it a poor choice for hair loss treatments. This is where cinnamic acid is a complete win for hair growth – it can mimic oxytocin’s hair-growth effects and can increase OXTR expression.",


#         "In a statement, Junji Fukuda, the study’s corresponding author and a professor with the university’s Faculty of Engineering added that this study can help in developing hair growth treatments that usually target oxytocin.",

#         "To determine the effects of cinnamic acid on hair growth, the researchers treated human scalp with various doses of cinnamic acid. It was observed that at doses up to 500 μg/mL, cinnamic acid triggered OXTR expression and other key genes related to hair growth. However, high doses can damage the cells.The researchers added that while more research is required in this space, it is known that cinnamon contains important compounds that can help in improving hair growth. Hence, the next time we catch a whiff of cinnamon in our drink or food, we should appreciate it. With a little bit of work, we can also include it in our hair case routine.",

#         "If there is one simple daily habit that can help you stay young, fit, and at the best of your energy levels, it's certainly walking. Whether at a leisurely pace or a brisk stride, the benefits are countless. The best thing about walking is that it works on multiple aspects of your well-being. From heart health, brain wellness to maintaining muscle and bone health, a regular walking routine can ensure overall well-being. Studies support the many marvels of walking.According to a study published in the British Journal of Sports Medicine, getting less physical activity is linked with premature death, while daily walks could extend people's lifespan, linking this habit to longevity. The study says it can add at least a decade to your life."
#     ]
# }


# def news_report_view(request):
#     return render(request, "news.html", context={"news": news_report})


news = {
    "title": "Best Anime Award: jujustu kaisen",
    "paras": ["We all spend a lot of time and money in salons to make our hair stronger, shiner, and smoother. But we fail to understand that sometimes home remedies are better than many salon treatments. One such home remedy for hair is carrots. They contain vitamins A, B6, B1, B3, B2, K, and C, as well as fibre, potassium, iron, zinc, phosphorus, beta-carotene, and antioxidants. These nutrients have the potential to enhance overall well-being and skin health. Know the benefits and how to use carrots for hair",
              "Carrot oil is excellent against bacteria and fungi because it contains carotol, lycopene, caffeic acid, polyacetylenes, and anthocyanins. Research published in Plant Cell Biotechnology and Molecular Biology Journal indicates that carrots contain a bioactive polyacetylene of the falcarinol type, which has potent antibacterial, antifungal, anti-inflammatory, and anti-cancer properties. These plant components can significantly limit microbial activities, which means they can prevent the growth of ringworm, folliculitis, and acne on the scalp.",
              "Carrots and carrot seed oil have anti-inflammatory properties that help control the symptoms of dandruff. Its antifungal properties, mostly attributed to the presence of carotol and anthocyanins, inhibit the growth of Malassezia globosa, the fungus that causes dandruff on your scalp. Additionally, carrots regulate oil production, which helps to further treat dandruff, according to a study published in the Journal of BioScience.",
              "“Essential growth-promoting nutrients found in carrots, such as biotin and vitamin A, encourage the development of keratin. Carrots also include vitamins C and E, which function as potent antioxidants that help maintain the strength of the hair shaft. Additionally, these vitamins increase blood flow, which enhances nutritional absorption. So, if you incorporate carrots into your daily hair care routine, you can guarantee long, thick hair in a few months, says dermatologist Dr DM Mahajan.",
              "Premature greying of the hair and hair loss are typically caused by oxidative stress. Carrots and their oils are regarded as superfoods for the hair due to their strong antioxidant content. Beta-carotene, vitamins E, and C, caffeic acid, flavonoids, and anthocyanins all serve to scavenge reactive oxygen species and minimise oxidative stress on the hair, as per a study published in Research Gate Journal",

              ]
}


def news_page(request):
    return render(request, "news_page.html", context={"news": news})


def blog_form1(request):

    if request.method == "GET":
        return render(request, "blog_form1.html")

    if request.method == "POST":
        title = request.POST.get('title')
        paras = request.POST.get('paragraphs')

        blog = {"title": title, "paras": paras}
        return render(request, "blog_view.html", {"blog": blog})
