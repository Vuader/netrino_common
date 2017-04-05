from __future__ import absolute_import
from __future__ import unicode_literals

from tachyonic.neutrino.model import Model
from tachyonic.neutrino.model import ModelDict

class NetworkDeviceFields(object):

    class Meta(object):
        db_table = 'device'

    ip = Model.Integer()
    snmp_comm = Model.Text()
    name = Model.Text()
    vendor = Model.Text()
    os = Model.Text()
    os_ver = Model.Text()
    last_discover = Model.Datetime()


class NetworkDevices(NetworkDeviceFields, Model):
    pass


class NetworkDevice(NetworkDeviceFields, ModelDict):
    pass


class NetworkDevicePortFields(object):

    class Meta(object):
        db_table = 'device_port'

    id = Model.Integer()
    port = Model.Text()
    alias = Model.Text()
    prefix_len = Model.Integer()
    descr = Model.Text()
    name = Model.Text()
    mac = Model.Text()
    vlan = Model.Text()
    present = Model.Bool()
    igroup = Model.Uuid()


class NetworkDevicePorts(NetworkDevicePortFields, Model):
    pass


class NetworkDevicePort(NetworkDevicePortFields, ModelDict):
    pass


class NetworkServiceFields(object):

    class Meta(object):
        db_table = 'services'

    id = Model.Uuid(hidden=True)
    name = Model.Text(label="Service Name", required=True)
    interface_group = Model.Uuid()
    user_role = Model.Uuid()
    config_snippet = Model.Text(
        label="Configuration Snippet", required=True)
    fields = Model.Text()
    activate_snippet = Model.Text(
        label="Activation Snippet", required=True)
    deactivate_snippet = Model.Text(
        label="Deactivation Snippet", required=True)


class NetworkServices(NetworkServiceFields, Model):
    pass


class NetworkService(NetworkServiceFields, ModelDict):
    pass


class IGroupFields(object):

    class Meta(object):
        db_table = 'interface_groups'

    id = Model.Uuid(hidden=True)
    name = Model.Text(label="Interface Group", required=True)


class IGroups(IGroupFields, Model):
    pass


class IGroup(IGroupFields, ModelDict):
    pass
