---
title: "AWS: Create EKS cluster IAM policy and role"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/aws-create-eks-cluster-iam-policy-and-role.html"
content_id: "zdM0DQuLxHO76gTAhYi9dQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:12.076784+00:00"
---

# AWS: Create EKS cluster IAM policy and role

Create the Amazon EKS cluster IAM role to manage permissions and access control for
resources within the EKS cluster. Refer to <https://docs.aws.amazon.com/eks/latest/userguide/create-cluster.html>.

1. Create the policy. For example:

   ```
       read -r -d '' TRUST_POLICY <<EOF
   {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Principal": {
             "Service": "eks.amazonaws.com"
           },
           "Action": "sts:AssumeRole"
         }
       ]
   }
   EOF
   ```
2. Echo the policy. For example:

   ```
   echo "${TRUST_POLICY}" > eks-cluster-role-trust-policy.json
   ```
3. Create the AWS IAM role. For example:

   ```
   aws iam create-role \
       --role-name ${AWS_IAM_ROLE_NAME} \
       --assume-role-policy-document file://eks-cluster-role-trust-policy.json \
       --tags Key=CreatedBy,Value=${CREATED_BY_LABEL} \
       --no-paginate
   ```
4. Attach the Amazon EKS managed policy named
   `AmazonEKSClusterPolicy` to the role.

   ```
   aws iam attach-role-policy \
       --policy-arn arn:aws:iam::aws:policy/AmazonEKSClusterPolicy \
       --role-name ${AWS_IAM_ROLE_NAME}
   ```
