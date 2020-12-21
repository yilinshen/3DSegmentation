from collections import OrderedDict
import os
import shutil
import json

if __name__ == "__main__":

    raw_data_path = '/home/yilin.shen/mi/covid19_internal/covid_ct_segmentation/data/COVID_19_20'
    raw_out_folder = '/home/yilin.shen/mi/3DnnUNet/data'

    out_folder = os.path.join(raw_out_folder, 'nnUNet_raw_data', 'Task101_COVID_19_20')
    if os.path.exists(out_folder):
        shutil.rmtree(out_folder)
    os.makedirs(out_folder, exist_ok=True)

    os.mkdir(os.path.join(out_folder, "imagesTr"))
    os.mkdir(os.path.join(out_folder, "imagesTs"))
    os.mkdir(os.path.join(out_folder, "labelsTr"))

    def link_files(data_type):
        output_type = 'Tr' if data_type == 'Train' else 'Ts'

        covid_image_path = os.path.join(raw_data_path, data_type, 'images')
        covid_infection_path = os.path.join(raw_data_path, data_type, 'labels')

        # handle images
        for ids in os.listdir(covid_image_path):
            src_file = os.path.join(covid_image_path, ids)
            dst_file_id = ids[:-10] + "_0000.nii.gz"
            dst_file = os.path.join(os.path.join(out_folder, "images%s" % output_type, dst_file_id))

            if os.path.isfile(src_file):
                os.symlink(src_file, dst_file)

        # handle labels
        for ids in os.listdir(covid_infection_path):
            src_file = os.path.join(covid_infection_path, ids)
            dst_file_id = ids[:-11] + ".nii.gz"
            dst_file = os.path.join(os.path.join(out_folder, "labels%s" % output_type, dst_file_id))

            if os.path.isfile(src_file):
                os.symlink(src_file, dst_file)

    link_files(data_type='Train')
    # link_files(data_type='Validation')
    link_files(data_type='Test')

    json_dict = OrderedDict()
    json_dict['name'] = "COVID_infection_20"
    json_dict['description'] = "COVID_infection_20"
    json_dict['tensorImageSize'] = "3D"
    json_dict['reference'] = "https://covid-segmentation.grand-challenge.org/COVID-19-20/"
    json_dict['licence'] = "https://covid-segmentation.grand-challenge.org/COVID-19-20/"
    json_dict['release'] = "0.0"
    json_dict['modality'] = {
        "0": "CT",
    }
    json_dict['labels'] = {
        "0": "background",
        "1": "infection"
    }
    json_dict['numTraining'] = len(os.listdir(os.path.join(out_folder, "imagesTr")))
    json_dict['numTest'] = 0
    json_dict['training'] = [{'image': "./imagesTr/%s.nii.gz" % i[:-12],
                              "label": "./labelsTr/%s.nii.gz" % i[:-12]} for i in
                             os.listdir(os.path.join(out_folder, "imagesTr"))]
    json_dict['test'] = ["./imagesTs/%s.nii.gz" % i[:-12] for i in
                         os.listdir(os.path.join(out_folder, "imagesTs"))]

    json.dump(json_dict, open(os.path.join(out_folder, "dataset.json"), 'w'))
