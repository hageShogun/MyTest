# About ImageNet dataset and ILSVRC2012 dataset

## ImageNet dataset
- ImageNet dataset is a large (more than 14M) image dataset which has the correspondig structure to the WordNet.
- ImageNet dataset cannot be download from the official site for commercial use.
- But you can download the image URL list and download them by yourself.

## ILSVRC2012 dataset
- ILSVRC2012 is the ImageNet Large Scale Visual Recognition Challenge held at 2012.
- In usual, when the model is saied to be trained with ImageNet dataset, it means the model is trained with ILSVRC2012 dataset.
- The dataset is consist of 1.2M images for training, 50,000 for validation and 100,000 for evaluation. The number of the classes is 1,000.


# ILSVRC2012 link

- [Competition official site](image-net.org/challenges/LSVRC/2012/index)
- [Class label list](http://image-net.org/challenges/LSVRC/2012/browse-synsets)
- [URL list](http://image-net.org/challenges/LSVRC/2012/browse-synsets)
- [WordNetID vs Image label]http://image-net.org/challenges/LSVRC/2012/browse-synsets

# Scripts
- gen_wnid_dictionary.py
  - generate a wnid(wordnet id) to label dictionary and label to wnid dictionary.
- gen_url_db.py
  - generate a URL database on sqlite3.


# Example class

```
jaguar, panther, Panthera onca, Felis onca
Siamese cat, Siamese
cheetah, chetah, Acinonyx jubatus
dugong, Dugong dugon
soccer ball
golfcart, golf cart
golf ball
airliner
warplane, military plane
airship, dirigible
acoustic guitar
electric guitar
violin, fiddle
cock
peacock
black grouse
great grey owl, great gray owl, Strix nebulosa
peacock
analog clock
digital clock
wall clock
hourglass
sundial
freight car
passenger car, coach, carriage
electric locomotive
steam locomotive
bullet train, bullet
great white shark, white shark, man-eater, man-eating shark, Carcharodon carcharias
tiger shark, Galeocerdo cuvieri
hammerhead, hammerhead shark
broccoli
cauliflower
zucchini, courgette
cucumber, cuke
```