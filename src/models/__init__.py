from .networks import *


def select_seg_model(model_arch: str,
                     encoder_type: str,
                     num_class_seg: int,
                     num_class_cls: int,
                     base_ch: int,
                     use_aspp=False,
                     pretrained=True):
    args_model = {
        'model_name': encoder_type,
        'out_channel': num_class_seg,
        'pretrained': pretrained,
        'use_aspp': use_aspp,
        'base_ch': base_ch
    }
    if model_arch == 'unet':
        return UNet(**args_model)
    elif model_arch == 'msunet':
        return MSUNet(**args_model)
    elif model_arch == 'clsunet':
        args_model.update({'num_class_cls': num_class_cls})
        return ClsUNet(**args_model)
    elif model_arch == 'msclsunet':
        args_model.update({'num_class_cls': num_class_cls})
        return MSClsUNet(**args_model)
    else:
        raise NotImplementedError
