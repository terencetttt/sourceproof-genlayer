from pathlib import Path

SOURCE = Path("contracts/source_proof.py").read_text(encoding="utf-8")

def require(text, message):
    assert text in SOURCE, message

require(
    'response = gl.nondet.web.get(source_url)',
    "SourceProof must independently fetch the source URL"
)

require(
    'source_bytes = self._fetch_source(source_url)',
    "Decisive verification path must use validator-fetched source bytes"
)

require(
    'if verification_id in self.records:',
    "Duplicate verification records must be blocked"
)

require(
    'raise gl.vm.UserError("Verification already finalized")',
    "Duplicate verification records must be immutable/finalized"
)

require(
    'if not source_url.startswith("https://")',
    "Non-HTTPS URLs must be rejected"
)

require(
    'MAX_URL_CHARS = 2048',
    "URL bound must be enforced"
)

require(
    'MAX_CLAIM_CHARS = 1000',
    "Claim bound must be enforced"
)

require(
    'MAX_SOURCE_BYTES = 300_000',
    "Fetched source size must be bounded"
)

require(
    '"SUPPORTED"',
    "SUPPORTED verdict missing"
)

require(
    '"CONTRADICTED"',
    "CONTRADICTED verdict missing"
)

require(
    '"INCONCLUSIVE"',
    "INCONCLUSIVE verdict missing"
)

assert "source_text" not in SOURCE.split("def verify_claim", 1)[1].split("def get_verification", 1)[0], (
    "verify_claim must not accept caller-supplied source contents"
)

print("PASS: SourceProof regression checks")
