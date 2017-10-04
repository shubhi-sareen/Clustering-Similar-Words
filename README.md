# Determining-Similarity-Among-Words
Using Document Level Co-Occurrence Matrix to determine similar words

## Document Level Co-Occurrence Matrix:

### Starting with an Example:
Let us consider 2 Documents:
* **Content of Document 1**: I like to design and paint
* **Contents of Document 2**: I like to code

**Resulting Co-Occurrence Matrix:**

| ... | I | like | to | design | and | paint | code |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I | 0 | 2 | 2 | 1 | 1 | 1 | 1 |
| like | 2 | 0 | 2 | 1 | 1 | 1 | 1 |
| to | 2 | 2 | 0 | 1 | 1 | 1 | 1 |
| design | 1 | 1 | 1 | 0 | 1 | 1 | 1 |
| and | 1 | 1 | 1 | 1 | 0 | 1 | 1 |
| paint | 1 | 1 | 1 | 1 | 1 | 0 | 1 |
| code | 1 | 1 | 1 | 0 | 0 | 0 | 0 |

**Intuition**: I and like occur together in 2 documents while I and design occur together in 1 document.

## Result for Database Used

The projection of the co-occurrence matrix for a subset of the datasbase on a 2 Dimensional Plane is as follows:

**Projecting Words:**
![alt text](https://github.com/shubhi-sareen/Determining-Similarity-Among-Words/blob/master/img/words.jpg "Word Projection in 2-D")

**Projecting Words as Dots:**
![alt text](https://github.com/shubhi-sareen/Determining-Similarity-Among-Words/blob/master/img/dots.jpg "Words Projected as Dots in 2-D")


**A few examples of words which cluster together:**
* Words like producing, plant, tea, plantation, green, cocoa, coffee cluster together.
* Words like grain, cereal, corn/sorghum, wheat/barley, maize together.
* Words like employees, purchased, insurance, company cluster together.

The clustered words represent **possible topics** in the underlying documents and it also in accordance with the pre-defined topics. Therefore this approach can be used to extract topics from underlying documents.


Dataset used: Reuters-21578, Distribution 1.0
