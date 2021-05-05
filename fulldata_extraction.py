from utils.urlparseimmo import urlparseimmo


url = 'https://www.immoweb.be/en/classified/house/for-sale/woluwe-saint-pierre/1150/9310094?searchId=60929d137685e'
infos_in_url = urlparseimmo(url)

print(infos_in_url)
