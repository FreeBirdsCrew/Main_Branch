document_1_text = 'This is document one'
document_2_text = 'This is document two'

document_1_words = document_1_text.split()
document_2_words = document_2_text.split()

common = set(document_1_words).intersection( set(document_2_words) )
unique = set(document_1_words).symmetric_difference( set(document_2_words) )
print(common)
print(unique)
