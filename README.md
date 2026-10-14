<!-- jr-brand:start -->
<p align="center">
  <a href="https://jannikreinhard.com/">
    <img src="https://raw.githubusercontent.com/JayRHa/.github/main/assets/readme/brand-header.png" alt="Jannik Reinhard — I help enterprises ship secure AI agents" width="100%">
  </a>
</p>
<p align="center">
  <a href="https://jannikreinhard.com/">Website</a> ·
  <a href="https://www.linkedin.com/in/jannik-r/">LinkedIn</a> ·
  <a href="https://x.com/jannik_reinhard">X</a> ·
  <a href="https://www.youtube.com/@jannikreinhard">YouTube</a>
</p>
<!-- jr-brand:end -->

# GPT device troubleshooter

**Type:** Examples and labs · **Status:** Archived · Reference

<a id="intro"></a>

## Overview

GPT-assisted device troubleshooting experiment for endpoint management scenarios.

---

You can find the Tool Intune Device Troubleshooter in this repository. The gole of this tool is to provide you an assistant which helps you to answer your questions arround your intune environment.
If you have further ideas I would be happy if you send them to me, open an issue on this repository or create a pull request.

<a id="prerequisites"></a>

## Requirements

- GPT enabled Subscription (https://aka.ms/oai/access)
- App registration with deligated permissions (DeviceManagementConfiguration.Read.All, DeviceManagementManagedDevices.Read.All, DeviceManagementApps.Read.All, Group.Read.All, User.Read, Device.Read.All)

![Alt text](https://github.com/JayRHa/gpt-device-troubleshooter/blob/main/assets/appRegistartion.png)

## Quickstart

Get the source locally:

```bash
git clone https://github.com/JayRHa/gpt-device-troubleshooter.git
cd gpt-device-troubleshooter
```

This repository is archived; the documentation below describes its last published implementation.

Entry points: [`requirements.txt`](requirements.txt).

## Documentation

[![Deploy To Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FJayRHa%2Fgpt-device-troubleshooter%2Fmain%2Fazuredeploy.json)

- Find more informations in my blog post on jannikreinhard.com

## Contribution

<table>
  <tbody>
    <tr>
        <td align="center"><a href="https://github.com/JayRHa"><img src="https://avatars.githubusercontent.com/u/73911860?v=4" width="100px;" alt="Jannik Reinhard"/><br /><sub><b>Jannik Reinhard</b></sub></a><br /><a href="https://twitter.com/jannik_reinhard" title="Twitter">💬</a> <a href="https://www.linkedin.com/in/jannik-r/" title="LinkedIn">💬</a></td>
  </tbody>
</table>

## How does it work

- Full infra deployment via ARM
- Code will be pulled from git hub
- User delegated permissions to authenticate on graph
- Azure App Service for the website and the code logic

![Alt text](https://github.com/JayRHa/gpt-device-troubleshooter/blob/main/assets/auth.png)

![Alt text](https://github.com/JayRHa/gpt-device-troubleshooter/blob/main/assets/flow.png)

## Deployment

[![Deploy To Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FJayRHa%2Fgpt-device-troubleshooter%2Fmain%2Fazuredeploy.json)

## Post steps

- Fill out in the App Service Settings the variables (APPLICATION_ID, AZURE_OPENAI_KEY)

## How to contribute?

If you have a ideas for improvements or for missing features as well as bugs, contact me via my blog, social media or open an issue on the repository with an description of your idea.

## Disclosure

This is a community repository. There is no guarantee for this. Please check thoroughly before running the scripts.

<!-- jr-brand-footer:start -->
---

[Articles and guides](https://jannikreinhard.com/) · [Repository index](https://github.com/JayRHa/.github/blob/main/REPOSITORIES.md)
<!-- jr-brand-footer:end -->
