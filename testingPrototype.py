from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
my_url = 'https://world.taobao.com/?scm=20140651.100.3.XGgFSnmlVbRzauVn0si&ali_trackid=2:mm_26632535_17502226_63504389:1539868704_115_545783917&clk1=5951522682332f8375a0a30f0c299957&upsid=5951522682332f8375a0a30f0c299957'

# read from the link
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# parse as html (can choose other types also)
page_soup = soup(page_html,'html.parser')
page_soup.body # can inspect the website

containers = page_soup.findAll("div",{"class":"item-container"})
container = containers[0] # for iteration purpose

filename = "test.csv"
f = open(filename,"w") # create a file for writing
for container in containers:
    image_container = container.findAll("img")
    image_container = image_container.src # to specify the attributes, like text
    f.write("the src is: " + image_container + "\n")
f.close()

'''
The sample container html code is shown as below:

<div class="item-container loading">
    <div class="banner">
        <img alt="" class="banner-img" data-ks-lazyload="" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=" />
        <a class="more" href="">
            <img alt="" data-ks-lazyload="" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=" />
        </a>
    </div>
    <div class="chaoshi-slider-container">
        <div class="slide chaoshi-slider">
            <a href="">
                <img alt="" data-ks-lazyload="" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=" />
                <div class="title"></div>
                <div class="price-sales">
                    <span class="price"></span>
                </div>
            </a>
            <a href="">
                <img alt="" data-ks-lazyload="" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=" />
                <div class="title"></div>
                <div class="price-sales">
                    <span class="price"></span>
                </div>
            </a>
            <a href="">
                <img alt="" data-ks-lazyload="" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=" />
                <div class="title"></div>
                <div class="price-sales">
                    <span class="price"></span>
                </div>
            </a>
            <a href="">
                <img alt="" data-ks-lazyload="" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=" />
                <div class="title"></div>
                <div class="price-sales">
                    <span class="price"></span>
                </div>
            </a>
            <a href="">
                <img alt="" data-ks-lazyload="" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=" />
                <div class="title"></div>
                <div class="price-sales">
                    <span class="price"></span>
                </div>
            </a>
        </div>
    </div>
</div>
'''
