---
title: "AWS: Create S3 Express bucket IAM policies"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/aws-create-s3-express-bucket-iam-policies.html"
content_id: "~Lg20Y~FKRA5omuME5RWKA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:14.071575+00:00"
---

# AWS: Create S3 Express bucket IAM policies

Note:

To create IAM policy for AWS S3 (not Express), see Specifying AWS S3 storage bucket and cache bucket IAM policy.

For Amazon AWS IAM documentation, see <https://docs.aws.amazon.com/iam/>.

If you are installing Scan Service in the cluster and using an S3 Express storage
buckets, create an IAM policy for each bucket created. These buckets can include a
storage bucket and a cache bucket.

If you create both a storage bucket and a cache bucket, using the IAM Policy Editor,
create an IAM policy for each resource.

When you define the the storage bucket and cache bucket resources within an IAM Statement
in the IAM policy, you can refer to your AWS S3 Express documentation such as: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam.html>.

An AWS resource ARN might use the following format described in the AWS document
linked-to above.

```
arn:aws:s3express:region:${account-id}:bucket/${base-bucket-name}--${azid}--x-s3
```

For example, the following example illustrates IAM policy for a single scan service
storage bucket:

- an S3 Express bucket
- all S3 Express actions
- account-id: 80...79
- base-bucket-name: scanstorage1-bucket

```
{
	"Statement": [
		{
			"Action": [
				"s3express:*"
			],
			"Effect": "Allow",
			"Resource": "arn:aws:s3express:us-east-1:80...79:bucket/scanstorage1-bucket--use1-az6--x-s3"
		},
		{
			"Action": [
				"s3express:*"
			],
			"Effect": "Allow",
			"Resource": "arn:aws:s3express:us-east-1:80...79:bucket/scanstorage1-bucket--use1-az6--x-s3/*"
		}
	],
	"Version": "2012-10-17"
}
```

As needed, override `storage-service.s3Express` Helm keys to support S3 Express.
See:

- For information on configuring the Helm keys for S3 Express, see Configure AWS S3 Express Helm keys.
