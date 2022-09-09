"""Tests for xiaomi."""

import zhaquirks
from zhaquirks.xiaomi.aqara.switch_h1 import (
    AqaraSwitchH1NoNeutral_1G,
    AqaraSwitchH1NoNeutral_2G,
)

zhaquirks.setup()


def test_h1_no_neutral_2face_signature(assert_signature_matches_quirk):
    """Tests signature for lumi.switch.l2aeu1."""
    signature = {
        "node_descriptor": "NodeDescriptor(logical_type=<LogicalType.EndDevice: 2>, complex_descriptor_available=0, user_descriptor_available=0, reserved=0, aps_flags=0, frequency_band=<FrequencyBand.Freq2400MHz: 8>, mac_capability_flags=<MACCapabilityFlags.AllocateAddress: 128>, manufacturer_code=4447, maximum_buffer_size=127, maximum_incoming_transfer_size=100, server_mask=11264, maximum_outgoing_transfer_size=100, descriptor_capability_field=<DescriptorCapability.NONE: 0>, *allocate_address=True, *is_alternate_pan_coordinator=False, *is_coordinator=False, *is_end_device=True, *is_full_function_device=False, *is_mains_powered=False, *is_receiver_on_when_idle=False, *is_router=False, *is_security_capable=False)",
        "endpoints": {
            "1": {
                "profile_id": 260,
                "device_type": "0x0100",
                "in_clusters": [
                    "0x0000",
                    "0x0002",
                    "0x0003",
                    "0x0004",
                    "0x0005",
                    "0x0006",
                    "0x0012",
                    "0xfcc0",
                ],
                "out_clusters": ["0x000a", "0x0019"],
            },
            "2": {
                "profile_id": 260,
                "device_type": "0x0100",
                "in_clusters": [
                    "0x0000",
                    "0x0003",
                    "0x0004",
                    "0x0005",
                    "0x0006",
                    "0x0012",
                    "0xfcc0",
                ],
                "out_clusters": [],
            },
            "41": {
                "profile_id": 260,
                "device_type": "0x0100",
                "in_clusters": ["0x0012"],
                "out_clusters": [],
            },
            "42": {
                "profile_id": 260,
                "device_type": "0x0100",
                "in_clusters": ["0x0012"],
                "out_clusters": [],
            },
            "51": {
                "profile_id": 260,
                "device_type": "0x0100",
                "in_clusters": ["0x0012"],
                "out_clusters": [],
            },
            "242": {
                "profile_id": 41440,
                "device_type": "0x0061",
                "in_clusters": [],
                "out_clusters": ["0x0021"],
            },
        },
        "manufacturer": "LUMI",
        "model": "lumi.switch.l2aeu1",
        "class": "zhaquirks.xiaomi.aqara.switch_h1.AqaraSwitchH1NoNeutral_2G",
    }
    assert_signature_matches_quirk(AqaraSwitchH1NoNeutral_2G, signature)


def test_h1_no_neutral_1face_signature(assert_signature_matches_quirk):
    """Tests signature for lumi.switch.l2aeu1."""
    signature = {
        "node_descriptor": "NodeDescriptor(logical_type=<LogicalType.EndDevice: 2>, complex_descriptor_available=0, user_descriptor_available=0, reserved=0, aps_flags=0, frequency_band=<FrequencyBand.Freq2400MHz: 8>, mac_capability_flags=<MACCapabilityFlags.AllocateAddress: 128>, manufacturer_code=4447, maximum_buffer_size=127, maximum_incoming_transfer_size=100, server_mask=11264, maximum_outgoing_transfer_size=100, descriptor_capability_field=<DescriptorCapability.NONE: 0>, *allocate_address=True, *is_alternate_pan_coordinator=False, *is_coordinator=False, *is_end_device=True, *is_full_function_device=False, *is_mains_powered=False, *is_receiver_on_when_idle=False, *is_router=False, *is_security_capable=False)",
        "endpoints": {
            "1": {
                "profile_id": 260,
                "device_type": "0x0100",
                "in_clusters": [
                    "0x0000",
                    "0x0002",
                    "0x0003",
                    "0x0004",
                    "0x0005",
                    "0x0006",
                    "0x0012",
                    "0xfcc0",
                ],
                "out_clusters": ["0x000a", "0x0019"],
            },
            "41": {
                "profile_id": 260,
                "device_type": "0x0100",
                "in_clusters": ["0x0012"],
                "out_clusters": [],
            },
            "242": {
                "profile_id": 41440,
                "device_type": "0x0061",
                "in_clusters": [],
                "out_clusters": ["0x0021"],
            },
        },
        "manufacturer": "LUMI",
        "model": "lumi.switch.l1aeu1",
        "class": "zhaquirks.xiaomi.aqara.switch_h1.AqaraSwitchH1NoNeutral_1G",
    }
    assert_signature_matches_quirk(AqaraSwitchH1NoNeutral_1G, signature)
