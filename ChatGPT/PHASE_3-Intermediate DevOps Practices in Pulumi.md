Perfect. Let's proceed to:

---

## 🧩 **PHASE 3: Intermediate DevOps Practices in Pulumi**

This phase focuses on **modular design**, **multi-stack environments**, **CI/CD automation**, and **testing your infra**.

---

### 🔹 Step 1: Reusable Components with `ComponentResource`

To avoid copy-pasting, you can create your own **components** — reusable building blocks.

#### ✅ Example: `MyS3Bucket` component

**📁 Structure:**

```
.
├── __main__.py
├── my_s3.py
```

#### ✨ `my_s3.py`

```python
import pulumi
import pulumi_aws as aws

class MyS3Bucket(pulumi.ComponentResource):
    def __init__(self, name, opts=None):
        super().__init__('custom:resource:MyS3Bucket', name, {}, opts)

        self.bucket = aws.s3.Bucket(name)

        self.register_outputs({
            "bucket_name": self.bucket.id
        })
```

#### ✨ `__main__.py`

```python
from my_s3 import MyS3Bucket
import pulumi

bucket = MyS3Bucket("my-reusable-bucket")
pulumi.export("bucket_name", bucket.bucket.id)
```

---

### 🔹 Step 2: Cross-Stack References

You can **import outputs from one stack into another** (like Terraform remote state).

#### In **Stack A** (`networking`)

```python
pulumi.export("vpc_id", vpc.id)
```

#### In **Stack B** (`ecs-app`)

```python
vpc_id = pulumi.StackReference("myorg/networking/dev").get_output("vpc_id")
```

---

### 🔹 Step 3: Environment-Specific Deployment (multi-env support)

Use different stacks for `dev`, `staging`, and `prod`.

#### Example:

```bash
pulumi stack init dev
pulumi config set dbPassword mydevpass --secret

pulumi stack init prod
pulumi config set dbPassword myprodpass --secret
```

Use `pulumi.Config()` in code to access secrets and env-specific values dynamically.

---

### 🔹 Step 4: Automate with GitHub Actions (CI/CD)

Pulumi has great GitHub Actions integration.

#### 📄 `.github/workflows/pulumi.yaml`

```yaml
name: Pulumi CI

on:
  push:
    branches:
      - main

jobs:
  up:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Setup Pulumi
        uses: pulumi/actions@v4

      - name: Login to Pulumi
        run: pulumi login

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Pulumi up
        run: pulumi up --yes
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
```

---

### 🔹 Step 5: Unit Testing with `pytest`

Pulumi supports unit testing via mocks.

#### ✅ Test Example

```python
from pulumi.runtime import set_mocks
import pulumi
import pulumi_aws as aws

def test_bucket_created():
    set_mocks(lambda args: {"id": "mock_id", "state": args.inputs})
    from __main__ import site_bucket

    def check_bucket(args):
        urn, bucket = args
        assert bucket.website is None

    pulumi.runtime.serialize_property(site_bucket).apply(lambda _: check_bucket(site_bucket))
```

---

## ✅ PHASE 3 SUMMARY:

| Concept                  | You Learned |
| ------------------------ | ----------- |
| Component Resources      | ✅           |
| Cross-Stack Outputs      | ✅           |
| Multi-environment config | ✅           |
| CI/CD GitHub Actions     | ✅           |
| Infra Unit Testing       | ✅           |

---

## 🔜 Coming Next: **PHASE 4 - Advanced & Enterprise Pulumi**

We’ll cover:

* Pulumi Automation API (build your own IaC CLI tools)
* Policy as Code with Pulumi CrossGuard
* Secrets Management with Azure Key Vault or AWS KMS
* Using Dynamic Providers
* Working in teams with backend locking and permissions

Let me know and I’ll continue to **PHASE 4**.
