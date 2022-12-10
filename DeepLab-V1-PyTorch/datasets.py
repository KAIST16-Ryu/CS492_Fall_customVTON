import numpy as np
import torch
from PIL import Image, ImageDraw
import os
import numpy as np
import cv2
import random

class VOCDataset(torch.utils.data.Dataset):
    def __init__(self, split='train_aug', crop_size=321, label_dir_path='clothes_labels', is_scale=True, is_flip=True, is_train=False):
        self.root = '/root/segmentation/dataset'
        self.ann_dir_path = os.path.join(self.root, 'Annotations')
        self.image_dir_path = os.path.join(self.root, 'images')
        self.label_dir_path = os.path.join(self.root, label_dir_path) # SegmentationClassAug_Round1

        self.image_ids = os.listdir(self.image_dir_path)
        self.label_ids = os.listdir(self.label_dir_path)
        print('%s datasets num = %s' % (split, self.__len__()))

        self.mean_bgr = np.array((104.008, 116.669, 122.675))
        self.split = split
        self.crop_size = crop_size
        self.ignore_label = 255
        self.base_size = None
        self.scales = [0.5, 0.75, 1.0, 1.25, 1.5]
        self.is_augment = True
        self.is_scale = is_scale
        self.is_flip = is_flip
        self.is_train = is_train
    
    def __len__(self):
        return len(self.image_ids)

    def __getitem__(self, index):
        image_id = self.image_ids[index]
        label_id = image_id[:-3]+'png'
        # image_id = self.image_ids[index]
        # image_path = os.path.join(self.image_dir_path, image_id + '.jpg')
        # label_path = os.path.join(self.label_dir_path, image_id + '.png')
        image_path = os.path.join(self.image_dir_path, image_id)
        label_path = os.path.join(self.label_dir_path, label_id)
        
        # Load an imageprint
        image = cv2.imread(image_path, cv2.IMREAD_COLOR).astype(np.float32)
        label = cv2.imread(label_path, cv2.IMREAD_COLOR).astype(np.float32)
        # label = np.asarray(Image.open(label_path), dtype=np.int32)

        label = label[:, :, 0]
        label[label != 0] = 15

        print("Dataset, image", image.shape)
        print("Dataset, label", label.shape)

        if self.is_augment:
            image, label, (crop_start_h, crop_start_w) = self._augmentation(image, label)
        
        image -= self.mean_bgr
        image = image.transpose(2, 0, 1)

        print("Dataset after, image", image.shape)
        print("Dataset after, label", label.shape)
        return image_id, image.astype(np.float32), label.astype(np.int64), (crop_start_h, crop_start_w)
    
    def _augmentation(self, image, label):
        # Scaling
        # if self.is_scale:
        #     print("Scaling...")
        #     h, w = label.shape
        #     if self.base_size:
        #         if h > w:
        #             h, w = (self.base_size, int(self.base_size * w / h))
        #         else:
        #             h, w = (int(self.base_size * h / w), self.base_size)
            
        #     scale_factor = random.choice(self.scales)
        #     h, w = (int(h * scale_factor), int(w * scale_factor))
        #     image = cv2.resize(image, (w, h), interpolation=cv2.INTER_LINEAR)
        #     label = Image.fromarray(label).resize((w, h), resample=Image.NEAREST)
        #     label = np.asarray(label, dtype=np.int64)

        # Padding to fit for crop_size
        # h, w = label.shape
        # pad_h = max(self.crop_size - h, 0)
        # pad_w = max(self.crop_size - w, 0)
        # pad_kwargs = {
        #     "top": 0,
        #     "bottom": pad_h,
        #     "left": 0,
        #     "right": pad_w,
        #     "borderType": cv2.BORDER_CONSTANT,
        # }
        # if pad_h > 0 or pad_w > 0:
        #     print("Padding...")
        #     image = cv2.copyMakeBorder(image, value=self.mean_bgr, **pad_kwargs)
        #     label = cv2.copyMakeBorder(label, value=self.ignore_label, **pad_kwargs)

        # Cropping
        print("Cropping...")
        h, w = label.shape
        if self.is_train:
            start_h = random.randint(0, h - self.crop_size)
            start_w = random.randint(0, w - self.crop_size)
        else:
            start_h = max(0, (h - self.crop_size) // 2)
            start_w = max(0, (w - self.crop_size) // 2)
        end_h = start_h + self.crop_size
        end_w = start_w + self.crop_size
        image = image[start_h:end_h, start_w:end_w]
        label = label[start_h:end_h, start_w:end_w]

        # if self.is_flip:
        #     # Random flipping
        #     print("Random flipping...")
        #     if random.random() < 0.5:
        #         image = np.fliplr(image).copy()  # HWC
        #         label = np.fliplr(label).copy()  # HW

        return image, label, (start_h, start_w)

if __name__ == "__main__":
    dataset = VOCDataset()
    id, image, label = dataset.__getitem__(0)