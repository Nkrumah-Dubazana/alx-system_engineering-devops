# HTTPS SSL

In this project, you'll learn about the importance of HTTPS and how it works. You'll configure your HolbertonBnB web servers with `certbot` certificates and HAproxy SSL termination.

## Tasks

### 0. World wide web
- **File**: [1-world_wide_web](./0-world_wide_web)
- **Description**:
  - Write a Bash script to display information about subdomains on your configured servers.
  - Usage: `./1-world_wide_web <domain> <subdomain>`
  - Output: `The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]`
  - If no `subdomain` parameter is passed, display information about the subdomains `www`, `lb-01`, `web-01`, and `web-02`, in that order.

### 2. HAproxy SSL termination
- **File**: [2-haproxy_ssl_termination](./2-haproxy_ssl_termination)
- **Description**:
  - Create an HAproxy configuration file that accepts encrypted SSL traffic for the subdomain `www.` on TCP port 443.

### 3. No loophole in your website traffic
- **File**: [100-redirect_http_to_https](./100-redirect_http_to_https)
- **Description**:
  - Write an HAproxy configuration file that automatically redirects HTTP traffic to HTTPS.

---
**Note**: Make sure to replace `<domain>` and `<subdomain>` with appropriate values when running the scripts.
