Excellent — moving on to **PHASE 2: Core Concepts & Cloud Resources** in Pulumi.

---

## ⚙️ **PHASE 2: Core Concepts & Cloud Resources**

---

### 🔹 Step 1: **Stacks & Projects**

* **Project**: Your infrastructure "application" (defined in `Pulumi.yaml`)
* **Stack**: An instance of your infrastructure (like `dev`, `prod`, etc.)
* You can have multiple stacks (dev, qa, prod) for the same code base.

**Useful Commands:**

```bash
pulumi stack ls              # List stacks
pulumi stack init dev        # Create new stack
pulumi stack select dev      # Select a stack
```

---

### 🔹 Step 2: **Pulumi Config & Secrets**

Pulumi allows stack-specific configuration — like environment variables, secrets, etc.

#### ✅ Set non-secret value:

```bash
pulumi config set aws:region us-east-1
```

#### ✅ Set secret (like DB password):

```bash
pulumi config set dbPassword mypass --secret
```

#### ✅ Access it in code:

```python
import pulumi
db_password = pulumi.Config().require_secret("dbPassword")
```

---

### 🔹 Step 3: **Deploy Multiple AWS Resources**

Let’s create a simple architecture:

* S3 Bucket (Static Hosting)
* IAM Role for Lambda
* Lambda Function (Python)

#### 🪣 `__main__.py`:

```python
import pulumi
import pulumi_aws as aws

# S3 bucket
site_bucket = aws.s3.Bucket("site-bucket")

# IAM role for Lambda
lambda_role = aws.iam.Role("lambda-role",
    assume_role_policy="""{
        "Version": "2012-10-17",
        "Statement": [{
            "Action": "sts:AssumeRole",
            "Principal": {
                "Service": "lambda.amazonaws.com"
            },
            "Effect": "Allow"
        }]
    }""")

# Lambda function
lambda_func = aws.lambda_.Function("hello-func",
    runtime="python3.8",
    role=lambda_role.arn,
    handler="handler.handler",
    code=pulumi.AssetArchive({
        ".": pulumi.FileArchive("./lambda"),
    }))

pulumi.export("bucket_name", site_bucket.id)
pulumi.export("lambda_name", lambda_func.name)
```

#### 🧾 Add `lambda/handler.py`:

```python
def handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from Pulumi Lambda!'
    }
```

---

### 🔹 Step 4: **Pulumi State Backends**

By default, Pulumi uses [https://app.pulumi.com](https://app.pulumi.com) for state storage. But you can also use:

* AWS S3
* Azure Blob
* GCP Bucket
* Local filesystem (not recommended for team use)

#### Example: Use S3 as backend

```bash
pulumi login s3://my-pulumi-state-bucket
```

---

### 🔹 Step 5: **Preview, Deploy, and Destroy Again**

```bash
pulumi preview
pulumi up       # Deploys S3 + Lambda + IAM
pulumi destroy  # Clean up
```

---

## ✅ PHASE 2 SUMMARY:

| Concept                                | You Learned |
| -------------------------------------- | ----------- |
| Stacks vs Projects                     | ✅           |
| Pulumi Config & Secrets                | ✅           |
| Multi-resource Infra (S3, IAM, Lambda) | ✅           |
| Code archive & Lambda handler          | ✅           |
| State Backends (SaaS, S3, etc.)        | ✅           |

---

## 🔜 Coming Next: **PHASE 3 - Intermediate DevOps Practices**

We'll cover:

* Reusable Components (`ComponentResource`)
* Cross-stack references
* Environment-specific deployments
* Automation API for CI/CD
* Unit testing infrastructure

Let me know when you're ready to proceed to **Phase 3**.
