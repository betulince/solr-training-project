import time
import add_doc

start = time.time()

for i in range(20):
    collection_name = "collection_20_2" + str(i)

    add_doc.add_document(collection_name)

end = time.time()

print(f"runtime of the program is {end-start}")