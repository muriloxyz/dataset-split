# Dataset Split
Splits your dataset folder into train/validation/test subsets. Very useful for non-csv data, like images.



### Installation
To be added

---

### Usage (will change soon) 

    python split.py <dataset_path> --ratio <ratios>
    
| Options | Usage | Description |
|--|--|--|
| ratio | `(-r) --ratio <train> <valid> <test>` | Sets the ratios that will split the dataset! Floats are interpreted as percentages. The order must be ratio-valid-test and must sum up to 1.0 (won't run otherwise) |
| noshuffle |  to be implemented | When present, data won't be shuffled and will go in alphabetic order to their respective new folders. |
| copy| to be implemented | When present, make copies instead of moving. Will generate a ``__splited__`` folder and generate the split inside it, preserving original directory structure and files. (May be slow and take a lot of space) |

---

### License
Built under the MIT License.
