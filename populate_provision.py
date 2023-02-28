import provisioning.base_62_counter as b62
from db_tool import ShortLinkDB


insert_data = []
db = ShortLinkDB('localhost', '5432', 'short_link', 'admin', 'temp')
for i in range (1, 916132831):
    insert_data.append((b62.encode(i), 0, None))
    if i % 5000 == 0:
        print('Inserting data {}'.format(str(i)))
        db.insert_provision_bulk(insert_data)
        insert_data = []
