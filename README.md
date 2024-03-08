# :cloud: CloudPulse: Curating Compelling Cloud News

<p align="center">
<img width=70% height=50% src="./docs/img/CloudPulse_Logo.png">
</p>

---

_A tool to curate compelling news on cloud technologies and cybersecurity. By aggregating information from RSS feeds and Reddit, it identifies the most noteworthy and impactful updates in the tech industry._

## Demo

https://github.com/RoseSecurity/CloudPulse/assets/72598486/2b56ce37-b944-4f69-9f8b-307de993fff1

## Installation

Download Repository:

```sh
$ mkdir CloudPulse
$ cd CloudPulse/
$ sudo git clone https://github.com/RoseSecurity/CloudPulse.git
```

Install Dependencies:

```sh
$ pip3 install -r requirements.txt
```

## CloudPulse Usage

The following keys, usernames, and passwords are required within the `src/config.ini` file to run CloudPulse:

```sh
[Credentials]
REDDIT_CLIENT_ID - Reddit client ID
REDDIT_CLIENT_SECRET - Reddit client secret
REDDIT_USERNAME - Reddit username
REDDIT_PASSWORD - Reddit password
```

```sh
usage: cloudpulse.py [-h] [-o {stdout,file,streamlit}]
```

Output cloud news to terminal:

```sh
$ python3 cloudpulse.py -o stdout
```

Output cloud news to `CloudPulse` file:

```sh
$ python3 cloudpulse.py -o file
```

Output cloud news to Streamlit application:

```sh
$ python3 cloudpulse.py -o streamlit
```

## Sources

### Reddit

- [r/hacking](https://www.reddit.com/r/hacking/)
- [r/infosec](https://www.reddit.com/r/infosec/)
- [r/redteamsec](https://www.reddit.com/r/redteamsec/)
- [r/cybersecurity](https://www.reddit.com/r/cybersecurity/)
- [r/netsec](https://www.reddit.com/r/netsec/)
- [r/hackernews](https://www.reddit.com/r/hackernews/)
- [r/devops](https://www.reddit.com/r/devops/)
- [r/terraform](https://www.reddit.com/r/terraform/)
- [r/ansible](https://www.reddit.com/r/ansible/)
- [r/aws](https://www.reddit.com/r/aws/)
- [r/github](https://www.reddit.com/r/github/)
- [r/homelab](https://www.reddit.com/r/homelab/)
- [r/homenetworking](https://www.reddit.com/r/homenetworking/)
- [r/kubernetes](https://www.reddit.com/r/kubernetes/)
- [r/networking](https://www.reddit.com/r/networking/)
- [r/proxmox](https://www.reddit.com/r/proxmox/)
- [r/sysadmin](https://www.reddit.com/r/sysadmin/)
- [r/vscode](https://www.reddit.com/r/vscode/)
- [r/sre](https://www.reddit.com/r/sre/)
- [r/azure](https://www.reddit.com/r/azure/)
- [r/docker](https://www.reddit.com/r/docker/)
- [r/linux](https://www.reddit.com/r/linux/)
- [r/bash](https://www.reddit.com/r/bash/)
- [r/ubuntu](https://www.reddit.com/r/ubuntu/)
- [r/vim](https://www.reddit.com/r/vim/)
- [r/debian](https://www.reddit.com/r/debian/)
- [r/freebsd](https://www.reddit.com/r/freebsd/)
- [r/fedora](https://www.reddit.com/r/fedora/)
- [r/golang](https://www.reddit.com/r/golang/)
- [r/kde](https://www.reddit.com/r/kde/)
- [r/gnome](https://www.reddit.com/r/gnome/)
- [r/opensource](https://www.reddit.com/r/opensource/)

### RSS Feeds

#### AWS Feeds

- [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/feed/)
- [AWS Blog](https://aws.amazon.com/blogs/aws/feed/)
- [AWS Compute Blog](https://aws.amazon.com/blogs/compute/feed/)
- [AWS Containers Blog](https://aws.amazon.com/blogs/containers/feed/)
- [AWS DevOps Blog](https://aws.amazon.com/blogs/devops/feed/)
- [AWS Database Blog](https://aws.amazon.com/blogs/database/feed/)
- [AWS Infrastructure and Automation Blog](https://aws.amazon.com/blogs/infrastructure-and-automation/feed/)
- [AWS Open Source Blog](https://aws.amazon.com/blogs/opensource/feed/)

#### GCP Feeds

- [GCP Release Notes](https://cloud.google.com/release-notes)

#### Breach Feeds

- [Have I Been Pwned - Latest Breaches](https://feeds.feedburner.com/HaveIBeenPwnedLatestBreaches)

#### DevOps Feeds

- [OpenToFu Releases](https://github.com/opentofu/opentofu/releases.atom)
- [Terraform Releases](https://github.com/hashicorp/terraform/releases.atom)
- [Kubernetes Releases](https://github.com/kubernetes/kubernetes/releases.atom)
