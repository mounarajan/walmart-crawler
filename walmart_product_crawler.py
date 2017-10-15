from request_lib import requests_lib_prod
import time
import csv
import re
import os
import codecs

def productInfoExtraction(url):
    #print url
    if url.startswith("http"):
        url = re.sub(r'amp\;','',url)
    else:
        url = "http://google.com"
    print url
    dataWeb = requests_lib_prod(url)



    if re.search(r'(?mis)<button class=\"choose\-button btn btn\-primary js\-start\-choosing\">Start\s*choosing\s*now<\/button>',dataWeb):
        pass
    elif re.search(r'(?mis)<button\s*class\s*\=\s*\"choose\-button\s*btn\s*btn\-primary\s*js\-start\-choosing\">\s*Start\s*Choosing\s*Now\s*<\/button>',dataWeb):
        pass
    else:
        
        product_pass = 0
        if re.search(r'(?mis)<h1 itemprop=name\s*class=\"heading\-b\s*product\-name[^\"]*\">([^<]+)<\/h1>',dataWeb):
            
            name = re.findall(r'(?mis)<h1 itemprop=name\s*class=\"heading\-b\s*product\-name[^\"]*\">([^<]+)<\/h1>',dataWeb)[0]
            product_pass = 1
            #product_info.append(name)
        elif re.search(r'(?mis)<meta\sname=\"title\"[^>]*content=\"([^\"]+)\"\/>',dataWeb):
            
            name = re.findall(r'(?mis)<meta\sname=\"title\"[^>]*content=\"([^\"]+)\"\/>',dataWeb)[0]
            product_pass = 1
            #product_info.append(name)
        elif re.search(r'(?mis)<h1 class=\"productTitle\"[^>]*>([^<]+)<\/h1',dataWeb):
            
            name = re.findall(r'(?mis)<h1 class=\"productTitle\"[^>]*>([^<]+)<\/h1',dataWeb)[0]
            product_pass = 1
            #product_info.append(name)
        elif re.search(r'(?mis)<h1 class=\"heading\-b product\-name product\-heading js\-product\-heading\"[^<]*>([^<]+)<\/h1>',dataWeb):
            
            name = re.findall(r'(?mis)<h1 class=\"heading\-b product\-name product\-heading js\-product\-heading\"[^<]*>([^<]+)<\/h1>',dataWeb)[0]
            product_pass = 1
            #product_info.append(name)

        elif re.search(r'(?mis)<h1 itemprop=name[^>]*>\s*<span>([^<]+)<\/span>',dataWeb):
            
            name = re.findall(r'(?mis)<h1 itemprop=name[^>]*>\s*<span>([^<]+)<\/span>',dataWeb)[0]
            product_pass = 1
            #product_info.append(name)

        elif re.search(r'(?mis)<h1 itemprop=\"name\"[^>]*>\s*<span>([^<]+)<\/span>\s*<\/h1>',dataWeb):
            
            name = re.findall(r'(?mis)<h1 itemprop=\"name\"[^>]*>\s*<span>([^<]+)<\/span>\s*<\/h1>',dataWeb)[0]
            product_pass = 1
            #product_info.append(name)
        elif re.search(r'(?mis)<h1\s*class\s*\=\s*\"prod\-ProductTitle\s*no\-margin\s*heading\-a\"\s*itemprop\s*\=\"name\"[^>]*>\s*<div>([^<]+)<\/div>',dataWeb):
            
            name = re.findall(r'(?mis)<h1\s*class\s*\=\s*\"prod\-ProductTitle\s*no\-margin\s*heading\-a\"\s*itemprop\s*\=\"name\"[^>]*>\s*<div>([^<]+)<\/div>',dataWeb)[0]
            product_pass = 1
            #product_info.append(name)

        if product_pass == 1:
            


            if re.search(r'(?mis)\"variantSelection\"\s*\:\s*\{.*?\"products\"\s*\:\s*\{(.*?)\"productAttributes\"\s*\:\s*\{',dataWeb):
            
                variations = re.findall(r'(?mis)\"variantSelection\"\s*\:\s*\{.*?\"products\"\s*\:\s*\{(.*?)\"productAttributes\"\s*\:\s*\{',dataWeb)[0]
                variation_ids = re.findall(r'(?mis)\"usItemId\"\s*\:\s*\"([^\"]+)\"',dataWeb)
                v_id_pass = 0
            elif re.search(r'(?mis)\"variantProducts\"\:\[(.*?)<\/script>',dataWeb):
            
                variations = re.findall(r'(?mis)\"variantProducts\"\:\[(.*?)<\/script>',dataWeb)[0]
                variation_ids = re.findall(r'(?mis)\"usItemId\"\s*\:\s*\"([^\"]+)\"',dataWeb)
                v_id_pass = 0
            else:
                
                v_id_pass = 1


            if v_id_pass == 0:

                for v_id in set(variation_ids):
                    product_info = []
                    variation_id_product_url = "https://www.walmart.com/ip/"+v_id
                    print variation_id_product_url
                    dataWeb_1 = requests_lib_prod(variation_id_product_url)

                    product_info.append(variation_id_product_url)

                    if re.search(r'(?mis)<h1 itemprop=name\s*class=\"heading\-b\s*product\-name[^\"]*\">([^<]+)<\/h1>',dataWeb_1):
            
                        name = re.findall(r'(?mis)<h1 itemprop=name\s*class=\"heading\-b\s*product\-name[^\"]*\">([^<]+)<\/h1>',dataWeb_1)[0]
            
                        product_info.append(name)
                    elif re.search(r'(?mis)<meta\sname=\"title\"[^>]*content=\"([^\"]+)\"\/>',dataWeb_1):
            
                        name = re.findall(r'(?mis)<meta\sname=\"title\"[^>]*content=\"([^\"]+)\"\/>',dataWeb_1)[0]
            
                        product_info.append(name)
                    elif re.search(r'(?mis)<h1 class=\"productTitle\"[^>]*>([^<]+)<\/h1',dataWeb_1):
            
                        name = re.findall(r'(?mis)<h1 class=\"productTitle\"[^>]*>([^<]+)<\/h1',dataWeb_1)[0]
            
                        product_info.append(name)
                    elif re.search(r'(?mis)<h1 class=\"heading\-b product\-name product\-heading js\-product\-heading\"[^<]*>([^<]+)<\/h1>',dataWeb_1):
            
                        name = re.findall(r'(?mis)<h1 class=\"heading\-b product\-name product\-heading js\-product\-heading\"[^<]*>([^<]+)<\/h1>',dataWeb_1)[0]
            
                        product_info.append(name)

                    elif re.search(r'(?mis)<h1 itemprop=name[^>]*>\s*<span>([^<]+)<\/span>',dataWeb_1):
            
                        name = re.findall(r'(?mis)<h1 itemprop=name[^>]*>\s*<span>([^<]+)<\/span>',dataWeb_1)[0]
           
                        product_info.append(name)

                    elif re.search(r'(?mis)<h1 itemprop=\"name\"[^>]*>\s*<span>([^<]+)<\/span>\s*<\/h1>',dataWeb_1):
            
                        name = re.findall(r'(?mis)<h1 itemprop=\"name\"[^>]*>\s*<span>([^<]+)<\/span>\s*<\/h1>',dataWeb_1)[0]
            
                        product_info.append(name)
                    elif re.search(r'(?mis)<h1\s*class\s*\=\s*\"prod\-ProductTitle\s*no\-margin\s*heading\-a\"\s*itemprop\s*\=\"name\"[^>]*>\s*<div>([^<]+)<\/div>',dataWeb_1):
            
                        name = re.findall(r'(?mis)<h1\s*class\s*\=\s*\"prod\-ProductTitle\s*no\-margin\s*heading\-a\"\s*itemprop\s*\=\"name\"[^>]*>\s*<div>([^<]+)<\/div>',dataWeb_1)[0]
            
                        product_info.append(name)
                    else:
                        product_info.append(name)

                    if re.search(r'(?mis)(<meta\s*property\=og\:image\s*content=\"[^\"]+\")',dataWeb_1):
            
                        images = re.findall(r'(?mis)(<meta\s*property\=og\:image\s*content=\"[^\"]+\")',dataWeb_1)[0]
            
            
                    elif re.search(r'(?mis)(<meta\s*property=\"og\:image\"\s*content\=\"[^\"]+\")',dataWeb_1):
                        images = re.findall(r'(?mis)(<meta\s*property=\"og\:image\"\s*content\=\"[^\"]+\")',dataWeb_1)[0]
                        image_pass = 1
                    elif re.search(r'(?mis)\"imageAssets\"\s*\:\s*\[(.*?)\]',dataWeb_1):
                        images = re.findall(r'(?mis)\"imageAssets\"\s*\:\s*\[(.*?)\]',dataWeb_1)[0]
                        image_pass = 1
                    elif re.search(r'(?mis)\"images\"\s*\:\s*\{([^\}]+.*?)\}\s*\}',dataWeb_1):
                        images = re.findall(r'(?mis)\"images\"\s*\:\s*\{([^\}]+.*?)\}\s*\}',dataWeb_1)[0]
                        image_pass = 1
                    else:
                        image_pass = 0
                    images_array = []
                    #print image_pass
                    if image_pass == 1:
                
                
                        if re.search(r'(?mis)content=\"([^\"]+)\"',images):
            
                            img = re.findall(r'(?mis)content=\"([^\"]+)\"',images)[0]

                    #for img in images:
                            img = re.sub(r'(?mis)_215X215\.jpg','_500X500.jpg',img)
                            img = re.sub(r'(?mis)^\/\/www\.walmart','http\:\/\/www\.walmart',img)
                            img = re.sub(r'(?mis)\?.*','',img)
                            images_array.append(img)
            
            
                        if re.search(r'(?mis)\"hero\"\s*\:\s*\"([^\"]+)\"',images):
            
                            img = re.findall(r'(?mis)\"hero\"\s*\:\s*\"([^\"]+)\"',images)[0]
                    #for img in images:
                            img = re.sub(r'(?mis)_215X215\.jpg','_500X500.jpg',img)
                            img = re.sub(r'(?mis)^\/\/www\.walmart','http\:\/\/www\.walmart',img)
                            img = re.sub(r'(?mis)\?.*','',img)
                            images_array.append(img)

                        if re.search(r'(?mis)\"main\"\s*\:\s*\"([^\"]+)\"',images):
            
                            img = re.findall(r'(?mis)\"main\"\s*\:\s*\"([^\"]+)\"',images)[0]
                    #for img in images:
                            img = re.sub(r'(?mis)_215X215\.jpg','_500X500.jpg',img)
                            img = re.sub(r'(?mis)^\/\/www\.walmart','http\:\/\/www\.walmart',img)
                            img = re.sub(r'(?mis)\?.*','',img)
                            images_array.append(img)

                    product_info.append(images_array[0])

                    ava_pri = "https://www.walmart.com/product/dynamic/"+v_id+"?selected=true"
                    dataWeb_ava = requests_lib_prod(ava_pri)

                    if re.search(r'(?mis)wasPrice":{"currencyAmount":([^\,]*)\,',dataWeb_ava):
            
                        was_price = re.findall(r'(?mis)wasPrice":{"currencyAmount":([^\,]*)\,',dataWeb_ava)[0]
            
                        product_info.append(was_price)
                    else:
                        product_info.append('')

                    

                    if re.search(r'(?mis)currencyAmount":([^\,]*)\,',dataWeb_ava):
            
                        price = re.findall(r'(?mis)currencyAmount":([^\,]*)\,',dataWeb_ava)[0]
            
                        product_info.append(price)
                    elif re.search(r'(?mis)Price-group" role="contentinfo" aria-label="\W([^\"]*)\"',dataWeb_ava):
            
                        price = re.findall(r'(?mis)Price-group" role="contentinfo" aria-label="\W([^\"]*)\"',dataWeb_ava)[0]
            
                        product_info.append(price)
                    else:
                        product_info.append('')

                    if re.search(r'(?mis)shippingDeliveryDateMessage":"([^\"]*)\"',dataWeb_ava):
            
                        ava = re.findall(r'(?mis)shippingDeliveryDateMessage":"([^\"]*)\"',dataWeb_ava)[0]
                        ava = re.sub(r'(?mis)See delivery options','available',ava)
                        product_info.append(ava)
                    else:
                        product_info.append('')

                    if re.search(r'(?mis)\"id\"\:\s*\"actual\_color\"\,\s*\"name\"\:\s*\"Actual\s*Color\"\,\s*\"selectedValue\"\:\s*\"([^\"]+)\"\,',dataWeb_1):
            
                        color = re.findall(r'(?mis)\"id\"\:\s*\"actual\_color\"\,\s*\"name\"\:\s*\"Actual\s*Color\"\,\s*\"selectedValue\"\:\s*\"([^\"]+)\"\,',dataWeb_1)[0]
            
                        product_info.append(color)
                    elif re.search(r'(?mis)<tr\s*class=js\-product\-specs\-row>\s*<td>\s*Color\s*\:\s*<\/td>\s*<td>([^<]+)<\/td>',dataWeb_1):
            
                        color = re.findall(r'(?mis)<tr\s*class=js\-product\-specs\-row>\s*<td>\s*Color\s*\:\s*<\/td>\s*<td>([^<]+)<\/td>',dataWeb_1)[0]
            
                        product_info.append(color)
                    elif re.search(r'(?mis)status\"\s*\:\s*\"FETCHED\"\s*\,\s*\"offers\"\s*.*?\"images\".*?\"variants\"\s*\:\s*\{\s*\"actual\_color\"\s*\:\s*\"actual_color\-([^\"]+)\"',dataWeb_1):
            
                        color = re.findall(r'(?mis)status\"\s*\:\s*\"FETCHED\"\s*\,\s*\"offers\"\s*.*?\"images\".*?\"variants\"\s*\:\s*\{\s*\"actual\_color\"\s*\:\s*\"actual_color\-([^\"]+)\"',dataWeb_1)[0]
            
                        product_info.append(color)
                    elif re.search(r'(?mis)status\"\s*\:\s*\"FETCHED\"\s*\,\s*\"offers\"\s*.*?\"images\".*?\"variants\"\s*\:\s*\{\s*\"size\"\s*\:\s*\"[^\"]+\"\s*\,\s*\"actual\_color\"\s*\:\s*\"actual_color\-([^\"]+)\"',dataWeb_1):
            
                        color = re.findall(r'(?mis)status\"\s*\:\s*\"FETCHED\"\s*\,\s*\"offers\"\s*.*?\"images\".*?\"variants\"\s*\:\s*\{\s*\"size\"\s*\:\s*\"[^\"]+\"\s*\,\s*\"actual\_color\"\s*\:\s*\"actual_color\-([^\"]+)\"',dataWeb_1)[0]
            
                        product_info.append(color)
                    elif re.search(r'(?mis)Color\s*<\/td>\s*<td\s*class\s*\=\"va[^>]*>\s*<div>([^<]+)',dataWeb_1):
            
                        color = re.findall(r'(?mis)Color\s*<\/td>\s*<td\s*class\s*\=\"va[^>]*>\s*<div>([^<]+)',dataWeb_1)[0]
            
                        product_info.append(color)
                    else:
                        product_info.append('')

                    if re.search(r'(?mis)\"id\"\:\s*\"size\"\,\s*\"name\"\:\s*\"Size\"\,\s*\"selectedValue\"\:\s*\"([^\"]+)\"\,',dataWeb_1):
            
                        size = re.findall(r'(?mis)\"id\"\:\s*\"size\"\,\s*\"name\"\:\s*\"Size\"\,\s*\"selectedValue\"\:\s*\"([^\"]+)\"\,',dataWeb_1)[0]
            
                        product_info.append(size)
                    elif re.search(r'(?mis)<option class=\"js\-variant\"\s*data\-id=\"[^<]*\" selected=\"\">([^<]*)<\/option>',dataWeb_1):
            
                        size = re.findall(r'(?mis)<option class=\"js\-variant\"\s*data\-id=\"[^<]*\" selected=\"\">([^<]*)<\/option>',dataWeb_1)[0]
            
                        product_info.append(size)
                    elif re.search(r'(?mis)label class=\"label\-bold\s*variant\-label\">\s*Size\:\s*<span class=\"js\-variant\-name\s*variant\-name\"[^<]*>([^<]+)<\/span>',dataWeb_1):
            
                        size = re.findall(r'(?mis)label class=\"label\-bold\s*variant\-label\">\s*Size\:\s*<span class=\"js\-variant\-name\s*variant\-name\"[^<]*>([^<]+)<\/span>',dataWeb_1)[0]
            
                        product_info.append(size)
                    elif re.search(r'(?mis)\"id\"\s*\:\s*\"diaper\_size\"\s*\,\s*\"name\"\s*\:\s*\"\s*Diaper\s*Size\"\s*\,\s*\"selectedValue\"\s*\:\s*\"([^\"]+)\"',dataWeb_1):
            
                        size = re.findall(r'(?mis)\"id\"\s*\:\s*\"diaper\_size\"\s*\,\s*\"name\"\s*\:\s*\"\s*Diaper\s*Size\"\s*\,\s*\"selectedValue\"\s*\:\s*\"([^\"]+)\"',dataWeb_1)[0]
            
                        product_info.append(size)
                    elif re.search(r'(?mis)status\"\s*\:\s*\"FETCHED\"\s*\,\s*\"offers\"\s*.*?\"images\".*?\"variants\"\s*\:\s*\{\s*\"size\"\s*\:\s*\"([^\"]+)\"\s*\,\s*\"actual\_color\"\s*\:\s*\"actual_color\-[^\"]+\"',dataWeb_1):
            
                        size = re.findall(r'(?mis)status\"\s*\:\s*\"FETCHED\"\s*\,\s*\"offers\"\s*.*?\"images\".*?\"variants\"\s*\:\s*\{\s*\"size\"\s*\:\s*\"([^\"]+)\"\s*\,\s*\"actual\_color\"\s*\:\s*\"actual_color\-[^\"]+\"',dataWeb_1)[0]
            
                        product_info.append(size)
                    else:
                        product_info.append('')

                    if re.search(r'(?mis)\"id\"\:\s*\"finish\"\,\s*\"name\"\:\s*\"Finish\"\,\s*\"selectedValue\"\:\s*\"([^\"]+)\"\,',dataWeb_1):
            
                        variation_tag = re.findall(r'(?mis)\"id\"\:\s*\"finish\"\,\s*\"name\"\:\s*\"Finish\"\,\s*\"selectedValue\"\:\s*\"([^\"]+)\"\,',dataWeb_1)[0]
            
                        product_info.append(variation_tag)
                    elif re.search(r'(?mis)status\"\s*\:\s*\"FETCHED\"\s*\,\s*\"offers\"\s*.*?\"images\".*?\"variants\"\s*\:\s*\{\s*\"capacity\"\s*\:\s*\"([^\"]+)\"',dataWeb_1):
            
                        variation_tag = re.findall(r'(?mis)status\"\s*\:\s*\"FETCHED\"\s*\,\s*\"offers\"\s*.*?\"images\".*?\"variants\"\s*\:\s*\{\s*\"capacity\"\s*\:\s*\"([^\"]+)\"',dataWeb_1)[0]
            
                        product_info.append(variation_tag)
                    elif re.search(r'(?mis)status\"\s*\:\s*\"FETCHED\"\s*\,\s*\"offers\"\s*.*?\"images\".*?\"variants\"\s*\:\s*\{\s*\"finish\"\s*\:\s*\"([^\"]+)\"',dataWeb_1):
            
                        variation_tag = re.findall(r'(?mis)status\"\s*\:\s*\"FETCHED\"\s*\,\s*\"offers\"\s*.*?\"images\".*?\"variants\"\s*\:\s*\{\s*\"finish\"\s*\:\s*\"([^\"]+)\"',dataWeb_1)[0]
            
                        product_info.append(variation_tag)
                    else:
                        product_info.append('')

                    f_walmart = open("walmart_product_information.csv", 'at')
                    writer = csv.writer(f_walmart,delimiter = ',', lineterminator='\r',quoting=csv.QUOTE_ALL) 
                    writer.writerow(product_info)
                    f_walmart.close()  
            


            elif v_id_pass == 1:

                pro_cs = 1

                if pro_cs == 1:
                    product_info = []
                    url_sub = re.sub(r'(?mis)(.*\/ip\/)[^\/]*\/(\d+).*',r'\1\2',url)
                    product_info.append(url_sub)
                    product_info.append(name)

                    if re.search(r'(?mis)(<meta\s*property\=og\:image\s*content=\"[^\"]+\")',dataWeb_1):
            
                        images = re.findall(r'(?mis)(<meta\s*property\=og\:image\s*content=\"[^\"]+\")',dataWeb)[0]
            
            
                    elif re.search(r'(?mis)(<meta\s*property=\"og\:image\"\s*content\=\"[^\"]+\")',dataWeb):
                        images = re.findall(r'(?mis)(<meta\s*property=\"og\:image\"\s*content\=\"[^\"]+\")',dataWeb)[0]
                        image_pass = 1
                    elif re.search(r'(?mis)\"imageAssets\"\s*\:\s*\[(.*?)\]',dataWeb):
                        images = re.findall(r'(?mis)\"imageAssets\"\s*\:\s*\[(.*?)\]',dataWeb)[0]
                        image_pass = 1
                    elif re.search(r'(?mis)\"images\"\s*\:\s*\{([^\}]+.*?)\}\s*\}',dataWeb):
                        images = re.findall(r'(?mis)\"images\"\s*\:\s*\{([^\}]+.*?)\}\s*\}',dataWeb)[0]
                        image_pass = 1
                    else:
                        image_pass = 0
                    images_array = []
                    #print image_pass
                    if image_pass == 1:
                
                
                        if re.search(r'(?mis)content=\"([^\"]+)\"',images):
            
                            img = re.findall(r'(?mis)content=\"([^\"]+)\"',images)[0]

                    #for img in images:
                            img = re.sub(r'(?mis)_215X215\.jpg','_500X500.jpg',img)
                            img = re.sub(r'(?mis)^\/\/www\.walmart','http\:\/\/www\.walmart',img)
                            img = re.sub(r'(?mis)\?.*','',img)
                            images_array.append(img)
            
            
                        if re.search(r'(?mis)\"hero\"\s*\:\s*\"([^\"]+)\"',images):
            
                            img = re.findall(r'(?mis)\"hero\"\s*\:\s*\"([^\"]+)\"',images)[0]
                    #for img in images:
                            img = re.sub(r'(?mis)_215X215\.jpg','_500X500.jpg',img)
                            img = re.sub(r'(?mis)^\/\/www\.walmart','http\:\/\/www\.walmart',img)
                            img = re.sub(r'(?mis)\?.*','',img)
                            images_array.append(img)

                        if re.search(r'(?mis)\"main\"\s*\:\s*\"([^\"]+)\"',images):
            
                            img = re.findall(r'(?mis)\"main\"\s*\:\s*\"([^\"]+)\"',images)[0]
                    #for img in images:
                            img = re.sub(r'(?mis)_215X215\.jpg','_500X500.jpg',img)
                            img = re.sub(r'(?mis)^\/\/www\.walmart','http\:\/\/www\.walmart',img)
                            img = re.sub(r'(?mis)\?.*','',img)
                            images_array.append(img)

                    product_info.append(images_array[0])

                    sku = re.sub(r'(?mis).*\/ip\/[^\/]*\/(\d+).*',r'\1',url)

                    ava_pri = "https://www.walmart.com/product/dynamic/"+sku+"?selected=true"
                    dataWeb_ava = requests_lib_prod(ava_pri)

                    if re.search(r'(?mis)wasPrice":{"currencyAmount":([^\,]*)\,',dataWeb_ava):
            
                        was_price = re.findall(r'(?mis)wasPrice":{"currencyAmount":([^\,]*)\,',dataWeb_ava)[0]
            
                        product_info.append(was_price)
                    else:
                        product_info.append('')

                    

                    if re.search(r'(?mis)currencyAmount":([^\,]*)\,',dataWeb_ava):
            
                        price = re.findall(r'(?mis)currencyAmount":([^\,]*)\,',dataWeb_ava)[0]
            
                        product_info.append(price)
                    elif re.search(r'(?mis)Price-group" role="contentinfo" aria-label="\W([^\"]*)\"',dataWeb_ava):
            
                        price = re.findall(r'(?mis)Price-group" role="contentinfo" aria-label="\W([^\"]*)\"',dataWeb_ava)[0]
            
                        product_info.append(price)
                    else:
                        product_info.append('')

                    if re.search(r'(?mis)shippingDeliveryDateMessage":"([^\"]*)\"',dataWeb_ava):
            
                        ava = re.findall(r'(?mis)shippingDeliveryDateMessage":"([^\"]*)\"',dataWeb_ava)[0]
                        ava = re.sub(r'(?mis)See delivery options','available',ava)
                        product_info.append(ava)
                    else:
                        product_info.append('')

                    if re.search(r'(?mis)\"id\"\:\s*\"actual\_color\"\,\s*\"name\"\:\s*\"Actual\s*Color\"\,\s*\"selectedValue\"\:\s*\"([^\"]+)\"\,',dataWeb):
            
                        color = re.findall(r'(?mis)\"id\"\:\s*\"actual\_color\"\,\s*\"name\"\:\s*\"Actual\s*Color\"\,\s*\"selectedValue\"\:\s*\"([^\"]+)\"\,',dataWeb)[0]
            
                        product_info.append(color)
                    elif re.search(r'(?mis)<tr\s*class=js\-product\-specs\-row>\s*<td>\s*Color\s*\:\s*<\/td>\s*<td>([^<]+)<\/td>',dataWeb):
            
                        color = re.findall(r'(?mis)<tr\s*class=js\-product\-specs\-row>\s*<td>\s*Color\s*\:\s*<\/td>\s*<td>([^<]+)<\/td>',dataWeb)[0]
            
                        product_info.append(color)
                    elif re.search(r'(?mis)status\"\s*\:\s*\"FETCHED\"\s*\,\s*\"offers\"\s*.*?\"images\".*?\"variants\"\s*\:\s*\{\s*\"actual\_color\"\s*\:\s*\"actual_color\-([^\"]+)\"',dataWeb):
            
                        color = re.findall(r'(?mis)status\"\s*\:\s*\"FETCHED\"\s*\,\s*\"offers\"\s*.*?\"images\".*?\"variants\"\s*\:\s*\{\s*\"actual\_color\"\s*\:\s*\"actual_color\-([^\"]+)\"',dataWeb)[0]
            
                        product_info.append(color)
                    elif re.search(r'(?mis)status\"\s*\:\s*\"FETCHED\"\s*\,\s*\"offers\"\s*.*?\"images\".*?\"variants\"\s*\:\s*\{\s*\"size\"\s*\:\s*\"[^\"]+\"\s*\,\s*\"actual\_color\"\s*\:\s*\"actual_color\-([^\"]+)\"',dataWeb):
            
                        color = re.findall(r'(?mis)status\"\s*\:\s*\"FETCHED\"\s*\,\s*\"offers\"\s*.*?\"images\".*?\"variants\"\s*\:\s*\{\s*\"size\"\s*\:\s*\"[^\"]+\"\s*\,\s*\"actual\_color\"\s*\:\s*\"actual_color\-([^\"]+)\"',dataWeb)[0]
            
                        product_info.append(color)
                    elif re.search(r'(?mis)Color\s*<\/td>\s*<td\s*class\s*\=\"va[^>]*>\s*<div>([^<]+)',dataWeb):
            
                        color = re.findall(r'(?mis)Color\s*<\/td>\s*<td\s*class\s*\=\"va[^>]*>\s*<div>([^<]+)',dataWeb)[0]
            
                        product_info.append(color)
                    else:
                        product_info.append('')

                    if re.search(r'(?mis)\"id\"\:\s*\"size\"\,\s*\"name\"\:\s*\"Size\"\,\s*\"selectedValue\"\:\s*\"([^\"]+)\"\,',dataWeb):
            
                        size = re.findall(r'(?mis)\"id\"\:\s*\"size\"\,\s*\"name\"\:\s*\"Size\"\,\s*\"selectedValue\"\:\s*\"([^\"]+)\"\,',dataWeb)[0]
            
                        product_info.append(size)
                    elif re.search(r'(?mis)<option class=\"js\-variant\"\s*data\-id=\"[^<]*\" selected=\"\">([^<]*)<\/option>',dataWeb):
            
                        size = re.findall(r'(?mis)<option class=\"js\-variant\"\s*data\-id=\"[^<]*\" selected=\"\">([^<]*)<\/option>',dataWeb)[0]
            
                        product_info.append(size)
                    elif re.search(r'(?mis)label class=\"label\-bold\s*variant\-label\">\s*Size\:\s*<span class=\"js\-variant\-name\s*variant\-name\"[^<]*>([^<]+)<\/span>',dataWeb):
            
                        size = re.findall(r'(?mis)label class=\"label\-bold\s*variant\-label\">\s*Size\:\s*<span class=\"js\-variant\-name\s*variant\-name\"[^<]*>([^<]+)<\/span>',dataWeb)[0]
            
                        product_info.append(size)
                    elif re.search(r'(?mis)\"id\"\s*\:\s*\"diaper\_size\"\s*\,\s*\"name\"\s*\:\s*\"\s*Diaper\s*Size\"\s*\,\s*\"selectedValue\"\s*\:\s*\"([^\"]+)\"',dataWeb):
            
                        size = re.findall(r'(?mis)\"id\"\s*\:\s*\"diaper\_size\"\s*\,\s*\"name\"\s*\:\s*\"\s*Diaper\s*Size\"\s*\,\s*\"selectedValue\"\s*\:\s*\"([^\"]+)\"',dataWeb)[0]
            
                        product_info.append(size)
                    elif re.search(r'(?mis)status\"\s*\:\s*\"FETCHED\"\s*\,\s*\"offers\"\s*.*?\"images\".*?\"variants\"\s*\:\s*\{\s*\"size\"\s*\:\s*\"([^\"]+)\"\s*\,\s*\"actual\_color\"\s*\:\s*\"actual_color\-[^\"]+\"',dataWeb):
            
                        size = re.findall(r'(?mis)status\"\s*\:\s*\"FETCHED\"\s*\,\s*\"offers\"\s*.*?\"images\".*?\"variants\"\s*\:\s*\{\s*\"size\"\s*\:\s*\"([^\"]+)\"\s*\,\s*\"actual\_color\"\s*\:\s*\"actual_color\-[^\"]+\"',dataWeb)[0]
            
                        product_info.append(size)
                    else:
                        product_info.append('')

                    if re.search(r'(?mis)\"id\"\:\s*\"finish\"\,\s*\"name\"\:\s*\"Finish\"\,\s*\"selectedValue\"\:\s*\"([^\"]+)\"\,',dataWeb):
            
                        variation_tag = re.findall(r'(?mis)\"id\"\:\s*\"finish\"\,\s*\"name\"\:\s*\"Finish\"\,\s*\"selectedValue\"\:\s*\"([^\"]+)\"\,',dataWeb)[0]
            
                        product_info.append(variation_tag)
                    elif re.search(r'(?mis)status\"\s*\:\s*\"FETCHED\"\s*\,\s*\"offers\"\s*.*?\"images\".*?\"variants\"\s*\:\s*\{\s*\"capacity\"\s*\:\s*\"([^\"]+)\"',dataWeb):
            
                        variation_tag = re.findall(r'(?mis)status\"\s*\:\s*\"FETCHED\"\s*\,\s*\"offers\"\s*.*?\"images\".*?\"variants\"\s*\:\s*\{\s*\"capacity\"\s*\:\s*\"([^\"]+)\"',dataWeb)[0]
            
                        product_info.append(variation_tag)
                    elif re.search(r'(?mis)status\"\s*\:\s*\"FETCHED\"\s*\,\s*\"offers\"\s*.*?\"images\".*?\"variants\"\s*\:\s*\{\s*\"finish\"\s*\:\s*\"([^\"]+)\"',dataWeb):
            
                        variation_tag = re.findall(r'(?mis)status\"\s*\:\s*\"FETCHED\"\s*\,\s*\"offers\"\s*.*?\"images\".*?\"variants\"\s*\:\s*\{\s*\"finish\"\s*\:\s*\"([^\"]+)\"',dataWeb)[0]
            
                        product_info.append(variation_tag)
                    else:
                        product_info.append('')

                    f_walmart = open("walmart_product_information.csv", 'at')
                    writer = csv.writer(f_walmart,delimiter = ',', lineterminator='\r',quoting=csv.QUOTE_ALL) 
                    writer.writerow(product_info)
                    f_walmart.close()  
            
                





def readCsvFile():

    dup_array = []
    process = 1
    count = 0
    f_walmart = open("walmart_product_information.csv", 'at')
    writer = csv.writer(f_walmart,delimiter = ',', lineterminator='\r',quoting=csv.QUOTE_ALL)
    writer.writerow(["URL","PRODUCT_NAME","IMAGES","WAS_PRICE","PRICE","AVAILABILITY","COLOR","SIZE","VARIATION_TAG"])
    f_walmart.close()

    f_write = open(r'product_urls_seen.txt','a')
    f_read = open(r'product_urls_seen.txt','r')

    for f_url in f_read:
        f_url = re.sub(r'(?mis)\n*','',f_url)
        
        dup_array.append(f_url)
    while process == 1:
        count = count + 1
        with codecs.open("product_urls.csv", 'rU') as csvfile1:
            walmart_product_urls = csv.reader(csvfile1, delimiter=',', quoting=csv.QUOTE_ALL)
            count  = 0
            for w_p in walmart_product_urls:
                count = count + 1
                if count == 1:
                    pass
                else:
                    
                    
                    if w_p[1] in dup_array:
                        print "product url already crawled"
                        pass
                    else:
                        productInfoExtraction(w_p[1])
                        dup_array.append(w_p[1])
                        f_write.write(w_p[1]+"\n")
        if count == 10000000:
            process = 0

readCsvFile()
#productInfoExtraction("https://www.walmart.com/ip/Faded-Glory-Men-s-Canvas-Slip-On-Shoe/50921906?variantFieldId=actual_color")
