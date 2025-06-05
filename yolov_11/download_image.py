from simple_image_download import simple_image_download

response = simple_image_download.simple_image_download()  # This line works in the correct version

keywords = ["closed cardboard boxes"]

for kw in keywords:
    response.download(kw, 200)
