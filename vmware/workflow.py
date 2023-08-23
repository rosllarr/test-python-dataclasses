from typing import List
from dataclasses import dataclass, asdict


@dataclass
class CreateGuestWorkflow:
    """
    Create Vmware Guest with initial user

    Remark:
      - initial user used user module, which is required inventory
    """
    vmware_guest__hostname: str
    vmware_guest__username: str
    vmware_guest__password: str
    vmware_guest__datacenter: str
    vmware_guest__cluster: str
    vmware_guest__folder: str
    vmware_guest__template: str
    vmware_guest__name: str
    vmware_guest__networks: List
    vmware_guest__disk: List
    user__name: str
    user__groups: str
    user__append: str = 'yes'
    user__shell: str = '/bin/bash'

    def execute(self):
        """
        1. Create payload from class's properties
        2. Send payload as body to PubSub
        """

        print("Creating payload from class's properties...")
        print(self.get_vars())
        print('Sending payload as body to Pubsub...')

    def get_vars(self):
        return asdict(self)


class UpdateGuestWorkflow:
    """
    1. Increase/Decrease Vmware Guest cpu, memory, disk numbers
    2. Power on/off Guest
    """
    pass


class DeleteGuestWorkflow:
    """
    Delete Vmware Guest
    """
    pass
