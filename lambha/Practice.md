Absolutely! Here’s a simple **Pulumi + AWS Lambda** project to help you test deploying a basic Lambda function. This example uses **Pulumi with TypeScript** (the most common combo), but let me know if you want Python instead.

---

# 🚀 Simple Pulumi AWS Lambda Project

This project will:

- Create a simple Lambda function (Node.js, “Hello World”)
- Use Pulumi to deploy it to AWS
- Set up an IAM role for Lambda execution

---

## 1. Prerequisites

- [Pulumi CLI](https://www.pulumi.com/docs/get-started/install/)
- [AWS CLI](https://aws.amazon.com/cli/) (configured with your credentials)
- [Node.js](https://nodejs.org/) (for this example)
- An AWS account

---

## 2. Project Setup

```bash
mkdir pulumi-aws-lambda-demo
cd pulumi-aws-lambda-demo
pulumi new aws-typescript
```

Follow prompts to set up your stack.

---

## 3. Lambda Function Code

Create a directory for your Lambda code:

```bash
mkdir lambda
```

Create `lambda/index.js`:

````javascript
exports.handler = async (event) => {
    return {
        statusCode: 200,
        body: JSON.stringify({ message: "Hello from Pulumi Lambda!" }),
    };
};
````

---

## 4. Update `index.ts` (Pulumi Program)

Replace the contents of `index.ts` with:

````typescript
import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";
import * as fs from "fs";

// Create IAM Role for Lambda
const role = new aws.iam.Role("lambda-exec-role", {
    assumeRolePolicy: aws.iam.assumeRolePolicyForPrincipal({ Service: "lambda.amazonaws.com" }),
});

// Attach AWSLambdaBasicExecutionRole policy
new aws.iam.RolePolicyAttachment("lambda-basic-exec-policy", {
    role: role.name,
    policyArn: aws.iam.ManagedPolicies.AWSLambdaBasicExecutionRole,
});

// Create Lambda Function
const lambdaFunc = new aws.lambda.Function("hello-lambda", {
    runtime: "nodejs18.x",
    code: new pulumi.asset.AssetArchive({
        ".": new pulumi.asset.FileArchive("./lambda"),
    }),
    timeout: 10,
    handler: "index.handler",
    role: role.arn,
});

// Export the Lambda function name and ARN
export const lambdaName = lambdaFunc.name;
export const lambdaArn = lambdaFunc.arn;
````

---

## 5. Install Dependencies

```bash
npm install @pulumi/aws
```

---

## 6. Deploy!

```bash
pulumi up
```

Accept the preview and Pulumi will deploy your Lambda.

---

## 7. Test the Lambda

You can invoke the Lambda via the AWS Console, AWS CLI, or add an API Gateway trigger.  
For a quick CLI test:

```bash
aws lambda invoke --function-name <your-lambda-name> response.json
cat response.json
```

Replace `<your-lambda-name>` with the value output by Pulumi.

---

## 📚 Summary

- You now have a minimal, working Pulumi project that deploys a Lambda!
- You can modify the Lambda code, redeploy, or add triggers as you wish.

---

If you’d like this example in **Python**, or want to add an API Gateway trigger (to call your Lambda via HTTP), just ask!
