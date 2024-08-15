import os

def change_label_class_ids(folder_path, new_class_id):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r') as file:
                lines = file.readlines()

            modified_lines = []
            for line in lines:
                components = line.strip().split()
                components[0] = str(new_class_id)
                modified_line = ' '.join(components)
                modified_lines.append(modified_line+"\n")

            with open(file_path, 'w') as file:
                file.writelines(modified_lines)

# Example usage

#change_label_class_ids('C:\\work\\yolo\\Dataset\\labels\\val', 0)


def delete_unassociated_labels(label_folder, image_folder):
    label_files = os.listdir(label_folder)
    for label_file in label_files:
        if label_file.endswith('.txt'):
            image_file = label_file.replace('.txt', '.jpg')
            if not os.path.isfile(os.path.join(image_folder, image_file)):
                os.remove(os.path.join(label_folder, label_file))

# label_folder = 'C:\\work\\yolo\\Person detection.v16i.yolov8\\valid\labels'
# image_folder = 'C:\\work\\yolo\\Person detection.v16i.yolov8\\valid\images'
#
# delete_unassociated_labels(label_folder, image_folder)