# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import ApiOperation
from ._models_py3 import ApiOperationDisplay
from ._models_py3 import ApiOperationListResult
from ._models_py3 import ApiOperationPropertiesServiceSpecification
from ._models_py3 import AscOperation
from ._models_py3 import BlobNfsTarget
from ._models_py3 import Cache
from ._models_py3 import CacheActiveDirectorySettings
from ._models_py3 import CacheActiveDirectorySettingsCredentials
from ._models_py3 import CacheDirectorySettings
from ._models_py3 import CacheEncryptionSettings
from ._models_py3 import CacheHealth
from ._models_py3 import CacheIdentity
from ._models_py3 import CacheNetworkSettings
from ._models_py3 import CacheSecuritySettings
from ._models_py3 import CacheSku
from ._models_py3 import CacheUpgradeSettings
from ._models_py3 import CacheUpgradeStatus
from ._models_py3 import CacheUsernameDownloadSettings
from ._models_py3 import CacheUsernameDownloadSettingsCredentials
from ._models_py3 import CachesListResult
from ._models_py3 import ClfsTarget
from ._models_py3 import CloudErrorBody
from ._models_py3 import Condition
from ._models_py3 import ErrorResponse
from ._models_py3 import KeyVaultKeyReference
from ._models_py3 import KeyVaultKeyReferenceSourceVault
from ._models_py3 import LogSpecification
from ._models_py3 import MetricDimension
from ._models_py3 import MetricSpecification
from ._models_py3 import NamespaceJunction
from ._models_py3 import Nfs3Target
from ._models_py3 import NfsAccessPolicy
from ._models_py3 import NfsAccessRule
from ._models_py3 import PrimingJob
from ._models_py3 import PrimingJobIdParameter
from ._models_py3 import ResourceSku
from ._models_py3 import ResourceSkuCapabilities
from ._models_py3 import ResourceSkuLocationInfo
from ._models_py3 import ResourceSkusResult
from ._models_py3 import ResourceUsage
from ._models_py3 import ResourceUsageName
from ._models_py3 import ResourceUsagesListResult
from ._models_py3 import Restriction
from ._models_py3 import StorageTarget
from ._models_py3 import StorageTargetResource
from ._models_py3 import StorageTargetSpaceAllocation
from ._models_py3 import StorageTargetsResult
from ._models_py3 import SystemData
from ._models_py3 import UnknownTarget
from ._models_py3 import UsageModel
from ._models_py3 import UsageModelDisplay
from ._models_py3 import UsageModelsResult
from ._models_py3 import UserAssignedIdentitiesValue


from ._storage_cache_management_client_enums import (
    CacheIdentityType,
    CreatedByType,
    DomainJoinedType,
    FirmwareStatusType,
    HealthStateType,
    MetricAggregationType,
    NfsAccessRuleAccess,
    NfsAccessRuleScope,
    OperationalStateType,
    PrimingJobState,
    ProvisioningStateType,
    ReasonCode,
    StorageTargetType,
    UsernameDownloadedType,
    UsernameSource,
)
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk
__all__ = [
    'ApiOperation',
    'ApiOperationDisplay',
    'ApiOperationListResult',
    'ApiOperationPropertiesServiceSpecification',
    'AscOperation',
    'BlobNfsTarget',
    'Cache',
    'CacheActiveDirectorySettings',
    'CacheActiveDirectorySettingsCredentials',
    'CacheDirectorySettings',
    'CacheEncryptionSettings',
    'CacheHealth',
    'CacheIdentity',
    'CacheNetworkSettings',
    'CacheSecuritySettings',
    'CacheSku',
    'CacheUpgradeSettings',
    'CacheUpgradeStatus',
    'CacheUsernameDownloadSettings',
    'CacheUsernameDownloadSettingsCredentials',
    'CachesListResult',
    'ClfsTarget',
    'CloudErrorBody',
    'Condition',
    'ErrorResponse',
    'KeyVaultKeyReference',
    'KeyVaultKeyReferenceSourceVault',
    'LogSpecification',
    'MetricDimension',
    'MetricSpecification',
    'NamespaceJunction',
    'Nfs3Target',
    'NfsAccessPolicy',
    'NfsAccessRule',
    'PrimingJob',
    'PrimingJobIdParameter',
    'ResourceSku',
    'ResourceSkuCapabilities',
    'ResourceSkuLocationInfo',
    'ResourceSkusResult',
    'ResourceUsage',
    'ResourceUsageName',
    'ResourceUsagesListResult',
    'Restriction',
    'StorageTarget',
    'StorageTargetResource',
    'StorageTargetSpaceAllocation',
    'StorageTargetsResult',
    'SystemData',
    'UnknownTarget',
    'UsageModel',
    'UsageModelDisplay',
    'UsageModelsResult',
    'UserAssignedIdentitiesValue',
    'CacheIdentityType',
    'CreatedByType',
    'DomainJoinedType',
    'FirmwareStatusType',
    'HealthStateType',
    'MetricAggregationType',
    'NfsAccessRuleAccess',
    'NfsAccessRuleScope',
    'OperationalStateType',
    'PrimingJobState',
    'ProvisioningStateType',
    'ReasonCode',
    'StorageTargetType',
    'UsernameDownloadedType',
    'UsernameSource',
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()