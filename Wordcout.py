#Function to remove all punctuation

import re
def removePunctuation(text):
    """Removes punctuation, changes to lower case, and strips leading and trailing spaces.

    Note:
        Only spaces, letters, and numbers should be retained.  Other characters should should be
        eliminated (e.g. it's becomes its).  Leading and trailing spaces should be removed after
        punctuation is removed.

    Args:
        text (str): A string.

    Returns:
        str: The cleaned up string.
    """
  
    return re.sub(r'[^a-z0-9\s]',"",text.lower()).strip()
print removePunctuation('Hi, you!')
print removePunctuation(' No under_score!')
print removePunctuation(' *      Remove punctuation then spaces  * ')



#Loading the dataset 
# link: http://www.gutenberg.org/cache/epub/100/pg100.txt
 
import os.path
baseDir = os.path.join('databricks-datasets')
inputPath = os.path.join('cs100', 'lab1', 'data-001', 'shakespeare.txt')
fileName = os.path.join(baseDir, inputPath)

shakespeareRDD = (sc
                  .textFile(fileName, 8)
                  .map(removePunctuation))
print '\n'.join(shakespeareRDD
                .zipWithIndex()  # to (line, lineNum)
                .map(lambda (l, num): '{0}: {1}'.format(num, l))  # to 'lineNum: line'
                .take(15))



#Splitting and counting the total number of words.

shakespeareWordsRDD = shakespeareRDD.flatMap(lambda line: line.split(' '))
shakespeareWordCount = shakespeareWordsRDD.count()
print shakespeareWordsRDD.top(5)
print shakespeareWordCount



#Remove empty elements

shakeWordsRDD = shakespeareWordsRDD.filter(lambda word: len(word)>0)
shakeWordCount = shakeWordsRDD.count()
print shakeWordCount


#Count the words

top15WordsAndCounts = wordCount(shakeWordsRDD).takeOrdered(15, key=lambda (w,c): -c)

print '\n'.join(map(lambda (w, c): '{0}: {1}'.format(w, c), top15WordsAndCounts))


