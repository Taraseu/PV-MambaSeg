# Copyright (c) OpenMMLab. All rights reserved.
import os.path as osp

import mmcv
import numpy as np

from PIL import Image

from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class UCFELDataset(CustomDataset):

    CLASSES = ('background', 'crack', 'contact', 'interconnect', 'corrosion')

    PALETTE = [[0, 0, 0], [228, 26, 27], [55, 126, 184], [152, 78, 163], [255, 153, 51]]

    def __init__(self,
                 img_suffix='.jpg',
                 seg_map_suffix='.png',
                 **kwargs) -> None:
        super(UCFELDataset, self).__init__(
            img_suffix=img_suffix, 
            seg_map_suffix=seg_map_suffix, 
            **kwargs)

