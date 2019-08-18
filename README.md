# Dataset Split [![Build Status](https://travis-ci.com/muriloxyz/dataset-split.svg?token=4VpFwZFY4CedtAWXHopv&branch=master)](https://travis-ci.com/muriloxyz/dataset-split)[![](https://img.shields.io/badge/pypi-v0.17-blue.svg?maxAge=3600)](https://pypi.org/project/dataset-split/)[![](https://img.shields.io/badge/license-MIT-orange.svg?maxAge=3600)](https://github.com/muriloxyz/dataset-split/blob/master/LICENSE)

Splits your dataset folder into train/validation/test subsets. Very useful for non-csv data, like images.

![](demo.gif)

## Installation

```
(sudo) pip install dataset-split
```

* * *

## Usage

```
dataset-split <path> (optional arguments)
```

| Options | Usage | Description |
| --- | --- | --- |
| ratio | `(-r or ratio) <train> <test> <valid>` | Sets the ratios that will split the dataset! Floats are interpreted as percentages. The order must be ratio-valid-test and must sum up to 1.0 (won't run otherwise + float inaccuracy doesn't crash the app) |
| noshuffle | `-ns or noshuffle` | When present, data won't be shuffled and will go in alphabetic order to their respective new folders. |
| copy | `-c or copy` | When present, make copies instead of moving. Will generate a ``_split_`` folder and generate the split inside it, preserving original directory structure and files. (May be slow and take a lot of space) |

* * *

## License

Built under the MIT License.
