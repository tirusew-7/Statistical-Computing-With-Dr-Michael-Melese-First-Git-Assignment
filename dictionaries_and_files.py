# Dictionary and Files

data =  """Video provides a powerful way to help you prove your point. When you click Online Video, you can paste in the embed code for the video you want to add. You can also type a keyword to search online for the video that best fits your document. To make your document look professionally produced, Word provides header, footer, cover page, and text box designs that complement each other. For example, you can add a matching cover page, header, and sidebar.
Click Insert and then choose the elements you want from the different galleries. Themes and styles also help keep your document coordinated. When you click Design and choose a new Theme, the pictures, charts, and SmartArt graphics change to match your new theme. When you apply styles, your headings change to match the new theme. Save time in Word with new buttons that show up where you need them.
To change the way a picture fits in your document, click it and a button for layout options appears next to it. When you work on a table, click where you want to add a row or a column, and then click the plus sign. Reading is easier, too, in the new Reading view. You can collapse parts of the document and focus on the text you want. If you need to stop reading before you reach the end, Word remembers where you left off - even on another device.
Video provides a powerful way to help you prove your point. When you click Online Video, you can paste in the embed code for the video you want to add. You can also type a keyword to search online for the video that best fits your document. To make your document look professionally produced, Word provides header, footer, cover page, and text box designs that complement each other. For example, you can add a matching cover page, header, and sidebar.
"""

# Step 1: Clean the text
preprocessed_data = data.replace(",", "").replace(".", "").replace("'", "").lower()

# Step 2: Split into words
word_list = preprocessed_data.split()

# Step 3: Count frequency using a dictionary
word_fre_count = {}

for word in word_list:
    if word in word_fre_count:
        word_fre_count[word] += 1
    else:
        word_fre_count[word] = 1

# Step 4: Save the result to a CSV file
with open("word_count.csv", "w", encoding="utf-8") as to_file:
    to_file.write("Word,Frequency\n")
    for stat in word_fre_count:
        to_file.write(stat + "," + str(word_fre_count[stat]) + "\n")

print("Done! Check your folder — word_count.csv has been created.")

# Display CSV content
with open("word_count.csv", 'r', encoding='utf-8') as reader:
    print(reader.read())
