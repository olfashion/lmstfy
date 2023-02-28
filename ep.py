import provisioning.base_62_counter as b62
from db_tool import ShortLinkDB


# for i in range(100):
#     print(b62.encode(i))

db = ShortLinkDB('localhost', '5432', 'short_link', 'admin', 'temp')
result = db.get_provisions(100)

for data in result:
    print(data[0])

