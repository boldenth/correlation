# correlation

## About

This software can be used to find correlations between datasets, even if the
data are relatively obscure. 

## Usage

For examples of the different functionality `correlation` provides, see the [sample notebook](sample_notebook.ipynb).

### Dependencies

correlation makes use of a few existing libraries, which you must install
yourself. (numpy, scipy, matplotlib, scikit-learn)

A large portion of the analysis in correlation takes advantage of the `DataFrame` object in [pandas][pandas].
Since [numpy][numpy] is a dependency of pandas, you must also install it.
```
pip install numpy
python3 -m pip install --upgrade pandas
```

The visual analysis in correlation is built on top of the powerful [matplotlib][matplotlib].
```
python -m pip install -U matplotlib
```

Finally, the machine learning library [scikit-learn][scikit] which is used to perform some data analysis.
```
pip install -U scikit-learn
```

### Installation

A PyPI package is in the works, but in the meantime, you mush clone the repository and use the API as follows:
```
git clone https://github.com/boldenth/correlation
python3
>>> import sys
>>> import os
>>> sys.path.append(os.getcwd() + '/correlation')
>>> import correlation as co
```

## License

This software is licensed under the [MIT](LICENSE.txt) License.

[numpy]: http://www.numpy.org/
[matplotlib]: https://matplotlib.org/
[scikit]: https://scikit-learn.org/stable.html
[pandas]: https://pandas.pydata.org/
