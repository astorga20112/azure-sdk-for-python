# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class ActionGroupPatchBody(Model):
    """An action group object for the body of patch operations.

    :param tags: Resource tags
    :type tags: dict[str, str]
    :param enabled: Indicates whether this action group is enabled. If an
     action group is not enabled, then none of its actions will be activated.
     Default value: True .
    :type enabled: bool
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
    }

    def __init__(self, *, tags=None, enabled: bool=True, **kwargs) -> None:
        super(ActionGroupPatchBody, self).__init__(**kwargs)
        self.tags = tags
        self.enabled = enabled


class Resource(Model):
    """An azure resource object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, location: str, tags=None, **kwargs) -> None:
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags


class ActionGroupResource(Resource):
    """An action group resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param group_short_name: Required. The short name of the action group.
     This will be used in SMS messages.
    :type group_short_name: str
    :param enabled: Required. Indicates whether this action group is enabled.
     If an action group is not enabled, then none of its receivers will receive
     communications. Default value: True .
    :type enabled: bool
    :param email_receivers: The list of email receivers that are part of this
     action group.
    :type email_receivers:
     list[~azure.mgmt.monitor.v2018_09_01.models.EmailReceiver]
    :param sms_receivers: The list of SMS receivers that are part of this
     action group.
    :type sms_receivers:
     list[~azure.mgmt.monitor.v2018_09_01.models.SmsReceiver]
    :param webhook_receivers: The list of webhook receivers that are part of
     this action group.
    :type webhook_receivers:
     list[~azure.mgmt.monitor.v2018_09_01.models.WebhookReceiver]
    :param itsm_receivers: The list of ITSM receivers that are part of this
     action group.
    :type itsm_receivers:
     list[~azure.mgmt.monitor.v2018_09_01.models.ItsmReceiver]
    :param azure_app_push_receivers: The list of AzureAppPush receivers that
     are part of this action group.
    :type azure_app_push_receivers:
     list[~azure.mgmt.monitor.v2018_09_01.models.AzureAppPushReceiver]
    :param automation_runbook_receivers: The list of AutomationRunbook
     receivers that are part of this action group.
    :type automation_runbook_receivers:
     list[~azure.mgmt.monitor.v2018_09_01.models.AutomationRunbookReceiver]
    :param voice_receivers: The list of voice receivers that are part of this
     action group.
    :type voice_receivers:
     list[~azure.mgmt.monitor.v2018_09_01.models.VoiceReceiver]
    :param logic_app_receivers: The list of logic app receivers that are part
     of this action group.
    :type logic_app_receivers:
     list[~azure.mgmt.monitor.v2018_09_01.models.LogicAppReceiver]
    :param azure_function_receivers: The list of azure function receivers that
     are part of this action group.
    :type azure_function_receivers:
     list[~azure.mgmt.monitor.v2018_09_01.models.AzureFunctionReceiver]
    :param arm_role_receivers: The list of ARM role receivers that are part of
     this action group. Roles are Azure RBAC roles and only built-in roles are
     supported.
    :type arm_role_receivers:
     list[~azure.mgmt.monitor.v2018_09_01.models.ArmRoleReceiver]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'group_short_name': {'required': True, 'max_length': 12},
        'enabled': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'group_short_name': {'key': 'properties.groupShortName', 'type': 'str'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
        'email_receivers': {'key': 'properties.emailReceivers', 'type': '[EmailReceiver]'},
        'sms_receivers': {'key': 'properties.smsReceivers', 'type': '[SmsReceiver]'},
        'webhook_receivers': {'key': 'properties.webhookReceivers', 'type': '[WebhookReceiver]'},
        'itsm_receivers': {'key': 'properties.itsmReceivers', 'type': '[ItsmReceiver]'},
        'azure_app_push_receivers': {'key': 'properties.azureAppPushReceivers', 'type': '[AzureAppPushReceiver]'},
        'automation_runbook_receivers': {'key': 'properties.automationRunbookReceivers', 'type': '[AutomationRunbookReceiver]'},
        'voice_receivers': {'key': 'properties.voiceReceivers', 'type': '[VoiceReceiver]'},
        'logic_app_receivers': {'key': 'properties.logicAppReceivers', 'type': '[LogicAppReceiver]'},
        'azure_function_receivers': {'key': 'properties.azureFunctionReceivers', 'type': '[AzureFunctionReceiver]'},
        'arm_role_receivers': {'key': 'properties.armRoleReceivers', 'type': '[ArmRoleReceiver]'},
    }

    def __init__(self, *, location: str, group_short_name: str, tags=None, enabled: bool=True, email_receivers=None, sms_receivers=None, webhook_receivers=None, itsm_receivers=None, azure_app_push_receivers=None, automation_runbook_receivers=None, voice_receivers=None, logic_app_receivers=None, azure_function_receivers=None, arm_role_receivers=None, **kwargs) -> None:
        super(ActionGroupResource, self).__init__(location=location, tags=tags, **kwargs)
        self.group_short_name = group_short_name
        self.enabled = enabled
        self.email_receivers = email_receivers
        self.sms_receivers = sms_receivers
        self.webhook_receivers = webhook_receivers
        self.itsm_receivers = itsm_receivers
        self.azure_app_push_receivers = azure_app_push_receivers
        self.automation_runbook_receivers = automation_runbook_receivers
        self.voice_receivers = voice_receivers
        self.logic_app_receivers = logic_app_receivers
        self.azure_function_receivers = azure_function_receivers
        self.arm_role_receivers = arm_role_receivers


class ArmRoleReceiver(Model):
    """An arm role receiver.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the arm role receiver. Names must be
     unique across all receivers within an action group.
    :type name: str
    :param role_id: Required. The arm role id.
    :type role_id: str
    """

    _validation = {
        'name': {'required': True},
        'role_id': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'role_id': {'key': 'roleId', 'type': 'str'},
    }

    def __init__(self, *, name: str, role_id: str, **kwargs) -> None:
        super(ArmRoleReceiver, self).__init__(**kwargs)
        self.name = name
        self.role_id = role_id


class AutomationRunbookReceiver(Model):
    """The Azure Automation Runbook notification receiver.

    All required parameters must be populated in order to send to Azure.

    :param automation_account_id: Required. The Azure automation account Id
     which holds this runbook and authenticate to Azure resource.
    :type automation_account_id: str
    :param runbook_name: Required. The name for this runbook.
    :type runbook_name: str
    :param webhook_resource_id: Required. The resource id for webhook linked
     to this runbook.
    :type webhook_resource_id: str
    :param is_global_runbook: Required. Indicates whether this instance is
     global runbook.
    :type is_global_runbook: bool
    :param name: Indicates name of the webhook.
    :type name: str
    :param service_uri: The URI where webhooks should be sent.
    :type service_uri: str
    """

    _validation = {
        'automation_account_id': {'required': True},
        'runbook_name': {'required': True},
        'webhook_resource_id': {'required': True},
        'is_global_runbook': {'required': True},
    }

    _attribute_map = {
        'automation_account_id': {'key': 'automationAccountId', 'type': 'str'},
        'runbook_name': {'key': 'runbookName', 'type': 'str'},
        'webhook_resource_id': {'key': 'webhookResourceId', 'type': 'str'},
        'is_global_runbook': {'key': 'isGlobalRunbook', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'service_uri': {'key': 'serviceUri', 'type': 'str'},
    }

    def __init__(self, *, automation_account_id: str, runbook_name: str, webhook_resource_id: str, is_global_runbook: bool, name: str=None, service_uri: str=None, **kwargs) -> None:
        super(AutomationRunbookReceiver, self).__init__(**kwargs)
        self.automation_account_id = automation_account_id
        self.runbook_name = runbook_name
        self.webhook_resource_id = webhook_resource_id
        self.is_global_runbook = is_global_runbook
        self.name = name
        self.service_uri = service_uri


class AzureAppPushReceiver(Model):
    """The Azure mobile App push notification receiver.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the Azure mobile app push receiver.
     Names must be unique across all receivers within an action group.
    :type name: str
    :param email_address: Required. The email address registered for the Azure
     mobile app.
    :type email_address: str
    """

    _validation = {
        'name': {'required': True},
        'email_address': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'email_address': {'key': 'emailAddress', 'type': 'str'},
    }

    def __init__(self, *, name: str, email_address: str, **kwargs) -> None:
        super(AzureAppPushReceiver, self).__init__(**kwargs)
        self.name = name
        self.email_address = email_address


class AzureFunctionReceiver(Model):
    """An azure function receiver.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the azure function receiver. Names must
     be unique across all receivers within an action group.
    :type name: str
    :param function_app_resource_id: Required. The azure resource id of the
     function app.
    :type function_app_resource_id: str
    :param function_name: Required. The function name in the function app.
    :type function_name: str
    :param http_trigger_url: Required. The http trigger url where http request
     sent to.
    :type http_trigger_url: str
    """

    _validation = {
        'name': {'required': True},
        'function_app_resource_id': {'required': True},
        'function_name': {'required': True},
        'http_trigger_url': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'function_app_resource_id': {'key': 'functionAppResourceId', 'type': 'str'},
        'function_name': {'key': 'functionName', 'type': 'str'},
        'http_trigger_url': {'key': 'httpTriggerUrl', 'type': 'str'},
    }

    def __init__(self, *, name: str, function_app_resource_id: str, function_name: str, http_trigger_url: str, **kwargs) -> None:
        super(AzureFunctionReceiver, self).__init__(**kwargs)
        self.name = name
        self.function_app_resource_id = function_app_resource_id
        self.function_name = function_name
        self.http_trigger_url = http_trigger_url


class Baseline(Model):
    """The baseline values for a single sensitivity value.

    All required parameters must be populated in order to send to Azure.

    :param sensitivity: Required. The sensitivity of the baseline. Possible
     values include: 'Low', 'Medium', 'High'
    :type sensitivity: str or
     ~azure.mgmt.monitor.v2018_09_01.models.Sensitivity
    :param low_thresholds: Required. The low thresholds of the baseline.
    :type low_thresholds: list[float]
    :param high_thresholds: Required. The high thresholds of the baseline.
    :type high_thresholds: list[float]
    """

    _validation = {
        'sensitivity': {'required': True},
        'low_thresholds': {'required': True},
        'high_thresholds': {'required': True},
    }

    _attribute_map = {
        'sensitivity': {'key': 'sensitivity', 'type': 'Sensitivity'},
        'low_thresholds': {'key': 'lowThresholds', 'type': '[float]'},
        'high_thresholds': {'key': 'highThresholds', 'type': '[float]'},
    }

    def __init__(self, *, sensitivity, low_thresholds, high_thresholds, **kwargs) -> None:
        super(Baseline, self).__init__(**kwargs)
        self.sensitivity = sensitivity
        self.low_thresholds = low_thresholds
        self.high_thresholds = high_thresholds


class BaselineMetadataValue(Model):
    """Represents a baseline metadata value.

    :param name: The name of the metadata.
    :type name: ~azure.mgmt.monitor.v2018_09_01.models.LocalizableString
    :param value: The value of the metadata.
    :type value: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'LocalizableString'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, *, name=None, value: str=None, **kwargs) -> None:
        super(BaselineMetadataValue, self).__init__(**kwargs)
        self.name = name
        self.value = value


class BaselineResponse(Model):
    """The response to a baseline query.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The metric baseline ID.
    :vartype id: str
    :ivar type: The resource type of the baseline resource.
    :vartype type: str
    :ivar name: The name and the display name of the metric, i.e. it is
     localizable string.
    :vartype name: ~azure.mgmt.monitor.v2018_09_01.models.LocalizableString
    :param timespan: The timespan for which the data was retrieved. Its value
     consists of two datetimes concatenated, separated by '/'.  This may be
     adjusted in the future and returned back from what was originally
     requested.
    :type timespan: str
    :param interval: The interval (window size) for which the metric data was
     returned in.  This may be adjusted in the future and returned back from
     what was originally requested.  This is not present if a metadata request
     was made.
    :type interval: timedelta
    :param aggregation: The aggregation type of the metric.
    :type aggregation: str
    :param timestamps: The array of timestamps of the baselines.
    :type timestamps: list[datetime]
    :param baseline: The baseline values for each sensitivity.
    :type baseline: list[~azure.mgmt.monitor.v2018_09_01.models.Baseline]
    :param metadata: The baseline metadata values.
    :type metadata:
     list[~azure.mgmt.monitor.v2018_09_01.models.BaselineMetadataValue]
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'LocalizableString'},
        'timespan': {'key': 'properties.timespan', 'type': 'str'},
        'interval': {'key': 'properties.interval', 'type': 'duration'},
        'aggregation': {'key': 'properties.aggregation', 'type': 'str'},
        'timestamps': {'key': 'properties.timestamps', 'type': '[iso-8601]'},
        'baseline': {'key': 'properties.baseline', 'type': '[Baseline]'},
        'metadata': {'key': 'properties.metadata', 'type': '[BaselineMetadataValue]'},
    }

    def __init__(self, *, timespan: str=None, interval=None, aggregation: str=None, timestamps=None, baseline=None, metadata=None, **kwargs) -> None:
        super(BaselineResponse, self).__init__(**kwargs)
        self.id = None
        self.type = None
        self.name = None
        self.timespan = timespan
        self.interval = interval
        self.aggregation = aggregation
        self.timestamps = timestamps
        self.baseline = baseline
        self.metadata = metadata


class CalculateBaselineResponse(Model):
    """The response to a calculate baseline call.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. The resource type of the baseline resource.
    :type type: str
    :param timestamps: The array of timestamps of the baselines.
    :type timestamps: list[datetime]
    :param baseline: Required. The baseline values for each sensitivity.
    :type baseline: list[~azure.mgmt.monitor.v2018_09_01.models.Baseline]
    """

    _validation = {
        'type': {'required': True},
        'baseline': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'timestamps': {'key': 'timestamps', 'type': '[iso-8601]'},
        'baseline': {'key': 'baseline', 'type': '[Baseline]'},
    }

    def __init__(self, *, type: str, baseline, timestamps=None, **kwargs) -> None:
        super(CalculateBaselineResponse, self).__init__(**kwargs)
        self.type = type
        self.timestamps = timestamps
        self.baseline = baseline


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class EmailReceiver(Model):
    """An email receiver.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the email receiver. Names must be
     unique across all receivers within an action group.
    :type name: str
    :param email_address: Required. The email address of this receiver.
    :type email_address: str
    :ivar status: The receiver status of the e-mail. Possible values include:
     'NotSpecified', 'Enabled', 'Disabled'
    :vartype status: str or
     ~azure.mgmt.monitor.v2018_09_01.models.ReceiverStatus
    """

    _validation = {
        'name': {'required': True},
        'email_address': {'required': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'email_address': {'key': 'emailAddress', 'type': 'str'},
        'status': {'key': 'status', 'type': 'ReceiverStatus'},
    }

    def __init__(self, *, name: str, email_address: str, **kwargs) -> None:
        super(EmailReceiver, self).__init__(**kwargs)
        self.name = name
        self.email_address = email_address
        self.status = None


class EnableRequest(Model):
    """Describes a receiver that should be resubscribed.

    All required parameters must be populated in order to send to Azure.

    :param receiver_name: Required. The name of the receiver to resubscribe.
    :type receiver_name: str
    """

    _validation = {
        'receiver_name': {'required': True},
    }

    _attribute_map = {
        'receiver_name': {'key': 'receiverName', 'type': 'str'},
    }

    def __init__(self, *, receiver_name: str, **kwargs) -> None:
        super(EnableRequest, self).__init__(**kwargs)
        self.receiver_name = receiver_name


class ErrorResponse(Model):
    """Describes the format of Error response.

    :param code: Error code
    :type code: str
    :param message: Error message indicating why the operation failed.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, code: str=None, message: str=None, **kwargs) -> None:
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = code
        self.message = message


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)


class ItsmReceiver(Model):
    """An Itsm receiver.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the Itsm receiver. Names must be unique
     across all receivers within an action group.
    :type name: str
    :param workspace_id: Required. OMS LA instance identifier.
    :type workspace_id: str
    :param connection_id: Required. Unique identification of ITSM connection
     among multiple defined in above workspace.
    :type connection_id: str
    :param ticket_configuration: Required. JSON blob for the configurations of
     the ITSM action. CreateMultipleWorkItems option will be part of this blob
     as well.
    :type ticket_configuration: str
    :param region: Required. Region in which workspace resides. Supported
     values:'centralindia','japaneast','southeastasia','australiasoutheast','uksouth','westcentralus','canadacentral','eastus','westeurope'
    :type region: str
    """

    _validation = {
        'name': {'required': True},
        'workspace_id': {'required': True},
        'connection_id': {'required': True},
        'ticket_configuration': {'required': True},
        'region': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'workspace_id': {'key': 'workspaceId', 'type': 'str'},
        'connection_id': {'key': 'connectionId', 'type': 'str'},
        'ticket_configuration': {'key': 'ticketConfiguration', 'type': 'str'},
        'region': {'key': 'region', 'type': 'str'},
    }

    def __init__(self, *, name: str, workspace_id: str, connection_id: str, ticket_configuration: str, region: str, **kwargs) -> None:
        super(ItsmReceiver, self).__init__(**kwargs)
        self.name = name
        self.workspace_id = workspace_id
        self.connection_id = connection_id
        self.ticket_configuration = ticket_configuration
        self.region = region


class LocalizableString(Model):
    """The localizable string class.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. The invariant value.
    :type value: str
    :param localized_value: The locale specific value.
    :type localized_value: str
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'localized_value': {'key': 'localizedValue', 'type': 'str'},
    }

    def __init__(self, *, value: str, localized_value: str=None, **kwargs) -> None:
        super(LocalizableString, self).__init__(**kwargs)
        self.value = value
        self.localized_value = localized_value


class LogicAppReceiver(Model):
    """A logic app receiver.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the logic app receiver. Names must be
     unique across all receivers within an action group.
    :type name: str
    :param resource_id: Required. The azure resource id of the logic app
     receiver.
    :type resource_id: str
    :param callback_url: Required. The callback url where http request sent
     to.
    :type callback_url: str
    """

    _validation = {
        'name': {'required': True},
        'resource_id': {'required': True},
        'callback_url': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'callback_url': {'key': 'callbackUrl', 'type': 'str'},
    }

    def __init__(self, *, name: str, resource_id: str, callback_url: str, **kwargs) -> None:
        super(LogicAppReceiver, self).__init__(**kwargs)
        self.name = name
        self.resource_id = resource_id
        self.callback_url = callback_url


class SmsReceiver(Model):
    """An SMS receiver.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the SMS receiver. Names must be unique
     across all receivers within an action group.
    :type name: str
    :param country_code: Required. The country code of the SMS receiver.
    :type country_code: str
    :param phone_number: Required. The phone number of the SMS receiver.
    :type phone_number: str
    :ivar status: The status of the receiver. Possible values include:
     'NotSpecified', 'Enabled', 'Disabled'
    :vartype status: str or
     ~azure.mgmt.monitor.v2018_09_01.models.ReceiverStatus
    """

    _validation = {
        'name': {'required': True},
        'country_code': {'required': True},
        'phone_number': {'required': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'country_code': {'key': 'countryCode', 'type': 'str'},
        'phone_number': {'key': 'phoneNumber', 'type': 'str'},
        'status': {'key': 'status', 'type': 'ReceiverStatus'},
    }

    def __init__(self, *, name: str, country_code: str, phone_number: str, **kwargs) -> None:
        super(SmsReceiver, self).__init__(**kwargs)
        self.name = name
        self.country_code = country_code
        self.phone_number = phone_number
        self.status = None


class TimeSeriesInformation(Model):
    """The time series info needed for calculating the baseline.

    All required parameters must be populated in order to send to Azure.

    :param sensitivities: Required. The list of sensitivities for calculating
     the baseline.
    :type sensitivities: list[str]
    :param values: Required. The metric values to calculate the baseline.
    :type values: list[float]
    :param timestamps: The array of timestamps of the baselines.
    :type timestamps: list[datetime]
    """

    _validation = {
        'sensitivities': {'required': True},
        'values': {'required': True},
    }

    _attribute_map = {
        'sensitivities': {'key': 'sensitivities', 'type': '[str]'},
        'values': {'key': 'values', 'type': '[float]'},
        'timestamps': {'key': 'timestamps', 'type': '[iso-8601]'},
    }

    def __init__(self, *, sensitivities, values, timestamps=None, **kwargs) -> None:
        super(TimeSeriesInformation, self).__init__(**kwargs)
        self.sensitivities = sensitivities
        self.values = values
        self.timestamps = timestamps


class VoiceReceiver(Model):
    """A voice receiver.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the voice receiver. Names must be
     unique across all receivers within an action group.
    :type name: str
    :param country_code: Required. The country code of the voice receiver.
    :type country_code: str
    :param phone_number: Required. The phone number of the voice receiver.
    :type phone_number: str
    """

    _validation = {
        'name': {'required': True},
        'country_code': {'required': True},
        'phone_number': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'country_code': {'key': 'countryCode', 'type': 'str'},
        'phone_number': {'key': 'phoneNumber', 'type': 'str'},
    }

    def __init__(self, *, name: str, country_code: str, phone_number: str, **kwargs) -> None:
        super(VoiceReceiver, self).__init__(**kwargs)
        self.name = name
        self.country_code = country_code
        self.phone_number = phone_number


class WebhookReceiver(Model):
    """A webhook receiver.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the webhook receiver. Names must be
     unique across all receivers within an action group.
    :type name: str
    :param service_uri: Required. The URI where webhooks should be sent.
    :type service_uri: str
    """

    _validation = {
        'name': {'required': True},
        'service_uri': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'service_uri': {'key': 'serviceUri', 'type': 'str'},
    }

    def __init__(self, *, name: str, service_uri: str, **kwargs) -> None:
        super(WebhookReceiver, self).__init__(**kwargs)
        self.name = name
        self.service_uri = service_uri
