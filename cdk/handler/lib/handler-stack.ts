import * as cdk from 'aws-cdk-lib';
import { Duration } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as ecr from 'aws-cdk-lib/aws-ecr-assets';
import * as lambda from 'aws-cdk-lib/aws-lambda';

export class HandlerStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const handler = new lambda.DockerImageFunction(this, 'GradioHandlerTemplate', {
      code: lambda.DockerImageCode.fromImageAsset('../../', {
        platform: ecr.Platform.LINUX_AMD64,
        file: './docker/lambda/Dockerfile',
      }),
      memorySize: 1024,
      timeout: Duration.seconds(60),
    });
  }
}
