import time
import configset
import collection
import add_field_type
import add_field
import add_doc
import add_synonyms
import define_resource_for_synonym

start = time.time()

#for i in range(20):
#+ str(i)

collection_name = "collection_13"
configset.create_configset(collection_name)
collection.create_collection(collection_name)
define_resource_for_synonym(collection_name)
add_synonyms(collection_name)
add_field_type.add_field_type(collection_name)
add_field.add_field(collection_name)
add_doc.add_document(collection_name)

end = time.time()

print(f"runtime of the program is {end - start}")
