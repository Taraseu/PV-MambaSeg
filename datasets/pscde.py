# Copyright (c) OpenMMLab. All rights reserved.
import os.path as osp

import mmcv
import numpy as np

from PIL import Image

from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class PSCDEDataset(CustomDataset):

    CLASSES = ('background', 'defect')

    PALETTE = [[0, 0, 0], [255, 255, 255]]

    def __init__(self,
                 img_suffix='.png',
                 seg_map_suffix='.png',
                 **kwargs) -> None:
        super(PSCDEDataset, self).__init__(
            img_suffix=img_suffix, 
            seg_map_suffix=seg_map_suffix, 
            **kwargs)

