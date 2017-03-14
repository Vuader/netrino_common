# Tachyon OSS Framework
#
# Copyright (c) 2016-2017, see Authors.txt
# All rights reserved.
#
# LICENSE: (BSD3-Clause)
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENTSHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
from __future__ import absolute_import
from __future__ import unicode_literals

import nfw

class NetworkDeviceFields(object):

    class Meta(object):
        db_table = 'device'

    ip = nfw.Model.Integer()
    snmp_comm = nfw.Model.Text()
    name = nfw.Model.Text()
    vendor = nfw.Model.Text()
    os = nfw.Model.Text()
    os_ver = nfw.Model.Text()
    last_discover = nfw.Model.Datetime()


class NetworkDevices(NetworkDeviceFields, nfw.Model):
    pass


class NetworkDevice(NetworkDeviceFields, nfw.ModelDict):
    pass


class NetworkDevicePortFields(object):

    class Meta(object):
        db_table = 'device_port'

    id = nfw.Model.Integer()
    port = nfw.Model.Text()
    alias = nfw.Model.Text()
    prefix_len = nfw.Model.Integer()
    descr = nfw.Model.Text()
    name = nfw.Model.Text()
    mac = nfw.Model.Text()
    vlan = nfw.Model.Text()
    present = nfw.Model.Bool()
    igroup = nfw.Model.Uuid()


class NetworkDevicePorts(NetworkDevicePortFields, nfw.Model):
    pass


class NetworkDevicePort(NetworkDevicePortFields, nfw.ModelDict):
    pass


class NetworkServiceFields(object):

    class Meta(object):
        db_table = 'services'

    id = nfw.Model.Uuid(hidden=True)
    name = nfw.Model.Text(label="Service Name", required=True)
    interface_group = nfw.Model.Uuid()
    user_role = nfw.Model.Uuid()
    config_snippet = nfw.Model.Text(
        label="Configuration Snippet", required=True)
    fields = nfw.Model.Text()
    activate_snippet = nfw.Model.Text(
        label="Activation Snippet", required=True)
    deactivate_snippet = nfw.Model.Text(
        label="Deactivation Snippet", required=True)


class NetworkServices(NetworkServiceFields, nfw.Model):
    pass


class NetworkService(NetworkServiceFields, nfw.ModelDict):
    pass


class IGroupFields(object):

    class Meta(object):
        db_table = 'interface_groups'

    id = nfw.Model.Uuid(hidden=True)
    name = nfw.Model.Text(label="Interface Group", required=True)


class IGroups(IGroupFields, nfw.Model):
    pass


class IGroup(IGroupFields, nfw.ModelDict):
    pass


