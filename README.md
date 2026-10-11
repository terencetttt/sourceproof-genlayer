# SourceProof

SourceProof is a GenLayer Intelligent Contract that verifies factual claims against public HTTPS sources using validator-fetched evidence.

## Trust Model

The caller supplies only source_url and claim.

Validators independently retrieve the source. Caller-supplied webpage contents or summaries are never accepted as evidence.

## Verdicts

- SUPPORTED
- CONTRADICTED
- INCONCLUSIVE

Finalized verification records store the deterministic verification ID, normalized source URL, normalized claim, verdict, confidence, evidence summary, reasoning, and submitting wallet.

Finalized records are immutable. Duplicate URL and claim pairs are rejected.

## Limits

- URL: 2,048 characters
- Claim: 1,000 characters
- Fetched source: 300,000 bytes
- HTTPS only

## Public Methods

- verify_claim
- get_verification
- get_verification_ids
- verification_count
- verification_id
- contract_info

## Live Deployment

GenLayer Studio Network

Contract:
0xFC90785207eaFC6753e7596aF632F706Ca422a64

Deployment transaction:
0xc51e2195c5ea821fa3c86604f6a4e5f9f10056d652c096ac7ae57f39eebda8a3

Deployment status: FINALIZED
Consensus: MAJORITY_AGREE

## Live Verification Proof

Live validator-fetched verification result:

- Verdict: SUPPORTED
- Confidence: 98
- Status: finalized
- Verification ID: 12c485bdc71f730150b5d82b9246697fb7f8360dbf8cca9f38db7240e8519db9

The live test confirmed:
caller claim -> validator source retrieval -> semantic consensus -> immutable stored result.

## Validation

Run:

python -m py_compile .\contracts\source_proof.py

python .\tests\test_sourceproof_regression.py

The regression checks verify that the decisive path depends on validator-fetched evidence rather than caller-provided source contents.
