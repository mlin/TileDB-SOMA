import pathlib
from typing import List, Sequence, Tuple, Union

import numpy as np
import pandas as pd
import scipy.sparse as sp

Path = Union[str, pathlib.Path]

Ids = Union[List[str], List[bytes], List[int]]

Labels = Union[Sequence[str], pd.Index]

Matrix = Union[np.ndarray, sp.csr_matrix, sp.csc_matrix]

NTuple = Union[Tuple[int], Tuple[int, int]]