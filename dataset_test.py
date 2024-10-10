import os
import random
import shutil

# 데이터셋 경로
images_dir = "D:/MINSEO/ultralytics/datasets/TLD_2024/origin/images"  # 이미지 파일들이 있는 경로
labels_dir = "D:/MINSEO/ultralytics/datasets/TLD_2024/origin/labels"  # 라벨 파일들이 있는 경로

# 데이터셋을 저장할 train과 val 폴더 경로
train_images_dir = "D:/MINSEO/ultralytics/datasets/TLD_2024/train/images"
train_labels_dir = "D:/MINSEO/ultralytics/datasets/TLD_2024/train/labels"
val_images_dir = "D:/MINSEO/ultralytics/datasets/TLD_2024/val/images"
val_labels_dir = "D:/MINSEO/ultralytics/datasets/TLD_2024/val/labels"

# train과 val 비율 설정
train_ratio = 0.8

# 이미지와 라벨 파일 목록 얻기
image_files = sorted([f for f in os.listdir(images_dir) if f.endswith(".jpg")])  # 이미지 파일이 .jpg일 경우
label_files = sorted([f for f in os.listdir(labels_dir) if f.endswith(".txt")])  # 라벨 파일이 .txt일 경우

# 이미지와 라벨 파일 일치 여부 확인 (파일명이 동일한지 확인)
assert len(image_files) == len(label_files), "이미지와 라벨 파일 개수가 일치하지 않습니다."
for img_file, lbl_file in zip(image_files, label_files):
    assert os.path.splitext(img_file)[0] == os.path.splitext(lbl_file)[0], f"{img_file}와 {lbl_file}의 이름이 일치하지 않습니다."

# 데이터 랜덤 섞기
combined = list(zip(image_files, label_files))
random.shuffle(combined)

# train과 val로 나누기
train_size = int(len(combined) * train_ratio)
train_data = combined[:train_size]
val_data = combined[train_size:]

# train 폴더에 데이터 복사
os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)
for img_file, lbl_file in train_data:
    shutil.copy(os.path.join(images_dir, img_file), os.path.join(train_images_dir, img_file))
    shutil.copy(os.path.join(labels_dir, lbl_file), os.path.join(train_labels_dir, lbl_file))

# val 폴더에 데이터 복사
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)
for img_file, lbl_file in val_data:
    shutil.copy(os.path.join(images_dir, img_file), os.path.join(val_images_dir, img_file))
    shutil.copy(os.path.join(labels_dir, lbl_file), os.path.join(val_labels_dir, lbl_file))

print("데이터셋 분할이 완료되었습니다.")
