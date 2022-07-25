# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AgentPool
from ._models_py3 import AgentPoolAvailableVersions
from ._models_py3 import AgentPoolAvailableVersionsPropertiesAgentPoolVersionsItem
from ._models_py3 import AgentPoolListResult
from ._models_py3 import AgentPoolUpgradeProfile
from ._models_py3 import AgentPoolUpgradeProfilePropertiesUpgradesItem
from ._models_py3 import CloudErrorBody
from ._models_py3 import ContainerServiceDiagnosticsProfile
from ._models_py3 import ContainerServiceLinuxProfile
from ._models_py3 import ContainerServiceMasterProfile
from ._models_py3 import ContainerServiceNetworkProfile
from ._models_py3 import ContainerServiceSshConfiguration
from ._models_py3 import ContainerServiceSshPublicKey
from ._models_py3 import ContainerServiceVMDiagnostics
from ._models_py3 import CredentialResult
from ._models_py3 import CredentialResults
from ._models_py3 import ManagedCluster
from ._models_py3 import ManagedClusterAADProfile
from ._models_py3 import ManagedClusterAccessProfile
from ._models_py3 import ManagedClusterAddonProfile
from ._models_py3 import ManagedClusterAgentPoolProfile
from ._models_py3 import ManagedClusterAgentPoolProfileProperties
from ._models_py3 import ManagedClusterIdentity
from ._models_py3 import ManagedClusterListResult
from ._models_py3 import ManagedClusterPoolUpgradeProfile
from ._models_py3 import ManagedClusterPoolUpgradeProfileUpgradesItem
from ._models_py3 import ManagedClusterServicePrincipalProfile
from ._models_py3 import ManagedClusterUpgradeProfile
from ._models_py3 import ManagedClusterWindowsProfile
from ._models_py3 import OperationListResult
from ._models_py3 import OperationValue
from ._models_py3 import Resource
from ._models_py3 import SubResource
from ._models_py3 import TagsObject


from ._container_service_client_enums import (
    AgentPoolType,
    ContainerServiceStorageProfileTypes,
    ContainerServiceVMSizeTypes,
    Count,
    LoadBalancerSku,
    NetworkPlugin,
    NetworkPolicy,
    OSType,
    ResourceIdentityType,
    ScaleSetEvictionPolicy,
    ScaleSetPriority,
)
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk
__all__ = [
    'AgentPool',
    'AgentPoolAvailableVersions',
    'AgentPoolAvailableVersionsPropertiesAgentPoolVersionsItem',
    'AgentPoolListResult',
    'AgentPoolUpgradeProfile',
    'AgentPoolUpgradeProfilePropertiesUpgradesItem',
    'CloudErrorBody',
    'ContainerServiceDiagnosticsProfile',
    'ContainerServiceLinuxProfile',
    'ContainerServiceMasterProfile',
    'ContainerServiceNetworkProfile',
    'ContainerServiceSshConfiguration',
    'ContainerServiceSshPublicKey',
    'ContainerServiceVMDiagnostics',
    'CredentialResult',
    'CredentialResults',
    'ManagedCluster',
    'ManagedClusterAADProfile',
    'ManagedClusterAccessProfile',
    'ManagedClusterAddonProfile',
    'ManagedClusterAgentPoolProfile',
    'ManagedClusterAgentPoolProfileProperties',
    'ManagedClusterIdentity',
    'ManagedClusterListResult',
    'ManagedClusterPoolUpgradeProfile',
    'ManagedClusterPoolUpgradeProfileUpgradesItem',
    'ManagedClusterServicePrincipalProfile',
    'ManagedClusterUpgradeProfile',
    'ManagedClusterWindowsProfile',
    'OperationListResult',
    'OperationValue',
    'Resource',
    'SubResource',
    'TagsObject',
    'AgentPoolType',
    'ContainerServiceStorageProfileTypes',
    'ContainerServiceVMSizeTypes',
    'Count',
    'LoadBalancerSku',
    'NetworkPlugin',
    'NetworkPolicy',
    'OSType',
    'ResourceIdentityType',
    'ScaleSetEvictionPolicy',
    'ScaleSetPriority',
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()