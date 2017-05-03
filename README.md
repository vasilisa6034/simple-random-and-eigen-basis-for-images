# simple-random-and-eigen-basis-for-images
my experience in variants basis for images
This little example can help in understanding of images vector space. 
We can consider an image as vector, which dimensionality equal to number of pixels. Let's consider images with just three pixels. Easy to see that simpleast basis for such space (1,0,0), (0,1,0) and (0,0,1), but what if our images lie on one surface, or even one line? Then we can transfere to another, more compact basis, for which we can store two (surface) or even one (line) rather three numbers (for each pixel). That's how compression  works.
Another case - we truncate our scape (simply throwing elements of basis - basis vectors). In straightforward case ((1,0,0), ...) we simply will throw pixels, but what will happen in more fitted basis case? In this sketch I tried to cover this questions.

I consider human face images. To form eigen basis I use this database http://vis-www.cs.umass.edu/lfw/. **dataPrepere.py** - help to form **referenceImages.dat** which consist of face images as columns in one matrix. Main file **simple_random_eigen_basis.py**. **inputImage.dat** consist of separated from database image. 



![figure_1](https://cloud.githubusercontent.com/assets/19648595/25664016/5ecdfb6c-302a-11e7-85ef-cfbac1f33ae2.png)
![figure_2](https://cloud.githubusercontent.com/assets/19648595/25662323/2ca23fae-3025-11e7-8171-6b25113e37d2.png)
![figure_3](https://cloud.githubusercontent.com/assets/19648595/25662316/2c351dfc-3025-11e7-8ae7-72343657cf51.png)
![figure_4](https://cloud.githubusercontent.com/assets/19648595/25662317/2c391b0a-3025-11e7-864b-fc45dcdcd263.png)
![figure_5](https://cloud.githubusercontent.com/assets/19648595/25662318/2c3cbc1a-3025-11e7-903d-038dab0de62c.png)
![figure_6](https://cloud.githubusercontent.com/assets/19648595/25662319/2c44acea-3025-11e7-8564-dac7a2b116ec.png)
![figure_7](https://cloud.githubusercontent.com/assets/19648595/25662320/2c52ec56-3025-11e7-8ae1-e70e212a54ce.png)
![figure_8](https://cloud.githubusercontent.com/assets/19648595/25662321/2c5c9e68-3025-11e7-89a8-30435b6435d6.png)

