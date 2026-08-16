---
title: "Virtual machines"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/virtual-machines.html"
content_id: "8Z9JgWcRi98uQVtAraO3OQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:49.589079+00:00"
---

# Virtual machines

Coverity Analysis can be deployed on bare metal or in virtual environments. For the best
Coverity Analysis performance in a virtual environment, observe the following guidance
when deploying and configuring the virtual environment. The resources must be reserved
and actually available to the VM.

Make sure that resource demand on the VM is planned and balanced to provide Coverity
Analysis the required CPUs and RAM. Make sure that the specified CPU and RAM is
available 100% of the time.

- When deploying a VM for Coverity Analysis, the following minimum resources must be
  met or exceeded:
  - Provision the application VM with a minimum of 4 CPU cores
    reserved.

    Note: Make sure that the VM is allocated an appropriate number
    of CPUs and appropriate RAM to handle all planned demand. VM supervisors
    tend to suspend high CPU and RAM users when resource requests exceed
    supply.
  - Provision the application VM with a minimum of 32GB memory reserved.
  - The application VM storage IOPS, whether embedded or external, must be a
    minimum 2000 IOPS reserved. The Coverity server is heavily reliant on fast
    database access. Ensuring high IO performance (IOPS) will have the greatest
    impact on responsiveness in a large deployment.
  - Thick provisioning is recommended for best performance. Beware of thin
    provisioning. Using thin provisioning can degrade Coverity Analysis
    performance if resources need to be expanded during an analysis.
  - For the VM Ethernet adapter, select vmxnet3.
  - Run the server on a local disk.
  - Consider running Coverity Analysis on Linux instead of on a Windows Server.
    Linux is generally more I/O efficient and can leverage larger RAM (>32GB)
    and shared buffer (>1GB) sizes than Windows.
- Maintain VMWare tools in the application VM at the latest version.
- When you run Coverity Analysis, ensure that real-time virus scanning and any other
  background processes that affect I/O performance are disabled.
