from request_lib import requests_lib
import time
import csv
import re
import os

def extractPaginationProductLinks(pagn_url):
    proceed = 1
    if proceed == 1:
        product_urls = []
        
        f_walmart = open("product_urls.csv", 'at')
        writer = csv.writer(f_walmart,delimiter = ',', lineterminator='\r',quoting=csv.QUOTE_ALL)
        pagn_url = re.sub(r'amp\;','',pagn_url)
        dataWeb = requests_lib(pagn_url)
        print "Extracting product urls form"+pagn_url
        if re.search(r'(?mis)productId":\".*?url\"\:\"([^\/]*\/ip\/[^\"]*)\"',dataWeb):
        
            product_links = re.findall(r'(?mis)productId":\".*?url\"\:\"([^\/]*\/ip\/[^\"]*)\"',dataWeb)

            for prod_link in product_links:
                if prod_link.startswith('https://www.') or prod_link.startswith('http://www.') or prod_link.startswith('https://') or prod_link.startswith('http://'):
                    product_urls.append(prod_link)
                else:
                    product_urls.append("https://www.walmart.com"+prod_link)

        for prod_url in product_urls:
            writer.writerow([pagn_url,prod_url])
        f_walmart.close()

        if re.search(r'(?mis)next" href="([^\"]*)\"',dataWeb):
        
            pag_links = re.findall(r'(?mis)next" href="([^\"]*)\"',dataWeb)[0]

            
            if pag_links.startswith('https://www.') or pag_links.startswith('http://www.') or pag_links.startswith('https://') or pag_links.startswith('http://'):

            
                extractPaginationProductLinks(pag_links)
            else:
                extractPaginationProductLinks("https://www.walmart.com"+pag_links)

def extractProductLinks(sub_url):
    f_walmart = open("product_urls.csv", 'at')
    writer = csv.writer(f_walmart,delimiter = ',', lineterminator='\r',quoting=csv.QUOTE_ALL)
    writer.writerow(["CATEGORY_URL","PRODUCT_URL"])
    f_walmart.close()
    
    for url in set(sub_url):
        if re.search(r'(?mis)\/browser\/|\/cp\/',url):
            product_urls = []
        
            f_walmart = open("product_urls.csv", 'at')
            writer = csv.writer(f_walmart,delimiter = ',', lineterminator='\r',quoting=csv.QUOTE_ALL)
            url = re.sub(r'amp\;','',url)
            dataWeb = requests_lib(url)
            print "Extracting product urls form"+url
            if re.search(r'(?mis)productId":\".*?url\"\:\"([^\/]*\/ip\/[^\"]*)\"',dataWeb):
        
                product_links = re.findall(r'(?mis)productId":\".*?url\"\:\"([^\/]*\/ip\/[^\"]*)\"',dataWeb)

                for prod_link in product_links:
                    if prod_link.startswith('https://www.') or prod_link.startswith('http://www.') or prod_link.startswith('https://') or prod_link.startswith('http://'):
                        product_urls.append(prod_link)
                    else:    
                        product_urls.append("https://www.walmart.com"+prod_link)

            for prod_url in product_urls:
                writer.writerow([url,prod_url])
            f_walmart.close()


            if re.search(r'(?mis)SingleItem","seeAllUrl":\"([^\"]*)\"',dataWeb):
        
                pag_links = re.findall(r'(?mis)SingleItem","seeAllUrl":\"([^\"]*)\"',dataWeb)

                for pag_link in pag_links:
                    if pag_link.startswith('https://www.') or pag_link.startswith('http://www.') or pag_link.startswith('https://') or pag_link.startswith('http://'):
                        extractPaginationProductLinks(pag_link)
                    else:
                        extractPaginationProductLinks("https://www.walmart.com"+pag_link)

            if re.search(r'(?mis)next" href="([^\"]*)\"',dataWeb):
        
                pag_links = re.findall(r'(?mis)next" href="([^\"]*)\"',dataWeb)[0]
                if pag_links.startswith('https://www.') or pag_links.startswith('http://www.') or pag_links.startswith('https://') or pag_links.startswith('http://'):

            
                    extractPaginationProductLinks(pag_links)
                else:
                    extractPaginationProductLinks("https://www.walmart.com"+pag_links)

            

        
            

            

def extractCateogryLinks(url):
    sub_url = []
    url = re.sub(r'amp\;','',url)
    dataWeb = requests_lib(url)



    if re.search(r'(?mis)uid\"[^\,]*\,\"linkText":"[^\,]*\,\"title[^\,]*\,\"clickThrough":{"type":\"url","value":"([^\"]*)\"',dataWeb):
        
        sub_cat_links = re.findall(r'(?mis)uid\"[^\,]*\,\"linkText":"[^\,]*\,\"title[^\,]*\,\"clickThrough":{"type":\"url","value":"([^\"]*)\"',dataWeb)
        for sub_cat in sub_cat_links:
            #print "https://www.walmart.com"+sub_cat
            if sub_cat.startswith('https://www.') or sub_cat.startswith('http://www.') or sub_cat.startswith('https://') or sub_cat.startswith('http://'):
                sub_url.append(sub_cat)
            else:
                sub_url.append("https://www.walmart.com"+sub_cat)
    #print sub_url[0]

    extractProductLinks(sub_url)


            




seed = "https://www.walmart.com/all-departments"

extractCateogryLinks(seed)

#extractPaginationProductLinks("https://www.walmart.com/c/kp/kitchen-islands?cat_id=4037&create_ids=counter-height-chairs,pub-table-sets,kitchen-islands,table-sets,kitchen-carts-on-wheels,dinning-table-sets,buffet-cabinets,bar-tables,curio-cabinets,counter-height-dining-sets,east-west-furniture-dining-tables,beechwood-stool")