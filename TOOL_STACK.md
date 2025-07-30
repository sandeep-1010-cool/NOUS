**✅ Getting Started To-Do List (While Credentials Are Pending)**
*Organized by User Stories & Tasks – No information left out*

---

### 🧩 **User Story 1: EC2 Deployment Mini Project**

**Goal**: Deploy EC2 instances using Pulumi (TypeScript) to learn company DevOps/infrastructure standards.

#### 📘 **Learn Pulumi Basics**

* [ ] Read about:

  * Projects & Stacks Overview

    * 📄 [Organizing Projects & Stacks](https://www.pulumi.com/docs/intro/concepts/project/)
    * 📄 [Stacks | Pulumi Docs](https://www.pulumi.com/docs/intro/concepts/stack/)
  * Pulumi.yaml & Configuration

    * 📄 [Pulumi YAML Reference](https://www.pulumi.com/docs/intro/languages/yaml/)
    * 📄 [Project File Reference](https://www.pulumi.com/docs/intro/concepts/project/)
  * Secrets & Configs

    * 📄 [Managing Configuration and Secrets](https://www.pulumi.com/docs/intro/concepts/config/)
    * 📄 [Secrets | Pulumi Concepts](https://www.pulumi.com/docs/intro/concepts/secrets/)
    * 📄 [How to Manage Secrets with Pulumi (Blog)](https://www.pulumi.com/blog/managing-secrets-with-pulumi/)
  * Managing Stacks

    * 📄 [Stacks Overview](https://www.pulumi.com/docs/intro/concepts/stack/)
    * 📄 [`pulumi stack change-secrets-provider`](https://www.pulumi.com/docs/cli/commands/pulumi_stack_change-secrets-provider/)
  * Using Commands

    * 📄 [Pulumi CLI Commands](https://www.pulumi.com/docs/cli/)
    * 📄 [`pulumi up`](https://www.pulumi.com/docs/cli/commands/pulumi_up/)

#### 🛠️ **Hands-on Tasks**

* [ ] Deploy **2 EC2 instances** using **Pulumi (TypeScript)** in **2 AWS regions**
* [ ] Create & attach **IAM Roles + Instance Profiles**
* [ ] Use **init scripts** to install **Wiz Sensor**
* [ ] Apply standardized **AWS tags + environment names**: `"dev"`, `"test"`

---

### 🤖 **User Story 2: AI Workflow Setup & Familiarization**

**Goal**: Use Claude/OpenAI tools to automate workflows and code generation.
Here’s a concise version of the steps for User Story 2:

### AI Tooling Tasks

1. Use **Nous credentials** to access **Claude AI** or **OpenAI Codex**.
2. Install and configure Claude Code or OpenAI Codex locally.
3. Ensure Claude Code is installed and configured with your API key.

### Workflow Setup

1. Run in project root terminal:

   ```bash
   claude /init
   ```

   This creates `CLAUDE.md`.

2. (Optional) Customize `CLAUDE.md` with:

   ```markdown
   ### /create-prd
   Prompt: Generate detailed Project Requirements Document.

   ### /generate-tasks
   Prompt: Break PRD into task list with estimates.

   ### /process-task-list
   Prompt: Scaffold Pulumi EC2 code from tasks.
   ```

3. Use commands to automate workflows:

   ```bash
   claude /create-prd
   claude /generate-tasks
   claude /process-task-list
   ```

---

### 🔐 **User Story 3: Information Security Policy Familiarization**

**Goal**: Read & comply with internal security policy.

#### 📘 **Tasks**

* [ ] Read and understand the **Information Security Policy**
* [ ] Ensure compliance in all work
* [ ] **DO NOT share** the policy outside the company

---

### 💻 **User Story 4: Developer Workstation Setup**

**Goal**: Set up local workstation with all required tools.

#### 📘 **Refer to OS-Specific Setup Guide** *(Pending Confluence Access)*

* [ ] Windows: **Windows Developer Local Workspace Setup**
* [ ] Ubuntu + Docker: **Ubuntu and Docker Setup**
* [ ] macOS: **Mac Developer Local Workspace Setup**

#### 🧰 **Minimum Tools to Install**

* [ ] `saml2aws` *(pending credentials)*
* [ ] Docker
* [ ] JumpCloud *(pending credentials)*
* [ ] Homebrew *(Linux only)*
* [ ] AWS CLI
* [ ] `kubectl`
* [ ] `kubectx`
* [ ] `kubens`
* [ ] `k9s`
* [ ] Node.js + npm
* [ ] Python 3.x

  * [ ] Understand `venv` for virtual environments
* [ ] GitHub *(pending credentials)*

  * [ ] Register with **Black Book email**
  * [ ] Enable **MFA**
* [ ] Ansible (installed and configured)

---

### 🛡️ **User Story 5: Enforce Basic Security Settings**

**Goal**: Apply basic laptop security configuration.

#### 🔒 **Tasks**

* [ ] Set **auto-lock** after **≤ 30 minutes of inactivity**
* [ ] Test lock functionality
* [ ] Apply setting on:

  * [ ] Windows
  * [ ] macOS
  * [ ] Linux
