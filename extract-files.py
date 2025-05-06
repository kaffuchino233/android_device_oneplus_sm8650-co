#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/oneplus/sm8650-common',
    'hardware/qcom-caf/sm8650',
    'hardware/qcom-caf/wlan',
    'hardware/oplus',
    'vendor/qcom/opensource/commonsys/display',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/qcom/opensource/dataservices',
]

def lib_fixup_odm_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'odm' else None

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'com.qti.sensor.lyt808',
        'com.qualcomm.qti.dpm.api@1.0',
        'libarcsoft_triple_sat',
        'libarcsoft_triple_zoomtranslator',
        'libdualcam_optical_zoom_control',
        'libdualcam_video_optical_zoom',
        'libhwconfigurationutil',
        'libpwirisfeature',
        'libpwirishalwrapper',
        'libtriplecam_optical_zoom_control',
        'libtriplecam_video_optical_zoom',
        'vendor.display.color@1.0',
        'vendor.display.color@1.1',
        'vendor.display.color@1.2',
        'vendor.display.color@1.3',
        'vendor.display.postproc@1.0',
        'vendor.oplus.hardware.cammidasservice-V1-ndk',
        'vendor.oplus.hardware.camera_rfi-V1-ndk',
        'vendor.oplus.hardware.displaycolorfeature-V1-ndk',
        'vendor.oplus.hardware.displaypanelfeature-V1-ndk',
        'vendor.pixelworks.hardware.display@1.0',
        'vendor.pixelworks.hardware.display@1.1',
        'vendor.pixelworks.hardware.display@1.2',
        'vendor.pixelworks.hardware.feature-V1-ndk',
        'vendor.pixelworks.hardware.feature@1.0',
        'vendor.pixelworks.hardware.feature@1.1',
        'vendor.qti.ImsRtpService-V1-ndk',
        'vendor.qti.diaghal@1.0',
        'vendor.qti.hardware.dpmaidlservice-V1-ndk',
        'vendor.qti.hardware.dpmservice@1.0',
        'vendor.qti.hardware.iop@2.0',
        'vendor.qti.hardware.limits@1.0',
        'vendor.qti.hardware.limits@1.1',
        'vendor.qti.hardware.ListenSoundModel@1.0',
        'vendor.qti.hardware.perf2-V1-ndk',
        'vendor.qti.hardware.qccsyshal@1.0',
        'vendor.qti.hardware.qccsyshal@1.1',
        'vendor.qti.hardware.qccsyshal@1.2',
        'vendor.qti.hardware.qxr-V1-ndk',
        'vendor.qti.hardware.wifidisplaysession@1.0',
        'vendor.qti.imsrtpservice@3.0',
        'vendor.qti.imsrtpservice@3.1',
        'vendor.qti.qccvndhal_aidl-V1-ndk',
        'vendor.qti.qccvndhal_aidl-halimpl',
        'vendor.qti.qspmhal-V1-ndk',
        'vendor.qti.hardware.fm@1.0',
        'vendor.qti.hardware.qxr-V1-ndk',
    ): lib_fixup_vendor_suffix,
    (
        'libagmclient',
        'libpalclient',
        'libwpa_client',
    ): lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
    ('odm/bin/hw/android.hardware.secure_element-service.qti', 'vendor/lib64/qcrilNr_aidl_SecureElementService.so'): blob_fixup()
        .replace_needed('android.hardware.secure_element-V1-ndk.so', 'android.hardware.secure_element-V1-ndk_odm.so'),
    'odm/bin/hw/vendor.oplus.hardware.biometrics.fingerprint@2.1-service_uff': blob_fixup()
        .add_needed('libshims_aidl_fingerprint_v3.oplus.so'),
    'odm/lib64/libAlgoProcess.so': blob_fixup()
        .replace_needed('android.hardware.graphics.common-V3-ndk.so', 'android.hardware.graphics.common-V5-ndk.so')
        .remove_needed('android.hardware.graphics.common-V4-ndk.so'),
    ('odm/lib64/libCOppLceTonemapAPI.so', 'odm/lib64/libSuperRaw.so', 'odm/lib64/libYTCommon.so', 'odm/lib64/libyuv2.so'): blob_fixup()
        .replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
    ('odm/lib64/libEIS.so', 'odm/lib64/libHIS.so', 'odm/lib64/libOPAlgoCamFaceBeautyCap.so', 'odm/lib64/libOGLManager.so'): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),
    'odm/lib64/libarcsoft_high_dynamic_range_v4.so': blob_fixup()
        .clear_symbol_version('remote_handle_close')
        .clear_symbol_version('remote_handle_invoke')
        .clear_symbol_version('remote_handle_open')
        .clear_symbol_version('remote_register_buf_attr')
        .clear_symbol_version('remote_register_buf'),
    ('odm/lib64/camera.device@3.3-impl_odm.so','odm/lib64/vendor.oplus.hardware.virtual_device.camera.provider@2.4-impl.so', 'odm/lib64/vendor.oplus.hardware.virtual_device.camera.provider@2.5-impl.so', 'odm/lib64/vendor.oplus.hardware.virtual_device.camera.provider@2.6-impl.so', 'odm/lib64/vendor.oplus.hardware.virtual_device.camera.provider@2.7-impl.so'): blob_fixup()
        .replace_needed('camera.device@3.2-impl.so', 'camera.device@3.2-impl_odm.so')
        .replace_needed('camera.device@3.3-impl.so', 'camera.device@3.3-impl_odm.so'),
    ('odm/lib64/vendor.oplus.hardware.virtual_device.camera.manager@1.0-impl.so', 'vendor/lib64/libcwb_qcom_aidl.so'): blob_fixup()
        .add_needed('libui_shim.so'),
    'vendor/bin/system_dlkm_modprobe.sh': blob_fixup()
        .regex_replace(r'.*\bzram or zsmalloc\b.*\n', '')
        .regex_replace(r'-e "zram" -e "zsmalloc"', ''),
    'vendor/etc/libnfc-nci.conf': blob_fixup()
        .regex_replace('NFC_DEBUG_ENABLED=1', 'NFC_DEBUG_ENABLED=0'),
    'vendor/etc/libnfc-nxp.conf': blob_fixup()
        .regex_replace('(NXPLOG_.*_LOGLEVEL)=0x03', '\\1=0x02')
        .regex_replace('NFC_DEBUG_ENABLED=1', 'NFC_DEBUG_ENABLED=0'),
    ('vendor/etc/media_codecs_pineapple.xml', 'vendor/etc/media_codecs_pineapple_vendor.xml'): blob_fixup()
        .regex_replace('.*media_codecs_(google_audio|google_c2|google_telephony|google_video|vendor_audio).*\n', ''),
    'vendor/etc/init/vendor.qti.camera.provider-service_64.rc': blob_fixup()
        .regex_replace(r'^(.*\n){5}', '\\1    setenv JE_MALLOC_ZERO_FILLING 1\n'),
    'vendor/lib64/vendor.libdpmframework.so': blob_fixup()
        .add_needed('libhidlbase_shim.so'),
    'vendor/lib64/libqcodec2_core.so': blob_fixup()
        .add_needed('libcodec2_shim.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'sm8650-common',
    'oneplus',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()