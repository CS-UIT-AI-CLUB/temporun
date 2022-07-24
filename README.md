# Data Centric Competition Summer 2022
The challenge organized by AICLUB@CS-UIT.

<img src="image.png">

## Mô tả 

[Data Centric Competition Summer 2022](https:/aiclub.uit.edu.vn/temporun/overview) với nhiệm vụ **XÂY DỰNG - PHÂN TÍCH - CẢI THIỆN** bộ dữ liệu huấn luyện để cải thiện hiệu suất mô hình trong bài toán Digit Recognition. 

## Dữ liệu huấn luyện
Các đội thi có thể sử dụng [dữ liệu mẫu](https://drive.google.com/file/d/1h8nwnshBjgSFkWxWY58D7O57IVc3xqw0/view) được xây dựng từ tập dữ liệu MNIST.

## Hướng dẫn huấn luyện
```
git clone https://github.com/CS-UIT-AI-CLUB/temporun.git
cd temporun
```
```
pip install -r requirements.txt
```

```
CUDA_VISIBLE_DEVICES=0 python3 train.py  \
    --train_path <folder path to train dataset> \
    --valid_path <folder path to valid dataset> 
```

Ví dụ

```
CUDA_VISIBLE_DEVICES=0 python3 train.py \
    --train_path mnist/train \
    --valid_path mnist/valid
```

## Định dạng dữ liệu:

```
temporun
├── train
    ├── 0
        ├── 0_img0.jpg
        ├── 0_img1.jpg
        └── ...
    ├── 1
    ├── 2
    └── ...
    └── ...
└── val
    └── ...
    └── ...
```

* Thư mục **train** và thư mục **val** cùng cấp, bên trong mỗi thư mục sẽ có **10** thư mục con được đánh số từ **0-9** tương ứng với nhãn của 10 chữ số.
* Với mỗi thư mục con tương ứng là tập hợp các file ảnh thuộc nhãn đó.
* **Lưu ý**: 
Không có ràng buộc về quy tắc đặt tên file ảnh; Chỉ chấp nhận định các định dạng ảnh bao gồm **jpg** và **png**.

* Kích thước bộ dữ liệu **không quá 500 MB**.


