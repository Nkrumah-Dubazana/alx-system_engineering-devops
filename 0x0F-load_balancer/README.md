## 0x0F. Load balancer

### Introduction
In this project, we aim to enhance our web stack by adding redundancy for our web servers. This will allow us to handle more traffic by doubling the number of web servers and making our infrastructure more reliable. We'll achieve this by configuring additional servers and setting up a load balancer to distribute incoming traffic among them. The tasks involve automating the configuration process using Bash scripts and Puppet manifests.

### Concepts
- [Load balancer](https://alx-intranet.hbtn.io/concepts/46)
- [Web stack debugging](https://alx-intranet.hbtn.io/concepts/68)

### Tasks

#### 0. Double the number of webservers
- **File**: [0-custom_http_response_header](./0-custom_http_response_header)
- **Description**:
  - Configure Nginx to include a custom header in its HTTP response (`X-Served-By`).
  - Write a Bash script to configure a new Ubuntu machine to match the requirements.
  - Ensure that the custom header contains the hostname of the server Nginx is running on.

#### 1. Install your load balancer
- **File**: [1-install_load_balancer](./1-install_load_balancer)
- **Description**:
  - Install and configure HAproxy on the `lb-01` server.
  - Configure HAproxy to send traffic to `web-01` and `web-02` using a round-robin algorithm.
  - Ensure HAproxy can be managed via an init script.
  - Write a Bash script to configure a new Ubuntu machine to meet the requirements.

#### 2. Add a custom HTTP header with Puppet
- **File**: [2-puppet_custom_http_response_header.pp](./2-puppet_custom_http_response_header.pp)
- **Description**:
  - Use Puppet to automate the task of creating a custom HTTP header response.
  - The custom header should be named `X-Served-By`, with its value being the hostname of the server Nginx is running on.

### Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files should end with a new line
- Scripts must be executable
- Use `Shellcheck` (version `0.3.7`) to check scripts for errors
- The first line of all Bash scripts should be `#!/usr/bin/env bash`

### Servers Information
| Name         | Username | IP              | State   |
|--------------|----------|-----------------|---------|
| 1733-web-01  | ubuntu   | 3.235.21.36     | running |
| 1733-web-02  | ubuntu   | 3.83.35.54      | running |
| 1733-lb-01   | ubuntu   | 34.231.109.143  | running |

### Resources
- [Introduction to load-balancing and HAproxy](https://alx-intranet.hbtn.io/rltoken/B7f3oz8i3Xvvom_YQZzLnQ)
- [HTTP header](https://alx-intranet.hbtn.io/rltoken/sZ9v3Vq2tgLwN_PWVQketw)
- [Debian/Ubuntu HAProxy packages](https://alx-intranet.hbtn.io/rltoken/2VRAgtKKR9g6Xfb0xzGiSg)

---
**Repo:** [alx-system_engineering-devops](https://github.com/username/alx-system_engineering-devops)  
**Directory:** `0x0F-load_balancer`
