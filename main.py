print("Breachforum CDN Downloader")

import os
import requests
import threading

def downloader_main(list_of_links):
    cwd = os.getcwd()
    files_path = os.path.join(cwd , "Downloads")
   
    if os.path.isdir(files_path):
        pass
    else:
        os.mkdir(files_path)

    for link in list_of_links:
        print(f"Downloading breach --> {link[1]}")
        r = requests.get(link[0], stream = True) 

        with open(os.path.join(files_path , link[1]),"wb") as f: 
            for chunk in r.iter_content(chunk_size=1024):
                if chunk: 
                    f.write(chunk) 


main_mirror = "https://river.bz"

r = requests.get(main_mirror)
all_links = r.text
all_links = all_links.split("\n")[4:-3:]

link_lists = []
link_list = []

for link in all_links:
    link = link.split(">")[1].replace("</a" , "").replace(" " , "_")
    full_url = f"https://river.bz/{link}"
    if len(link_list) == 10:
        link_lists.append(link_list)
        link_list = []
    else:
        link_list.append((full_url , link))
else:
    link_lists.append(link_list)

for lst in link_lists:
    threading.Thread(target=downloader_main,args=(lst,)).start()

