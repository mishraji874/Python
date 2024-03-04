line = "The website is http://www.example.com and it has great content."
start = line.find("http://")
if start != -1:
    end = line.find(" ", start)
    if end != -1:
        url = line[start:end]
        print("The URL is:", url)
else:
    print("No URL found in the line.")