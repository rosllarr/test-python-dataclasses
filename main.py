from vmware.workflow import CreateGuestWorkflow


if __name__ == '__main__':
    create_guest_wf = CreateGuestWorkflow(
        vmware_guest__hostname='vcenter.opsta.co.th',
        vmware_guest__username='admin',
        vmware_guest__password='P@ssword',
        vmware_guest__datacenter='opsta-site',
        vmware_guest__cluster='opsta-site-2',
        vmware_guest__folder='/test',
        vmware_guest__template='rhel86_template',
        vmware_guest__name='test',
        vmware_guest__networks=[
            {
                'ip': '192.168.0.1',
                'mark': '255.255.255.0',
            }
        ],
        vmware_guest__disk=[
            {
                'size_gb': 50
            }
        ],
        user__name='bob',
        user__groups='wheel,docker',
    )
    create_guest_wf.execute()
