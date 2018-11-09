# Ansible role: Postfix

Install and configure postfix on an Ubuntu or Redhat server.

Primarily for use in hosting environments so a website can deliver mail via 127.0.0.1.

## Requirements

* Redhat or Ubuntu

## Role Variables

* default_mail_recipient: The email address of the person who should receive mail for root (stuff that was generated by the server; ie cron failure notifications)

For servers that accept incoming mail:
* postfix_tls_cert: Absolute path to the TLS public certificate
* postfix_tls_key: Absolute path to the TLS private key

For systems behind a load balancer:
* postfix_myhostname: In some cases, ansible won't be able to figure out what to use for this, so you'll need to specify it manually

## Dependencies

None

## Example Playbook

    ---
    - hosts: servers
      roles:
       - name: Install postfix
         role: acromedia.postfix
         default_mail_recipient: webmaster@example.com

## License

GPLv3

## Author Information

Acro Media Inc.
https://www.acromedia.com/