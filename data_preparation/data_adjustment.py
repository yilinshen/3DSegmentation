import pickle
import numpy as np

# # with open('/home/yilin.shen/mi/3DnnUNet/preprocessed_data/Task101_COVID_19_20/nnUNetPlansv2.1_plans_3D.pkl', 'rb') as f:
# with open('/home/yilin.shen/mi/3DnnUNet/preprocessed_data/Task101_COVID_19_20/splits_final.pkl', 'rb') as f:
#     data = pickle.load(f)
#
#     print(data)

lowres_output = np.load('/home/yilin.shen/mi/3DnnUNet/checkpoints/nnUNet_trained_models/nnUNet/3d_lowres/Task101_COVID_19_20/nnUNetTrainerV2__nnUNetPlansv2.1/pred_next_stage/volume-covid19-A-0698_segFromPrevStage.npz')
print(lowres_output)

img0 = np.load('/home/yilin.shen/mi/3DnnUNet/preprocessed_data/Task101_COVID_19_20/nnUNetData_plans_v2.1_stage0/volume-covid19-A-0698.npz')
print(img0)

img1 = np.load('/home/yilin.shen/mi/3DnnUNet/preprocessed_data/Task101_COVID_19_20/nnUNetData_plans_v2.1_stage1/volume-covid19-A-0698.npz')
print(img1)
