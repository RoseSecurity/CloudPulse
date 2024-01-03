# :cloud: CloudPulse: Curating Compelling Cloud News

<p align="center">
<img width=70% height=50% src="./docs/img/CloudPulse_Logo.png">
</p>

---

_A tool to curate compelling news on cloud technologies and cybersecurity. By aggregating information from RSS feeds and Reddit, it identifies the most noteworthy and impactful updates in the tech industry._

## Demo

![](./docs/img/CloudPulse_Demo.mov)

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
