# Update Reddit and RSS Feeds

To update the RSS and Reddit feeds collected by `CloudPulse`, navigate to `CloudPulse/src/collector/reddit.py` and `CloudPulse/src/collector/rss.py` and update or add any feeds to the following lists:

Reddit:

```python
    subreddits = ["hacking", "infosec", "redteamsec",
                  "cybersecurity", "netsec", "hackernews", "devops", "terraform", "ansible", "aws",
                  "github", "homelab", "homenetworking",
                  "kubernetes", "networking", "proxmox", "sysadmin", "vscode", "sre", "azure",
                  "docker", "linux", "bash", "ubuntu", "vim", "debian",
                  "freebsd", "fedora", "golang", "kde", "gnome", "opensource"]
```

RSS:

```python
    aws_feeds = ["https://aws.amazon.com/blogs/architecture/feed/",
                 "https://aws.amazon.com/blogs/aws/feed/",
                 "https://aws.amazon.com/blogs/compute/feed/",
                 "https://aws.amazon.com/blogs/containers/feed/", "https://aws.amazon.com/blogs/devops/feed/",
                 "https://aws.amazon.com/blogs/database/feed/",
                 "https://aws.amazon.com/blogs/infrastructure-and-automation/feed/",
                 "https://aws.amazon.com/blogs/opensource/feed/",
                 "https://aws.amazon.com/blogs/opensource/feed/",
                 ]

    breach_feeds = [
        "https://feeds.feedburner.com/HaveIBeenPwnedLatestBreaches"]

    devops_feeds = ["https://github.com/opentofu/opentofu/releases.atom",
                    "https://github.com/hashicorp/terraform/releases.atom",
                    "https://github.com/kubernetes/kubernetes/releases.atom"
                    ]
```
