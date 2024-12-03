## SP-API SDK Workflows

The following workflows are currently available:
* [Build Java SDK](https://github.com/amzn/selling-partner-api-sdk/blob/main/.github/workflows/build-java-sdk.yml)
* [Create Release](https://github.com/amzn/selling-partner-api-sdk/blob/main/.github/workflows/create-release.yml)

### Overview

<img alt="Github Workflows" src="images/github-workflows.png" width="600px"/>

Building and releasing the SDK is a multistep approach. Whenever one of the [clients](https://github.com/amzn/selling-partner-api-models/tree/main/clients) or [models](https://github.com/amzn/selling-partner-api-models/tree/main/models) from [Selling Partner API Models](https://github.com/amzn/selling-partner-api-models) changes, the build workflow is triggered in this repository. This automatically rebuilds the SDK for all programming languages and incorporates changes from upstream. When the SDK is built successfully and there are new changes, a PR will be automatically opened for review.

Whenever there is a meaningful set of changes to be released, the release workflow can be triggered manually. This rebuilds all SDKs and creates a new [release](https://github.com/amzn/selling-partner-api-sdk/releases) in Github. Additionally a new PR is created which automatically bumps the version to the next minor version.
