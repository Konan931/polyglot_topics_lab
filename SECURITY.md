# Security

This repository is currently a learning, data-modeling, and scientific-computing project.

## Please report

Report issues that could expose credentials, unsafe configuration, vulnerable dependencies, or unintended access to future connected services.

## Current boundaries

- No production credentials belong in the repository.
- Local environment files must remain untracked.
- Future database access must use least privilege and explicit row-level security where exposed through an API.
- Service-role or equivalent privileged secrets must never be shipped to browser code.

Security-sensitive integrations will receive their own threat model before deployment.
