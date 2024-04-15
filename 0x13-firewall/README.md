# Firewall

In this project, you'll work with firewalls to secure your servers. You'll configure the `ufw` firewall and set up port forwarding on your servers.

## Tasks

### 0. Block all incoming traffic but
- **File**: [0-block_all_incoming_traffic_but](./0-block_all_incoming_traffic_but)
- **Description**:
  - Install the `ufw` firewall and set up rules on `web-01` to block all incoming traffic except for specific TCP ports (`22`, `443`, `80`).
  - Share the `ufw` commands used in your answer file.

### 1. Port forwarding
- **File**: [100-port_forwarding](./100-port_forwarding)
- **Description**:
  - Configure `web-01` to forward port `8080/TCP` to port `80/TCP`.
  - Provide a copy of the `ufw` configuration file that you modified to make this happen.

---
**Note**: Remember to be cautious when configuring firewall rules, especially when blocking or forwarding ports, to avoid unintended consequences.
