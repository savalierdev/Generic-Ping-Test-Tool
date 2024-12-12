from functions import *



list_and_print_categories()
catnum = get_category_input()
listandprintservicelist(catnum)
serviceip = getserviceinput(catnum)
print('')
print(ping_server(serviceip))
print('')