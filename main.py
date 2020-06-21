from shutil import copyfile

source_file = 'format.html'

url_list = ["https://www.abc.com/d-e/f-y-z.html", 
             "https://www.abc.com/x-y-z.html"]

for url in url_list:
    file_name = url.split("/")[-1]
    with open(file_name, 'a') as f:
        f.write(f"url: {file_name}\n")
        copyfile(source_file, file_name)
        
        
