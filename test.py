# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

## open website for the information of semiconductor industry
import webbrowser

# A list of websites you want to open
urls = [
    "https://www.electronicsweekly.com/",
    "https://www.semiconductor-digest.com/category/semiconductors/",
    "https://xtech.nikkei.com/top/latestdaily.html",
    "https://www.gartner.com/en?utm_source=google&utm_medium=cpc&utm_campaign=GTR_NA_2022_GTR_CPC_SEM1_BRANDCAMPAIGNCORE&utm_adgroup=137260808579&utm_term=gartner&ad=603410086008&matchtype=e&gad_source=1&gclid=Cj0KCQiAouG5BhDBARIsAOc08RQoCoG8SakmzCa95IXRJGj9ZjeFlcObpFF1Jw7nZ-1oGC8mebCEsbEaArH8EALw_wcB",
    "https://www.idc.com/"
]

# Open each URL
for url in urls:
    webbrowser.open(url)