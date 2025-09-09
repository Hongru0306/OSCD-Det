_base_ = [
    '../_base_/datasets/hrsc.py', 
    '../_base_/schedules/schedule_3x.py', # 108epochs
    '../_base_/default_runtime.py'
]


model = dict(
    bbox_head=dict(
        reg_decoded_bbox=True,
        loss_bbox=dict(type='GDLoss', loss_type='gwd', loss_weight=5.0)))
