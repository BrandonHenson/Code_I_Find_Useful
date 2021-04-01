from bing_image_downloader import downloader

list = ['']

for i in list:
   item = i
   downloader.download(item, limit=150,  output_dir='IMAGES',adult_filter_off=False, force_replace=False, timeout=1)







'''
from bing_image_downloader import downloader

list = ['water meter','car','flower']
for i in list:
  item = i
  downloader.download(item, limit=5, output_dir='IMAGES', adult_filter_off=True, force_replace=False, timeout=60)
'''